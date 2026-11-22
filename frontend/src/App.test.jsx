// @vitest-environment jsdom
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { cleanup, fireEvent, render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import App from './App'
import { api } from './services/api'

vi.mock('./services/api', () => ({
  api: { dashboard: vi.fn(), predict: vi.fn(), forecast: vi.fn(), modelInfo: vi.fn() },
}))

// jsdom does not lay out SVG charts. Preserve page rendering and exercise chart
// data contracts through the API and browser integration checks.
vi.mock('recharts', async importOriginal => ({
  ...await importOriginal(),
  ResponsiveContainer: () => null,
}))

function page(path) {
  render(<MemoryRouter initialEntries={[path]}><App /></MemoryRouter>)
}

beforeEach(() => vi.resetAllMocks())
afterEach(cleanup)

describe('AirLedger pages', () => {
  it('loads and renders dashboard statistics and the budget', async () => {
    api.dashboard.mockResolvedValue({
      stats: { avg_aqi: 196.5, max_aqi: 500, safe_days: 236, high_risk_days: 448, total_days: 1095 },
      trend: [], monthly: [], by_location: [], risk_dist: [],
      pollution_budget: { safe_limit: 100, observations_exceeded: 859 },
    })
    page('/')
    expect(screen.getByText(/Fetching dashboard data/)).toBeTruthy()
    expect(await screen.findByText('Days Over Budget')).toBeTruthy()
    expect(screen.getByText('196.5')).toBeTruthy()
  })

  it('shows a dashboard error and supports retry', async () => {
    api.dashboard.mockRejectedValue(new Error('Service unavailable'))
    page('/')
    expect(await screen.findByText('Service unavailable')).toBeTruthy()
    fireEvent.click(screen.getByRole('button', { name: /retry/i }))
    expect(api.dashboard).toHaveBeenCalledTimes(2)
  })

  it('rejects a blank pollutant and accepts a seasonal preset', async () => {
    api.predict.mockResolvedValue({
      aqi: 344.7, category: 'Very Poor', risk_label: 'High Risk',
      pollution_budget: { safe_limit: 100, predicted: 344.7, exceeded: true, overshoot: 244.7 },
      risk_probabilities: { 'High Risk': 100 }, recommendations: [{ action: 'Restrict dust', priority: 'High' }],
    })
    page('/predict')
    const pm = screen.getByRole('spinbutton', { name: /PM2.5/ })
    fireEvent.change(pm, { target: { value: '' } })
    fireEvent.click(screen.getByRole('button', { name: /predict/i }))
    expect(screen.getByRole('alert').textContent).toMatch(/PM2.5/)
    expect(api.predict).not.toHaveBeenCalled()
    fireEvent.click(screen.getByRole('button', { name: 'Winter' }))
    fireEvent.click(screen.getByRole('button', { name: /predict/i }))
    expect(api.predict.mock.calls[0][0].pm25).toBe(180)
    expect(await screen.findByText('Restrict dust')).toBeTruthy()
    expect(screen.getByText(/244.7/)).toBeTruthy()
  })

  it('renders seven simulated days', async () => {
    api.forecast.mockResolvedValue({ forecast: Array.from({ length: 7 }, (_, i) => ({
      date: `Mon Jan 0${i + 1}`, iso_date: `2027-01-0${i + 1}`, aqi: 93.5,
      category: 'Satisfactory', risk: 'Safe',
    })) })
    page('/forecast')
    fireEvent.click(screen.getByRole('button', { name: 'Run Simulation' }))
    expect(await screen.findByText('Simulated 7-Day AQI')).toBeTruthy()
    expect(screen.getAllByText('Satisfactory')).toHaveLength(7)
  })

  it('shows prediction progress and a request error', async () => {
    let rejectRequest
    api.predict.mockReturnValue(new Promise((_, reject) => { rejectRequest = reject }))
    page('/predict')
    fireEvent.click(screen.getByRole('button', { name: /predict/i }))
    expect(screen.getByRole('button', { name: /predicting/i }).disabled).toBe(true)
    rejectRequest(new Error('Prediction service unavailable'))
    expect((await screen.findByRole('alert')).textContent).toContain('Prediction service unavailable')
    expect(screen.getByRole('button', { name: /predict/i }).disabled).toBe(false)
  })

  it('shows the selected models using the API metadata', async () => {
    api.modelInfo.mockResolvedValue({
      regression: { Linear: { r2: 0.99, mae: 8, rmse: 10 } }, classification: { Forest: { accuracy: 0.94 } },
      selected_regressor: 'Linear', selected_classifier: 'Forest', coefficients: { pm25: 65 },
      features: ['pm25'], test_size: 219, confusion_matrix: [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    })
    page('/model')
    expect(await screen.findByText('Standardized Regression Coefficients')).toBeTruthy()
    expect(screen.getByText('Accuracy = 94.00%')).toBeTruthy()
  })
})


"""Model feature order and API input validation."""

FEATURE_RANGES = {
    "pm25": (0, 500),
    "pm10": (0, 600),
    "no2": (0, 200),
    "so2": (0, 100),
    "co": (0, 20),
    "temperature": (-5, 50),
    "humidity": (0, 100),
    "wind_speed": (0, 60),
    "rainfall": (0, 100),
    "visibility": (0, 25),
    "month": (1, 12),
    "day_of_week": (0, 6),
}
FEATURES = [*FEATURE_RANGES, "is_weekend"]
CALENDAR_FIELDS = {"month", "day_of_week", "is_weekend"}


class InputError(ValueError):
    """A client supplied invalid input."""


def number(data, field, bounds):
    if field not in data:
        raise InputError(f"Missing required field: {field}")
    value = data[field]
    low, high = bounds
    if type(value) not in (int, float) or not low <= value <= high:
        raise InputError(f"{field} must be a number between {low} and {high}")
    if field in CALENDAR_FIELDS and int(value) != value:
        raise InputError(f"{field} must be an integer")
    return value


def prediction_inputs(data):
    values = {field: number(data, field, bounds) for field, bounds in FEATURE_RANGES.items()}
    values["is_weekend"] = int(values["day_of_week"] >= 5)
    if "is_weekend" in data and number(data, "is_weekend", (0, 1)) != values["is_weekend"]:
        raise InputError("is_weekend must agree with day_of_week")
    return values

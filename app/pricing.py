from datetime import datetime, timezone


def surge_multiplier(now: datetime | None = None) -> float:
    """Return the surge pricing multiplier for the payments-api transaction fee.

    Peak hours (9-11am and 5-7pm) apply a 1.25x multiplier; all other hours
    are standard rate (1.0x).
    """
    now = now or datetime.now(timezone.utc)
    hour = now.hour
    if 9 <= hour < 11 or 17 <= hour < 18:
        return 1.25
    return 1.0

from datetime import datetime, timezone

from app.pricing import surge_multiplier


def test_standard_rate():
    assert surge_multiplier(datetime(2026, 9, 6, 12, 0, 0, tzinfo=timezone.utc)) == 1.0


def test_surge_rate_morning():
    assert surge_multiplier(datetime(2026, 9, 6, 9, 30, 0, tzinfo=timezone.utc)) == 1.25


def test_surge_rate_evening():
    assert surge_multiplier(datetime(2026, 9, 6, 18, 0, 0, tzinfo=timezone.utc)) == 1.25

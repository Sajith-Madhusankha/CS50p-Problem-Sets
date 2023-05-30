import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("06:00 to 17:30")
    with pytest.raises(ValueError):
        convert("13:00 PM to 25:00 PM")
    with pytest.raises(ValueError):
        convert("6:60 AM to 8:90 AM")
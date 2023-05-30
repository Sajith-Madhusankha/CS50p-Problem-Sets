from seasons import convert


def test_date():
    assert convert(9229) == "Thirteen million, two hundred eighty-nine thousand, seven hundred sixty minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
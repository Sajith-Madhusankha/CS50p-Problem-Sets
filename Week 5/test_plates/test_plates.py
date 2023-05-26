from plates import is_valid

def test_is_valid_empty():
    assert is_valid("") == False


def test_is_valid_over6():
    assert is_valid("AAAA222") == False


def test_is_valid_under2():
    assert is_valid("A") == False


def test_is_valid_proper():
    assert is_valid("HICS50") == True


def test_is_valid_not_alnum():
    assert is_valid("AA!@42") == False


def test_is_valid_start():
    assert is_valid("22AA22") == False
    assert is_valid("CS") == True
    assert is_valid("50") == False


def test_is_valid_zero():
    assert is_valid("AAA022") == False
    assert is_valid("AAA201") == True


def test_is_valid_midnumbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
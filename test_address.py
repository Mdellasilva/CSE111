from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city(f"525 S Center St, Rexburg, ID 83460") == f"Rexburg"

def test_extract_state():
    assert extract_state(f"525 S Center St, Rexburg, ID 83460") == f"ID"

def test_extract_zipcode():
    assert extract_zipcode(f"525 S Center St, Rexburg, ID 83460") == "83460"

pytest.main(["-v", "--tb=line", "-rN", "test_address.py"])
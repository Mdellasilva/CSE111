from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest


def test_make_full():
    assert make_full_name("Sally", "Brown-Bob") == f"Brown-Bob; Sally"
    assert make_full_name("Sally", "Brown") == f"Brown; Sally"
    assert make_full_name("S", "Br") == f"Br; S"
    assert make_full_name("", "") == f"; "    

def test_extract_family():
    assert extract_family_name("Brown-Bob; Sally") == f"Brown-Bob"
    assert extract_family_name("Brown; Sally") == f"Brown"
    assert extract_family_name("Br; S") == f"Br"
    assert extract_family_name("; ") == f""

def test_extract_given():
    assert extract_given_name("Brown-Bob; Sally") == f"Sally"
    assert extract_given_name("Brown; Sally") == f"Sally"
    assert extract_given_name("Br; S") == f"S"
    assert extract_given_name("; ") == f""



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "names_test.py"])
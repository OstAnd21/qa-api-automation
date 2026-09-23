from unittest.mock import Mock
from utils.response_validator import assert_status_code, assert_content_type
import pytest

def test_status_code_validator_fails():
    response = Mock(status_code=404)
    with pytest.raises(AssertionError):
        assert_status_code(response, 200)
        
def test_content_type_validator_passes():
    response = Mock()
    response.headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    assert_content_type(response, "application/json")

def test_content_type_validator_fails():
    response = Mock()
    response.headers = {
        "Content-Type": "text/html"
    }
    with pytest.raises(AssertionError):
        assert_content_type(response, "application/json")
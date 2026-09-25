from api.users_api import UsersAPI
from unittest.mock import patch
from config import settings
from api.base_api import BaseAPI
import pytest
import requests
import allure

@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle invalid URL")
def test_invalid_url():
    api = UsersAPI()
    with allure.step("Send request to invalid URL"):
        with pytest.raises(requests.exceptions.ConnectionError):
            api.get_users_from_invalid_url()

@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle request timeout")
def test_request_timeout():
    api = UsersAPI()
    with patch.object(
        api.session,
        "request",
        side_effect=requests.exceptions.Timeout
    ):
        with allure.step("Send request with timeout"):
            with pytest.raises(requests.exceptions.Timeout):
                api.get_users_with_timeout()
                
def test_retry_configuration():
    api = BaseAPI(settings.BASE_URL)
    adapter = api.session.get_adapter("https://")
    retry = adapter.max_retries
    assert retry.total is None
    assert retry.connect == 0
    assert retry.read is False
    assert retry.status == 3
    assert retry.status_forcelist == [502, 503, 504]

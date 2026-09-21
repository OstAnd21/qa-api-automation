from api.users_api import UsersAPI
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
    with allure.step("Send request with timeout"):
        with pytest.raises(requests.exceptions.Timeout):
            api.get_users_with_timeout()
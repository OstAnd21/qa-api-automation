from api.users_api import UsersAPI
from utils.allure_helpers import attach_response
from utils.response_validator import (
    assert_status_code,
    assert_response_time
)
import allure
import pytest

@allure.feature("Users API")
@allure.story("Delete user")
@allure.title("Delete user by ID")
@pytest.mark.smoke
def test_delete_user(user_id):
    api = UsersAPI()
    with allure.step("Send DELETE request"):
        response = api.delete_user(user_id)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
  
@allure.feature("Users API")
@allure.story("Delete user")
@allure.title("Delete user from API class")
def test_delete_user_from_api_class():
    api = UsersAPI()
    with allure.step("Send DELETE request"):
        response = api.delete_user(1)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    
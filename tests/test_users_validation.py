from api.users_api import UsersAPI
from utils.allure_helpers import attach_response
from utils.response_validator import (
    assert_status_code,
    assert_content_type,
    assert_response_time
)
import allure

@allure.feature("Users API")
@allure.story("User validation")
@allure.title("Check required user fields")

def test_user_has_required_fields(user_id):
    api = UsersAPI()
    with allure.step("Send GET request"):
        response = api.get_user(user_id)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check required fields"):
        required_fields = ["id", "name", "username", "email"]
        for field in required_fields:
            assert field in data

@allure.feature("Users API")
@allure.story("User validation")
@allure.title("Check required user fields")

def test_user_data_types(user_id):
    api = UsersAPI()
    with allure.step("Send GET request"):
        response = api.get_user(user_id)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check user data types"):
        assert isinstance(data["id"], int)
        assert isinstance(data["name"], str)
        assert isinstance(data["username"], str)
        assert isinstance(data["email"], str)

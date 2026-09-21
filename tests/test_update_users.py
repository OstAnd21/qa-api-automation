from api.users_api import UsersAPI
from utils.allure_helpers import attach_response
from utils.response_validator import (
    assert_status_code,
    assert_content_type,
    assert_response_time
)
import allure


@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Update user by ID")

def test_update_user(user_id):
    user_data = {
        "name": "Andrii Updated",
        "username": "andrii_updated",
        "email": "updated@example.com"
    }
    api = UsersAPI()
    with allure.step("Send PUT request"):
        response = api.update_user(user_id, user_data)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check updated user data"):
        assert data["name"] == "Andrii Updated"
        assert data["username"] == "andrii_updated"
        assert data["email"] == "updated@example.com"
 
@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Patch user by ID") 
 
def test_patch_user(user_id):
    user_data = {
        "name": "Andrii PATCH"
    }
    api = UsersAPI()
    with allure.step("Send PATCH request"):
        response = api.patch_user(user_id, user_data)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check patched user data"):
        assert data["name"] == "Andrii PATCH"

@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Update user from API class")

def test_update_user_from_api_class():
    api = UsersAPI()
    with allure.step("Send PUT request"):
        response = api.update_user(
            1,
            {
                "name": "Andrii Updated",
                "username": "andrii_updated",
                "email": "updated@example.com"
            }
        )
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check updated user data"):
        assert data["name"] == "Andrii Updated"
        assert data["username"] == "andrii_updated"
        assert data["email"] == "updated@example.com"

@allure.feature("Users API")
@allure.story("Update user")
@allure.title("Patch user from API class")

def test_patch_user_from_api_class():
    api = UsersAPI()
    with allure.step("Send PATCH request"):
        response = api.patch_user(
            1,
            {
                "name": "Andrii PATCH"
            }
        )
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check patched user data"):
        assert data["name"] == "Andrii PATCH"

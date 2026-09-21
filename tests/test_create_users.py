from api.users_api import UsersAPI
from utils.allure_helpers import attach_response
from utils.response_validator import (
    assert_status_code,
    assert_content_type,
    assert_response_time
)
import allure

@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create new user")

def test_create_user(user_data):
    api = UsersAPI()
    with allure.step("Send POST request"):
        response = api.create_user(user_data)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 201)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check user data"):
        assert data["name"] == user_data["name"]
        assert data["username"] == user_data["username"]
        assert data["email"] == user_data["email"]
        assert "id" in data

@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user without email")

def test_create_user_with_missing_email():
    user_data = {
        "name": "Andrii",
        "username": "andrii_test"
    }
    api = UsersAPI()
    with allure.step("Send POST request"):
        response = api.create_user(user_data)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 201)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check user data"):
        assert data["name"] == "Andrii"
        assert data["username"] == "andrii_test"
        assert "email" not in data

@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user without email")

def test_create_user_with_headers(user_data):
    api = UsersAPI()
    with allure.step("Send POST request with headers"):
        response = api.create_user_with_headers(user_data)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 201)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check user data"):
        assert data["name"] == user_data["name"]
        assert data["username"] == user_data["username"]
        assert data["email"] == user_data["email"]
        assert "id" in data

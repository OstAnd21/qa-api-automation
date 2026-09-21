from api.users_api import UsersAPI
from utils.allure_helpers import attach_response
from utils.response_validator import(
    assert_status_code,
    assert_content_type,
    assert_response_time
    )
import pytest
import allure

pytestmark = allure.feature("Users API")
@allure.story("Get user by username")
@allure.title("Get users by username: {username}")
@pytest.mark.parametrize("username", [
    "Bret",
    "Antonette",
    "Samantha"
])
def test_get_users_by_different_usernames(username):
    api = UsersAPI()
    response = api.get_users_by_username(username)
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time(response.elapsed_time, 2)
    data = response.json()
    assert len(data) > 0
    for user in data:
        assert user["username"] == username

@allure.story("Get user")
@allure.title("Get user by ID")
def test_get_user(user_id):
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
    attach_response(response)
    with allure.step("Check user data"):
        assert data["id"] == 1
        assert data["name"] == "Leanne Graham"
        assert data["username"] == "Bret"
        assert data["email"] == "Sincere@april.biz"
        
@allure.story("Get user")
@allure.title("Get nonexistent user")
def test_get_nonexistent_user():
    api = UsersAPI()
    response = api.get_user(9999)
    assert_status_code(response, 404)
    assert_response_time(response.elapsed_time, 2)

@allure.story("Get user")
@allure.title("Check user content type")
def test_get_user_content_type(user_id):
    api = UsersAPI()
    response = api.get_user(user_id)
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time(response.elapsed_time, 2)

@allure.story("Get user by username")
@allure.title("Get user by username")
def test_get_user_by_username():
    api = UsersAPI()
    response = api.get_users_by_username("Bret")
    attach_response(response)
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time(response.elapsed_time, 2)
    data = response.json()
    assert len(data) > 0
    assert data[0]["username"] == "Bret"

@allure.story("Get user by username")
@allure.title("Check only matching users are returned")
def test_get_user_by_username_only_matching():
    api = UsersAPI()
    response = api.get_users_by_username("Bret")
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time(response.elapsed_time, 2)
    data = response.json()
    for user in data:
        assert user["username"] == "Bret"

@allure.story("Get user by username")
@allure.title("Check username filter in URL")
def test_get_user_by_username_url():
    api = UsersAPI()
    response = api.get_users_by_username("Bret")
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time(response.elapsed_time, 2)
    assert "username=Bret" in response.url
    
def test_get_users_with_headers():
    api = UsersAPI()
    response = api.get_users_by_username("Bret")
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

@allure.story("Get users")
@allure.title("Get users with headers")
def test_get_users_with_session():
    api = UsersAPI()
    response = api.get_users_with_headers()
    assert_status_code(response, 200)
    assert_content_type(response, "application/json")
    assert_response_time(response.elapsed_time, 2)
    data = response.json()
    assert len(data) > 0

@allure.story("Get user")
@allure.title("Check status code for different user IDs")
@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (9999, 404)
])
def test_get_user_status(user_id, expected_status):
    api = UsersAPI()
    response = api.get_user(user_id)
    assert_status_code(response, expected_status)
    assert_response_time(response.elapsed_time, 2)
    
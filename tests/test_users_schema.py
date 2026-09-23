from jsonschema import validate
from api.users_api import UsersAPI
from schemas.user_schema import user_schema, users_schema
from utils.allure_helpers import attach_response
from utils.response_validator import (
    assert_status_code,
    assert_content_type,
    assert_response_time
)
import allure

@allure.feature("Users API")
@allure.story("Schema validation")
@allure.title("Validate single user schema")
def test_get_user_schema():
    api = UsersAPI()
    with allure.step("Send GET request"):
        response = api.get_user(1)
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Validate user schema"):
        validate(instance=data, schema=user_schema)

@allure.feature("Users API")
@allure.story("Schema validation")
@allure.title("Validate users list schema")
def test_get_users_schema():
    api = UsersAPI()
    with allure.step("Send GET request"):
        response = api.get_users_session()
    attach_response(response)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Check content type"):
        assert_content_type(response, "application/json")
    with allure.step("Check response time"):
        assert_response_time(response.elapsed_time, 2)
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Validate users schema"):
        validate(instance=data, schema=users_schema)

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from schemas.user_schema import user_schema
import copy
import pytest
import allure

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid user field: {field}")
@pytest.mark.parametrize("field, invalid_value", [
    ("id", "wrong_id"),
    ("email", 12345),
    ("name", 12345),
    ("username", 12345),
    ("phone", 12345),
    ("website", 12345),
])
def test_user_schema_invalid_field(valid_user, field, invalid_value):
    invalid_user = copy.deepcopy(valid_user)
    with allure.step(f"Set invalid value for field: {field}"):
        invalid_user[field] = invalid_value
    with allure.step("Validate user schema"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid address field: {field}")        
@pytest.mark.parametrize("field, invalid_value", [
    ("city", 12345),
    ("street", 12345),
    ("suite", 12345),
    ("zipcode", 12345),
])
def test_user_schema_invalid_address_field(valid_user, field, invalid_value):
    invalid_user = copy.deepcopy(valid_user)
    with allure.step(f"Set invalid value for address field: {field}"):
        invalid_user["address"][field] = invalid_value
    with allure.step("Validate user schema"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid geo field: {field}")       
@pytest.mark.parametrize("field, invalid_value", [
    ("lat", 12345),
    ("lng", 12345),
])
def test_user_schema_invalid_geo_field(valid_user, field, invalid_value):
    invalid_user = copy.deepcopy(valid_user)
    with allure.step(f"Set invalid value for geo field: {field}"):
        invalid_user["address"]["geo"][field] = invalid_value
    with allure.step("Validate user schema"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid company field: {field}")      
@pytest.mark.parametrize("field, invalid_value", [
    ("name", 12345),
    ("catchPhrase", 12345),
    ("bs", 12345),
])
def test_user_schema_invalid_company_field(valid_user, field, invalid_value):
    invalid_user = copy.deepcopy(valid_user)
    with allure.step(f"Set invalid value for company field: {field}"):
        invalid_user["company"][field] = invalid_value
    with allure.step("Validate user schema"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

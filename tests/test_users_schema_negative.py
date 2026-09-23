from jsonschema import validate
from jsonschema.exceptions import ValidationError
from schemas.user_schema import user_schema
import pytest
import copy
import allure

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid user ID type")
def test_user_schema_invalid_id(valid_user):
    invalid_user = copy.deepcopy(valid_user)
    invalid_user["id"] = "1"
    with allure.step("Validate invalid user data"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid email type")
def test_user_schema_invalid_email(valid_user):
    invalid_user = copy.deepcopy(valid_user)
    invalid_user["email"] = 12345
    with allure.step("Validate invalid user data"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid address field type")
def test_user_schema_invalid_address(valid_user):
    invalid_user = copy.deepcopy(valid_user)
    invalid_user["address"]["city"] = 12345
    with allure.step("Validate invalid user data"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject invalid geo latitude type")
def test_user_schema_invalid_geo_lat(valid_user):
    invalid_user = copy.deepcopy(valid_user)
    invalid_user["address"]["geo"]["lat"] = 12345
    with allure.step("Validate invalid user data"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

@allure.feature("Users API")
@allure.story("Negative schema validation")
@allure.title("Reject unexpected company field")
def test_user_schema_invalid_company_extra_field(valid_user):
    invalid_user = copy.deepcopy(valid_user)
    invalid_user["company"]["extra"] = "unexpected"
    with allure.step("Validate invalid user data"):
        with pytest.raises(ValidationError):
            validate(instance=invalid_user, schema=user_schema)

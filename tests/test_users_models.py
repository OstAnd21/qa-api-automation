from pydantic import ValidationError
from api.users_api import UsersAPI
from copy import deepcopy
from unittest.mock import patch
from models.user import (
    UserResponse,
    UserCreateRequest,
    UserPatchRequest,
    UserUpdateRequest,
    )
import pytest


def test_user_response_model(valid_user):
    user = UserResponse.model_validate(valid_user)
    assert user.id == 1
    assert user.name == "Leanne Graham"
    assert user.username == "Bret"
    assert user.email == "Sincere@april.biz"

def test_user_response_model_invalid():
    invalid_user = {
        "id": "wrong",
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }
    with pytest.raises(ValidationError):
        UserResponse.model_validate(invalid_user)
        
def test_get_user_model():
    api = UsersAPI()
    user = api.get_user_model(1)
    assert user.id == 1
    assert user.name == "Leanne Graham"
    assert user.username == "Bret"
    assert user.email == "Sincere@april.biz"
    assert user.address.city == "Gwenborough"
    assert user.address.geo.lat == "-37.3159"
    assert user.address.geo.lng == "81.1496"
    assert user.company.name == "Romaguera-Crona"
    
def test_user_response_model_invalid_nested_data(valid_user):
    invalid_user = deepcopy(valid_user)
    invalid_user["address"]["geo"]["lat"] = 123
    with pytest.raises(ValidationError):
        UserResponse.model_validate(invalid_user)
        
def test_get_user_model_types():
    api = UsersAPI()
    user = api.get_user_model(1)
    assert isinstance(user.id, int)
    assert isinstance(user.name, str)
    assert isinstance(user.username, str)
    assert isinstance(user.email, str)
    assert isinstance(user.address.city, str)
    assert isinstance(user.address.geo.lat, str)
    assert isinstance(user.company.name, str)
    
def test_user_create_request_model():
    user_data = {
        "name": "Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    user = UserCreateRequest.model_validate(user_data)
    assert user.name == "Andrii"
    assert user.username == "andrii_test"
    assert user.email == "andrii@example.com"
    
def test_user_create_request_model_invalid():
    invalid_user = {
        "name": "Andrii",
        "username": "andrii_test",
        "email": 123
    }
    with pytest.raises(ValidationError):
        UserCreateRequest.model_validate(invalid_user)

def test_create_user_invalid_data_does_not_send_request():
    api = UsersAPI()
    invalid_user = {
        "name": "Andrii",
        "username": "andrii_test",
        "email": 123
    }
    with patch.object(api.session, "request") as mock_request:
        with pytest.raises(ValidationError):
            api.create_user(invalid_user)
        mock_request.assert_not_called()
        
def test_user_patch_request_model():
    user_data = {
        "name": "Patched Andrii"
    }
    user = UserPatchRequest.model_validate(user_data)
    assert user.name == "Patched Andrii"
    assert user.username is None
    assert user.email is None

def test_user_patch_request_model_invalid():
    invalid_user = {
        "name": 123
    }
    with pytest.raises(ValidationError):
        UserPatchRequest.model_validate(invalid_user)

def test_user_update_request_model():
    user_data = {
        "name": "Updated Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    user = UserUpdateRequest.model_validate(user_data)
    assert user.name == "Updated Andrii"
    assert user.username == "andrii_test"
    assert user.email == "andrii@example.com"
    
def test_user_update_request_model_invalid():
    invalid_user = {
        "name": "Updated Andrii",
        "username": "andrii_test"
    }
    with pytest.raises(ValidationError):
        UserUpdateRequest.model_validate(invalid_user)

from unittest.mock import Mock, patch, call
from api.users_api import UsersAPI
from jsonschema import validate
from schemas.user_schema import user_schema
from utils.response_validator import (
    assert_status_code,
    assert_content_type,
    assert_response_time
)
import pytest
import requests
import allure

@allure.feature("Users API")
@allure.story("Mock testing")
@allure.title("Get user with mock")
def test_get_user_mock(api_mock):
    api, mock_request = api_mock
    mock_request.return_value.json.return_value = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }
    with allure.step("Send mocked GET request"):
        response = api.get_user(1)
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check user data"):
        assert data["id"] == 1
        assert data["username"] == "Bret"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        )

@allure.feature("Users API")
@allure.story("Mock testing")
@allure.title("Get nonexistent user with mock")
def test_get_nonexistent_user_mock(api_mock):
    api, mock_request = api_mock
    with allure.step("Configure mocked 404 response"):
        mock_request.return_value.status_code = 404
        mock_request.return_value.json.return_value = {
            "error": "User not found"
        }
    with allure.step("Send mocked GET request"):
        response = api.get_user(9999)
    with allure.step("Check status code"):
        assert response.status_code == 404
    with allure.step("Check error message"):
        assert response.json()["error"] == "User not found"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/9999",
            params=None,
            headers=None,
            timeout=None
        )

@allure.feature("Users API")
@allure.story("Mock testing")
@allure.title("Create user with mock")
def test_create_user_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    with allure.step("Configure mocked response"):
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = {
            "id": 11,
            "name": "Andrii",
            "username": "andrii_test",
            "email": "andrii@example.com"
        }
    with allure.step("Send mocked POST request"):
        response = api.create_user(user_data)
    with allure.step("Check status code"):
        assert response.status_code == 201
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check created user data"):
        assert data["id"] == 11
        assert data["name"] == user_data["name"]
        assert data["username"] == user_data["username"]
        assert data["email"] == user_data["email"]
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "POST",
            "https://jsonplaceholder.typicode.com/users",
            json=user_data,
            headers=None
        )
 
@allure.feature("Users API")
@allure.story("Mock testing")
@allure.title("Update user with mock") 
def test_update_user_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Updated Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    with allure.step("Configure mocked response"):
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {
            "id": 1,
            "name": "Updated Andrii",
            "username": "andrii_test",
            "email": "andrii@example.com"
        }
    with allure.step("Send mocked PUT request"):
        response = api.update_user(1, user_data)
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check updated user data"):
        assert data["id"] == 1
        assert data["name"] == "Updated Andrii"
        assert data["email"] == "andrii@example.com"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "PUT",
            "https://jsonplaceholder.typicode.com/users/1",
            json=user_data,
            headers=None
        )
        
@allure.feature("Users API")
@allure.story("Mock testing")
@allure.title("Patch user with mock")
def test_patch_user_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Patched Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    with allure.step("Configure mocked response"):
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {
            "id": 1,
            "name": "Patched Andrii",
            "username": "andrii_test",
            "email": "andrii@example.com"
        }
    with allure.step("Send mocked PATCH request"):
        response = api.patch_user(1, user_data)
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check patched user data"):
        assert data["id"] == 1
        assert data["name"] == "Patched Andrii"
        assert data["email"] == "andrii@example.com"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "PATCH",
            "https://jsonplaceholder.typicode.com/users/1",
            json=user_data,
            headers=None
        )

@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle timeout with mock")
def test_get_user_timeout_mock(api_mock):
    api, mock_request = api_mock
    with allure.step("Configure mocked timeout"):
        mock_request.side_effect = requests.exceptions.Timeout
    with allure.step("Send mocked GET request"):
        with pytest.raises(requests.exceptions.Timeout):
            api.get_user(1)
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        )
    
@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle connection error with mock")     
def test_get_user_server_error_mock(api_mock):
    api, mock_request = api_mock
    with allure.step("Configure mocked connection error"):
        mock_request.side_effect = requests.exceptions.ConnectionError
    with allure.step("Send mocked GET request"):
        with pytest.raises(requests.exceptions.ConnectionError):
            api.get_user(1)
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        )

@allure.feature("Users API")
@allure.story("Get user")
@allure.title("Get users by username with mock")
def test_get_users_by_username_mock(api_mock):
    api, mock_request = api_mock
    mock_request.return_value.json.return_value = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz"
        }
    ]
    with allure.step("Send mocked GET request by username"):
        response = api.get_users_by_username("Bret")
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check returned user"):
        assert len(data) == 1
        assert data[0]["username"] == "Bret"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users",
            params={"username": "Bret"},
            headers=None,
            timeout=None
        )

@allure.feature("Users API")
@allure.story("Request headers")
@allure.title("Get users with headers using mock")
def test_get_users_with_headers_mock(api_mock):
    api, mock_request = api_mock
    with allure.step("Send mocked GET request with headers"):
        response = api.get_users_with_headers()
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Verify HTTP request headers"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users",
            params=None,
            headers={"Accept": "application/json"},
            timeout=None
        )
        
@allure.feature("Users API")
@allure.story("Create user")
@allure.title("Create user with headers using mock")
def test_create_user_with_headers_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    with allure.step("Configure mocked response"):
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = {
            "id": 11,
            "name": "Andrii",
            "username": "andrii_test",
            "email": "andrii@example.com"
        }
    with allure.step("Send mocked POST request with headers"):
        response = api.create_user_with_headers(user_data)
    with allure.step("Check status code"):
        assert response.status_code == 201
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check created user data"):
        assert data["id"] == 11
        assert data["name"] == "Andrii"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "POST",
            "https://jsonplaceholder.typicode.com/users",
            json=user_data, headers={"Content-Type": "application/json"}
        )
        
@allure.feature("Users API")
@allure.story("Delete user")
@allure.title("Delete nonexistent user with mock")
def test_delete_nonexistent_user_mock(api_mock):
    api, mock_request = api_mock
    with allure.step("Configure mocked 404 response"):
        mock_request.return_value.status_code = 404
        mock_request.return_value.json.return_value = {
            "error": "User not found"
        }
    with allure.step("Send mocked DELETE request"):
        response = api.delete_user(9999)
    with allure.step("Check status code"):
        assert response.status_code == 404
    with allure.step("Check error message"):
        assert response.json()["error"] == "User not found"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "DELETE",
            "https://jsonplaceholder.typicode.com/users/9999",
            headers=None
        )

@allure.feature("Users API")
@allure.story("Mock testing")
@allure.title("Delete user with mock")
def test_delete_user_mock(api_mock):
    api, mock_request = api_mock
    with allure.step("Configure mocked response"):
        mock_request.return_value.status_code = 200
    with allure.step("Send mocked DELETE request"):
        response = api.delete_user(1)
    with allure.step("Check status code"):
        assert_status_code(response, 200)
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "DELETE",
            "https://jsonplaceholder.typicode.com/users/1",
            headers=None
        )

@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle connection error when creating user with mock")
def test_create_user_connection_error_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    with allure.step("Configure mocked connection error"):
        mock_request.side_effect = requests.exceptions.ConnectionError
    with allure.step("Send mocked POST request"):
        with pytest.raises(requests.exceptions.ConnectionError):
            api.create_user(user_data)
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "POST",
            "https://jsonplaceholder.typicode.com/users",
            json=user_data,
            headers=None
        )

@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle server error when updating user with mock")
def test_update_user_server_error_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Updated Andrii",
        "username": "andrii_test",
        "email": "andrii@example.com"
    }
    with allure.step("Configure mocked 500 response"):
        mock_request.return_value.status_code = 500
        mock_request.return_value.json.return_value = {
            "error": "Internal Server Error"
        }
    with allure.step("Send mocked PUT request"):
        response = api.update_user(1, user_data)
    with allure.step("Check status code"):
        assert response.status_code == 500
    with allure.step("Check error message"):
        assert response.json()["error"] == "Internal Server Error"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "PUT",
            "https://jsonplaceholder.typicode.com/users/1",
            json=user_data,
            headers=None
        )

@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle timeout when patching user with mock")
def test_patch_user_timeout_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Patched Andrii"
    }
    with allure.step("Configure mocked timeout"):
        mock_request.side_effect = requests.exceptions.Timeout
    with allure.step("Send mocked PATCH request"):
        with pytest.raises(requests.exceptions.Timeout):
            api.patch_user(1, user_data)
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "PATCH",
            "https://jsonplaceholder.typicode.com/users/1",
            json=user_data,
            headers=None
        )
        
@allure.feature("Users API")
@allure.story("Error handling")
@allure.title("Handle server error when patching user with mock")
def test_patch_user_server_error_mock(api_mock):
    api, mock_request = api_mock
    user_data = {
        "name": "Patched Andrii"
    }
    with allure.step("Configure mocked 500 response"):
        mock_request.return_value.status_code = 500
        mock_request.return_value.json.return_value = {
            "error": "Internal Server Error"
        }
    with allure.step("Send mocked PATCH request"):
        response = api.patch_user(1, user_data)
    with allure.step("Check status code"):
        assert response.status_code == 500
    with allure.step("Check error message"):
        assert response.json()["error"] == "Internal Server Error"
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "PATCH",
            "https://jsonplaceholder.typicode.com/users/1",
            json=user_data,
            headers=None
        )
        
@allure.feature("Users API")
@allure.story("Multiple responses")
@allure.title("Handle multiple mocked responses")
def test_get_user_multiple_responses_mock(api_mock):
    api, mock_request = api_mock
    response_200 = Mock()
    response_200.status_code = 200
    response_200.json.return_value = {
        "id": 1,
        "name": "Leanne Graham"
    }
    response_404 = Mock()
    response_404.status_code = 404
    response_404.json.return_value = {
        "error": "User not found"
    }
    mock_request.side_effect = [
        response_200,
        response_404
    ]
    with allure.step("Send first mocked GET request"):
        response_1 = api.get_user(1)
    with allure.step("Send second mocked GET request"):
        response_2 = api.get_user(9999)
    with allure.step("Check first response"):
        assert response_1.status_code == 200
        assert response_1.json()["id"] == 1
    with allure.step("Check second response"):
        assert response_2.status_code == 404
        assert response_2.json()["error"] == "User not found"
    with allure.step("Verify number of HTTP requests"):
        assert mock_request.call_count == 2

@allure.feature("Users API")
@allure.story("Request verification")
@allure.title("Verify multiple mocked GET requests")
def test_get_user_multiple_calls_mock(api_mock):
    api, mock_request = api_mock
    mock_request.return_value.json.return_value = {
        "id": 1,
        "name": "Leanne Graham"
    }
    with allure.step("Send first mocked GET request"):
        api.get_user(1)
    with allure.step("Send second mocked GET request"):
        api.get_user(2)
    with allure.step("Check number of HTTP requests"):
        assert mock_request.call_count == 2
    expected_calls = [
        call(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        ),
        call(
            "GET",
            "https://jsonplaceholder.typicode.com/users/2",
            params=None,
            headers=None,
            timeout=None
        )
    ]
    with allure.step("Verify HTTP request calls"):
        mock_request.assert_has_calls(expected_calls)

@allure.feature("Users API")
@allure.story("Mock fixture")
@allure.title("Get user using mock fixture")
def test_get_user_with_fixture(api_mock):
    api, mock_request = api_mock
    with allure.step("Send mocked GET request"):
        response = api.get_user(1)
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        )
    
@pytest.mark.parametrize("status_code", [200, 201, 400, 404, 500])
@allure.feature("Users API")
@allure.story("Status codes")
@allure.title("Get user with status code: {status_code}")
def test_get_user_different_status_codes(api_mock, status_code):
    api, mock_request = api_mock
    with allure.step("Configure mocked status code"):
        mock_request.return_value.status_code = status_code
    with allure.step("Send mocked GET request"):
        response = api.get_user(1)
    with allure.step("Check status code"):
        assert response.status_code == status_code
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        )
    
@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
])
@allure.feature("Users API")
@allure.story("Get user")
@allure.title("Get user with ID: {user_id}")
def test_get_user_different_users_mock(api_mock, user_id, expected_name):
    api, mock_request = api_mock
    mock_request.return_value.json.return_value = {
        "id": user_id,
        "name": expected_name
    }
    with allure.step("Send mocked GET request"):
        response = api.get_user(user_id)
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Check user data"):
        assert data["id"] == user_id
        assert data["name"] == expected_name
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            params=None,
            headers=None,
            timeout=None
        )

@allure.feature("Users API")
@allure.story("Schema validation")
@allure.title("Validate mocked user schema")
def test_get_user_schema_mock(api_mock):
    api, mock_request = api_mock
    mock_request.return_value.json.return_value = {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                  "lat": "-37.3159",
                  "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
            }
        }
    with allure.step("Send mocked GET request"):
        response = api.get_user(1)
    with allure.step("Check status code"):
        assert response.status_code == 200
    with allure.step("Parse response JSON"):
        data = response.json()
    with allure.step("Validate user schema"):
        validate(instance=data, schema=user_schema)
    with allure.step("Verify HTTP request"):
        mock_request.assert_called_once_with(
            "GET",
            "https://jsonplaceholder.typicode.com/users/1",
            params=None,
            headers=None,
            timeout=None
        )
        
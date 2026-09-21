import pytest
from unittest.mock import Mock, patch
from api.users_api import UsersAPI
from test_data.users_data import NEW_USER, USER_ID, VALID_USER

@pytest.fixture
def user_data():
    return NEW_USER

@pytest.fixture
def user_id():
    return USER_ID

@pytest.fixture
def api_mock():
    api = UsersAPI()
    mock_response = Mock()
    mock_response.status_code = 200
    with patch.object(
        api.session,
        "request",
        return_value=mock_response
    ) as mock_request:
        yield api, mock_request
        
@pytest.fixture
def valid_user():
    return VALID_USER
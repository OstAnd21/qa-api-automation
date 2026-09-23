from unittest.mock import Mock, patch
from api.users_api import UsersAPI
from test_data.users_data import NEW_USER, USER_ID, VALID_USER
import pytest

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

def pytest_collection_modifyitems(items):
    regression_marker = pytest.mark.regression
    for item in items:
        item.add_marker(regression_marker)
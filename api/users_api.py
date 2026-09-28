from config import settings
from api.base_api import BaseAPI
from models.user import (
    UserResponse,
    UserCreateRequest,
    UserPatchRequest,
    UserUpdateRequest,
    )

class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__(settings.BASE_URL)

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, data):
        user = UserCreateRequest.model_validate(data)
        return self.post("/users", data)

    def update_user(self, user_id, data):
        user = UserUpdateRequest.model_validate(data)
        return self.put(
            f"/users/{user_id}",
            user.model_dump()
        )

    def patch_user(self, user_id, data):
        user = UserPatchRequest.model_validate(data)
        return self.patch(
            f"/users/{user_id}",
            user.model_dump(exclude_none = True)
        )

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")

    def get_users_by_username(self, username):
        return self.get(
            "/users",
            params={"username": username}
        )

    def get_users_with_headers(self):
        headers = {
            "Accept": "application/json"
        }
        return self.get(
            "/users",
            headers=headers
        )

    def get_users_session(self):
        return self.get("/users")

    def create_user_with_headers(self, user_data):
        return self.post("/users", user_data)

    def get_users_from_invalid_url(self):
        return self.get(
            "https://invalid-url-example-12345.com",
            timeout=2
        )

    def get_users_with_timeout(self):
        return self.get(
            "https://httpbin.org/delay/3",
            timeout=1
        )

    def get_user_model(self, user_id):
        response = self.get(f"/users/{user_id}")
        return UserResponse.model_validate(response.json())
    
    
from config import BASE_URL
from api.base_api import BaseAPI

class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__(BASE_URL)
    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")
    def create_user(self, data):
        return self.post("/users", data)
    def update_user(self, user_id, data):
        return self.put(f"/users/{user_id}", data)
    def patch_user(self, user_id, data):
        return self.patch(f"/users/{user_id}", data)
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
        headers = {
            "Content-Type": "application/json"
        }
        return self.post(
            "/users",
            user_data,
            headers=headers
        )
    def get_users_from_invalid_url(self):
        return self.session.get(
            "https://invalid-url-example-12345.com",
            timeout=2
        )
    def get_users_with_timeout(self):
        return self.session.get(
            "https://httpbin.org/delay/3",
            timeout=1
        )
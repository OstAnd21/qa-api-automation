from utils.logger import logger
import requests
import time

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json"
        })

    def get(self, endpoint, params=None, headers=None, timeout=None):
        return self._request(
            "GET",
            endpoint,
            params=params,
            headers=headers,
            timeout=timeout
        )

    def post(self, endpoint, data, headers=None):
        return self._request(
            "POST",
            endpoint,
            json=data,
            headers=headers
        )

    def put(self, endpoint, data, headers=None):
        return self._request(
            "PUT",
            endpoint,
            json=data,
            headers=headers
        )

    def patch(self, endpoint, data, headers=None):
        return self._request(
            "PATCH",
            endpoint,
            json=data,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return self._request(
            "DELETE",
            endpoint,
            headers=headers
        )

    def _request(self, method, endpoint, **kwargs):
        if endpoint.startswith(("http://", "https://")):
            url = endpoint
        else:
            url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending {method} request: {url}")
        start_time = time.perf_counter()
        response = self.session.request(
            method,
            url,
            **kwargs
        )
        elapsed_time = time.perf_counter() - start_time
        logger.info(
            f"Response status: {response.status_code} | "
            f"Time: {elapsed_time:.3f}s"
        )
        response.elapsed_time = elapsed_time
        return response

def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}"
    )
    
def assert_content_type(response, expected_content_type):
    actual_content_type = response.headers.get("Content-Type", "")
    assert expected_content_type in actual_content_type, (
        f"Expected Content-Type to contain '{expected_content_type}', "
        f"but got '{actual_content_type}'"
    )
    
def assert_response_time(elapsed_time, max_time):
    assert elapsed_time <= max_time, (
        f"Expected response time <= {max_time}s, "
        f"but got {elapsed_time:.3f}s"
    )
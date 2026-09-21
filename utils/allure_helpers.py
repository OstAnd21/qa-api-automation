import allure

def attach_response(response):
    allure.attach(
        str(response.status_code),
        name="Status code",
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.JSON
    )
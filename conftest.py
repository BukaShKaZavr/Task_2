import pytest
import api_methods
import api_requests

@pytest.fixture(scope="function")
def requests_object():
    return api_requests.RequestsApi()

@pytest.fixture(scope="function")
def create_and_delete_user(requests_object):
    user = api_methods.register_new_user_and_return_login_password()

    yield user
    headers = {"Authorization": user[2]}
    requests_object.delete_user(headers)
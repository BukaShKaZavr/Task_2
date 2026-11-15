import allure
import pytest
import data
import helpers


class TestUserLogin:

    @allure.title('Позитивная проверка логина пользователя')
    def test_user_login_success(self, requests_object, create_and_delete_user):
        user = create_and_delete_user
        payload = {'email': user[0], 'password': user[1]}

        response = requests_object.login_user(payload)

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Негативная проверка логина пользователя, неправильные данные входа')
    @pytest.mark.parametrize(
        'payload_field',
        [
            {"email": helpers.generate_random_strings(5), "password": helpers.generate_random_strings(5)},
            {"email": "", "password": helpers.generate_random_strings(5)},
            {"email": helpers.generate_random_strings(5), "password": ""},
        ])
    def test_user_login_fail(self, requests_object, payload_field):
        payload = payload_field
        response = requests_object.login_user(payload)

        assert response.status_code == 401
        assert response.json()['message'] == data.incorrect_login_data_msg
import allure
import pytest
import data
import helpers


class TestChangeUserData:

    @allure.title('Позитивная проверка изменений данных пользователя')
    @pytest.mark.parametrize(
        'payload_field',
        [
            {"email": f'{helpers.generate_random_strings(5)}@test.ru'},
            {"name": helpers.generate_random_strings(5)}
        ])
    def test_change_user_data(self, create_and_delete_user, requests_object, payload_field):
        user = create_and_delete_user
        payload = payload_field
        response = requests_object.change_user_data(user[2], payload)

        assert response.status_code == 200
        user_data = response.json()['user']
        for key, value in payload.items():
            current_data = user_data[key]
            assert current_data == value

    @allure.title('Негативная проверка изменений данных пользователя неавторизованным аккаунтом')
    @pytest.mark.parametrize(
        'payload_field',
        [
            {"email": f'{helpers.generate_random_strings(5)}@test.ru'},
            {"name": helpers.generate_random_strings(5)}
        ])
    def test_change_user_data_failure(self, requests_object, payload_field):
        payload = payload_field
        response = requests_object.change_user_data_without_auth(payload)

        assert response.status_code == 401
        assert response.json()["message"] == data.data_change_no_auth_msg
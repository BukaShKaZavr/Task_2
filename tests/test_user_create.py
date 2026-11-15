import allure
import pytest
import data
import helpers


class TestUserCreate:

    @allure.title('Позитивная проверка регистрации пользователя')
    def test_user_create_success(self, requests_object):
        payload = {
    "email": f'{helpers.generate_random_strings(5)}@test.ru',
    "password": helpers.generate_random_strings(5),
    "name": helpers.generate_random_strings(5)
        }
        response = requests_object.create_user(payload)
        r = response.json()

        assert response.status_code == 200
        assert r["success"] == True

    @allure.title('Негативная проверка регистрации уже существующего пользователя')
    def test_register_existing_user(self, create_and_delete_user, requests_object):
        user = create_and_delete_user

        payload = {
            "email": user[0],
            "password": helpers.generate_random_strings(5),
            "name": helpers.generate_random_strings(5)
        }
        response = requests_object.create_user(payload)
        r = response.json()

        assert response.status_code == 403
        assert r["message"] == data.existing_user_msg

    @allure.title('Негативная проверка регистрации пользователя, не заполнение обязательных полей')
    @pytest.mark.parametrize(
        'payload_field',
        [
            {"email": f'{helpers.generate_random_strings(5)}@test.ru', "password": "", "name": helpers.generate_random_strings(5)},
            {"email": "", "password": helpers.generate_random_strings(5), "name": helpers.generate_random_strings(5)},
            {"email": f'{helpers.generate_random_strings(5)}@test.ru', "password": helpers.generate_random_strings(5), "name": ""}
        ])
    def test_register_user_failure(self, requests_object, payload_field):
        payload = payload_field
        response = requests_object.create_user(payload)
        r = response.json()

        assert response.status_code == 403
        assert r['message'] == data.missing_register_fields_msg


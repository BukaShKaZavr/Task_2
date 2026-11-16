import random
import allure
import api_methods
import data


class TestCreateOrder:

    @allure.title('Позитивная проверка создания заказа неавторизированным пользователем')
    def test_create_order_no_auth_success(self, requests_object):
        ingredients = api_methods.get_ingredients()
        payload = {"ingredients": random.sample(ingredients, 3)}

        response = requests_object.create_order_without_auth(payload)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Позитивная проверка создания заказа авторизированным пользователем')
    def test_create_order_with_auth_success(self, create_and_delete_user, requests_object):
        user = create_and_delete_user
        ingredients = api_methods.get_ingredients()
        payload = {"ingredients": random.sample(ingredients, 3)}

        response = requests_object.create_order_with_auth(user[2], payload)

        expected_ingredients = []
        for ingredient in response.json()['order']['ingredients']:
            expected_ingredients.append(ingredient['_id'])

        assert response.status_code == 200
        assert expected_ingredients == payload['ingredients']

    @allure.title('Негативная проверка создания заказа без ингредиентов')
    def test_create_order_no_ingredients(self, requests_object):
        payload = {
            "ingredients": []
        }

        response = requests_object.create_order_without_auth(payload)
        assert response.status_code == 400
        assert response.json()['message'] == data.empty_ingredients_create_order_msg

    @allure.title('Негативная проверка создания заказа с опечаткой с хэше ингредиента')
    def test_create_order_invalid_id_same_amount_symbols(self, requests_object):
        payload = {
            "ingredients": data.invalid_hash_ingredient_same_amount_symbols
        }

        response = requests_object.create_order_without_auth(payload)
        assert response.status_code == 400
        assert response.json()['message'] == data.incorrect_ingredients_create_order_msg

    @allure.title('Негативная проверка создания заказа с неполным хэшем ингредиента')
    def test_create_order_invalid_id(self, requests_object):
        payload = {
            "ingredients": data.invalid_hash_ingredient
        }

        response = requests_object.create_order_without_auth(payload)
        assert response.status_code == 500


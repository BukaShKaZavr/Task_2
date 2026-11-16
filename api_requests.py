import allure
import requests
import urls

class RequestsApi:

    @allure.step('Делаем API запрос на регистрацию пользователя')
    def create_user(self, payload):
        return requests.post(urls.create_user_url, json=payload)

    @allure.step('Делаем API запрос на логин пользователя')
    def login_user(self, payload):
        return requests.post(urls.login_user_url, json=payload)

    @allure.step('Делаем API запрос на удаление пользователя')
    def delete_user(self, header):
        return requests.delete(urls.delete_user_url, headers = header)

    @allure.step('Делаем API запрос на изменение данных авторизированного пользователя')
    def change_user_data(self, header, payload):
        headers = {"Authorization": header}
        return requests.patch(urls.change_user_data_url, headers = headers, json=payload)

    @allure.step('Делаем API запрос на изменение данных без авторизации')
    def change_user_data_without_auth(self, payload):
        return requests.patch(urls.change_user_data_url, json=payload)

    @allure.step('Делаем API запрос на создание заказа без авторизации пользователя')
    def create_order_without_auth(self, payload):
        return requests.post(urls.create_order_url, json=payload)

    @allure.step('Делаем API запрос на моздание заказа авторизированным пользователем')
    def create_order_with_auth(self, header, payload):
        headers = {"Authorization": header}
        return requests.post(urls.create_order_url, headers=headers, json=payload)

    @allure.step('Делаем API запрос на получение списка ингредиентов')
    def get_ingredients_list(self):
        return requests.get(urls.ingredients_url)

    @allure.step('Делаем API запрос на получение списка заков без авторизации пользователем')
    def order_list_without_auth(self):
        return requests.get(urls.get_orders_url)

    @allure.step('Делаем API запрос на получение списка заказов авторизованным пользователем')
    def order_list_with_auth(self, header):
        headers = {"Authorization": header}
        return requests.get(urls.get_orders_url, headers = headers)
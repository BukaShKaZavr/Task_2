import allure
import data


class TestGetOrders:

    @allure.title('Позитивная проверка получения списка заказов авторизованным пользователем')
    def test_get_orders_with_auth(self, requests_object, create_and_delete_user):
        user = create_and_delete_user
        response = requests_object.order_list_with_auth(user[2])

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Негативная проверка получения списка заказов неавторизованным пользователем')
    def test_get_orders_without_auth(self, requests_object):
        response = requests_object.order_list_without_auth()

        assert response.status_code == 401
        assert response.json()['message'] == data.get_order_no_auth_msg
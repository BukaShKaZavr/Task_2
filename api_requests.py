import requests
import urls

class RequestsApi:

    def create_user(self, payload):
        return requests.post(urls.create_user_url, json=payload)

    def login_user(self, payload):
        return requests.post(urls.login_user_url, json=payload)

    def delete_user(self, header):
        return requests.delete(urls.delete_user_url, headers = header)

    def change_user_data(self, header, payload):
        headers = {"Authorization": header}
        return requests.patch(urls.change_user_data_url, headers = headers, json=payload)

    def change_user_data_without_auth(self, payload):
        return requests.patch(urls.change_user_data_url, json=payload)

    def create_order_without_auth(self, payload):
        return requests.post(urls.create_order_url, json=payload)

    def create_order_with_auth(self, header, payload):
        headers = {"Authorization": header}
        return requests.post(urls.create_order_url, headers=headers, json=payload)

    def get_ingredients_list(self):
        return requests.get(urls.ingredients_url)

    def order_list_without_auth(self):
        return requests.get(urls.get_orders_url)

    def order_list_with_auth(self, header):
        headers = {"Authorization": header}
        return requests.get(urls.get_orders_url, headers = headers)
import configuration
import requests
import data
import configuration


def post_new_order(user_body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER_PATH,
                         json=user_body,
                         headers=data.headers)
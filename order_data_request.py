import requests
import configuration


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))

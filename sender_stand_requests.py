import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_NEW_ORDER , json=body, headers=data.headers)


def get_order_track(track):
    return requests.get(configuration.URL_SERVICE+configuration.GET_ORDERS+str(track))
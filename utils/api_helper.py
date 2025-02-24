import requests

class APIHelper:
    @staticmethod
    def get(url, headers=None):
        return requests.get(url, headers=headers)

    @staticmethod
    def post(url, data, headers=None):
        return requests.post(url, json=data, headers=headers)

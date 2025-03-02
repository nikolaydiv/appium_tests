import json
import requests


class ProfileFetcher:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.support_id = None


class TagsUpdater:

    def __init__(self, put_url, headers_put):
        self.put_url = put_url
        self.headers_put = headers_put

    def update_tags(self, value_1, value_2, value_3):
        payload = json.dumps({
            "your_profile_id": {
                "nicknameLowercase": "skip",
                "value_1": value_1,
                "value_2": 0.99,
                "value_3": 0.99,
                "value_4": 0.99,
                "value_5": 0.99,
                "value_6": 0.99,
                "value_7": 0.99,
                "value_8": 0.99,
                "dateFromLastPurch": 1710309974,
                "value_9": 1,
                "value_10": 1,
                "value_11": 1,
                "value_12": value_2,
                "value_13": 0.99,
                "value_14": 0.99,
                "value_15": 0.99,
                "value_16": 0.99,
                "value_17": 0.99,
                "value_18": 0.99,
                "value_19": 0.99,
                "value_20": 0.99,
                "value_21": 0.99,
                "value_22": 0.99,
                "value_23": 1,
                "value_24": 1,
                "value_25": 1,
                "value_26": 0.99,
                "value_27": 0.99,
                "value_28": 0.99,
                "value_29": 0.99,
                "value_30": 0.99,
                "value_31": 0.99,
                "value_32": 0,
                "value_33": 0.99,
                "value_34": 0.99,
                "value_35": 0.99,
                "value_36": 0,
                "value_37": 0.99,
                "value_38": 0.99,
                "value_39": value_3
            }
        })
        try:
            response = requests.request("PUT", self.put_url, headers=self.headers_put, data=payload, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при выполнении запроса: {e}')


put_url = "https://test_url.com"
headers_put = {
    'X-Application-Key': 'some_key',
    'Content-Type': 'application/json'
}
tags_updater = TagsUpdater(put_url, headers_put)


# TAGS 11

def update_tags_11_1_function():
    tags_updater.update_tags(0.99, 0.99, 0.99)


def update_tags_11_2_function():
    tags_updater.update_tags(2.5, 4, 0.99)


def update_tags_11_3_function():
    tags_updater.update_tags(3.5, 5, 0.99)


def update_tags_11_4_function():
    tags_updater.update_tags(4.5, 8, 0.99)


def update_tags_11_5_function():
    tags_updater.update_tags(4.5, 8, 18)


def update_tags_11_6_function():
    tags_updater.update_tags(6, 18, 18)


def update_tags_11_7_function():
    tags_updater.update_tags(6, 18, 37)


def update_tags_11_8_function():
    tags_updater.update_tags(10, 30, 37)


def update_tags_11_9_function():
    tags_updater.update_tags(10, 30, 61)


def update_tags_11_10_function():
    tags_updater.update_tags(20, 50, 61)


def update_tags_11_11_function():
    tags_updater.update_tags(20, 50, 121)


# TAGS 10

def update_tags_10_1_function():
    tags_updater.update_tags(0.99, 0.99, 0.99)


def update_tags_10_2_function():
    tags_updater.update_tags(2.5, 4, 0.99)


def update_tags_10_3_function():
    tags_updater.update_tags(3.5, 5, 0.99)


def update_tags_10_4_function():
    tags_updater.update_tags(4.5, 0.99, 17)


def update_tags_10_5_function():
    tags_updater.update_tags(6, 18, 18)


def update_tags_10_6_function():
    tags_updater.update_tags(6, 18, 37)


def update_tags_10_7_function():
    tags_updater.update_tags(10, 30, 37)


def update_tags_10_8_function():
    tags_updater.update_tags(10, 30, 61)


def update_tags_10_9_function():
    tags_updater.update_tags(20, 50, 61)


def update_tags_10_10_function():
    tags_updater.update_tags(20, 50, 121)


# TAGS 9

def update_tags_9_1_function():
    tags_updater.update_tags(0.99, 0.99, 0.99)


def update_tags_9_2_function():
    tags_updater.update_tags(2.5, 4, 0.99)


def update_tags_9_3_function():
    tags_updater.update_tags(3.5, 5, 0.99)


def update_tags_9_4_function():
    tags_updater.update_tags(4.5, 5, 17)


def update_tags_9_5_function():
    tags_updater.update_tags(6, 5, 24)


def update_tags_9_6_function():
    tags_updater.update_tags(10, 30, 24)


def update_tags_9_7_function():
    tags_updater.update_tags(10, 30, 61)


def update_tags_9_8_function():
    tags_updater.update_tags(20, 50, 61)


def update_tags_9_9_function():
    tags_updater.update_tags(20, 50, 121)


# TAGS 3


def update_tags_3_1_function():
    tags_updater.update_tags(0.99, 0.99, 0.99)


def update_tags_3_2_function():
    tags_updater.update_tags(5, 0.99, 0.99)


def update_tags_3_3_function():
    tags_updater.update_tags(10, 0.99, 0.99)

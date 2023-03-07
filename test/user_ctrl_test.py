import unittest
import requests


class TestUserCtrlAPI(unittest.TestCase):
    url = "http://localhost:8080/rest/user"

    insert_data = {
        "admin": {
            "EMAIL": "pkb@gmail.com"
        },
        "user": {
            "EMAIL": "test1@gmail.com",
            "NAME": "Test B"
        }
    }

    update_data = {
        "admin": {
            "EMAIL": "pkb@gmail.com"
        },
        "user": {
            "EMAIL": "test1@gmail.com",
            "NAME": "Test 1"
        }
    }

    def test1_get_all_user(self):
        response = requests.get(self.url + "/user-list")
        self.assertEqual(response.status_code, 200)
        print("Get All User Test Passed")

    def test2_insert_user(self):
        response = requests.post(self.url + "/insert", json=self.insert_data)
        self.assertEqual(response.status_code, 200)
        print("Insert User Test Passed")

    def test3_update_user(self):
        response = requests.put(self.url + "/update", json=self.update_data)
        self.assertEqual(response.status_code, 200)
        print("Update User Test Passed")


if __name__ == '__main__':
    testClassObj = TestUserCtrlAPI()
    testClassObj.test1_get_all_user()
    testClassObj.test2_insert_user()
    testClassObj.test3_update_user()

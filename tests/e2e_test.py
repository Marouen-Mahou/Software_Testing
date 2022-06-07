import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"

    #POST request to /hash/md5 returns hash of TEST
    def test_1_hash_md5(self):
        message = "TEST"
        expected = "\"033bd94b1168d7e4f0d644c3c95e35bf\"\n"

        r = requests.post("{}/hash/md5".format(ApiTest.API_URL), {"message": message})

        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected,r.text)

    #POST request to /hash/sha1 returns hash of TEST
    def test_2_hash_sha1(self):
        data = {"message": "TEST"}
        expected = "\"984816fd329622876e14907634264e6f332e9fb3\"\n"

        r = requests.post("{}/hash/sha1".format(ApiTest.API_URL), json=data )
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected, r.text)

    #POST request to /hash/sha256 returns hash of TEST
    def test_3_hash_sha256(self):
        data = {"message":"TEST"}
        expected = "\"94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2\"\n"

        r = requests.post("{}/hash/sha256".format(ApiTest.API_URL), json=data )

        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected, r.text )

    #POST request to /crack/md5 returns the hashed text TEST
    def test_4_crack_md5(self):
        # When Hash exists
        valid_data = {"message": "033bd94b1168d7e4f0d644c3c95e35bf", "lines": ["Test","Hello","TEST"]}
        invalid_data = {"message": "033bd94b1168d7e4f0d644c3c95e35bf", "lines": ["Test","Hello"]}

        expected_valid = "\"TEST\"\n"
        expected_invalid = "\"Hash not found\"\n"


        r = requests.post("{}/crack/md5".format(ApiTest.API_URL), json=valid_data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected_valid, r.text)

        # When Hash doesn't exist
        r = requests.post("{}/crack/md5".format(ApiTest.API_URL), json=invalid_data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected_invalid, r.text)

    #POST request to /crack/sha1 returns the hashed text TEST
    def test_5_crack_sha1(self):

        valid_data = {"message": "984816fd329622876e14907634264e6f332e9fb3", "lines": ["Test", "Hello", "TEST"]}
        invalid_data = {"message": "984816fd329622876e14907634264e6f332e9fb3", "lines": ["Test", "Hello"]}

        expected_valid = "\"TEST\"\n"
        expected_invalid = "\"Hash not found\"\n"

        r = requests.post("{}/crack/sha1".format(ApiTest.API_URL), json=valid_data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected_valid, r.text)

        #When Hash doesn't exist
        r = requests.post("{}/crack/sha1".format(ApiTest.API_URL), json=invalid_data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected_invalid, r.text)

    #POST request to /crack/sha256 returns the hashed text TEST
    def test_6_crack_sha256(self):
        valid_data = {"message": "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2", "lines": ["Test", "Hello", "TEST"]}
        invalid_data = {"message": "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2", "lines": ["Test", "Hello"]}

        expected_valid = "\"TEST\"\n"
        expected_invalid = "\"Hash not found\"\n"

        # When Hash exists
        lines = ["Test","Hello","TEST"]
        r = requests.post("{}/crack/sha256".format(ApiTest.API_URL), json=valid_data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected_valid, r.text)

        # When Hash doesn't exist
        lines = ["Test","Hello"]
        r = requests.post("{}/crack/sha256".format(ApiTest.API_URL), json=invalid_data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected_invalid, r.text)

    # Register and Login scenario tested
    def test_register_login(self):
        register_data = {
            "email":"marouen_test@gmail.com",
            "username":"marouen_mahou",
            "phone":"12345678",
            "password":"marouenpass"
        }

        login_data = {
            "email": "marouen_test@gmail.com",
            "password": "marouenpass"
        }

        expected_data = "Logged in"
        expected_status = 200

        # Register
        r = requests.post("{}/register".format(ApiTest.API_URL), json=register_data)
        self.assertEqual(expected_status, r.status_code)


        # Login
        r = requests.post("{}/login".format(ApiTest.API_URL), json=login_data)
        self.assertEqual(r.status_code, expected_status)
        self.assertEqual(expected_data, r.json()['message'])




if __name__ == '__main__':
    unittest.main()
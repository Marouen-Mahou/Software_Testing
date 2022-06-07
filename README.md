# Software Testing

## Unit tests
UNIT TESTING is a type of software testing where individual units or components of a software are tested. 
The purpose is to validate that each unit of the software code performs as expected. Unit Testing is done during the development (coding phase) of 
an application by the developers. Unit Tests isolate a section of code and verify its correctness. A unit may be an individual function, method, procedure, module, or object.

### How?
In our case we have a pool of functions in  functions.py that we are going to perform some unit tests on them using the python testing package unittests.


The tested functions are : 
- Hashing : :white_check_mark: MD5 - :white_check_mark: SHA1 - :white_check_mark: SHA256
- Cracking : :white_check_mark: MD5 - :white_check_mark: SHA1 - :white_check_mark: SHA256
- Encoding : :white_check_mark: Base8 - :white_check_mark: Base16 - :white_check_mark: Base32
- Cracking : :white_check_mark: Base8 - :white_check_mark: Base16 - :white_check_mark: Base32

We are going to use the *** assertEqual(expected, actual) *** of unittest package function to test every function if it is behaving like expected and returning 
the expected result.

```python
class UnitTest(unittest.TestCase):

    # TEST CRACK FUNCTION with md5 type
    def test_1_crack_md5(self):
        # When exists
        
        # Given
        message = "033bd94b1168d7e4f0d644c3c95e35bf"
        lines = ["Test", "Hello", "TEST"]
        expected = "TEST"
        
        # When
        result = Crack('md5', message, lines)
        
        # Then
        self.assertEqual(expected, result)

        # When doesn't exist
        
        # Given
        message = "033bd94b1168d7e4f0d644c3c95e35bf"
        lines = ["Test", "Hello"]
        expected = "Hash not found"
        
        # When
        result = Crack('md5', message, lines)

        # Then
        self.assertEqual(expected, result)
        
        
     # TEST HASH FUNCTION with sha256 type
     def test_5_hash_md5(self):
        # Given
        message = "TEST"
        expected = "033bd94b1168d7e4f0d644c3c95e35bf"
       
        # When
        result = Hash('md5', message)
        
        # Then
        self.assertEqual(expected, result)
```

In some cases like the attacks list there is a call to the Data Base but we are doing unit tests so we have to mock the result of the database call 
using the patch of the unittest.mock which allows us to simulate the Data Base call without actually calling the Data Base.


```python
    @patch("functions.get_all_attacks_data", return_value=[{'name': 'Denial-of-Service', 'description': 'DoS attacks work by flooding systems, servers, and/or networks with traffic to overload resources and bandwidth.'}])
    def test_all_attack(self, mock_attacks):

        # given
        expected_len = 1

        # when
        result = all_attacks()

        # then
        self.assertEqual(expected_len, len(result))
```

The final result of the unittests :

![Unit test result image](images/unit_tests_result.PNG?raw=true)


## Integration tests
Integration testing is defined as a type of testing where software modules are integrated logically and tested as a group. 
A typical software project consists of multiple software modules, coded by different programmers. 
The purpose of this level of testing is to expose defects in the interaction between these software modules when they are integrated.
Integration Testing focuses on checking data communication amongst these modules.

### How?
In our case we are going to test the interfaces of our API plateform specialy the communication with the database. We are going to rely on the python test package
 pytest to create a test client that will help us perform our intergation test on it.
 
 The tested functions are : 
- Register :white_check_mark:
- Hashing : :white_check_mark: MD5 - :white_check_mark: SHA1 - :white_check_mark: SHA256
- Cracking : :white_check_mark: MD5 - :white_check_mark: SHA1 - :white_check_mark: SHA256
- Encoding : :white_check_mark: Base8 - :white_check_mark: Base16 - :white_check_mark: Base32
- Cracking : :white_check_mark: Base8 - :white_check_mark: Base16 - :white_check_mark: Base32
 
 First we start by creating the Database_test fixture with session scope of the test Data Base that we are going to perform tests on. 
 
 ```python
@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ["DATABASE_FILENAME"] = str(database_filename)
```

Then we create the flask test client fixture with the scope module that we are going to use.

 ```python
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()
```

After that we start performing our integration tests using the test client fixture created.
We check the:
- Status code returned
- Response Type
- Body returned
- Body keys
- Types of returned values

 ```python
def test_register(test_client):
    # Given
    request_payload = {
        "username": "userTest",
        "phone": "213456",
        "email": "email@gmail.com",
        "password": "Hello"
    }

    expected_body = {
        "user_id": 1,
        "username": "userTest",
        "phone": 213456,
        "email": "email@gmail.com",
    }

    expected_status_code = 200

    expected_body_keys = ["user_id", "username", "phone", "email"]

    # When
    response = test_client.post('/register', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["user_id"])
```

Final results :

![Integration test result image](images/integration_tests_result.PNG?raw=true)

## End to end tests

End-to-end testing is a methodology used in the software development lifecycle (SDLC) to test the functionality and performance of an application under product-like circumstances and data to replicate live settings. The goal is to simulate what a real user scenario looks like from start to finish. The completion of this testing is not only to validate the system under test, but to also ensure that its sub-systems work and behave as expected. 

### How ?
In our case we are going to test the API calls when the server is running ( Production like environment ) and check if the server is behaving as expected or not. We are going to rely on the same package as the unit tests and the requests package of python to perform the HTTP requests to the running server. 

 The tested functions are : 
- Login :white_check_mark:
- Register :white_check_mark:
- Hashing : :white_check_mark: MD5 - :white_check_mark: SHA1 - :white_check_mark: SHA256
- Cracking : :white_check_mark: MD5 - :white_check_mark: SHA1 - :white_check_mark: SHA256
- Encoding : :white_check_mark: Base8 - :white_check_mark: Base16 - :white_check_mark: Base32
- Cracking : :white_check_mark: Base8 - :white_check_mark: Base16 - :white_check_mark: Base32


 ```python
 class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"
    
    def test_register(test_client):
        # Given
        request_payload = {
            "username": "userTest",
            "phone": "213456",
            "email": "email@gmail.com",
            "password": "Hello"
        }

        expected_body = {
            "user_id": 1,
            "username": "userTest",
            "phone": 213456,
            "email": "email@gmail.com",
        }

        expected_status_code = 200

        expected_body_keys = ["user_id", "username", "phone", "email"]

        # When
        response = test_client.post('/register', json=request_payload)

        # Then
        assert expected_status_code == response.status_code
        assert response.json | expected_body == response.json
        assert set(expected_body_keys) == response.json.keys()
        assert int == type(response.json["user_id"])
        
    #POST request to /hash/md5 returns hash of TEST
    def test_1_hash_md5(self):
        message = "TEST"
        expected = "\"033bd94b1168d7e4f0d644c3c95e35bf\"\n"

        r = requests.post("{}/hash/md5".format(ApiTest.API_URL), {"message": message})

        self.assertEqual(r.status_code, 200)
        self.assertEqual(expected,r.text)
```

The final results : 

![End to end test result image](images/end_to_end_tests_result.PNG?raw=true)

## User Acceptance Test
User Acceptance Testing (UAT), also known as beta or end-user testing, is defined as testing the software by the user or client to determine whether it can be accepted or not. This is the final testing performed once the functional, system and regression testing are completed.

The main purpose of this testing is to validate the software against the business requirements. This validation is carried out by the end-users who are familiar with the business requirements.

UAT, alpha and beta testing are different types of acceptance testing.

As the user acceptance test is the last testing that is carried out before the software goes live, obviously this is the last chance for the customer to test the software and measure if it is fit for the purpose.

### How?
In our case we have gave the API access to the futur user ( My colleagues) which are familiar with the Security field buisness requirements to validate some use cases
 and make sure that our server fullfils the right needs of the buisness requirements. 
The document of the User Acceptance Test is found in the file ***tests/user_acceptance_test.pdf***. 


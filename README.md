# Virta_Test
Simple API Get Request for Virta Stations API
Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.
The requests module allows you to send HTTP requests using Python.
Getting started
To download and install pytest, run this command from the terminal : pip install pytest
To download and install requests, run this command from the terminal : pip install requests
To ensure all dependencies are resolved in a CI environment, in one go, add them to a requirements.txt file.

Then run the following command : pip install -r requirements.txt
By default pytest only identifies the file names starting with test_ or ending with _test as the test files.

Pytest requires the test method names to start with test. All other method names will be ignored even if we explicitly ask to run those methods.
def test_fetch_user() :
    path = "api/users/2"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2
    
# Running tests
If your tests are contained inside a folder 'Tests', then run the following command :python -m pytest

To generate html results, run the following command : python -m pytest --html=report.html

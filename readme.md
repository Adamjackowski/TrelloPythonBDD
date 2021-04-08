Automated tests
========================

## Instructions for starting automated tests 

### 1 - General requirements:

1. The driver for the given browser(Firefox/Geckodriver, Chrome, Edge) must be added to the PATH environment path.
2. Python3 must be added to the PATH environment path.
3. PyTest must be installed. It can be the newest version.
4. Selenium must be installed. It can be the newest version.
5. Pytest-html must be installed. It can be the newest version.
6. Pytest-bdd must be installed. It can be the newest version.
7. After each failed test, the screenshot of last viewed screen is saved in /screenshots folder.
8. Tu generate html report file run test with --html report_name.html. Eg. pytest --html report.html

### 2 - For the VS Code program:

1. Download the "Python" extension. Open the project folder.
2. To run a given test, in the explorer (upper left corner) discover the tests, select the test file of interest, press PPM and select the option to run tests from a given file.
3. To run each method you can open a test file and choose run/debug button above each test method.

### 3 - To be run in the console

1. Open the console window in the project folder (Ctrl + Shift + RightMouseButton -> open console window).
2. To run all tests use the pytest command in the root direcory. The test will be executed on default browser - Firefox -> See "Run on different browsers".
```
pytest
```
3. To run the selected test, use the command pytest filename with Tests_py.
```
pytest test_name.py
```


### 5 - Test scructure

1. Tests are written in "Page Object Pattern" - please get familiar with it before starting to implement new ones.
2. Each test is in each file and each file contain each test methods. Each method contain each test data and setUp and tearDown fuctions -> see next points.S
3. Some setUp and a little bit of test data is put into a fixtures in conftest.py file. Be aware to not change the scope of each and keep names of each params unique. See -> https://docs.pytest.org/en/latest/fixture.html.
# config interpreter
# pip install selenium
# pip install pytest - for test run
# pip install pytest-html - to generate report
# pip install pytest-xdist - to run parallel
# pip install allure-pytest - to generate allure report
# Select pytest as default runner in python (Go to setting --> Tools-->integrated Tools
#  to run specific file with abs file path --> pytest -v -n=4 --html=Report/myreport.html "D:\Credence Class Notes
# \CredenceBatches\CredenceBatch#14 & 15\Pytest_July\test_file_002.py"
import allure
from selenium import webdriver
import pytest


# file name should start with test_
# class name should start with Test_
# testcases should start with  test_

# To run the test files from terminal--> pytest
# For more details on lib/ plugins--> pytest -v
# For printing the output on console --> pytest -s
# To run specific file in project dir --> pytest filename.py (eg. pytest test_file_001.py)
# To run testcases parallel --> pytest -n=number (eg. pytest -n=2) number--> worker processor
# To generate html report --> (pytest --html=Reports/report.html)
# To set marker for testcases use @pytest.marker.marker_name before testcase
# to run testcases with use define marker--> pytest -m credence

class Test_Credence_001:

    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False

    def test_CredenceUrl_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            assert True
            driver.close()
        else:
            print("You are at Wrong url")
            driver.close()
            assert False

    @pytest.mark.xfail
    def test_sub_003(self):
        a = 3
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == -4:
            assert True
        else:
            assert False

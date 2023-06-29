import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# Load test data from CSV file
def load_test_data(path):
    with open(path, "r") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            print(row)
            if row:
                yield row

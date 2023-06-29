import allure
import pytest
from conftest import load_test_data
from pages.elements_page import SearchBoxPage
from allure_commons._allure import epic, feature
@pytest.fixture(autouse=True)
def search_box_page(driver):
    search_box_page = SearchBoxPage(driver, "https://www.symptos.com/")
    search_box_page.open()
    yield search_box_page
    driver.delete_all_cookies()
    driver.refresh()

@allure.suite('Elements Suite')
class TestElements:
    @allure.feature('SearchBox Feature')
    class TestSearchBox:
        @allure.severity(allure.severity_level.CRITICAL)
        @allure.title('Check SearchBox Success')
        @pytest.mark.parametrize(
            "medicine_1, medicine_2, quantity_1, quantity_2, zipcode, pharmacy",
             load_test_data("test_data_success.csv"),
        )
        def test_search_box_success(
            self, search_box_page, driver, medicine_1, medicine_2, quantity_1, quantity_2, zipcode, pharmacy
        ):
          with allure.step("Step description: Open Symptos and validate title"):

            assert (
                    driver.title == "Compare Prescription Prices, Coupons, and Pharmacy Locations | Symptos"
                    or driver.title == "Compare Prescription Prices, Coupons and Pharmacy Locations | Symptos"
            )
          with allure.step("Step description: Fill in the search box and submit"):
            search_result = search_box_page.fill_fields_and_submit(
                medicine_1, medicine_2, quantity_1, quantity_2, zipcode,
            )
          with allure.step("Step description: Validate first search result"):
            assert search_box_page.first_search_result() == pharmacy

        @allure.severity(allure.severity_level.NORMAL)
        @allure.title('Check SearchBox Failure')
        @pytest.mark.parametrize(
            "medicine, zipcode",
            load_test_data("test_data_failure.csv"),
        )
        def test_search_box_failure(
            self, search_box_page, driver, medicine, zipcode
        ):
          with allure.step("Step description: Open Symptos and validate title"):

            assert (
                    driver.title == "Compare Prescription Prices, Coupons, and Pharmacy Locations | Symptos"
                    or driver.title == "Compare Prescription Prices, Coupons and Pharmacy Locations | Symptos"
            )
          with allure.step("Step description: Fill in the search box with incorrect medicine and submit"):
            search_box_page.fill_fields_and_submit_incorrect_medicine(
                 medicine, zipcode
            )

          with allure.step("Step description: Validate alert text"):
            assert search_box_page.alert_text() == "Some medicine requests are incorrect."




from locators.elements_page_locators import SearchBoxPageLocators
from pages.base_page import BasePage


class SearchBoxPage(BasePage):
    locators = SearchBoxPageLocators

    def fill_fields_and_submit(
        self, medicine_1, medicine_2, quantity_1, quantity_2, zipcode
    ):
        self.element_is_visible(self.locators.SEARCH_BOX).send_keys(medicine_1)
        self.element_is_visible(self.locators.ASPIRIN_OPTION).click()
        self.element_is_visible(self.locators.CAP_25_200MG_OPTION).click()
        self.element_is_visible(self.locators.QUANTITY_INPUT).send_keys(quantity_1)
        self.element_is_visible(self.locators.SAVE_AND_CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.LOCATION_BUTTON).click()
        self.element_is_visible(self.locators.WITHIN_MILES_FROM_BUTTON).click()
        self.element_is_visible(self.locators.MILES_OPTION).click()
        self.element_is_visible(self.locators.ZIP_CODE_TEXTBOX).clear()
        self.element_is_visible(self.locators.ZIP_CODE_TEXTBOX).send_keys(zipcode)
        self.element_is_visible(self.locators.SAVE_AND_CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.SEARCH_BOX_NEW).send_keys(medicine_2)
        self.element_is_visible(self.locators.DEXAMETHASONE_OPTION).click()
        self.element_is_visible(self.locators.BOTTLE_OPTION).click()
        self.element_is_visible(self.locators.QUANTITY_SELECTION).send_keys(quantity_2)
        self.element_is_visible(self.locators.SAVE_AND_CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.SEARCH_BUTTON).click()

        pass

    def first_search_result(self):
        return self.element_is_visible(self.locators.FIRST_SEARCH_RESULT).text

    def fill_fields_and_submit_incorrect_medicine(self, medicine, zipcode):
        self.element_is_visible(self.locators.SEARCH_BOX).send_keys(medicine)
        self.element_is_visible(self.locators.LOCATION_BUTTON).click()
        self.element_is_visible(self.locators.WITHIN_MILES_FROM_BUTTON).click()
        self.element_is_visible(self.locators.MILES_OPTION).click()
        self.element_is_visible(self.locators.ZIP_CODE_TEXTBOX).clear()
        self.element_is_visible(self.locators.ZIP_CODE_TEXTBOX).send_keys(zipcode)
        self.element_is_visible(self.locators.SAVE_AND_CONTINUE_BUTTON).click()
        self.element_is_visible(self.locators.SEARCH_BUTTON_2).click()

    def alert_text(self):
        return self.element_is_visible(self.locators.ALERT).text

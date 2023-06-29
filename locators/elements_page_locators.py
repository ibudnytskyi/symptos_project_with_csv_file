from selenium.webdriver.common.by import By


class SearchBoxPageLocators:
    # form fields
    SEARCH_BOX = (By.XPATH, '//*[@id="medicine-request-0__name"]')
    ASPIRIN_OPTION = (By.XPATH, '//span[@class="mat-option-text"]')
    CAP_25_200MG_OPTION = (By.XPATH, "//div[contains(text(), 'CAP 25-200MG')]")
    QUANTITY_INPUT = (By.XPATH, "//input[@id='quantity-dialog-number']")
    SAVE_AND_CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Save & Continue')]",
    )
    LOCATION_BUTTON = (By.XPATH, "//button[.//span[contains(text(), 'Location')]]")
    WITHIN_MILES_FROM_BUTTON = (By.XPATH, "//select[@id='refined-search-radius']")
    MILES_OPTION = (
        By.XPATH,
        '//option[@class="ng-star-inserted" and normalize-space(text())="20"]',
    )
    ZIP_CODE_TEXTBOX = (By.XPATH, '//*[@id="refined-search-location-zip"]')
    SEARCH_BOX_NEW = (By.XPATH, "//input[@id='medicine-request-1__name']")
    DEXAMETHASONE_OPTION = (By.XPATH, "(//mat-option)[1]")
    BOTTLE_OPTION = (By.XPATH, "//div[@id='pick-medicine__button-7']")
    QUANTITY_SELECTION = (By.XPATH, '//*[@id="quantity-dialog-number"]')
    SEARCH_BUTTON = (By.XPATH, "(//button)[6]")
    ALERT = (By.XPATH, '//*[@class="question-dialog__question"]')
    FIRST_SEARCH_RESULT = (By.XPATH, '//*[@id="medicine-response-0__pharmacy-name"]')
    SEARCH_BUTTON_2 = (By.XPATH, "//button[contains(text(), 'SEARCH')]")
    pass

from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_LINK = (By.CSS_SELECTOR, "#header-search")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type = "submit"]")

class ResultPageLocators():
    TELE_LINK = (By.CSS_SELECTOR, "//p[text() = 'Телевизоры'")

from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_search_link(self):
        search_link = self.browser.find_element(*BasePageLocators.SEARCH_LINK)
        search_link.click()
        input.send_keys('samsung')
        submit_button = self.browser.find_element(*BasePageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def go_to_tele_link(self):
        tele_link = self.browser.find_element(*BasePageLocators.TELE_LINK)
        tele_link.click()



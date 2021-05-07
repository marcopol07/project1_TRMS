from selenium.webdriver.chrome.webdriver import WebDriver


class TRMSHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def url(self, url):
        return self.driver.get(url)

    def credential_input_bar(self):
        return self.driver.find_element_by_id('userInput')

    def credential_submit(self):
        return self.driver.find_element_by_id('submitButton')

    def navigate_to_dash(self, username, password):
        self.credential_input_bar().send_keys(username)
        self.credential_submit().click()
        self.credential_input_bar().send_keys(password)
        return self.credential_submit().click()

    def date_input_bar(self):
        return self.driver.find_element_by_id('date')

    def cost_input_bar(self):
        return self.driver.find_element_by_id('costInput')

    def justify_input_bar(self):
        return self.driver.find_element_by_id('justifyInput')

    def form_submit_button(self):
        return self.driver.find_element_by_id('formButton')

    def approval_selector(self):
        return self.driver.find_element_by_id('approveDeny1')

    def approval_submit(self):
        return self.driver.find_element_by_id('approveDenyButton1')

    def query_input_bar(self):
        return self.driver.find_element_by_id('queryBody1')

    def query_submit(self):
        return self.driver.find_element_by_id('queryButton1')

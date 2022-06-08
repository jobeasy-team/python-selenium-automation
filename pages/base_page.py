class Page:

    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, exp_txt, *locator):
        act_txt = self.driver.find_element(*locator).text

        assert exp_txt == act_txt, \
            f'Error,{act_txt} does not match {exp_txt}'
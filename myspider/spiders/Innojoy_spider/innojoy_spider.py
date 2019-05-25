from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys


class innojoy_spider():
    def __init__(self):
        # self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()

        # Selenium+Headless Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        self.url = "http://www.innojoy.com/search/index.html"

    def get_source(self, search_message):
        self.driver.get(self.url)
        sleep(3)
        # wait = WebDriverWait(self.driver, 10)
        # input = wait.until(EC.presence_of_element_located((By.ID, 'idPhone')))
        # print(input)
        self.driver.switch_to.frame('_userlogin')
        try:
            phone = self.driver.find_element_by_id('idPhone')
            # print(phone)
            phone.send_keys("18918615423")
        except NoSuchElementException:
            print("no element name")
        sleep(3)
        try:
            password = self.driver.find_element_by_xpath(
                '//div[@class="control-group"]/div[@class="controls"]/input[@id="idPassword"]')
            password.send_keys('ZHJ1995369')
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print('no elment pass')
        self.driver.switch_to.parent_frame()

        try:
            search_ = self.driver.find_element_by_class_name('searchinput')
            # print(search_)
            sleep(3)
            search_.send_keys(search_message)
            search_.send_keys(Keys.ENTER)
            print("hello")
        except StaleElementReferenceException:
            search_ = self.driver.find_element_by_xpath('//div[@class="searchinput"]/input[@id="queryExpr-str"]')
            # print(search_)
            sleep(3)
            search_.send_keys(search_message)
            search_.send_keys(Keys.ENTER)
            print(123)


if __name__ == '__main__':
    USER = innojoy_spider()
    USER.get_source("上海电机学院")

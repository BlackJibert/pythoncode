from time import sleep

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys


class goWhere():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://flight.qunar.com/'

    def get_source(self, start_city, arrive_city, start_time):
        try:
            self.driver.get(self.url)
            # start city
            sleep(2)
            input_start_city = self.driver.find_element_by_class_name('textbox')
            input_start_city.clear()
            input_start_city.send_keys(start_city)

            # start time
            sleep(2)
            input_start_time = self.driver.find_element_by_id('fromDate')
            input_start_time.clear()
            input_start_time.send_keys(start_time)

            # arrive city
            input_arrive_city = self.driver.find_element_by_xpath(
                '//div[@class="crl_sp_city"]/div[@class="controls"][2]/div[contains(@class,"qcbox")]/input[@class="textbox"]')
            input_arrive_city.clear()
            input_arrive_city.send_keys(arrive_city)
            sleep(2)
            input_arrive_city.send_keys(Keys.ENTER)
            # button = ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('//div[@id="searchboxList"]/button[@class="btn_search"]'))
            try:
                # 定位到搜索按钮位置
                button = self.driver.find_element_by_xpath(
                    '//div[@class="crl_sp_action"][1]/button[@class="btn_search"]')
                print(button)
                # 运用js代码点击搜索按钮
                self.driver.execute_script("arguments[0].click();", button)
                sleep(2)
                # button.click()
            except ElementNotVisibleException:
                print("error: element not visible")
            # input_arrive_city.send_keys(Keys.ENTER)
            sleep(3)

            print(self.driver.current_url)
        except NoSuchElementException:
            print("No element")
        finally:
            # self.driver.close()
            print('---')
            new_url = self.driver.current_url
            self.driver.get(new_url)
            sleep(3)
            html = self.driver.page_source
            doc = pq(html)
            airflys = doc('.b-airfly').items()
            for airfly in airflys:
                messages = {
                    "air": airfly.find(".air").text(),
                    "start_time_": airfly.find(".sep-lf").text(),
                    "arrive_time": airfly.find(".sep-rt").text()
                }
                print(messages)


GoWhere = goWhere()
GoWhere.get_source("上海", "北京", "2019-04-09")

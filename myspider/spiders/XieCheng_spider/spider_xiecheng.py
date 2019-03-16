from time import sleep

from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


# br= webdriver.PhantomJS()

# start_city = "广州"
# end_city = "上海"
# time_ = '2019-04-08'
class XieCheng():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.start_city = start_city
        # self.end_city = end_city
        # self.time = time_

    def get_source(self, start_city, end_city, start_time, another_start_city=None, anoter_end_city=None,
                   another_start_time=None, end_time=None, single_trip=True, multipass=None):
        if single_trip == True:
            try:
                first_url = "https://flights.ctrip.com/"
                self.driver.get(first_url)
            except TimeoutException:
                print('Time out')
            try:
                sleep(2)
                input1 = self.driver.find_element_by_id('DepartCity1TextBox')
                input1.send_keys(start_city)
            except NoSuchElementException:
                print("No start city Element")
            try:
                sleep(2)
                input2 = self.driver.find_element_by_id('ArriveCity1TextBox')
                input2.send_keys(end_city)
            except NoSuchElementException:
                print("No end city element")
            try:
                sleep(2)
                input_time = self.driver.find_element_by_id('DepartDate1TextBox')
                input_time.send_keys(start_time)
                sleep(2)
                input_time.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("No  time Element")
            # ActionChains(br).move_to_element(br.find_element_by_xpath('//div[@class="btn_box"]/input[@class="search_flthotel"]')).click()
            # br.find_element_by_xpath('//div[@class="btn_box"]/input[@class="search_flthotel"]').click()
            sleep(3)
            login_url = self.driver.current_url
            self.driver.get(login_url)
            sleep(4)
            html = self.driver.page_source
            doc = pq(html)
            # class有多个值
            divs = doc('.search_box.search_box_tag.search_box_light.Label_Flight').items()
            div_me = []
            for div in divs:
                messages = {
                    'airplane': div.find('.logo-item.flight_logo').text().replace('\n', ''),
                    'start_time': div.find('.inb.right .time').text(),
                    'start_airport': div.find('.inb.right .airport').text(),
                    'end_time': div.find('.inb.left .time').text(),

                    'end_airport': div.find('.inb.left .airport').text(),
                    # 价格（class有多个属性，只写了前两个）,
                    'price': div.find('.inb.price').text().replace('\n', ''),
                }
                div_me.append(messages)
            return div_me

        elif single_trip == False:
            # 往返
            try:
                first_url = "https://flights.ctrip.com/"
                self.driver.get(first_url)
            except TimeoutException:
                print('Time out')

            try:
                # 选择航程类型为:"往返"，点击事件
                self.driver.find_element_by_id('radio_D').click()
            except NoSuchElementException:
                print("No  label element")
            try:
                sleep(2)
                input1 = self.driver.find_element_by_id('DepartCity1TextBox')
                input1.send_keys(start_city)
            except NoSuchElementException:
                print("No start city Element")
            try:
                sleep(2)
                input2 = self.driver.find_element_by_id('ArriveCity1TextBox')
                input2.send_keys(end_city)
            except NoSuchElementException:
                print("No end city element")
            try:
                sleep(2)
                input_time_start = self.driver.find_element_by_id('DepartDate1TextBox')
                input_time_start.send_keys(start_time)
            except NoSuchElementException:
                print("No  START time Element")
            try:
                sleep(2)
                input_time_end = self.driver.find_element_by_id('ReturnDepartDate1TextBox')
                input_time_end.send_keys(end_time)
                sleep(3)
                input_time_end.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("No RETURN tim Element")
            # ActionChains(br).move_to_element(br.find_element_by_xpath('//div[@class="btn_box"]/input[@class="search_flthotel"]')).click()
            # br.find_element_by_xpath('//div[@class="btn_box"]/input[@class="search_flthotel"]').click()
            sleep(2)
            print(self.driver.current_url)
            login_url = self.driver.current_url
            self.driver.get(login_url)
            sleep(3)
            html = self.driver.page_source
            doc = pq(html)
            # class有多个值
            divs = doc('.search_box.search_box_tag.search_box_light.Label_Flight').items()
            div_me = []
            for div in divs:
                messages = {
                    'airplane': div.find('.logo-item.flight_logo').text().replace('\n', ''),
                    'start_time': div.find('.inb.right .time').text(),
                    'start_airport': div.find('.inb.right .airport').text(),
                    'end_time': div.find('.inb.left .time').text(),

                    'end_airport': div.find('.inb.left .airport').text(),
                    # 价格（class有多个属性，只写了前两个）,
                    'price': div.find('.inb.price').text().replace('\n', ''),
                }
                div_me.append(messages)
            return div_me

        elif multipass != None:
            # 往返
            try:
                first_url = "https://flights.ctrip.com/"
                self.driver.get(first_url)
            except TimeoutException:
                print('Time out')

            try:
                # 选择航程类型为:"多程"，点击事件
                self.driver.find_element_by_id('radio_M').click()
            except NoSuchElementException:
                print("No  label element")
            try:
                sleep(2)
                # 出发城市1
                input1 = self.driver.find_element_by_id('M_DepartCity1TextBox')
                input1.send_keys(start_city)
            except NoSuchElementException:
                print("No start firstcity Element")
            try:
                sleep(2)
                # 到达城市1
                input2 = self.driver.find_element_by_id('M_ArriveCity1TextBox')
                input2.send_keys(end_city)
            except NoSuchElementException:
                print("No first end city element")
            try:
                sleep(2)
                # 出发时间1
                input_time_start = self.driver.find_element_by_id('DepartDate1TextBox2')
                input_time_start.send_keys(start_time)
            except NoSuchElementException:
                print("No  start first time Element")

            try:
                sleep(2)
                # 出发城市2
                input1 = self.driver.find_element_by_id('M_DepartCity2TextBox')
                input1.send_keys(another_start_city)
            except NoSuchElementException:
                print("No start second city Element")
            try:
                sleep(2)
                # 到达城市2
                input2 = self.driver.find_element_by_id('M_ArriveCity2TextBox')
                input2.send_keys(anoter_end_city)
            except NoSuchElementException:
                print("No end second city element")

            try:
                sleep(2)
                # 开始时间2
                input_time_start2 = self.driver.find_element_by_id('DepartDate2TextBox')
                input_time_start2.send_keys(another_start_time)
                sleep(3)
                input_time_start2.send_keys(Keys.ENTER)
            except NoSuchElementException:
                print("No RETURN time Element")
            # ActionChains(br).move_to_element(br.find_element_by_xpath('//div[@class="btn_box"]/input[@class="search_flthotel"]')).click()
            # br.find_element_by_xpath('//div[@class="btn_box"]/input[@class="search_flthotel"]').click()
            sleep(2)
            print(self.driver.current_url)
            login_url = self.driver.current_url
            self.driver.get(login_url)
            sleep(3)
            html = self.driver.page_source
            doc = pq(html)
            # class有多个值
            divs = doc('.search_box.search_box_tag.search_box_light.Label_Flight').items()
            div_ = []
            div_me = []
            for div in divs:
                messages = {
                    'airplane': div.find('.logo-item.flight_logo').text().replace('\n', ''),
                    'start_time': div.find('.inb.right .time').text(),
                    'start_airport': div.find('.inb.right .airport').text(),
                    'end_time': div.find('.inb.left .time').text(),

                    'end_airport': div.find('.inb.left .airport').text(),
                    # 价格（class有多个属性，只写了前两个）,
                    'price': div.find('.inb.price').text().replace('\n', ''),
                }
                div_me.append(messages)
            div_.append(div_me)
            sleep(5)
            try:
                self.driver.find_element_by_xpath(
                    '//div[contains(@class,"book")]/a[contains(@class,"btn_book")]').click()
                sleep(5)
                print(self.driver.current_url)
                second_url2 = self.driver.current_url
                self.driver.get(second_url2)
                sleep(3)
                html = self.driver.page_source
                doc = pq(html)
                # class有多个值
                divs = doc('.search_box.search_box_tag.search_box_light.Label_Flight').items()

                div_me2 = []
                for div in divs:
                    messages = {
                        'airplane': div.find('.logo-item.flight_logo').text().replace('\n', ''),
                        'start_time': div.find('.inb.right .time').text(),
                        'start_airport': div.find('.inb.right .airport').text(),
                        'end_time': div.find('.inb.left .time').text(),

                        'end_airport': div.find('.inb.left .airport').text(),
                        # 价格（class有多个属性，只写了前两个）,
                        'price': div.find('.inb.price').text().replace('\n', ''),
                    }
                    div_me2.append(messages)
                div_.append(div_me2)
            except NoSuchElementException:
                print("no second messages")
            return div_


xiecheng = XieCheng()
# 单程
# source = xiecheng.get_source("北京", '上海', "2019-04-02")
# 往返
source = xiecheng.get_source("北京", '上海', "2019-04-02", None, None, None, "2019-04-04", False, False)

# 多程

# source = xiecheng.get_source("北京", '上海', "2019-04-02", "广州", "南京", "2019-04-04", None, None, True)
print(source)

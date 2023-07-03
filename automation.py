from selenium import webdriver
import selenium.webdriver.support.ui
import select
import time


# Enter roll number start range
i = 12620005001

web = webdriver.Chrome(executable_path="C://chromedriver//chromedriver.exe")

# enter roll number end range
while i <= 12620005100:
    web.get('http://136.232.2.202:8084/stud23e.aspx')

    time.sleep(2)

    RollNo = i
    roll = web.find_element_by_xpath(
        '//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input')
    roll.send_keys(RollNo)

    # copy and paste xpath of semester
    option = web.find_element_by_xpath(
        '//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select/option[7]')

    # option = web.find_element_by_xpath('xpath')
    option.click()

    submit = web.find_element_by_xpath('//*[@id="Button1"]')
    submit.click()
    title = web.title

    # crash = web.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr/td/table/tbody/tr[2]/td/span/span[2]/strong').text
    if title == 'HERITAGE INSTITUTE OF TECHNOLOGY':

        name = web.find_element_by_xpath('//*[@id="lblname"]')
        print(name.text)
    # print('\n')
        rollprint = web.find_element_by_xpath('//*[@id="lblroll"]')
        print(rollprint.text)
    # print('\n')
        sgpa = web.find_element_by_xpath('//*[@id="lblbottom1"]')
        print(sgpa.text)

        sgpa2 = web.find_element_by_xpath('//*[@id="lblbottom2"]')
        print(sgpa2.text)
        ygpa = web.find_element_by_xpath('//*[@id="lblbottom3"]')
        print(ygpa.text)
        print('\n')
    # print('\n')

    i = i+1

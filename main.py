#BDD
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
@given(u'launch chrome browser')
def launchbrowser (context):
   context.driver=webdriver.Chrome(executable_path="C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")



@when(u'open orange hrm home page')
def homepage(context):
  context.driver.get("https://opensource-demo.orangehrmlive.com/")



@then(u'verify that the logo present on page')
def verify(context):
  context.driver.find_element(by=By.XPATH,value="//div[@id='divLogo']//img")



@then(u'close browser')
def close(context):
    context.driver.close

Feature:OrangeHRM logo
  Scenario:logo presence on orangeHRM home page
    Given launch chrome browser
    When open orange hrm home page
    Then verify that the logo present on page
    And close browser


#PYTEST

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def test_a():
    global  driver
    driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield
    driver.close()
    print("test passed")


def test_b(test_a):
    driver.find_element(by=By.ID,value="txtUsername").send_keys("Admin")
    driver.find_element(by=By.ID,value="txtPassword").send_keys("admin123")
    driver.find_element(by=By.ID,value="btnLogin").click()
def test_c():
    print("test passed")
    driver.close()



#NEWWW

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\\Users\\conta\\.wdm\\drivers\\chromedriver\\win32\\103.0.5060.53\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# driver.save_screenshot("C:\screenshort\homepage.png")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.find_element(by=By.LINK_TEXT,value='Download').click()
text=driver.page_source
word="user"
print(word in text)


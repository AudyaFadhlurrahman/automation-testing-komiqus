import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTS07AdminModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS07AdminModul(self):
    # Test name: TS_07 Admin Modul
    # Step # | name | target | value
    # 1 | open | /home/feed | 
    self.driver.get("http://103.183.75.202:819//home/feed")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | mouseOver | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | click | css=#navbarDropdownUser .komiqus-pp | 
    self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp").click()
    # 5 | mouseOut | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 7 | mouseOver | linkText=Dashboard | 
    element = self.driver.find_element(By.LINK_TEXT, "Dashboard")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | linkText=Dashboard | 
    self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
    # 9 | mouseOut | css=.card-body > .nav-item:nth-child(3) .stretched-link | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 10 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 11 | click | linkText=lihat komik | 
    self.driver.find_element(By.LINK_TEXT, "lihat komik").click()
    # 12 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 13 | click | css=#content-your-book .sub-l > .btn > .de-none | 
    self.driver.find_element(By.CSS_SELECTOR, "#content-your-book .sub-l > .btn > .de-none").click()
    # 14 | click | linkText=Beranda | 
    self.driver.find_element(By.LINK_TEXT, "Beranda").click()
    # 15 | click | css=#navbarDropdownUser .komiqus-pp | 
    self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp").click()
    # 16 | click | linkText=Dashboard | 
    self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
    # 17 | click | linkText=lihat komik | 
    self.driver.find_element(By.LINK_TEXT, "lihat komik").click()
    # 18 | click | css=.bi-pencil-square:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".bi-pencil-square:nth-child(2)").click()
  

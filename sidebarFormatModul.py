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

class TestTS010SidebarFormatModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS010SidebarFormatModul(self):
    # Test name: TS_010 Sidebar Format Modul
    # Step # | name | target | value
    # 1 | open | /home/feed | 
    self.driver.get("http://103.183.75.202:819//home/feed")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | mouseOver | css=#sm-browse > .nav-item:nth-child(1) .d-flex | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#sm-browse > .nav-item:nth-child(1) .d-flex")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | click | css=#sm-browse > .nav-item:nth-child(1) .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#sm-browse > .nav-item:nth-child(1) .d-flex").click()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | runScript | window.scrollTo(0,5.599999904632568) | 
    self.driver.execute_script("window.scrollTo(0,5.599999904632568)")
    # 9 | click | css=#book-list-1 .img-fluid | 
    self.driver.find_element(By.CSS_SELECTOR, "#book-list-1 .img-fluid").click()
    # 10 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 11 | runScript | window.scrollTo(0,600) | 
    self.driver.execute_script("window.scrollTo(0,600)")
    # 12 | mouseOver | css=#dropdownBookStatus-1 > .bi-bookmark | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#dropdownBookStatus-1 > .bi-bookmark")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 13 | click | css=#dropdownBookStatus-1 > .bi-bookmark | 
    self.driver.find_element(By.CSS_SELECTOR, "#dropdownBookStatus-1 > .bi-bookmark").click()
    # 14 | mouseOut | css=#dropdownBookStatus-1 > .bi-bookmark | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 15 | click | linkText=Want to Read | 
    self.driver.find_element(By.LINK_TEXT, "Want to Read").click()
    # 16 | click | id=dropdownBookStatus-1 | 
    self.driver.find_element(By.ID, "dropdownBookStatus-1").click()
    # 17 | click | id=rs-menu | 
    self.driver.find_element(By.ID, "rs-menu").click()
    # 18 | click | css=#sm-rdstats > .nav-item:nth-child(1) .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#sm-rdstats > .nav-item:nth-child(1) .d-flex").click()
  

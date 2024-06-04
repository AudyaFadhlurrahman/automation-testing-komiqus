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

class TestTS04BookModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS04BookModul(self):
    # Test name: TS_04 Book Modul
    # Step # | name | target | value
    # 1 | open | /home/feed | 
    self.driver.get("http://103.183.75.202:819//home/feed")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 4 | click | css=#sm-browse > .nav-item:nth-child(1) .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#sm-browse > .nav-item:nth-child(1) .d-flex").click()
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 7 | click | css=#book-list-1 .img-fluid | 
    self.driver.find_element(By.CSS_SELECTOR, "#book-list-1 .img-fluid").click()
    # 8 | runScript | window.scrollTo(0,370.3999938964844) | 
    self.driver.execute_script("window.scrollTo(0,370.3999938964844)")
    # 9 | runScript | window.scrollTo(0,376) | 
    self.driver.execute_script("window.scrollTo(0,376)")
    # 10 | click | css=.btn-primary > .bi-chevron-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .bi-chevron-down").click()
    # 11 | click | css=.btn-primary > .bi-chevron-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .bi-chevron-down").click()
    # 12 | click | css=.bk-btn-buy | 
    self.driver.find_element(By.CSS_SELECTOR, ".bk-btn-buy").click()
  

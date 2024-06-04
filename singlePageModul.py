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

class TestTS011SinglePageModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS011SinglePageModul(self):
    # Test name: TS_011 Single Page Modul
    # Step # | name | target | value
    # 1 | open | http://103.183.75.202:819/home/feed | 
    self.driver.get("http://103.183.75.202:819/home/feed")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | click | css=#mm-community .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#mm-community .d-flex").click()
  

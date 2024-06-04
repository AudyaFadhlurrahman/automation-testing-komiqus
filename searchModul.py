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

class TestTS06SearchModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS06SearchModul(self):
    # Test name: TS_06 Search Modul
    # Step # | name | target | value
    # 1 | open | /home/feed | 
    self.driver.get("http://103.183.75.202:819//home/feed")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | click | id=search-bar-title | 
    self.driver.find_element(By.ID, "search-bar-title").click()
    # 4 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | type | id=search-bar-title | komiqus
    self.driver.find_element(By.ID, "search-bar-title").send_keys("komiqus")
    # 7 | click | id=search-bar-title | 
    self.driver.find_element(By.ID, "search-bar-title").click()
    # 8 | click | css=.tt-dataset-src_comic > .dropdown-item:nth-child(2) > .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, ".tt-dataset-src_comic > .dropdown-item:nth-child(2) > .d-flex").click()
  

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

class TestTS02UserModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS02UserModul(self):
    # Test name: TS_02 User Modul
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://103.183.75.202:819//")
    # 2 | setWindowSize | 794x816 | 
    self.driver.set_window_size(794, 816)
    # 3 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 4 | mouseOver | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | click | css=#navbarDropdownUser .komiqus-pp | 
    self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp").click()
    # 6 | mouseOut | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 7 | click | css=.stretched-link:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".stretched-link:nth-child(1)").click()
    # 8 | click | linkText=Edit Profil | 
    self.driver.find_element(By.LINK_TEXT, "Edit Profil").click()
    # 9 | click | id=biodata | 
    self.driver.find_element(By.ID, "biodata").click()
    # 10 | type | id=biodata | indonesian
    self.driver.find_element(By.ID, "biodata").send_keys("indonesian")
    # 11 | click | id=phone | 
    self.driver.find_element(By.ID, "phone").click()
    # 12 | type | id=phone | 123456767896
    self.driver.find_element(By.ID, "phone").send_keys("123456767896")
    # 13 | click | css=.btn-primary:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(1)").click()
    # 14 | mouseOver | css=.avatar-2xl > .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".avatar-2xl > .komiqus-pp")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 15 | click | css=.avatar-2xl > .komiqus-pp | 
    self.driver.find_element(By.CSS_SELECTOR, ".avatar-2xl > .komiqus-pp").click()
    # 16 | mouseOut | css=.avatar-2xl > .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 17 | click | linkText=Pengaturan | 
    self.driver.find_element(By.LINK_TEXT, "Pengaturan").click()
    # 18 | click | linkText=Social Link | 
    self.driver.find_element(By.LINK_TEXT, "Social Link").click()
    # 19 | click | id=platform | 
    self.driver.find_element(By.ID, "platform").click()
    # 20 | select | id=platform | label=Twitter
    dropdown = self.driver.find_element(By.ID, "platform")
    dropdown.find_element(By.XPATH, "//option[. = 'Twitter']").click()
    # 21 | click | name=label | 
    self.driver.find_element(By.NAME, "label").click()
    # 22 | type | name=label | twitter/gcgy
    self.driver.find_element(By.NAME, "label").send_keys("twitter/gcgy")
    # 23 | click | css=.rounded-sm-start | 
    self.driver.find_element(By.CSS_SELECTOR, ".rounded-sm-start").click()
  

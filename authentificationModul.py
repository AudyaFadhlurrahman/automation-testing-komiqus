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

class TestTS01AuthentificationModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS01AuthentificationModul(self):
    # Test name: TS_01 Authentification Modul
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://103.183.75.202:819//")
    # 2 | setWindowSize | 794x817 | 
    self.driver.set_window_size(794, 817)
    # 3 | click | id=navbarSignup | 
    self.driver.find_element(By.ID, "navbarSignup").click()
    # 4 | click | id=subscribe-komiqus-username | 
    self.driver.find_element(By.ID, "subscribe-komiqus-username").click()
    # 5 | type | id=subscribe-komiqus-username | testkomiqus12345
    self.driver.find_element(By.ID, "subscribe-komiqus-username").send_keys("testkomiqus12345")
    # 6 | click | id=subscribe-komiqus-fullname | 
    self.driver.find_element(By.ID, "subscribe-komiqus-fullname").click()
    # 7 | type | id=subscribe-komiqus-fullname | testkomiqussss
    self.driver.find_element(By.ID, "subscribe-komiqus-fullname").send_keys("testkomiqussss")
    # 8 | click | id=subscribe-komiqus-email | 
    self.driver.find_element(By.ID, "subscribe-komiqus-email").click()
    # 9 | type | id=subscribe-komiqus-email | testkomiqus12345.com
    self.driver.find_element(By.ID, "subscribe-komiqus-email").send_keys("testkomiqus12345.com")
    # 10 | click | id=subscribe-komiqus-role | 
    self.driver.find_element(By.ID, "subscribe-komiqus-role").click()
    # 11 | select | id=subscribe-komiqus-role | label=Pembaca
    dropdown = self.driver.find_element(By.ID, "subscribe-komiqus-role")
    dropdown.find_element(By.XPATH, "//option[. = 'Pembaca']").click()
    # 12 | click | css=.btn-warning:nth-child(5) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-warning:nth-child(5)").click()
    # 13 | click | id=subscribe-komiqus-email | 
    self.driver.find_element(By.ID, "subscribe-komiqus-email").click()
    # 14 | type | id=subscribe-komiqus-email | testkomiqus12345@gmail.com
    self.driver.find_element(By.ID, "subscribe-komiqus-email").send_keys("testkomiqus12345@gmail.com")
    # 15 | mouseDown | css=.btn-warning:nth-child(5) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-warning:nth-child(5)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 16 | mouseUp | css=#subscribe-komiqus-modal .modal-body | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#subscribe-komiqus-modal .modal-body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 17 | click | css=#subscribe-komiqus-modal .modal-body | 
    self.driver.find_element(By.CSS_SELECTOR, "#subscribe-komiqus-modal .modal-body").click()
    # 18 | click | css=.btn-warning:nth-child(5) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-warning:nth-child(5)").click()
    # 19 | mouseDownAt | css=.bi-arrow-right | -91.80001831054688,23.762481689453125
    element = self.driver.find_element(By.CSS_SELECTOR, ".bi-arrow-right")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 20 | mouseMoveAt | css=.slider | 23.199981689453125,30.762481689453125
    element = self.driver.find_element(By.CSS_SELECTOR, ".slider")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 21 | mouseUpAt | css=.slider | 23.199981689453125,30.762481689453125
    element = self.driver.find_element(By.CSS_SELECTOR, ".slider")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 22 | click | css=.bi-arrow-right | 
    self.driver.find_element(By.CSS_SELECTOR, ".bi-arrow-right").click()
    # 23 | click | css=.swal2-confirm | 
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    # 24 | click | id=navbarDropdownLogin | 
    self.driver.find_element(By.ID, "navbarDropdownLogin").click()
    # 25 | click | id=signin-username | 
    self.driver.find_element(By.ID, "signin-username").click()
    # 26 | type | id=signin-username | 12345
    self.driver.find_element(By.ID, "signin-username").send_keys("12345")
    # 27 | type | id=signin-password | 123455
    self.driver.find_element(By.ID, "signin-password").send_keys("123455")
    # 28 | click | name=submit | 
    self.driver.find_element(By.NAME, "submit").click()
    # 29 | click | id=signin-username-page | 
    self.driver.find_element(By.ID, "signin-username-page").click()
    # 30 | click | id=signin-username-page | 
    self.driver.find_element(By.ID, "signin-username-page").click()
    # 31 | type | id=signin-username-page | tester.user
    self.driver.find_element(By.ID, "signin-username-page").send_keys("tester.user")
    # 32 | click | id=signin-password-page | 
    self.driver.find_element(By.ID, "signin-password-page").click()
    # 33 | type | id=signin-password-page | 1234qwerASDF?
    self.driver.find_element(By.ID, "signin-password-page").send_keys("1234qwerASDF?")
    # 34 | click | css=div:nth-child(5) > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > .btn").click()
    # 35 | mouseOver | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 36 | click | css=#navbarDropdownUser .komiqus-pp | 
    self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp").click()
    # 37 | mouseOut | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 38 | click | id=sign_out | 
    self.driver.find_element(By.ID, "sign_out").click()
    # 39 | click | id=navbarDropdownLogin | 
    self.driver.find_element(By.ID, "navbarDropdownLogin").click()
    # 40 | click | linkText=Lupa Password? | 
    self.driver.find_element(By.LINK_TEXT, "Lupa Password?").click()
    # 41 | click | id=forgot-find-account | 
    self.driver.find_element(By.ID, "forgot-find-account").click()
    # 42 | type | id=forgot-find-account | tester.user@komiqus.com
    self.driver.find_element(By.ID, "forgot-find-account").send_keys("tester.user@komiqus.com")
    # 43 | click | css=.btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
  

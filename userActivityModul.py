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

class TestTS03UserActivityModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS03UserActivityModul(self):
    # Test name: TS_03 User Activity Modul
    # Step # | name | target | value
    # 1 | open | /home/feed | 
    self.driver.get("http://103.183.75.202:819//home/feed")
    # 2 | setWindowSize | 1552x832 | 
    self.driver.set_window_size(1552, 832)
    # 3 | mouseOver | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | mouseOut | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 5 | mouseOver | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | click | css=#navbarDropdownUser .komiqus-pp | 
    self.driver.find_element(By.CSS_SELECTOR, "#navbarDropdownUser .komiqus-pp").click()
    # 7 | mouseOut | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 8 | click | css=.stretched-link:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".stretched-link:nth-child(1)").click()
    # 9 | click | css=.col-xxl-2:nth-child(4) .h-sub-caps | 
    self.driver.find_element(By.CSS_SELECTOR, ".col-xxl-2:nth-child(4) .h-sub-caps").click()
    # 10 | click | css=.cr-itm:nth-child(2) .img-fluid | 
    self.driver.find_element(By.CSS_SELECTOR, ".cr-itm:nth-child(2) .img-fluid").click()
    # 11 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 12 | click | css=.single > .button__loader | 
    self.driver.find_element(By.CSS_SELECTOR, ".single > .button__loader").click()
    # 13 | mouseOver | css=.single | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".single")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | mouseOver | css=.btn-outline-danger > .button__loader | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-danger > .button__loader")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 15 | click | css=.btn-outline-danger > .button__loader | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-danger > .button__loader").click()
    # 16 | mouseOut | css=.btn-outline-danger > .button__loader | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 17 | click | css=.swal2-confirm | 
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    # 18 | click | css=.col-xxl-2:nth-child(3) .font-sans-serif | 
    self.driver.find_element(By.CSS_SELECTOR, ".col-xxl-2:nth-child(3) .font-sans-serif").click()
    # 19 | click | linkText=Genre | 
    self.driver.find_element(By.LINK_TEXT, "Genre").click()
    # 20 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 21 | click | linkText=4-koma | 
    self.driver.find_element(By.LINK_TEXT, "4-koma").click()
    # 22 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 23 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 24 | click | css=#sm-browse > .nav-item:nth-child(1) .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#sm-browse > .nav-item:nth-child(1) .d-flex").click()
    # 25 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 26 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 27 | runScript | window.scrollTo(0,28.799999237060547) | 
    self.driver.execute_script("window.scrollTo(0,28.799999237060547)")
    # 28 | click | css=#book-list-1 .img-fluid | 
    self.driver.find_element(By.CSS_SELECTOR, "#book-list-1 .img-fluid").click()
    # 29 | runScript | window.scrollTo(0,597.5999755859375) | 
    self.driver.execute_script("window.scrollTo(0,597.5999755859375)")
    # 30 | runScript | window.scrollTo(0,300) | 
    self.driver.execute_script("window.scrollTo(0,300)")
    # 31 | click | id=rater | 
    self.driver.find_element(By.ID, "rater").click()
    # 32 | runScript | window.scrollTo(0,300) | 
    self.driver.execute_script("window.scrollTo(0,300)")
    # 33 | click | css=.nav-item:nth-child(1) > .active > .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(1) > .active > .d-flex").click()
    # 34 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 35 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 36 | click | css=#sb-tmp-tb .arrow-more | 
    self.driver.find_element(By.CSS_SELECTOR, "#sb-tmp-tb .arrow-more").click()
    # 37 | mouseOver | css=#book-list-1 .img-fluid | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#book-list-1 .img-fluid")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 38 | click | css=#book-list-1 .img-fluid | 
    self.driver.find_element(By.CSS_SELECTOR, "#book-list-1 .img-fluid").click()
    # 39 | runScript | window.scrollTo(0,800) | 
    self.driver.execute_script("window.scrollTo(0,800)")
    # 40 | click | css=.btn-review > .de-none | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-review > .de-none").click()
    # 41 | click | id=title | 
    self.driver.find_element(By.ID, "title").click()
    # 42 | type | id=title | Review
    self.driver.find_element(By.ID, "title").send_keys("Review")
    # 43 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 44 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 45 | editContent | id=tinymce | <p>Komiknya keren!</p>
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Komiknya keren!</p>'}", element)
    # 46 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 47 | click | css=.btn-sm:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-sm:nth-child(3)").click()
    # 48 | click | id=discussion-tab | 
    self.driver.find_element(By.ID, "discussion-tab").click()
    # 49 | click | css=.rounded-end > .de-none | 
    self.driver.find_element(By.CSS_SELECTOR, ".rounded-end > .de-none").click()
    # 50 | click | id=topic-title | 
    self.driver.find_element(By.ID, "topic-title").click()
    # 51 | type | id=topic-title | Test diskusi 3
    self.driver.find_element(By.ID, "topic-title").send_keys("Test diskusi 3")
    # 52 | selectFrame | index=1 | 
    self.driver.switch_to.frame(1)
    # 53 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 54 | editContent | id=tinymce | <p>Test pendapat kalian</p>
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Test pendapat kalian</p>'}", element)
    # 55 | selectFrame | relative=parent | 
    self.driver.switch_to.default_content()
    # 56 | click | css=.write-btn > .rounded-start:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".write-btn > .rounded-start:nth-child(2)").click()
    # 57 | click | css=.ng-scope:nth-child(1) > .position-relative .stretched-link | 
    self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .position-relative .stretched-link").click()
    # 58 | mouseOver | id=dropdown-sngl-opt | 
    element = self.driver.find_element(By.ID, "dropdown-sngl-opt")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 59 | click | id=dropdown-sngl-opt | 
    self.driver.find_element(By.ID, "dropdown-sngl-opt").click()
    # 60 | mouseOut | id=dropdown-sngl-opt | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 61 | click | linkText=Hapus | 
    self.driver.find_element(By.LINK_TEXT, "Hapus").click()
    # 62 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 63 | click | css=.swal2-confirm | 
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
    # 64 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 65 | click | linkText=Komik | 
    self.driver.find_element(By.LINK_TEXT, "Komik").click()
    # 66 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 67 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 68 | runScript | window.scrollTo(0,202.39999389648438) | 
    self.driver.execute_script("window.scrollTo(0,202.39999389648438)")
    # 69 | click | css=#book-list-1 .bi-info-square | 
    self.driver.find_element(By.CSS_SELECTOR, "#book-list-1 .bi-info-square").click()
    # 70 | runScript | window.scrollTo(0,323.20001220703125) | 
    self.driver.execute_script("window.scrollTo(0,323.20001220703125)")
    # 71 | click | id=book-info-modal | 
    self.driver.find_element(By.ID, "book-info-modal").click()
    # 72 | click | css=.show > .bi-collection | 
    self.driver.find_element(By.CSS_SELECTOR, ".show > .bi-collection").click()
    # 73 | click | linkText=Action | 
    self.driver.find_element(By.LINK_TEXT, "Action").click()
  

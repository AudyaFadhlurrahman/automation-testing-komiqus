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

class TestTS05FeedModul():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tS05FeedModul(self):
    # Test name: TS_05 Feed Modul
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
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | mouseOut | css=#navbarDropdownUser .komiqus-pp | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | click | linkText=Pengaturan | 
    self.driver.find_element(By.LINK_TEXT, "Pengaturan").click()
    # 9 | click | linkText=Social Link | 
    self.driver.find_element(By.LINK_TEXT, "Social Link").click()
    # 10 | click | css=#sm-browse > .nav-item:nth-child(3) .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#sm-browse > .nav-item:nth-child(3) .d-flex").click()
    # 11 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 12 | click | name=keyword | 
    self.driver.find_element(By.NAME, "keyword").click()
    # 13 | type | name=keyword | aksi
    self.driver.find_element(By.NAME, "keyword").send_keys("aksi")
    # 14 | click | css=.card:nth-child(3) .light > img | 
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .light > img").click()
    # 15 | click | css=#mm-home .d-flex | 
    self.driver.find_element(By.CSS_SELECTOR, "#mm-home .d-flex").click()
    # 16 | click | id=newsfeed-tab | 
    self.driver.find_element(By.ID, "newsfeed-tab").click()
    # 17 | click | css=#lv-typ_feed-94 .ng-binding | 
    self.driver.find_element(By.CSS_SELECTOR, "#lv-typ_feed-94 .ng-binding").click()
    # 18 | click | css=#cmnt-act-typ_feed-94 .btn-cmnt | 
    self.driver.find_element(By.CSS_SELECTOR, "#cmnt-act-typ_feed-94 .btn-cmnt").click()
    # 19 | type | css=#form-cmnt-typ_feed-94 > .form-control | keren!
    self.driver.find_element(By.CSS_SELECTOR, "#form-cmnt-typ_feed-94 > .form-control").send_keys("keren!")
    # 20 | click | css=#form-cmnt-typ_feed-94 .bi-arrow-right | 
    self.driver.find_element(By.CSS_SELECTOR, "#form-cmnt-typ_feed-94 .bi-arrow-right").click()
    # 21 | runScript | window.scrollTo(0,1223.199951171875) | 
    self.driver.execute_script("window.scrollTo(0,1223.199951171875)")
    # 22 | click | css=.text-primary > .ng-binding | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-primary > .ng-binding").click()
    # 23 | click | linkText=Hapus | 
    self.driver.find_element(By.LINK_TEXT, "Hapus").click()
    # 24 | click | css=.swal2-confirm | 
    self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
  

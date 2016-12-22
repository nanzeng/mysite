from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://127.0.0.1:8000')

assert 'Django' in driver.title
#Selenium Example (Python) for Login Page Testing:
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example-login.com")

# Test valid login
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("pass")
driver.find_element(By.ID, "login").click()
assert "Dashboard" in driver.title

# Test invalid login
driver.get("https://example-login.com")
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "login").click()
assert "Invalid credentials" in driver.page_source
driver.quit()

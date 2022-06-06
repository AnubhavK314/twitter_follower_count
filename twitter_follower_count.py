from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Setup webdriver
driver = webdriver.Firefox(executable_path='./geckodriver.exe')
driver.implicitly_wait(10)

#Followers count
driver.get('https://twitter.com/anubhavk314')
followers_count = int(driver.find_element_by_css_selector('a[href="/anubhavk314/followers"] > span > span').text)
print(followers_count)
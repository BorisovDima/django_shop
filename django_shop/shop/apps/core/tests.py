import os

if os.environ.get('PROJECT_TEST') == 'PRODUCTION':
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    WebDriver = webdriver.Remote(
          command_executor='http://selenium:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
else:
    from selenium.webdriver.firefox.webdriver import WebDriver
    WebDriver = WebDriver

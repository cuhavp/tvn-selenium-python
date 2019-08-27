import pytest
import selenium.webdriver
import json
from os import path


@pytest.fixture
def browser(cbt_config, request):
    # This browser will be local
    # ChromeDriver must be on the system PATH
    b = selenium.webdriver.Chrome("/Users/hdo/Documents/chromedriver")
    b.implicitly_wait(10)
    b.get(cbt_config['env']['base_url'])
    failed_before = request.session.testsfailed
    yield b
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(b, test_name)
    b.quit()


@pytest.fixture
def cbt_config(scope='session'):
    config_path = path.realpath('project/cbt_config.json')
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config


def take_screenshot(browser, test_name):
    screenshots_dir = "project/reports"
    screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
    browser.save_screenshot(
        screenshot_file_path
    )

from selene import browser, have
import pytest

@pytest.fixture(params=[(1366, 768), (1600, 900), (1920, 1080)], scope='function')
def dekstop_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()

@pytest.fixture(params=[(375, 768), (414, 896), (390, 844)], scope='function')
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()

def test_github_dekstop(dekstop_browser):
    browser.open('/')
    browser.element('[class~="HeaderMenu-link--sign-in"]').click()
    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))

def test_github_mobile(mobile_browser):
    browser.open('/')

    browser.element('[class="flex-1 flex-order-2 text-right"] .Button-content').click()
    browser.element('[class~="HeaderMenu-link--sign-in"]').click()

    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))
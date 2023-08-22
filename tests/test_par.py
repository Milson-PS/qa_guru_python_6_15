import pytest
from selene import browser, have

mobile = pytest.mark.parametrize('browser_manager', [(375, 667), (414, 896), (390, 844)], indirect=True)
dekstop = pytest.mark.parametrize('browser_manager', [(1366, 768), (1600, 900), (1920, 1080)], indirect=True)

@pytest.fixture(params=[(1366, 768), (1600, 900), (1920, 1080),
                        (375, 667), (414, 896), (390, 844)],
                scope='function',
                autouse=True)
def browser_manager(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()

@dekstop
def test_github_desktop(browser_manager):
    browser.open('/')

    browser.element('[class~="HeaderMenu-link--sign-in"]').click()

    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))


@mobile
def test_github_mobile(browser_manager):
    browser.open('/')

    browser.element('[class="flex-1 flex-order-2 text-right"] .Button-content').click()
    browser.element('[class~="HeaderMenu-link--sign-in"]').click()

    browser.element('[class="auth-form-header p-0"]').should(have.text('Sign in to GitHub'))

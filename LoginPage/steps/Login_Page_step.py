from behave import *
from selenium import webdriver
from POM.Browser import MyBrowser
from POM.Dashboard import DashBoard
from POM.Base import Base
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage


@given('Open "{url}"')
def navigate_to_url(context, url):
    context.driver.get(url)


@when('Move to login page')
def navigate_to_login(context):
    HomePage(context.driver).move_to_login_page()


@then('Login page should be loaded')
def verify_on_login_page(context):
    element = LoginPage(context.driver).verify_login_page()
    assert element is not None, 'Failed to load login page.'


@given('Wait for login page')
def wait_for_login_page(context):
    LoginPage(context.driver).verify_login_page()


@when('enter "{username}" and "{password}" as credentials')
def input_creds(context, username, password):
    LoginPage(context.driver).login(username, password)


@then('Dashboard should be loaded.')
def verify_login_complete(context):
    element = DashBoard(context.driver).verify_dashboard()
    assert element is not None, 'Failed to login'


@when('Click on Logout option')
def perform_logout(context):
    HomePage(context.driver).logout()


@then('User should be logged out')
def verify_logout(context):
    status = HomePage(context.driver).verify_logout()
    assert status is True, 'Successful Logout message is not appearing'

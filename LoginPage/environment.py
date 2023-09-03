from POM.Browser import MyBrowser


def before_all(context):
    context.driver = MyBrowser().chrome()
    context.driver.maximize_window()
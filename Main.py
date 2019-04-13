from WebdriverController import WebdriverController

url = 'https://www.google.com/recaptcha/api2/demo' #input('Enter website url:\n') #'https://www.google.com/recaptcha/api2/demo' 'https://patrickhlauke.github.io/recaptcha/' 'https://www.mozilla.org/'

webdriver = WebdriverController(url)

webdriver.solve_recaptcha()
webdriver.close()
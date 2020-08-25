from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.keys import Keys

url = 'http://www.portalredevw.com.br/'

login = 'test'
password = '1234'

browser = Firefox()

browser.get(url)

sleep(5)

frame1 = browser.find_element_by_xpath('/html/frameset/frame[1]')
browser.switch_to.frame(frame1)

frame2 = browser.find_element_by_xpath('//*[@id="divframe"]')
browser.switch_to.frame(frame2)

frame3 = browser.find_element_by_xpath('//*[@id="main"]')
browser.switch_to.frame(frame3)

frame4 = browser.find_element_by_xpath('//*[@id="mainApp"]')
browser.switch_to.frame(frame4)

frame5 = browser.find_element_by_xpath('//*[@id="HeaderMenu"]')
browser.switch_to.frame(frame5)

input_login = browser.find_element_by_xpath('//*[@id="txtCPFCNPJ"]')
input_login.send_keys(login)

input_password = browser.find_element_by_xpath('//*[@id="txtSenha"]')
input_password.send_keys(password)

button = browser.find_element_by_xpath('//*[@id="btnLogin"]')
button.click()



# browser.switch_to.frame(iframe)

# login = "test"
# password = "1234"

# input_login = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/table/tbody/tr/td[1]/table/tbody/tr/td[3]/input[1]')
# input_login.send_keys('test')
# browser.switch_to.default_content()

# element.close()

# browser.find_element_by_name("submit").click()

# driver = webdriver.Firefox()

# browser.quit()
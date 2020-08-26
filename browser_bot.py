from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.keys import Keys

url = 'http://www.portalredevw.com.br/'

login = 'test'
password = '1234'

browser = Firefox()

browser.get(url)

sleep(1)

frame_1 = browser.find_element_by_xpath('/html/frameset/frame[1]')
browser.switch_to.frame(frame_1)

frame_2 = browser.find_element_by_xpath('//*[@id="divframe"]')
browser.switch_to.frame(frame_2)

frame_3 = browser.find_element_by_xpath('//*[@id="main"]')
browser.switch_to.frame(frame_3)

frame_4 = browser.find_element_by_xpath('//*[@id="mainApp"]')
browser.switch_to.frame(frame_4)

frame_5 = browser.find_element_by_xpath('//*[@id="HeaderMenu"]') # frame de login e senha
browser.switch_to.frame(frame_5)

input_login = browser.find_element_by_xpath('//*[@id="txtCPFCNPJ"]')
sleep(1)
input_login.send_keys(login)

input_password = browser.find_element_by_xpath('//*[@id="txtSenha"]')
sleep(1)
input_password.send_keys(password)

button = browser.find_element_by_xpath('//*[@id="btnLogin"]')
button.click()

alert_obj = browser.switch_to.alert #mudando o foco para o alert
sleep(1)
alert_obj.accept()

browser.switch_to.default_content() #voltando para o html pai

browser.switch_to.frame(frame_1)
browser.switch_to.frame(frame_2)
browser.switch_to.frame(frame_3)
browser.switch_to.frame(frame_4)

frame_6 = browser.find_element_by_xpath('//*[@id="App"]') #frame do link no rodapé
browser.switch_to.frame(frame_6)

window_before = browser.window_handles[0] #armazenar identificador da janela

linkVolkswagen = browser.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a[1]')
linkVolkswagen.click()

window_after = browser.window_handles[1] #armazenar identificador da nova janela

browser.switch_to.window(window_after) #mudando de janela






# element.close()

# browser.quit()
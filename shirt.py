from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

pwd = "troloddssdd"
#driver = webdriver.Firefox()
#driver.get("http://www.facebook.com")
#assert "Facebook" in driver.title
#elem = driver.find_element_by_id("email")
#elem.send_keys(user)
#elem = driver.find_element_by_id("pass")
#elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)

#flipkart = webdriver.Firefox()
#flipkart.get("https://www.flipkart.com/")
#flipkart.maximize_window()
#flipkart.find_element_by_link_text("Log In").click()
#flipkart.find_element_by_class_name("_2zrpKA").send_keys(user2 , Keys.TAB , pwd2 , Keys.RETURN)


#while im.getpixel((1244, 278)) != (59, 159, 226)
#	email.implicitly_wait(5)
#	email.find_element_by_id("click-to-refresh").click()
for i in range (1,5):
	email = webdriver.Firefox()
	bit = webdriver.Firefox()
	email.get("https://temp-mail.org/en/")
	bit.get("https://www.interviewbit.com/invite/fedjhb")
	email.maximize_window()
	bit.maximize_window()
	email.find_element_by_id("click-to-copy").click() 
	bit.find_element_by_link_text("Sign Up").click()
	bit.find_element_by_id("user_email").send_keys(Keys.CONTROL, 'v') 
	bit.find_element_by_id("user_email").send_keys(Keys.TAB , 'KOLPOL'+str(i) ,Keys.TAB , pwd ,Keys.TAB , pwd ,Keys.TAB , Keys.RETURN)
	email.implicitly_wait(10)
	while (pyautogui.pixelMatchesColor(1244, 278, (26, 188, 156)))==False:
		email.implicitly_wait(3)
		email.find_element_by_id("click-to-refresh").click()
	email.find_element_by_link_text("Confirmation instructions").click()
	while (pyautogui.pixelMatchesColor(878, 819, (106, 198, 219)))==False:
		email.implicitly_wait(1)
	email.find_element_by_link_text("Verify Email Address").click()
	email.close()
	bit.close()

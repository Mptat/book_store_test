#Registration_login:регистрация аккаунта
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# # 1.Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2.Нажмите на вкладку "My Account Menu"
# my_account=driver.find_element_by_css_selector("#menu-item-50 >a")
# my_account.click()
# # 3.В разделе " Register", введите email для регистрации
# email= driver.find_element_by_id("reg_email")
# text_reg_email = "Nat_Oreiro@gmail.com"
# email.send_keys(text_reg_email)
# # 4.В разделе " Register", введите пароль для регистрации
# password=driver.find_element_by_id("reg_password")
# text_reg_password="Brazilia2001!&?"
# password.send_keys(text_reg_password)
# # 5.Нажмите на кнопку "Register"
# name_reg=driver.find_element_by_name("register")
# name_reg.click()
# driver.quit()

###############################
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1.Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2.Нажмите на вкладку "My Account Menu"
my_account=driver.find_element_by_css_selector("#menu-item-50 >a")
my_account.click()
# 3.В разделе "Login", введите email для логина
email= driver.find_element_by_id("username")
text_email = "Nat_Oreiro@gmail.com"
email.send_keys(text_email)
# 4.В разделе "Login", введите пароль для логина
password=driver.find_element_by_id("password")
text_password="Brazilia2001!&?"
password.send_keys(text_password)
# 5.Нажмите на кнопку "Login"
login=driver.find_element_by_name("login")
login.click()
#6.Добавьте проверку, что на странице есть элемент "Logout"
logout=driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation > ul > li:nth-child(6) >a")
assert logout
#driver.quit()
# HOME. Добавление комментария
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1.Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2.Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
# 3.Нажмите на название книги "Selenium Ruby" или на кнопку "READ"
selenium_ruby=driver.find_element_by_css_selector('[title="Selenium Ruby"]')
selenium_ruby.click()
# 4.Нажмите на вкладку "REVIEW"
reviews=driver.find_element_by_css_selector('a[href="#tab-reviews"]')
reviews.click()
# 5.Поставьте 5 звёзд
star5 = driver.find_element_by_css_selector('a.star-5')
star5.click()
# 6.Заполните поле "Rewiew" сообщением : "Nice book!"
comment= driver.find_element_by_id("comment")
text = "Nice book!"
comment.send_keys(text)
# 7.Заполните поле "Name"
name= driver.find_element_by_id("author")
text_au = "Natali Oreiro"
name.send_keys(text_au)
# 8.Заполните "Email"
email = driver.find_element_by_id("email")
text_email = "Nat_Oreiro@gmail.com"
email.send_keys(text_email)
# 9.Нажмите на кнопку "SUBMIT"
submit_ = driver.find_element_by_id("submit")
submit_.click()
driver.quit()
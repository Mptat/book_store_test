# Shop:  отображение страницы товара
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
# 1.Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2.Залогиньтесь
my_account=driver.find_element_by_css_selector("#menu-item-50 >a")
my_account.click()
email= driver.find_element_by_id("username")
text_email = "Nat_Oreiro@gmail.com"
email.send_keys(text_email)
password=driver.find_element_by_id("password")
text_password="Brazilia2001!&?"
password.send_keys(text_password)
login=driver.find_element_by_name("login")
login.click()
# 3.Нажмите на вкладку "Shop"
shop=driver.find_element_by_css_selector("#menu-item-40 >a")
shop.click()
# 4.Откройте книгу "HTML 5 Forms"
html5=driver.find_element_by_css_selector('img[alt="Mastering HTML5 Forms"]')
html5.click()
# 5.Добавьте тест, что заголовок книги назвается :"HTML5 Forms"
reviews=driver.find_element_by_css_selector('a[href="#tab-reviews"]')
reviews.click()
comment= driver.find_element_by_id("comment")
text = "Заголовок книги называется : 'HTML5 Forms'"
comment.send_keys(text)
submit_ = driver.find_element_by_id("submit")
submit_.click()
print(text)
driver.quit()
###############################################################################
##Shop:количество товаров в категории
# #1.Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# ##2.Залогиньтесь
# my_account=driver.find_element_by_css_selector("#menu-item-50 >a")
# my_account.click()
# email= driver.find_element_by_id("username")
# text_email = "Nat_Oreiro@gmail.com"
# email.send_keys(text_email)
# password=driver.find_element_by_id("password")
# text_password="Brazilia2001!&?"
# password.send_keys(text_password)
# login=driver.find_element_by_name("login")
# login.click()
# ##3.Нажмите на вкладку "Shop"
# shop=driver.find_element_by_css_selector("#menu-item-40 >a")
# shop.click()
# ##4.Откройте категорию "HTML"
# html = driver.find_element_by_css_selector(".product-categories > li:nth-child(2) > a")
# html.click()
# ##5.Добавьте тест, что отображается три товара
# #html_count = driver.find_element_by_css_selector(".product-categories > li:nth-child(2) > span")
# html_count = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-categories > li:nth-child(2) > span"), "(3)"))
# #print(html_count)
# if html_count == True:
#     print('Отображается три товара')
# else:
#     print('Отображается не три товара')
# driver.quit()

############################################################
# from selenium.webdriver.support.select import Select
# # Shop:сортировка товаров
# # 1.Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2.Залогиньтесь
# my_account=driver.find_element_by_css_selector("#menu-item-50 >a")
# my_account.click()
# email= driver.find_element_by_id("username")
# text_email = "Nat_Oreiro@gmail.com"
# email.send_keys(text_email)
# password=driver.find_element_by_id("password")
# text_password="Brazilia2001!&?"
# password.send_keys(text_password)
# login=driver.find_element_by_name("login")
# login.click()
# # 3.Нажмите на вкладку "Shop"
# shop=driver.find_element_by_css_selector("#menu-item-40 >a")
# shop.click()
# # 4.Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# # •Используйте проверку по value
# element = driver.find_element_by_name("orderby")
# select = Select(element)
# selected_ = element.get_attribute("value")
# if selected_ == 'menu_order':
#    print("Выбран вариант сортировки по умолчанию")
# else:
#     print("Выбран другой вариант сортировки "+selected_)
# select.select_by_value("menu_order")
# # 5.Отсортируйте товары от большего к меньшему
# # •в селекторах используйте класс Select
# select.select_by_value("price-desc")
# # 6.Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# element = driver.find_element_by_name("orderby")
# # 7.Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
# # •Используйте проверку по value
# selected_ = element.get_attribute("value")
# if selected_ == 'price-desc':
#    print("Выбран вариант сортировки: price-desc")
# else:
#     print("Выбран другой вариант сортировки "+selected_)
# driver.quit()
#########################################################
# #Shop:отображение, скидка товара
# #1.Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# #2.Залогиньтесь
# my_account=driver.find_element_by_css_selector("#menu-item-50 >a")
# my_account.click()
# email= driver.find_element_by_id("username")
# text_email = "Nat_Oreiro@gmail.com"
# email.send_keys(text_email)
# password=driver.find_element_by_id("password")
# text_password="Brazilia2001!&?"
# password.send_keys(text_password)
# login=driver.find_element_by_name("login")
# login.click()
# #3.Нажмите на вкладку "Shop"
# shop=driver.find_element_by_css_selector("#menu-item-40 >a")
# shop.click()
# # 4.Откройте книгу "Android Quick Start Guide"
# book_android=driver.find_element_by_css_selector('img[alt="Android Quick Start Guide"]')
# book_android.click()
# # 5.Добавьте тест, что содержимое старой цены = 600.00 используйте assert
# old_price=driver.find_element_by_css_selector(".price>del>span")
# assert old_price.text == "₹600.00"
# # 6.Добавьте тест, что содержимое новой цены = 450 .00 используйте assert
# new_price=driver.find_element_by_css_selector(".price>ins>span")
# assert new_price.text == "₹450.00"
# # 7.Добавьте явное ожидание и нажмите на обложку книги
# # •Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# book1 = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Android Quick Start Guide"]')))
# book1.click()
# # 8.Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# pp_close = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.pp_close')))
# pp_close.click()
# driver.quit()
##############################################################################
# # Shop:проверка цены в корзине
# # 1.Откройте http://practice.automationtesting.in
# driver.get("http://practice.automationtesting.in/")
# # 2.Нажмите на вкладку "Shop"
# shop=driver.find_element_by_css_selector("#menu-item-40 >a")
# shop.click()
# # 3.Добавьте в корзину книгу "HTML5 WebApp Development"
# product182=driver.find_element_by_css_selector('[data-product_id="182"]')
# product182.click()
# # 4.Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item, а стоимость = "₹180.00"
# # •Используйте для проверки assert
# item_ = driver.find_element_by_css_selector(".wpmenucart-contents> span:nth-child(2)")
# price=driver.find_element_by_css_selector(".wpmenucart-contents> span:nth-child(3)")
# #print(item_.text)
# #print(price.text)
# assert item_.text == "1 Item"
# assert price.text == "₹180.00"
# # 5.Перейдите в корзину
# busket=driver.find_element_by_css_selector('a[title="View your shopping cart"]')
# busket.click()
# # 6.Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal = WebDriverWait(driver, 20).until(
# EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-title="Subtotal"]>span')))
# print(subtotal)
# # 7.Используя явное ожидание, проверьте что в Total отобразилась стоимость
# total = WebDriverWait(driver, 20).until(
# EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-title="Total"]>span')))
# print(total)
# driver.quit()

###################################################
# Shop:работа в корзине
# # 1.Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
# # 2.Нажмите на вкладку "Shop"
# shop=driver.find_element_by_css_selector("#menu-item-40 >a")
# shop.click()
# # 3.Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # •Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# driver.execute_script("window.scrollBy(0, 300);")
# product182=driver.find_element_by_css_selector('[data-product_id="182"]')
# product182.click()
# time.sleep(2)
# product180=driver.find_element_by_css_selector('[data-product_id="180"]')
# product180.click()
# # •После добавления 1 й книги добавьте sleep
# # 4.Перейдите в корзину
# busket=driver.find_element_by_css_selector('a[title="View your shopping cart"]')
# busket.click()
# # 5.Удалите первую книгу
# time.sleep(3)
# product182del=driver.find_element_by_css_selector('a[data-product_id="182"]')
# product182del.click()
# # •Перед удалением добавьте sleep
# # 6.Нажмите на Undo (отмена удаления)
# time.sleep(3)
# undo = driver.find_element_by_css_selector('.woocommerce-message > a')
# undo.click()
# # 7.В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm"
# # •Предварительно очистите поле с помощью локатор_поля .
# count_book=driver.find_element_by_css_selector('table>:nth-child(2)>tr:nth-child(1)>td:nth-child(5)>div>input')
# count_book.clear()
# text_="3"
# count_book.send_keys(text_)
# #table>:nth-child(2)>tr:nth-child(1)>td:nth-child(5)>div>input
# # 8.Нажмите на кнопку "UPDATE BASKET"
# update_cart = driver.find_element_by_name("update_cart")
# update_cart.click()
# # 9.Добавьте тест, что value элемента quantity для "JS Data Structures and равно 3 используйте assert
# count_book=driver.find_element_by_css_selector('table>:nth-child(2)>tr:nth-child(1)>td:nth-child(5)>div>input')
# val_count_book = count_book.get_attribute("value")
# assert val_count_book == '3'
# # 10.Нажмите на кнопку "APPLY COUPON"
# # •Перед нажатимем добавьте sleep
# time.sleep(3)
# coupon_btn = driver.find_element_by_name("apply_coupon")
# coupon_btn.click()
# # 11.Добавьте тест, что возникло сообщение : "Please enter a coupon code"
# time.sleep(3)
# element=driver.find_element_by_css_selector(".woocommerce-error>li")
# element_get_text = element.text
# assert "Please enter a coupon code" in element_get_text
# driver.quit()
############################################
## Shop:покупка товара
from selenium.webdriver.support.select import Select
## 1.Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
## 2.Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop = driver.find_element_by_css_selector("#menu-item-40 >a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)
## 3.Добавьте в корзину книгу "HTML5 WebApp DEvelopment"
product182 = driver.find_element_by_css_selector('[data-product_id="182"]')
product182.click()
## 4.Перейдите в корзину
time.sleep(3)
busket = driver.find_element_by_css_selector('a[title="View your shopping cart"]')
busket.click()
## 5.Нажмите "PROCEED TO CHECKOUT"
## •Перед нажатием, добавьте явное ожидание
checkout_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))
)
checkout_btn.click()
## 6.Заполните все обязательные поля
first_name= driver.find_element_by_id("billing_first_name")
text_first_name = "Nata"
first_name.send_keys(text_first_name)
last_name= driver.find_element_by_id("billing_last_name")
text_last_name = "Oreiro"
last_name.send_keys(text_last_name)
email = driver.find_element_by_id("billing_email")
text_email = "Nat_Oreiro@gmail.com"
email.send_keys(text_email)
phone= driver.find_element_by_id("billing_phone")
text_phone = "89213456778"
phone.send_keys(text_phone)
billing_address= driver.find_element_by_id("billing_address_1")
text_billing_address = "ul.Lenina"
billing_address.send_keys(text_billing_address)
billing_address2= driver.find_element_by_id("billing_address_2")
text_billing_address2 = "233-34"
billing_address2.send_keys(text_billing_address2)
billing_city= driver.find_element_by_id("billing_city")
text_billing_city = "Moscow"
billing_city.send_keys(text_billing_city)
billing_state= driver.find_element_by_id("billing_state")
text_billing_state = "Russia"
billing_state.send_keys(text_billing_state)
billing_postcode = driver.find_element_by_id("billing_postcode")
text_billing_postcode='203405'
billing_postcode.send_keys(text_billing_postcode)
## 7.Выберите способ оплаты "Check Payments"
## •Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payment= driver.find_element_by_id("payment_method_cheque")
payment= driver.find_element_by_css_selector('[for="payment_method_cheque"]')
payment.click()
## 8.Нажмите PLACE ORDER
place_order_btn  = driver.find_element_by_id("place_order")
place_order_btn.click()
## 9.Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been reseived"
thanks_text = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-template-default"), "Thank you. Your order has been reseived"))
# 10.Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
check_text = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "table>:nth-child(3)>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()
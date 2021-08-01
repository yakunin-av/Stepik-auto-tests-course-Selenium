from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # Нажать на кнопку "Book"     
    #button = browser.find_element_by_xpath("//button[@id='book']") 
    #button.click()
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
        )    
    #button = 
    #WebDriverWait(browser, 5).until(
    #   EC.element_to_be_clickable((By.ID, "price"))
    #   )
    browser.execute_script("window.scrollBy(0, 105);")
    button = browser.find_element_by_xpath("//button[@id='book']") 
    button.click()
    browser.execute_script("window.scrollBy(0, 110);")
    x_element = browser.find_element_by_xpath("//span[@id='input_value']") 
    x = x_element.text
    y = calc(x)
    print(x)
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)  
    button = browser.find_element_by_xpath("//button[@id='solve']")
    button.click()  
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

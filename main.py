from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# путь до файла
path_upload = "C:\\!!!путь до файла!!!\\image.png"

# загрузка файла
click_button = driver_chrome.find_element(By.ID, "file")
click_button.send_keys(path_upload)

# проверка загрузки
value_text = driver_chrome.find_element(By.XPATH, "//*[@id='error']").text
text_after_loading = "File Successfully Uploaded"
assert value_text == text_after_loading, "Ошибка: Текст должен совпадать!"
print("Успешная загрузка.")

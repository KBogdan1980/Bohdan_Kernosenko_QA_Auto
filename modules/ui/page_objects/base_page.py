#тут будуть базові операції для роботи з браузером, такі як проініціалізувати драйвер і закрити браузер
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    PATH = r"/home/bohdan/Bohdan_Kernosenko_QA_Auto/"
    DRIVER_NAME = "chromedriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
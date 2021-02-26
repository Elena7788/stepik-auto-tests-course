from selenium import webdriver
import math, time, pytest


def test_with_firefox():
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    driver = webdriver.Firefox()

    driver.get("https://stepik.org/lesson/25969/step/8")

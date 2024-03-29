#pytest -v --tb=line --language=en test_main_page.py
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

    link = "http://selenium1py.pythonanywhere.com/"


    def test_guest_can_go_to_login_page(self, browser):

        page = MainPage(browser, TestLoginFromMainPage.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, TestLoginFromMainPage.link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        """
        Гость открывает главную страницу
        Переходит в корзину по кнопке в шапке сайта
        Ожидаем, что в корзине нет товаров
        Ожидаем, что есть текст о том что корзина пуста
        """


        page = MainPage(browser, TestLoginFromMainPage.link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_for_blank_basket()
        basket_page.check_text_for_blank_basket()

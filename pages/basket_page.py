from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_for_blank_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_BOX), "Basket is not blank"

    def check_text_for_blank_basket(self):
        assert  self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket has not text what she blank"

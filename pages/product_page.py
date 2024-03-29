from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_card(self):
        button_add_to_card = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        button_add_to_card.click()

    def get_list_of_messages(self):
        message_box = self.browser.find_element(*ProductPageLocators.MESSAGE_BOX)
        return message_box.find_elements(*ProductPageLocators.MESSAGES)

    def check_message_for_correct_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert any([product_name == mess.text for mess in self.get_list_of_messages()]), "Not product name in messages"

    def check_card_price_for_one_good(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert any([product_price == mess.text for mess in self.get_list_of_messages()]), "Not product price in messages"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES), \
           "Success message is presented, but should not be"

    def should_not_be_success_message_with_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES), \
           "Success message is presented, but should not be"

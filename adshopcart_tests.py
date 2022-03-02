import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdvShoppingPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_open_adv_shopping_cart():
        methods.setUp()
        methods.sign_up()
        methods.check_account_info()
        methods.logout()
        methods.login(locators.new_username, locators.new_password)
        methods.delete_account()
        methods.login(locators.new_username, locators.new_password)
        methods.check_deleted_credentials()
        methods.tearDown()


    @staticmethod
    def test_check_adv_shopping_cart_homepage():
        methods.setUp()
        methods.check_main_logo()
        methods.check_advshoppingcart_homepage()
        methods.check_top_navigation_menu()
        methods.check_contact_us_form()

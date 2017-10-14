from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lets check out the new to-do web app!
        self.browser.get(self.live_server_url)

        # Notice the title page and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # You are invite to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                                                'Enter a to-do item')

        # Type buy peacock feathers into a text box
        inputbox.send_keys('Buy peacock feathers')
        # Hit enter, the page updates, and the page lists #1: buy peacock feathers
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        import time
        time.sleep(5)
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting addition of another item
        # Enter, use peacock feathers to make a fly
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        import time
        time.sleep(2)
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.checl_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail('Finish the test')

        # The page updates and both list items are shown

        # Will the site remember the list?
        # -Explanatory text that a unique url has been generated for the list

        # Revisit url - list still there


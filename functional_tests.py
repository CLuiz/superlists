from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Lets check out the new to-do web app!
        self.browser.get('http://localhost:8000')

        # Notice the title page and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


        # You are invite to enter a to-do item right away

# Type buy peacock feathers into atext box

# Hit enter, the page updates, adn the apge lists #1: buy peacock feathers

# There is still a text box inviting addition of another item
# Enter, use peacock feathers to fly

# The page updates and both list items are shown

# Will the site remember the list?
# -Explanatory text that a unique url has been generated for the list

# Revisit url - list still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')

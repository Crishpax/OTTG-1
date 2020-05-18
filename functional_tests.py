from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # X has heard about a new online to-do app
        # they go to check it out
        self.browser.get('http://localhost:8000')

        # they notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # they are invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # they type "Buy peacock feathers" into a text box
        # (it's their hobby)
        inputbox.send_keys('Buy peacock feathers')

        # once enter is hit, the page updates and now the page
        # lists: "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # there is still a text box inviting them to add another item
        # they enter "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the page updates again and now shows both items on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # X wonders whether the site will remember their list. Then they see
        # that the site has generated a unique URL for them -- there is some
        # explanatory text to that effect
        self.fail('Finish the test!')

        # X visits that URL - the to-do list is still there

        # satisfied, they go back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')

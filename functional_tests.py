from selenium import webdriver
import unittest


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
        self.fail('Finish the test!')

        # they are invited to enter a to-do item right away

        # they type "Buy peacock feathers" into a text box
        # (it's their hobby)

        # once enter is hit, the page updates and now the page
        # lists: "1: Buy peacock feathers" as an item in a to-do list

        # there is still a text box inviting them to add another item
        # they enter "Use peacock feathers to make a fly"

        # the page updates again and now shows both items on the list

        # X wonders whether the site will remember their list. Then they see
        # that the site has generated a unique URL for them -- there is some
        # explanatory text to that effect

        # X visits that URL - the to-do list is still there

        # satisfied, they go back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')

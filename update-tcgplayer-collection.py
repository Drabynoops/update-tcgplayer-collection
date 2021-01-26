from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas

chrome_driver_path = "{path}chromedriver.exe"
TCGPLAYER_EMAIL = "email@email.com"
TCGPLAYER_PASSWORD = "password"
SLEEP_TIME = 5 #Varies with internet speed. 5 is default

class TcgplayerCollectionAdder:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.card_data = {}

    def login(self):
        self.driver.get("https://www.tcgplayer.com/login?returnUrl=store.tcgplayer.com%2Fcollection")

        sleep(SLEEP_TIME)
        email = self.driver.find_element_by_name("Email")
        email.send_keys(TCGPLAYER_EMAIL)

        password = self.driver.find_element_by_name("Password")
        password.send_keys(TCGPLAYER_PASSWORD)

        sleep(SLEEP_TIME)
        password.send_keys(Keys.RETURN)

        sleep(SLEEP_TIME)
    
    def get_card_data(self, file="Collection.csv"):
        collection = pandas.read_csv("Collection.csv")
        self.card_data = pandas.DataFrame.to_dict(collection, orient="index")

    def add_cards_to_collection(self):
        errors = []
        add_tab = self.driver.find_element_by_id("addProductsTab")
        add_tab.click()
        sleep(SLEEP_TIME)

        input_box = self.driver.find_element_by_id("addProductSearchTerm")

        for card_index in self.card_data:
            card = self.card_data[card_index]
            input_box.clear()
            input_box.send_keys(card['Card Name'])
            sleep(SLEEP_TIME)
            search_name = card['Card Name'] + " - [Foil]" if card['Foil'] else card['Card Name']

            results_table = self.driver.find_element_by_id("resultsTable")
            table_rows = results_table.find_elements_by_xpath('table/tbody/tr')

            card_found = False
            for row in table_rows:
                have_up_arrow = row.find_element_by_class_name("CollectionUpArrow")
                card_name = row.find_element_by_xpath('td[4]/a').text
                set_name = row.find_element_by_xpath('td[5]').text
                if card_name == search_name and set_name == card['Set']:
                    for _ in range(card['Quantity']):
                        have_up_arrow.click()
                    card_found = True
                    break
            
            if not card_found:
                errors.append(card)
                print(f"{search_name} not found, possibly more than 50 results or site error")

        df = pandas.DataFrame(errors)
        df.to_csv("error_cards.csv", index=False)


collection_adder = TcgplayerCollectionAdder()
collection_adder.login()
collection_adder.get_card_data()
collection_adder.add_cards_to_collection()
# update-tcgplayer-collection
A script for updating your tcgplayer collection tracker using a csv file. (The best it can)

A simple script to automate the emptying out of large tcgplayer.com collections.

Written using Python version 3.9.0 so you'll need to install that. Might work using earlier versions, haven't tested.

Need the chromedriver for your particular version of Chrome

Required libraries: Selenium

Variables: chrome_driver_path - The location of the chromedriver file 
TCGPLAYER_EMAIL - The email you use to log into tcgplayer.com 
TCGPLAYER_PASSWORD = Your password 
SLEEP_TIME = The amount (in seconds) to wait for the page to load/accept input. Likes to lag especially on the log in screen

What is does: Logs you in using the link that will bring you straight to your TCGPlayer collection tracker. Clicks the add "Add Products to Collection" tab. Reads the csv file and searchs for and adds cards based on information provided. This is important, if the information is bad, it won't add them or it will add them incorrectly. 

Note: Etched cards and extended cards currently have to be manually added to the card name. 

Potential improvements: 
Adding fields for extended and etched cards that automatically add them to the card name.
Add a field to change with game/product type to search for.

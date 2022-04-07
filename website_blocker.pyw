# Imports
import time
from datetime import datetime as dt

# Location of Hosts File which contains the sites to be blocked
host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
host_temp = 'C:\\Users\\IFEANYI PC\\hosts'

# The site will be redirected to this host
redirect = '127.0.0.1'

# List of site to be blocked
website_list = ['www.instagram.com', 'instagram.com', 'www.twitter.com', 'twitter.com', 'www.google.com']

# Loop
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          12):
        print('Working Hours...')
        # Opens the hosts file
        with open(host_path, 'r+') as file:
            content = file.read()
            # Loop which checks the hosts file if the website is in the website_list
            for website in website_list:
                if website in content:
                    pass
                else:
                    # Writes the redirect host and website into the hosts file
                    file.write(redirect + "          " + website + '\n')
    else:
        # Opens the hosts file
        with open(host_path, 'r+') as file:
            # Stores the lines in the hosts file as a list
            content = file.readlines()
            # Places the pointer before the first character in the hosts file
            file.seek(0)
            # Iterates through the content list and checks if the website is in the line
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print('Fun hours...')
    # Runs the script every 5 seconds
    time.sleep(5)

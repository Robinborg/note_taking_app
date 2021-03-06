# Note taking app
A program to keep track of your information.
## Description
The program stores notes, podcasts, books and websites (the website module is able to webscrape).
## Prerequisites 
python 3.8 or newer. Link for [python](https://www.python.org/downloads/)
## Installing mongodb on macos

    brew tap mongodb/brew
    brew install mongodb-community@5.0
Starting mongodb:

    brew services start mongodb-community@5.0
Stopping mongodb:

    brew services stop mongodb-community@5.0
    
## Installation
    git clone https://github.com/Robinborg/note_taking_app
    cd note_taking_app
    python3 -m pip install -r requirements.txt

## Commands
    
    #Start prompt to enter notes
    python3 main.py --note 
    #Start prompt to enter website and search it for links
    python3 main.py --website
    #Start prompt to enter podcast
    python3 main.py --podcast
    #Start prompt to enter book
    python3 main.py --book 
    
    #display data
    python3 main.py --show_notes
    python3 main.py --show_websites
    python3 main.py --show_podcasts
    python3 main.py --show_books
## About
The program uses:

[Mongodb](https://www.mongodb.com) 

[requests](https://docs.python-requests.org/en/latest/)

[beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

[pymongo](https://pymongo.readthedocs.io/en/stable/index.html)

import requests
from bs4 import BeautifulSoup
import sqlite3

# Step 1: Scrape Pokemon data
url = 'https://pokemondb.net/pokedex/all'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table
table = soup.find('table', {'id': 'pokedex'})

# Extract column headers
headers = [header.text for header in table.find('thead').find_all('th')]

# Extract rows
rows = table.find('tbody').find_all('tr')

# Parse data
pokemon_data = []
for row in rows:
    cells = row.find_all('td')
    number = cells[0].text.strip()
    name = cells[1].text.strip()
    type_ = ', '.join([t.text for t in cells[2].find_all('a')])
    total = cells[3].text.strip()
    hp = cells[4].text.strip()
    attack = cells[5].text.strip()
    defense = cells[6].text.strip()
    sp_atk = cells[7].text.strip()
    sp_def = cells[8].text.strip()
    speed = cells[9].text.strip()
    
    pokemon_data.append((number, name, type_, total, hp, attack, defense, sp_atk, sp_def, speed))

# Step 2: Store data in SQLite database
conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS pokemon
             (number TEXT, name TEXT, type TEXT, total TEXT, hp TEXT,
              attack TEXT, defense TEXT, sp_atk TEXT, sp_def TEXT, speed TEXT)''')

# Insert data
c.executemany('INSERT INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', pokemon_data)

# Commit and close connection
conn.commit()
conn.close()

print("Data successfully scraped and stored in 'pokemon.db'")

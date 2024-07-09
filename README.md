# Pokémon Scraper

This project is a Python script that scrapes Pokémon data from the [Pokémon Database](https://pokemondb.net/pokedex/all) and stores the results in an SQLite database.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Pokémon Scraper fetches data such as Pokémon number, name, type, and stats (total, HP, attack, defense, special attack, special defense, speed) from the Pokémon Database and stores it in an SQLite database for easy querying and analysis.

## Features

- Scrapes Pokémon data from the Pokémon Database.
- Stores data in an SQLite database.
- Easy setup and usage.

## Requirements

- Python 3.6+
- `requests` library
- `beautifulsoup4` library
- `sqlite3` library (comes with Python)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/uxprogrammr/pokemon_scraper.git
    cd pokemon_scraper
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

3. **Install the required libraries**:
    ```sh
    pip install requests beautifulsoup4
    ```

## Usage

1. **Run the script**:
    ```sh
    python pokemon_scraper.py
    ```

    This will scrape the Pokémon data and store it in `pokemon.db`.

2. **Query the SQLite database**:
    You can use any SQLite client or tool to query the `pokemon.db` file. For example, using the SQLite command-line tool:
    ```sh
    sqlite3 pokemon.db
    ```

    Then you can run SQL queries like:
    ```sql
    SELECT * FROM pokemon;
    ```

## Database Schema

The SQLite database contains a table named `pokemon` with the following schema:

- `number` (TEXT): Pokémon number
- `name` (TEXT): Pokémon name
- `type` (TEXT): Pokémon type(s)
- `total` (TEXT): Total stats
- `hp` (TEXT): HP stat
- `attack` (TEXT): Attack stat
- `defense` (TEXT): Defense stat
- `sp_atk` (TEXT): Special attack stat
- `sp_def` (TEXT): Special defense stat
- `speed` (TEXT): Speed stat

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

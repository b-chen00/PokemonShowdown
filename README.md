# Project CovidStats

## Summary/Description
This is my version of the popular online game Pokemon Showdown. In Pokemon Showdown, a player is given a random Pokemon team and is faced off against another player to simulate a battle. This project will continue the battle simulator genre and have the player face off against a computer instead of another player. The player has to build a team with different ways to customize their Pokemons through their EVs, abilities, happiness, and movesets. Once a team has been built, the goal of the game is to get as high of a score as possible. One point is added to the score once an enemy team of six is defeated. New enemies are generated once the previous enemy team is defeated in an endless battle until the player has no more Pokemons left and the score is saved.

## APIs:
[PokeAPI](https://pokeapi.co/api/v2/pokemon/1/) [[Documentation](https://pokeapi.co/docs/v2.html/)]
- This is the API used to retrieve information about all the pokemons up to generation 5. (battle statistics, images, etc)

## How to Run the Project:  
### Requirements:
Python3 and pip is required to run the project  
[Download Python3 here](https://www.python.org/downloads/) (pip3 comes with python3 download)

### Creating and activating a virtual environment:
`$ python3 -m venv <name>`  
`$ ./<name>/bin/activate`

### Clone the project and install requirments.txt:
`$ git clone https://github.com/b-chen00/PokemonShowdown.git`  
After activating the virutal environment:  
`(venv)$ cd PokemonShowdown`    
`(venv)$ pip3 install -r doc/requirements.txt`  

### Run the project:
`$ python3 app.py`  

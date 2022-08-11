# Project CovidStats

## Summary/Description
This is my version of the popular online game Pokemon Showdown. In Pokemon Showdown, a player is given a random Pokemon team and is faced off against another player to simulate a battle. This project will continue the battle simulator genre and have the player face off against a computer instead of another player. The player has to build a team with different ways to customize their Pokemons through their EVs, abilities, happiness, and movesets. Once a team has been built, the goal of the game is to get as high of a score as possible. One point is added to the score once an enemy team of six is defeated. New enemies are generated once the previous enemy team is defeated in an endless battle until the player has no more Pokemons left and the score is saved.

## APIs:
[PokeAPI](https://pokeapi.co/api/v2/pokemon/1/) [[Documentation](https://pokeapi.co/docs/v2.html/)]
- This is the API used to retrieve information about all the pokemons up to generation 5. (battle statistics, images, etc)

## How to Run the Project:  

### Requirements:
Python3 and pip is required to run the project.  
[Download Python3 here.](https://www.python.org/downloads/) (pip3 comes with python3 download)  
All required packages for the virutal environment can be found in doc/requirements.txt.

### Run the project:
1. Create a virtual environment with `python3 -m venv <virtual-environment-name>`.
2. Use `<virtual-environment-name>/Scripts/activate` to activate your virtual environment.<br>Use `source <virtual-environment-name>/Scripts/activate` if you are using Git Bash.
4. Clone this project and `cd` into the cloned repository.
5. Use `pip3 install -r doc/requirements.txt` to install all necessary packages.
6. Use `python3 app.py` to run the project on your local host.
7. Go to the url listed as the local host.  

## Website purpose:
This is a version of the popular online game Pokemon showdown. The API we plan on using is PokeAPI. The user will choose a team of 6 Pokemon to face off against an infinite number of bots until the user loses. We will implement a turn-based system.

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

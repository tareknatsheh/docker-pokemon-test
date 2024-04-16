from math import exp
from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/api/getpokemon")
def get_pokemon(name: str):
    try:
        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
        return data.json()
    except Exception as error:
        print(error)
        return error
        
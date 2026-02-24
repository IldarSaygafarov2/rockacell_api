import requests
from environs import Env

env = Env()
env.read_env()

API_URL = env.str("API_URL")
headers = {"Accept-Language": "uz"}

print(requests.get(f"{API_URL}/categories", headers=headers).json())

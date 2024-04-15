import requests
from ascii_logo import logo

URL = "https://www.random.org/integers/?"
PARAMS = {"num":4,"min":1,"max":6,"col":1,"base":10,"format":"plain","rnd":"new"}

def generate_random_sequence(url,params):
    response = requests.get(url,params)
    integer_list = [int(num) for num in response.text.strip().split()]
    return integer_list

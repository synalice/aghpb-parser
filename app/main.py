import requests
import json

data = requests.get(
    "https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/"
).text
json_data = json.loads(data)

parsed_data = json_data[4]['name']
print(parsed_data)

# Folders in repo are sorted alphabetically.
# Theoretically, I should be able to make a search for the user input as O(log n)
# and not O(n).

# TODO: Implement cashing of indexes in that json.

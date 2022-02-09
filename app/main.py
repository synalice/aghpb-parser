import requests
import json


def send_request(api_link):
    data = requests.get(api_link).text
    json_data = json.loads(data)
    return json_data


def compare_input_to_json(user_input, json_data):
    for i in json_data:
        if i['name'] == user_input:
            return i['name']
    return "No results found"

if __name__ == '__main__':
    request_data = send_request(
        "https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/"
    )
    print(compare_input_to_json('Python', request_data))


# Folders in repo are sorted alphabetically.
# Theoretically, I should be able to make a search for the user input as O(log n)
# instead of O(n).
# Not that it's nesessary...

# TODO: Make search faster.
# TODO: Implement cashing of indexes in that json.

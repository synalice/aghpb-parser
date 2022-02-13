from typing import Optional
import requests


def parse_json(pr_language: str) -> Optional[list]:
    api_link = f"https://api.github.com/repos/cat-milk/Anime-Girls-Holding-Programming-Books/contents/{pr_language}"
    json_data = requests.get(api_link).json()
    result = []
    if "message" in json_data:
        return None
    for i in json_data:
        result.append({"img_link": i.get("download_url")})
    return result


# Folders in repo are sorted alphabetically.
# Theoretically, I should be able to make a search for the user input as O(log n)
# instead of O(n).
# Not that it's necessary...

# TODO: Make search faster.

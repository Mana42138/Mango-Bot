import requests

json = {
    "1114359434806833192": {
        "1245472088479760405": {
            "Name": "Mango",
            "DisplayName": "Mango",
            "ID": 1245472088479760405
        },
        "701833199780626474": {
            "Name": "mana_dw",
            "DisplayName": "Mana",
            "ID": 701833199780626474
        }
    }
}

response = requests.post("https://ba249bb1-1eb3-476e-abcd-271b5a8ca4ca-00-1sdl3vs4jxlr5.spock.replit.dev/v1/API/add_users", json=json)

print(response.text)
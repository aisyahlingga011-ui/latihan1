# %% Dictionary mutability
profile = {
    "id": 2,
    "name": "mario",
    "hobbies": ("playing with luigi", "saving the mushroom kingdom"),
    "is_female": False,
    "affiliations": [
        {
            "name": "luigi",
            "affiliation": "brother"
        },
        {
            "name": "mushroom kingdom",
            "affiliation": "protector"
        },
    ]
}

print(profile["affiliations"][0]["name"])

profile["affiliations"][0]["name"] = "luigi steven"

print(profile["affiliations"][0]["name"])
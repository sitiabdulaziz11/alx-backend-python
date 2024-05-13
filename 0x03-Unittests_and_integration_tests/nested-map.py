from utils import access_nested_map

house = {
    "living_room": {
        "sofa": "comfy",
        "tv": "big",
    },
    "kitchen": {
        "fridge": "cold",
        "oven": "hot",
    }
}

tv_status = access_nested_map(house, ("living_room", "tv"))
print(tv_status)  # Output: "big"

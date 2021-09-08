from typing import Dict, List, Tuple

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {"argentina": 1, "mexico": 34, "colombia": 45}

countries: List[Dict[str, str]] = [
    {
        "name": "Argentina",
        "people": "450000",
    },
    {"name": "Mexico", "people": "9000000"},
    {"name": "Colombia", "people": "9999999999"},
]

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {"coor1": (1, 2), "coor2": (3, 4)},
    {"coor1": (0, 1), "coor2": (6, 9)},
]

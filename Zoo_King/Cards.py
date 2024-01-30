from enum import IntEnum


class Type(IntEnum):
    Dangerous: 0
    Felines: 1
    Endangered: 2
    Bird: 3
    Show: 4
    Reptiles: 5
    Zoovenir: 6


class Habitats(IntEnum):
    Savanna: 0
    Jungle: 1
    Mountain: 2
    Water: 3
    Dessert: 4
    Polar: 5
    Outback: 6


cards = [
    {
        "ID": 0,
        "Name": "African Wild Dog",
        "Amount": 1,
        "Cost": [300, 300],
        "Stars": 4,
        "Type": [True, False, True, False, False, False, False],
        "Habitat": [True, False, False, False, False, False, False],
        "Expansion": False
    },
    {
        "ID": 1,
        "Name": "Alligator",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 2,
        "Name": "Anaconda",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 3,
        "Name": "Bald Eagle",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 4,
        "Name": "Black Panther",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 5,
        "Name": "Capybara",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 6,
        "Name": "Cheetah",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 7,
        "Name": "Chimpanzee",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 8,
        "Name": "Elephant",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 9,
        "Name": "Flamingo",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 10,
        "Name": "Gemsbok",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 11,
        "Name": "Giraffe",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 12,
        "Name": "Gorilla",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 13,
        "Name": "Great Horned Owl",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 14,
        "Name": "Grizzled Bear",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 15,
        "Name": "Hippopotamus",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 16,
        "Name": "Komodo Dragon",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 17,
        "Name": "Lemur",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 18,
        "Name": "Leopard",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 19,
        "Name": "Lion",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 20,
        "Name": "Mountain Lion",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 21,
        "Name": "Okapi",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 22,
        "Name": "Ostrich",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 23,
        "Name": "Panda",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 24,
        "Name": "Penguin",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 25,
        "Name": "Platypus",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 26,
        "Name": "Polar Bear",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 27,
        "Name": "Red Panda",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 28,
        "Name": "Rhinoceros",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 29,
        "Name": "River Otter",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 30,
        "Name": "Scarlet Macaw",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 31,
        "Name": "Sea Lion",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 32,
        "Name": "Secretary Bird",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 33,
        "Name": "Snow Leopard",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 34,
        "Name": "Spider Monkey",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 35,
        "Name": "Tapir",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 36,
        "Name": "Tiger",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 37,
        "Name": "Tortoise",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 38,
        "Name": "Toucan",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 39,
        "Name": "Warthog",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 40,
        "Name": "Wolf",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    },
{
        "ID": 41,
        "Name": "Zebra",
        "Amount": 0,
        "Cost": [0, 0],
        "Stars": 0,
        "Type": [False, False, False, False, False, False, False],
        "Habitat": [False, False, False, False, False, False, False],
        "Expansion": False
    }
]

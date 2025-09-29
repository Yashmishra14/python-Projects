import random

subjects=[

    "The Governments",
    "The Media",
    "The Scientists",
    "The pm-modi",
    "The Actors"
]
actions=[
    "are hiding the truth about",
    "are spreading false ",
    "are manipulating the public",
    "are involved in a conspiracy about",
    "are trying to control the narrative"
]

places_or_actions=[
    " Covid-19",
    " climate change",
    " the economy",
    " result",
    " the music",
    " the body image issues ",

]
while True:
    subject= random.choice(subjects)
    action= random.choice(actions)
    places= random.choice(places_or_actions)

    headline= f"BREAKING NEWS:{subject}{action}{places}"
    print("\n"+headline) 

    user_input= input("\nDo you want to generate another headline?(yes/no):").strip().lower()
    if user_input !="yes":
        print("\n Thank for using fake generator")
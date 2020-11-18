"""
Advanture into the JACK land!

You might have heard of the story Jack and the magic beans. Jack accidentally
get a hold of the bean yesterday and planted them in his back garden.

He watered them day after day not knowing its magical property.

As time passes the tiny beans grow into a giant bean sprout.

Now the adventure in the giant land await him.

For Jack to win and survive, we MUST to help Jack retrieves as much treasures
and items to fight against the giants.

Hope you enjoy the game!

Authors: Natnaree Chongsiriwattana, Ziying Wu, Chollada Panbutr,
 Pradchayaporn Nonthavanich

License: AGPLv3 or later

Usage:
  main.py

"""


from utils import say
from stage1 import stage1
import json


def main():
    """Start the game."""
    player = {}
    player["hp"] = 3
    player["items"] = {}
    questions = loadquestion()
    stage1_result = stage1(player, questions)
    if not stage1_result:
        return
    question_left = 5
    say("Congrats! You have passed 10 levels")
    say("You have to answer 5 questions to kill the giant!")
    weapons = []
    for k, v in player["items"].items():
        if k != "healing" and k not in weapons and v > 0:
            weapons.append(k)
        if len(weapons) == 4:
            say("Since you have all weapons.",
                "You have to answer only two questions to kill the giant!")
            question_left = 2
    special_question = loadspecialquestion()
    stage2_result = stage2(player, special_question, question_left)
    if not stage2_result:
        say("You can't kill the giant!!! Good Bye O.O")
        return
    say("Congratulations!!!!! You won the game :D")

def loadquestion():
    questions = None
    with open("question.json", "r") as question:
        questions = json.load(question)
    return questions


if __name__ == "__main__":
    main()

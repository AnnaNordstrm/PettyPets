from random import randint
def joker():

    build_up = ["whats up",
                "whats the difference between a fish and a piano?",
                "My friend Tony asked me not to say his name backwards...",
                "Life hack for cutting onions without crying:"]
    punchline = ["chicken butt",
                 "You can tune a piano but you cant piano a tuna",
                 "I asked Y not..",
                 "The trick is to not form an emotional bond with it"]
    ran = len(build_up)
    temp = randint(0, ran)
    joke = {"buildup": build_up[temp],
            "punchline": punchline[temp]
            }
    return joke
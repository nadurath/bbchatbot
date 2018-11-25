branches = ["albums","members","songs","band"]

topics = ["Beach Boys","Brian Wilson","Pet Sounds","Mike Love","Good Vibrations","God Only Knows","Al Jardine","Smiley Smile","Bruce Johnston","Carl Wilson"]

modifiers = ["statement","greeting","bot comment","answer","favorite","affirmative","negative"]

farewell = ["bye","goodbye","good-bye","farewell", "see ya", "adios"]

negative = ["no","nope","nuh-uh","never","nah","don't","not","negative"]

affirmative = ["yes","yeah","yep","sure","affirmative"]

# This function uses the current state of the memory, and the text input by the human, to adjust memory so the responseGenerator can better respond to the human

def extractName(text):
    text = text.lower()
    name = ""

    not_names = ["hi","hello","my","name","is"]
    for x in text.split():
        for y in not_names:
            if y in x:
                text = text.replace(y+" ","")
    text = text.split()
    for x in text:
        x = x.capitalize()
        name += x + " "
    name = name[:-1]
    return name

def handleHumanResponse(text, memory):
    text = text.lower()

    # Determines if the user is exiting or not.
    for x in farewell:
        if x in text:
            memory["goodbye"] = True

    # TODO only allow topics to be accessed while on their designated branch

    if memory.get("asking branch") is True:
        # Determines if user response is a request for a branch or not.
        for x in branches:
            lower = x.lower()
            if lower in text:
                memory["branch"] = x
        del(memory["asking branch"])

    elif memory.get("asking topics") is True:
        # Determines if user response is a request for a fact or not.
        for x in topics:
            lower = x.lower()
            if lower in text:
                memory["topic"] = x
                del (memory["asking topics"])
            elif "other" in text or "another" in text or "something else" in text:
                del(memory["asking topics"])
                del(memory["branch"])
                break

    elif memory.get("asking more") is True:
        for x in text.split():
            lower = x.lower()
            if lower in negative:
                if not memory.get("topic"):
                    del(memory["branch"])
                else:
                    del(memory["topic"])
            elif lower in affirmative:
                pass
        del(memory["asking more"])

    return memory
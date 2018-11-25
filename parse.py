import nltk

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
    for x in text.split():
        if "hi" in x:
            text = text.replace("hi ","")
        if "hello" in x:
            text = text.replace("hello ","")
        if "my" in x:
            text = text.replace("my ","")
        if "name" in x:
            text = text.replace("name ","")
        if "is" in x:
            text = text.replace("is ","")
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

''' 
    Convo flow example:
        Greeting - Hello, I'm the Beach Bot! What's your name? -> Name set 
        Branch - Hello {name}! Would you like to know about the Beach Boys' members, albums, or songs?) -> State set (xyz)
        State (albums, members, songs) - We can tell you about x1/x2/x3, who/what/which would you like to know more about? -> Pull from facts set
        State fulfilled - *facts about xi*
        Branch - Would you like to know more about x, some of the (y), or the (z)? -> State set
        State (albums, members, songs) - I can tell you about y1/y2/y3, who/what/which would you like to know more about? -> Pull from facts set
        State fulfilled - *facts about yi*
        Branch - Would you like to know more about y, some of (x), or the (z)? -> State set (farewell condition)
        Farewell - Goodbye!
'''
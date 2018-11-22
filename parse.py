branches = ["albums","members","songs"]

topics = ["beach boys","brian wilson","pet sounds","mike love","good vibrations","god only knows","al jardine","smiley smile","bruce johnston","carl wilson"]

modifiers = ["statement","greeting","bot comment","answer","favorite","affirmative","negative"]

farewell = ["bye","goodbye","farewell", "see ya", "adios"]

# TODO handle modifier sentiment
def handleHumanResponse(text, memory):
    text = text.lower()

    # Determines if user response is a request for a branch or not.
    for x in branches:
        if x in text:
            memory["branches"] = x

    # Determines if user response is a request for a fact or not.
    for x in topics:
        if x in text:
            memory["topics"] = x

    # Determines if the user is exiting or not.
    for x in farewell:
        if x in text:
            memory["modifiers"] = x

    # If the name key is the only one in the dictionary that holds a value, it is determined that the bot should
    # generate a greeting response.
    if memory["name"] is not "" and memory["branches"] is "" and memory["topics"] is "":
        memory["modifiers"] = "greeting"

    # If the branches key holds a value, it is determined that the bot should generate a fact response.
    if memory["branches"] is not "" and memory["topics"] is "":
        memory["modifiers"] = "topics"

    # If the topics key holds a value, it is determined that the bot should generate a branch response.
    if memory["branches"] is "" and memory["topics"] is not "":
        memory["modifiers"] = "branches"

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
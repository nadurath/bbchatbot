branches = ["albums","members","songs"]

topics = ["beach boys","brian wilson","pet sounds","mike love","good vibrations","god only knows","al jardine","smiley smile","bruce johnston","carl wilson"]

modifiers = ["statement","greeting","bot comment","answer","favorite","affirmative","negative"]

farewell = ["bye","goodbye","farewell", "see ya", "adios"]

# TODO handle modifier sentiment
# This function uses the current state of the memory, and the text input by the human, to adjust memory so the responseGenerator can better respond to the human
def handleHumanResponse(text, memory):
    text = text.lower()

    #TODO use flags such as "asking topic" in memory to better adjust memory so rG can generate the correct responses

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

    # if memory.get("asking more") and memory.get("asking more") is False:

    if "no" in text and memory.get("asking more") is True:
        del(memory["topic"])
        memory["asking more"] = False

    if "brian" in text: # This is for testing, bad code as it'd produce incorrect behavior if someone named brian used the bot
        memory["branch"] = "members"
        memory["topic"] = "brian wilson"

    if "bye" in text:
        memory["goodbye"] = True

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
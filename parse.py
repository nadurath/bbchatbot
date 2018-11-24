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
            memory["goodbye"] = True

    # TODO add a case for detecting if the user said their name

    # TODO this is the primary shape that this class should take, with a lot more of tags that'll be basically written as their counterparts appear in rG
    # TODO fix this block to accept more "no" phrases, and not just any sentence that contains the two consecutive letters
    if "no" in text:
        if memory.get("asking more") is True:
            del(memory["topic"])
            memory["asking more"] = False
        elif True:
            pass

    if "yes" in text:
        # TODO fill this with cases for each instance we ask a yes/no question
        pass



    # TODO remove this, eventually...
    # This is for testing, bad code as it'd produce incorrect behavior if someone named brian used the bot
    if "brian" in text:
        memory["branch"] = "members"
        memory["topic"] = "brian wilson"

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
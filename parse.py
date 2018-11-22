from nltk.corpus import sentiwordnet

subjects = ["albums","members","songs","beach boys","brian wilson","pet sounds","mike love","good vibrations","god only knows","al jardine","smiley smile","bruce johnston","carl wilson"]

modifiers = ["statement","greeting","bot comment","answer","favorite","affirmative","negative"]

# TODO everything
def handleHumanResponse(text, context):

    human_response_subjects = []
    human_response_modifiers = []

    if "expect answer" in context.lower():
        human_response_modifiers.append("answer")

    # Basically we just need a bunch of if statements detecting things

    return human_response_subjects,human_response_modifiers

''' Convo flow example:
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

subjects = ["albums","members","songs"]

modifiers = ["statement","greeting","bot comment","answer","favorite"]

# TODO everything
def handleHumanResponse(text, context):
    human_response_subjects = []
    human_response_modifiers = []

    if "expect answer" in context.lower():
        human_response_modifiers.append("answer")

    # Basically we just need a bunch of if statements detecting things

    return human_response_subjects,human_response_modifiers

''' Convo flow:
        Greeting - Hello, I'm the Beach Bot! 
        Branch - Would you like to know about the Beach Boys' members, albums, or songs?) -> State set
        State (albums, members, songs) - We can tell you about xyz, who/what/which would you like to know more about? -> Pull from facts set
        State fulfilled - *facts about x*
        Branch - Would you like to know more about x, some of the (y), or the (z)? -> State set
        State (albums, members, songs) - 
        
'''
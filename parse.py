
subjects = ["beach boys","Brian Wilson","Pet Sounds","Mike Love","Good Vibrations","God only knows","Al Jardine","smiley smile","bruce johnston","Carl Wilson","albums","members"]

modifiers = ["question","statement","greeting","bot comment","answer","favorite"]

# TODO everything
def handleHumanResponse(text, context):
    human_response_subjects = []
    human_response_modifiers = []

    if "expect answer" in context.lower():
        human_response_modifiers.append("answer")

    # Basically we just need a bunch of if statements detecting things

    return human_response_subjects,human_response_modifiers
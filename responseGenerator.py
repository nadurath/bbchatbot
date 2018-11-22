import factsDictionary

context = ["expect answer"]

subjects = ["beach boys","Brian Wilson","Pet Sounds","Mike Love","Good Vibrations","God only knows","Al Jardine","smiley smile","bruce johnston","Carl Wilson","albums","members","songs"]

modifiers = ["question","statement","greeting","bot comment","answer","favorite"]


def generateMovingOn(subject,modifiers,memory):
    generated = "Anyway, "
    generated += generateQuestion(subject,modifiers,memory)
    return generated

def generateRobotResponse(subject,modifiers,memory):
    generated = "I'm just here to give facts about the Beach Boys. Do you want to know about members, albums, or songs?"
    generated += generateQuestion(subject,modifiers,memory)
    return generated

def generateAnswer(subject,modifiers,memory):
    generated = "My favorite beach boy is Mike Love."
    generated += " " + generateQuestion(subject,modifiers)
    return generated

def generateResponseToStatement(subject,modifiers,memory):
    return "Why do you feel this way about {subject}?"


def generateResponseToAnswer(subject,modifiers,memory):
    return "I see, did you know {uuggggggg}"


def generateQuestion(subject,modifiers,memory):
    return "Would you like to know about members, albums, or songs of the Beach Boys?"


def generateGoodbye(subject,modifiers,memory):
    return "Bye, {name}, thanks for talking!"


def generate_response(subject, modifiers,memory):
    facts = factsDictionary.get_facts()

    answer = "I'm not sure how to respond to that"

    if "bot comment" in modifiers:
        answer = generateRobotResponse(subject, modifiers,memory)
    if "question" in modifiers:
        answer = generateAnswer(subject, modifiers,memory)
    elif "answer" in modifiers:
        answer = generateResponseToAnswer(subject,modifiers,memory)
        context.add("expect response")
    elif "statement" in modifiers:
        answer = generateResponseToStatement(subject,modifiers,memory)

    return answer, context



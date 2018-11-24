import random
import factsDictionary


def generateFact(memory):
    if memory.get("topic"):
        facts = factsDictionary.get_facts()
        if facts.get(memory.get("topic")):
            index = random.randint(0, len(facts[memory["topic"]])-1)
            generated = memory["topic"] + " " + facts[memory["topic"]][index]
    return generated

def generateContinue(memory):
    if memory.get("topic"):
        generated =  "Do you want to hear more about "+memory.get("topic")+"?"
    return generated

def generateGoodbye(memory):
    if memory.get("name"):
        audios = "Bye, "+memory["name"]+", thanks for talking!"
        return audios

def generateHello(memory):
    if memory.get("name"):
        audios = "Hello, "+memory["name"]+", I'm the beach bot, would you like to know about the Beach boy's albums, songs, or members?"
        memory["asking branch"] = True
        return audios

# TODO use the current branch to select from available topic
def generateTopicSelection(memory):
    memory["asking topics"] = True
    if memory.get("branch") is "members":
        return "There have been a total of nine members of the beach boys\n" \
               "I know some facts on Brian Wilson, Mike Love, Al Jardine, Bruce Johnston, and Carl Wilson if you'd like to know about some boys"

# TODO use this to select between branch
def generateBranchSelection(memory):
    pass


def generate_response(memory):


    if memory.get("goodbye"):
        answer = generateGoodbye(memory)

    # If the name key is the only one in the dictionary that holds a value, it is determined that the bot should
    # generate a greeting response.
    elif memory.get("name") and not memory.get("branch") and not memory.get("topic"):
        answer = generateHello(memory)

    # If the topic key does not hold a value, it is determined that the bot should generate a branch response.
    elif not memory.get("branch"):
        answer = generateBranchSelection(memory)
        # memory["modifiers"] = "branch"

    # If the branch key holds a value, it is determined that the bot should generate a fact response.
    elif memory.get("branch") and not memory.get("topic"):
        answer = generateTopicSelection(memory)

    elif memory.get("branch") and memory.get("topic"):
        answer = generateFact(memory)
        answer += "\n"+generateContinue(memory)
        memory["asking more"] = True

    # TODO add at least one elif statement that responds to a UNIQUE combination of variables that basically describes every state in the tree and its possible options

    if not answer:
        answer = "I'm not sure how to respond to that"

    return answer, memory



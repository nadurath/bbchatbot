import random
import factsDictionary


def generateFact(memory):
    if memory.get("topic"):
        key = memory.get("topic")
        low_key = key.lower()
        facts = factsDictionary.get_facts()
        if facts.get(low_key):
            index = random.randint(0, len(facts[low_key])-1)
            generated = key + " " + facts[low_key][index]
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
        message = "Hello, "+memory["name"]+", I'm the beach bot!"
        return message


def generateTopicSelection(memory):
    memory["asking topics"] = True
    response = ""
    if memory.get("branch") is "members":
        response += "There have been a total of nine members of the beach boys\n" \
               "I know some facts on Brian Wilson, Mike Love, Al Jardine, Bruce Johnston, and Carl Wilson if you want to know about them,"
    elif memory.get("branch") is "albums":
        response += "The beach boys have released 29 albums!\n" \
               "That's too many to list, but i could give you facts on Pet Sounds or Smiley Smile if you would like to know about those,"
    elif memory.get("branch") is "songs":
        response +="The beach boys have released dozens and dozens of songs!\n" \
               "That's too many to list, but i could give you facts on Good Vibrations and God only Knows if you want to know about those,"
    response +="\nor we can talk about another topic. So what do you want to know?"
    return response

def generateBranchSelection(memory):
    memory["asking branch"] = True
    message = "would you like to know about the Beach boy's albums, songs, members, or the band itself?"
    return message


def generate_response(memory):


    if memory.get("goodbye"):
        answer = generateGoodbye(memory)

    # If the name key is the only one in the dictionary that holds a value, it is determined that the bot should
    # generate a greeting response.
    elif memory.get("name") and not memory.get("branch") and not memory.get("topic"):
        answer = generateHello(memory)
        answer += "\n"+generateBranchSelection(memory)

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



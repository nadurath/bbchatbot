import random

def generateFact(memory):
    generated = ""
    if memory.get("topic"):
        key = memory.get("topic")
        if key is "band":
            key = "The Beach Boys"
        low_key = key.lower()
        facts = memory.get("facts")
        if facts.get(low_key):
            index = random.randint(0, len(facts[low_key])-1)
            generated = key + " " + facts[low_key][index]
            del(facts[low_key][index])
            generated += "\n"+generateContinue(memory)
        else:
            generated = "Well, that's actually all I know about " + key
            if not memory.get("branch") is "band":
                del (memory["topic"])
                generated += "\nWould you like to know about any other " + memory.get("branch")+"?"
            else:
                del (memory["branch"])
                generated += "\nI know about the Beach boy's albums, songs, and its members. Which would you like to know about?"
    return generated


def generateContinue(memory):
    generated = ""
    if memory.get("topic"):
        generated = "Do you want to hear more about "+memory.get("topic")+"?"
        memory["asking more"] = True
    return generated


def generateGoodbye(memory):
    if memory.get("name"):
        audios = "Bye, "+memory["name"]+", thanks for talking!"
    else:
        audios = "Bye, Beach Boys fan, thanks for talking!"
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
               "That's too many to list, but I could give you facts on Pet Sounds or Smiley Smile if you would like to know about those,"
    elif memory.get("branch") is "songs":
        response +="The beach boys have released HUNDREDS of songs!\n" \
               "That's too many to list, but I could give you facts on Good Vibrations and God only Knows if you want to know about those,"
    response +="\nor we can talk about another topic. So what do you want to do now?"
    return response

def generateBranchSelection(memory):
    memory["asking branch"] = True
    message = "I know about the Beach boy's albums, songs, members, and the band itself. Which would you like to know about?"
    return message


def generate_response(memory):
    answer = ""

    if memory.get("goodbye"):
        answer = generateGoodbye(memory)

    elif memory.get("asking more"):
        answer = "I'm not sure what you mean - was that a yes or a no?"

    elif memory.get("branch") is "band":
        memory["topic"] = "band"
        answer = generateFact(memory)
        if memory.get("topic"):
            del(memory["topic"])
        memory["asking more"] = True

    # If the name key is the only one in the dictionary that holds a value, it is determined that the bot should
    # generate a greeting response.
    elif memory.get("name") and not memory.get("branch") and not memory.get("topic"):
        answer = ""
        if not memory.get("helloed"):
            answer += generateHello(memory)+"\n"
            memory["helloed"] = True
        answer += generateBranchSelection(memory)

    # If the topic key does not hold a value, it is determined that the bot should generate a branch response.
    elif not memory.get("branch"):
        answer = generateBranchSelection(memory)
        # memory["modifiers"] = "branch"

    # If the branch key holds a value, it is determined that the bot should generate a fact response.
    elif memory.get("branch") and not memory.get("topic"):
        answer = generateTopicSelection(memory)

    elif memory.get("branch") and memory.get("topic"):
        answer = generateFact(memory)

    if not answer:
        answer = "I'm not sure how to respond to that"

    return answer, memory



import random
import factsDictionary


def generateFact(memory,facts):
    if memory.get("topic"):
        if facts.get(memory.get("topic")):
            index = random.randint(0, len(facts[memory["topic"]])-1)
            generated = memory["topic"] + " " + facts[memory["topic"]][index]
    return generated

def generateContinue(memory):
    generated =  "Do you want to hear more about "+memory.get("topic")+"?"
    return generated

def generateGoodbye(memory):
    if memory.get("name"):
        audios = "Bye, "+memory["name"]+", thanks for talking!"
        return audios


def generate_response(memory):
    if memory.get("goodbye"):
        answer = generateGoodbye(memory)
    else:
        memory["topic"] = "brian wilson"
        facts = factsDictionary.get_facts()
        answer = generateFact(memory,facts)
        answer += "\n"+generateContinue(memory)

    if not answer:
        answer = "I'm not sure how to respond to that"

    return answer, memory



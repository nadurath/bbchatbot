import random
import factsDictionary


def generateFact(memory,facts):
    generated = "Brian Wilson"
    memory["topic"] = "brian wilson"
    if memory["topic"]:
        if facts[memory["topic"]]:
            index = random.randint(0, len(facts[memory["topic"]]))
            generated += " " + facts[memory["topic"]][index]


    return generated

def generateGoodbye(memory):
    if memory["name"]:
        audios = "Bye, "+memory["name"]+", thanks for talking!"
        return audios


def generate_response(memory):
    facts = factsDictionary.get_facts()

    print(generateFact(memory,facts))
    answer = "I'm not sure how to respond to that"



    return answer, memory



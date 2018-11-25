import parse
import responseGenerator
import factsDictionary



running = True
introduced = False
memory = {}
memory["facts"] = facts = factsDictionary.get_facts()


while running:
    if not introduced:
        name = input("HELLO I AM THE BEACH BOT- WHAT IS YOUR NAME:\n")
        # TODO move this logic into the parse class
        name = parse.extractName(name)
        memory["name"] = name
        user_response = name
        introduced = True
    else:
        user_response = input(bot_response+"\n:")

    # this should set the variables that are interpreted by generateBotResponse
    memory = parse.handleHumanResponse(user_response,memory)

    #This will use the inputs and generate the statement to tell the user
    bot_response,memory = responseGenerator.generate_response(memory)

    if memory.get("goodbye"):
        running = False
        print(bot_response)

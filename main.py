import parse
import responseGenerator

running = True
introduced = False
used_facts = {}
memory = {}

while running:
    if not introduced:
        name = input("HELLO I AM THE BEACH BOT- WHAT IS YOUR NAME:\n")
        memory["name"] = name
        user_response = name
        introduced = True
    else:
        user_response = input(bot_response+"\n:")

    # this should set the variables that are interpreted by generateBotResponse
    # memory,nothing = parse.handleHumanResponse(user_response,"memory")

    #This will use the inputs and generate the statement to tell the user
    bot_response,memory = responseGenerator.generate_response(memory)

    # TODO this needs to check context for goodbye
    if memory.get("running"):
        if memory["running"] is False:
            running = False

    if not running:
        final = "bye "+memory["name"]+"!"
        print(final)

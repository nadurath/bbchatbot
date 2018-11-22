import parse
import responseGenerator

running = True
introduced = False
used_facts = {}
context = ""
memory = []

while running:
    if not introduced:
        user_response = input("HELLO I AM THE BEACH BOT\n:")
        introduced = True
    else:
        user_response = input(bot_response+"\n:")

    # this should set the variables that are interpreted by generateBotResponse
    subject, modifiers = parse.handleHumanResponse(user_response,context)

    #This will use the inputs and generate the statement to tell the user
    bot_response,context = responseGenerator.generate_response(subject,modifiers,memory,context)

    # TODO this needs to check context for goodbye
    if True:
        running = False

    if not running:
        print("bye {user_name}!")

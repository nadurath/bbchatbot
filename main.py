import parse
import responseGenerator

running = True
introduced = False
used_facts = {}
context = ""
memory = []

'''
There should also be a handful of current topics such as nouns, subjs, names
These will be populated and changed by hHR() and used by gBR()

'''

while running:
    if not introduced:
        print("AHHHHHH")
        introduced = True

    #user_response askUser(bot_response)
    user_response = "hello bot"

    # this should set the variables that are interpreted by generateBotResponse
    subject, modifiers = parse.handleHumanResponse(user_response,context)

    #This will use the inputs and generate the statement to tell the user
    bot_response,context = responseGenerator.generate_response(subject,modifiers,memory)

    #promptUser(bot_response)

    if True:
        running = False

    if not running:
        print("bye {user_name}!")

# bbchatbot

## Written by Dawood Nadurath and Sam Britton for NLP 2018

### how to run:

Simply run "python main.py" from a directory that contains all the python files, and contains a directory named "docs" that has the selection of facts in a file named "facts.txt"


    Convo flow example:  
    - Greeting - Hello, I'm the Beach Bot! What's your name? -> Name set 
    - Branch - Hello {name}! Would you like to know about the Beach Boys' members, albums, or songs?) -> State set (xyz)
    - State (albums, members, songs) - We can tell you about x1/x2/x3, who/what/which would you like to know more about? -> Pull from facts set
    - State fulfilled - *facts about xi*
    - Branch - Would you like to know more about x, some of the (y), or the (z)? -> State set
    - State (albums, members, songs) - I can tell you about y1/y2/y3, who/what/which would you like to know more about? -> Pull from facts set
    - State fulfilled - *facts about yi*
    - Branch - Would you like to know more about y, some of (x), or the (z)? -> State set (farewell condition)
    - Farewell - Goodbye!

pip install python-aiml

import aiml

kernel = aiml.Kernel()

kernel.learn("C:\\Users\\91922\\hospital.xml")

kernel.respond("load aiml")

while True:
    input_txt= input(">input")
    response =kernel.respond(input_txt)
    print(">Bot: "+response)
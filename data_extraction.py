questions = {
    'What is your name':'Ifedolapo',
    'How old are you':11
}

for question in questions:
    print(question)
    
    
for answer in questions.values():
    print(answer)
    
for question, answer in questions.items():
    print(question, "=>", answer)
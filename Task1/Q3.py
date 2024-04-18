questions = ["What is the capital of France?\n(a) London\n(b) Paris\n(c) Rome\n",
             "Which planet is known as the Red Planet?\n(a) Mars\n(b) Venus\n(c) Jupiter\n",
             "Is the Earth round?\n(a) True\n(b) False\n"]
correct_answer=['b','a','a']
score=0
answer=input('question[0]')
if answer==correct_answer:
    print('correct')
    score+=1
else:
    print('incorrect')
score=0
answer=input('question[01]')
if answer==correct_answer:
    print('correct')
    score+=1
else:
    print('incorrect')
score=0
answer=input('question[2]')
if answer==correct_answer:
    print('correct')
    score+=1
else:
    print('incorrect')

print('your srouce is:',score'out of',len(questions))
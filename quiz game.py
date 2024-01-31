questions = ["who is the founder of washing machine?",
             "who is the father of nation?",
             "who is the father of computer?"]
answer = ["james king",
          "gandhiji",
          "charles babeji"]
score=0
for i in range(0, len(questions)):
    print(questions[i])
    user_answer  = input("Answer:  ")
    if user_answer == answer[i]:
        print("corret")
        score = score + 1
    else:
        print("incorrect")
print(f"score {score}")


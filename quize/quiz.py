print("Welcome to the Quiz!")


playing = input("Do you want to play the game? (y/n): ")
score = 0

if playing.lower() == "yes" or playing.lower() == "y":
    
    print("Okay!, Let's play the game 😊 ")

    answer = input("What does CPU stand for? ")

    if answer.lower() == "centeral processing unit":
        print("Correct!")
        score +=1

    else: 
        print("Wrong!")
        # print("CPU stands for Centeral Processing Unit")


    answer = input("What does RAM stand for? ")

    if answer.lower() == "random access memory":
        print("Correct!")
        score +=1

    else: 
        print("Wrong!")
        # print("CPU stands for Radom Access Memory")

    answer = input("What does GPU stand for? ")

    if answer.lower() == "graphic processing unit":
        print("Correct!")
        score +=1

    else: 
        print("Wrong!")
        # print("CPU stands for Graphic Processing Unit")


    print(f"You got {score} questions correct")
    print(f"You got {(score/3) * 100 } % .")

else: 
    print("Okay, Goodbye!")    
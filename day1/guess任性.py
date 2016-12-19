#Author:Ivor

age_of_oldboy = 32

count = 0
while count < 3:
    guess_age = int(input("age:"))
    if guess_age == age_of_oldboy:
        print("You have got it!")
        break
    elif guess_age > age_of_oldboy:
        print ("guess smaller!")
    elif guess_age < age_of_oldboy:
        print("guess bigger!")
    count += 1
    if count == 3:
        continue_confir = input("Do you want to keep guessing...(Y/n)?")
        if continue_confir != "n":
            count = 0
#else:
#    print("you have tried too many times.. fuck off!")

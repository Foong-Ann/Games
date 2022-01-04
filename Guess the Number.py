import random

rand_num= random.randint(1,100)
guesses=[]
print("Guess a number between 1 and 100! Use as little guesses as you can to get it right ;) \nOn your first try, 'COLD' means the difference between the correct answer and your guess is greater than 10, and 'WARM' means that the difference is less than 10. \nIn your subsequent tries, 'warmer' means you're closer to getting it right compared to your last answer (vice versa for 'colder')!\n")

while True:

    guess= input("What's your guess?? ")
    
    try:
      guess=int(guess)
      guesses.append(guess)
      num_guesses= len(guesses)
    except:
      print("I'm gonna need an integer!!")
      break

    if guess== rand_num:
      print(f"You're a winner!! ;) It took you {num_guesses} tries")
      break

    elif guess <1 or guess >100: 
      print("OUT OF BOUNDS: ONLY BETWEEN 1 AND 100 PLS")
    
    if num_guesses==1:
      if abs(rand_num-guesses[0])<=10:
        print("WARM!")
      else:
        print("COLD!") 
    
    else: 
      if abs(rand_num-guess)< abs(rand_num-guesses[-2]):
        print('WARMER! :) ')
      elif abs(rand_num-guess)> abs(rand_num-guesses[-2]):
        print('COLDER! :/')

    pass

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
print(f'{rock}\nrock')
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
print(f'{paper}\npaper')
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(f'{scissors}\nscissors')
game = [rock, paper, scissors]
print("What fo you choose? Type 0 for Rock, 1 for Paper of 2 for Scissors.")
person = int(input())
print(person)
print(game[person])

computer = random.randint(0, 2)
print(computer)
print(game[computer])

if person == computer:
    print("It's draw.")
elif person >= 3 and person < 0:
    print("You typed an invalid number, you lose!")
elif person == 0 and computer == 2:
    print("You win!")
elif computer == 0 and person == 2:
    print("You lose!")
elif computer > person:
    print("You lose!")
elif person > computer:
    print("You win!")




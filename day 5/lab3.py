# Write a Python program to guess a number between 1 to 9.Note :User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct,
# On successful guess, user will get a "Well guessed!" message, and the program will exit.
import random
target_num,guess_num=random.randint(1,10),0
while target_num !=guess_num:
    guess_num=int(input("guess any num:"))
    print("congratulation")
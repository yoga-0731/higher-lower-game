import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo + "\n\n")
A_ACCOUNT = {}

score = 0
end_game = False

def get_data(count):
  if count == 1:
    instagram_data = []
    instagram_data.append(A_ACCOUNT)
    account_b = random.choice(data)
    if A_ACCOUNT == account_b:
      account_b = random.choice(data)
    instagram_data.append(account_b)
  else:
    instagram_data = random.choices(data, k = count)
  return instagram_data

def find_max_follower_account(instagram_data):
  max_followers = 0
  for i in range(2):
    follower_count = instagram_data[i]['follower_count']
    if follower_count > max_followers:
      max_followers = follower_count
      type = 'A' if i == 0 else 'B'
      correct_guess = type
  return correct_guess

while not end_game:
  count = 2 if score == 0 else 1
  instagram_data = get_data(count)

  correct_guess = find_max_follower_account(instagram_data)

  ascii_value_of_A = 65
  for i in range(2):
    print(f"Compare {chr(ascii_value_of_A + i)}: {instagram_data[i]['name']}, a {instagram_data[i]['description']}, from {instagram_data[i]['country']}\n")
    if i == 0:
      print(vs)

  guess = input("Who has more followers: Type 'A' or 'B': ")
  clear()
  print(logo + "\n\n")

  if guess != correct_guess:
    end_game = True
    print(f"Sorry, that's wrong. Final score is {score}")
  else:
    score += 1
    A_ACCOUNT = instagram_data[1]
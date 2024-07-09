import random
import string

def generate_password(length, complexity):

  characters = string.ascii_letters
  if complexity == "medium":
    characters += string.digits
  elif complexity == "high":
    characters += string.digits + string.punctuation

  else:
    print("Invalid complexity. Please choose 'low', 'medium', or 'high'.")
    return None

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      print("Password length must be at least 8 characters.")
      continue
    complexity = input("Choose complexity (low, medium, high): ").lower()
    break
  except ValueError:
    print("Invalid input. Please enter a number for length.")

password = generate_password(length, complexity)

if password:
  print("Your generated password is:", password)

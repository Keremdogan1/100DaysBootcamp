# age = input("How old are you?")
# if age.isdigit():
#      age = int(age)
#      if age >= 18 :
#          print(f"You can drive at age {age}.")
# else:
#     print("Enter a valid input! ")

try:
    age = int(input("How old are you? : "))
except ValueError:
    print("You have typed a invalid input. Please try again with a numerical response.")

if age >= 18:
    print(f"You can drive at age {age}.")
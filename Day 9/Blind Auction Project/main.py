from art import logo
import os
print(logo)

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

secret_auction_list = []
max = 0
max_index = 0
index = 0

will_program_run = True

while(will_program_run):
    buyer = {
        "name": "",
        "bid": 0
    }

    buyer["name"] = input("What is your name? : ")
    buyer["bid"] = int(input("What is your bid? : $"))


    if(buyer["bid"] > max):
        max = buyer["bid"]
        max_index = index
    secret_auction_list.append(buyer)

    check = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if check == "yes":
        will_program_run = True
        index += 1
        print("\n" *100)
    else:
        will_program_run = False

print(f"The winner is {secret_auction_list[index]["name"]} with a bid of ${secret_auction_list[index]["bid"]}!")
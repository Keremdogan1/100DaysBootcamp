programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

secret_auction_list = []
max = 0
max_index = 0
index = 0

will_program_run = True

while(will_program_run):
    buyer = []

    name = input("What is your name? : ")
    buyer.append(name)
    bid = int(input("What is your bid? : $"))
    buyer.append(bid)

    if(buyer[1] > max):
        max = buyer[1]
        max_index = index
    secret_auction_list.append(buyer)

    check = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if check == "yes":
        will_program_run = True
        index += 1
    else:
        will_program_run = False

print(f"The winner is {secret_auction_list[index][0]} with a bid of ${secret_auction_list[index][1]}!")
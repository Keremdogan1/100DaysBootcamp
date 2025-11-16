print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? :"))

if height >= 120:
    print("You can ride the rollercoaster")
    ticket_price = 0
    age = int(input("What is your age? :"))
    if age <= 12:
        ticket_price+= 5
        print("Child tickets are $5.")
    elif age <= 18:
        ticket_price+= 7
        print("Youth tickets are $7.")
    else:
        print("Adult tickets are $12.")
        ticket_price+= 12

    photo = input("Do you want to have a photo take? Type 'y' for yes and 'n' for No. :")
    if(photo == 'y'):
        ticket_price+= 3

    print(f"Please pay ${ticket_price}.")

else:
    print("Sorry you have to grow taller before you can ride.")

print("***Leap year calculator***\n")

year = int(input("What year do you wanna know about?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"\nThe year {year} its a leap year")
        else:
            print(f"\nThe year {year} its not a leap year")
    else:
        print(f"\nThe year {year} its a leap year")
else:
    print(f"\nThe year {year} its not a leap year")

print(input("\nClick ENTER to close"))
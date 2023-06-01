print()

print("Do you want to use calculator ? ")
ui= int(input('''
    1. YES
    2. NO
'''))

if ui==1:

    print("Select Any Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    u_choice = int(input("Select One Operation : "))

    if u_choice == 1:
        v1=int(input("Enter Value 1 : "))
        v2=int(input("Enter Value 2 : "))
        result = v1+v2
        print(result)

    elif u_choice == 2:
        v1=int(input("Enter Value 1 : "))
        v2=int(input("Enter Value 2 : "))
        result = v1-v2
        print(result)

    elif u_choice == 3:
        v1=int(input("Enter Value 1 : "))
        v2=int(input("Enter Value 2 : "))
        result = v1*v2
        print(result)

    elif u_choice == 4:
        v1=int(input("Enter Value 1 : "))
        v2=int(input("Enter Value 2 : "))
        result = v1/v2
        print(result)

    elif u_choice == 5:
        exit()

else:
    exit()
class Menu:
    items1 = {"Veg Biryani":350,"Chicken Biryani":600,"Mutton Biryani":850,"Paneer Biryani":550}
while True:
    print("Enter\n 1 to add\n 2 to modify\n 3 to delete\n 4 to display")
    n = int(input())
    obj=Menu()
    if(n==1 or n==2):
        print("Enter item and its price")
        item=input()
        price=int(input())
        obj.items1[item]=price
    elif(n==3):
        print("Enter delete item")
        obj.items1.pop(item)
    elif(n==4):
        print("The items are\n")
        print("ITEMS\t\t\tPRICE\n\n")
        for i in obj.items1:
            print(i+"      "+str(obj.items1[i]))
    else:
        print("Enter valid no.")
    print("Press\n y to continue\n n to stop")
    p=input()
    if(p=="n"):
        break
    elif(p=="y"):
        a=8
    else:
        print("Enter valid no.")

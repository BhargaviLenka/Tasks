names = []
phone_numbers = []
n=0
while(1<2):
    print("Enter \n1 to add a new contact \n" 
          "2 to search for a contact \n"
          "3 to view all contacts\n""4 to delete")
    num=int(input())
    if(num==1):
        n+=1
        no=int(input("enter no. of contacts to be added"))
        for i in range(no):
            name = input("Name: ")
            phone_number = input("Phone Number: ") # for convert to int => int(input("Phone Number: "))

            names.append(name)
            phone_numbers.append(phone_number)

    if(num==3):
        print("\nName\t\t\tPhone Number\n")

        for i in range(len(names)):
            print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
    if(num==2 or num==4):
    
        search_term = input("\nEnter search term: ")

        print("Search result:")

        if search_term in names:
            index = names.index(search_term)
            phone_number = phone_numbers[index]
            print("Name: {}, Phone Number: {}".format(search_term, phone_number))

        else:
            print("Name Not Found")
        if(num==4):
            p=names.index(search_term)
            names.pop(p)
            phone_numbers.pop(p)
            n-=1
            print("deleted successfully")
    print("Enter anything to continue\n" "Enter s to stop")
    c=input()
    if(c=="s"):
        break

import time
t=time.ctime()
txt="Health management system for gym"
print("\033[1;036m",txt.center(70))
print("\nPress 1 for write and press 2 for retrive:")
input1=int(input())
if input1==1:
    print("Press 1 for Arvind Press 2 for Prince and Press 3 for Rahal:")
    input2=int(input())
    if input2==1:
        print("\033[1;032m\nPress 1 for Exercise Press 2 for food:")
        input3=int(input())
        if input3==1:
            f1=open("ArvindE.txt","a")
            f1.write("\nThis is Exercise Time: ")
            f1.write(str(t))
            f1.write("\n")
            f1.write(input("Enter About Exercise of Arvind:"))
            f1.close()
        elif(input3==2):
            f2=open("ArvindF.txt","a")
            f2.write(input("Enter Here:"))
            f2.close()
        else:
            print("Invalid Input.")
    elif input2==2:
        print("Press 1 for Exercise and 2 for Food:")
        input3=int(input())
        if input3==1:
            f1=open("PrinceE.txt","a")
            f1.write("This is Exercise Time: ")
            f1.write(str(t))
            f1.write("\n")
            f1.write(input("Enter About Exercise of Prince:"))
            f1.write("\n")
            f1.close()
        elif(input3==2):
            f2=open("PrinceF.txt","w")  
            f2.write(input("Enter Here:"))
            f2.close()
        else:
            print("Invalid Input.")
    elif input2==3:
        print("Press 1 for Exercise and 2 for Food:")
        input3=int(input())
        if input3==1:
            f1=open("RahulE.txt","a")
            f1.write("This is Exercise Time: ")
            f1.write(str(t))
            f1.write("\n")
            f1.write(input("Enter About Exercise of Rahul:"))
            f1.write("\n")
            f1.close()
        elif(input3==2):
            f2=open("RahulF.txt","w")  
            f2.write(input("Enter Here:"))
            f2.close()
        else:
            print("Invalid Input.")
elif input1==2:
    print("Press 1 for Arvind Press 2 for Prince and 3 for Rahul:")
    input2=int(input())
    if input2==1:
        input3=int(input("Press 1 for Exercise and 2 for FOOD:"))
        if input3==1:
            f1=open("ArvindE.txt","r")
            print(f1.read())
            f1.close()
        elif input3==2:
            f1=open("ArvindF.txt","r")
            print(f1.read())
            f1.close()
        else:
            print("Invalid Input.")
    if input2==2:
        input3=int(input("Press 1 for Exercise and 2 for FOOD:"))
        if input3==1:
            f1=open("PrinceE.txt","r")
            print(f1.read())
            f1.close()
        elif input3==2:
            f1=open("PrinceF.txt","r")
            print(f1.read())
            f1.close()
        else:
            print("Invalid Input.")
    if input2==3:
        input3=int(input("Press 1 for Exercise and 2 for FOOD:"))
        if input3==1:
            f1=open("RahulE.txt","r")
            print(f1.read())
            f1.close()
        elif input3==2:
            f1=open("RahulF.txt","r")
            print(f1.read())
            f1.close()
        else:
            print("Invalid Input.")
    else:
        print("Invalid Input.")
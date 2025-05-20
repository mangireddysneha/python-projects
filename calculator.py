def additon():
    num1=int(input("enter the 1st number:"))
    num2=int(input("enter the 2nd number:"))
    print("The additon of num1 and num2 numebrs is :",num1+num2)

def subtraction():
    num1=int(input("enter the 1st number:"))
    num2=int(input("enter the 2nd number:"))
    print("The subtraction of num1 and num2 numebrs is :",num1-num2)


def multiplation():
    num1=int(input("enter the 1st number:"))
    num2=int(input("enter the 2nd number:"))
    print("The multiplation of num1 and num2 numebrs is :",num1*num2)


def division():
   num1=int(input("enter the 1st number:"))
   num2=int(input("enter the 2nd number:"))
   print("The division of num1 and num2 numebrs is :",num1/num2)


def modulo():
   num1=int(input("enter the 1st number:"))
   num2=int(input("enter the 2nd number:"))
   print("The modulo of num1 and num2 numebrs is :", num1%num2)


while True:
    x=int(input('''
Addition=1
Subtraction=2
Multiplation=3
Division=4
Modulo=5
quit=6
enter the number here:'''))
    if x==1:
        additon()
    if x==2:
        subtraction()
    if x==3:
        multiplation()
    if x==4:
        division()
    if x==5:
        modulo()
    if x==6:
        print("quitting the process..")
        break
    else:
        print("enter valid number..!")


            
 
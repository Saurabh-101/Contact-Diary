contact={"Saurabh":7705870678, "Anshu":8409675604, "Aditya":7899623412, "Karan":7845128956, "Ankesh":9304580938, "Rocky":6205254781, "Rohit":9865327814}
numberlist=[]

for i in contact:
    numberlist.append(contact[i])

def main():
    
    Y=input("\nCommand Key: ").upper() 
   
    if Y=="Y" :
        addingcontact()
    elif Y=="U":
        update()
    elif Y=="F":
        search()
    elif Y=="V":
        showing()
    elif Y=="V":
        commandkey()
        main()
    elif Y=="X":
        main()
    elif Y=="D":
        delete()
    elif Y=="EXIT":
        exit()
    else:
        
        print("\n! Invalid Input !")
       
        print("\nEnter command key again.")
        
        main()
    

    
def addingcontact():
    data1=input("Name: ")
    data2=int(input("Contact no: "))
    if len(str(data2))!=10:
        
                def reenter():
            
                    print("Invalid number (not 10 digit), re-entrer the number.")
                    data6=input("Re-enter the number: ")
                    data2=int(data6)
                    if len(str(data6))!=10:
                        reenter()
                    elif data6.upper()=="x":
                        main()
                reenter()
    if data1 not in contact:
        contact[data1]=data2
        
    elif data1 in contact:
        
        print("\nThis name already exist.")
        
        print("\nTo update the existing contact, Key:'U'")
        
        print("\nTo change name entered, Key:'N'")
        
        condition=input("Key: ").upper()
        if condition=="U":
            
            contact[data1]=data2
        elif condition=="N":
            data3=input("Name: ")
            if len(str(data2))!=10:
        
                def reenter():
            
                    print("Invalid number (not 10 digit), re-entrer the number.")
                    data6=input("Re-enter the number: ")
                    contact[data3]=int(data6)
                    if len(str(data6))!=10:
                        reenter()
                    elif data6.lower()=="x":
                        main()
                reenter()
            else:
                contact[data3]=data2
        elif condition=="X" or condition=="x":
            main()
        
    if data2 in numberlist:
        print()
        print("This contact number already exist.")
        print()
        print("To change number, Key:'N'")
        print()
        print("To update the name of contact number, Key:'C'")
        print()
        number=input("Key: ")
        def samenumber():
            print()
            print("Number already exist in diary.")
            print()
            
            data4=input("Re-enter the number to comfirm: ")

            if data4 in numberlist:
                samenumber()
            elif data4 not in numberlist:
                contact[data1]=data4
        if number=="N" or number=="n":
            
            data4=int(input("New Number: "))
            
 #Still some error , second input is not compared with condition.           
            if data4 in numberlist:
                samenumber()
            else:
                contact[data1]=data4
                
                
            
            

        elif number=="C" or number=="c":
            data5=input("New Name: ")
            if data5 not in contact:
                contact[data5]=data2
            else:
                samename()
            def samename():
                data5=input("New Name: ")
                if data5 not in contact:
                    contact[data5]=data2
                else:

                    samename()



        elif number=="X" or number=="x":
            main()
    if len(str(contact[data1]))!=10:
        
        def reenter():
    
            print("Invalid number (not 10 digit), re-entrer the number.")
            data6=input("Re-enter the number: ")
            contact[data1]=int(data6)
            if len(str(data6))!=10:
                reenter()
            elif data6=="X" or data6=="x":
                main()
        reenter()
    main() 


def update():
    name=input("Enter the name of contact to be updated: ")
    if name in contact:
        data1=int(input("Enter the NEW Number: "))
        contact[name]=data1
    elif name not in contact:
        print("Namre given doesn't exist in the Contact Diary.")
        print()
        print("To re-enter the name: Key'R'")
        print()
        R=input("Key: ")
        if R=="R" or R=="r":
            update()
        elif R=="X" or R=="x":
            main()
    if len(str(contact[name]))!=10:
        
        def reenter():
    
            print("Invalid number, re-entrer the number.")
            data6=int(input("Re-enter the number: "))
            contact[name]=data6
            if len(str(data6))!=10:
                reenter()
        reenter()
    main()




def showing():    
    print()
    print("|:Contact Diary:|")
    print()
    for i,value in sorted(contact.items()):
        print(i,":",value) 
    main()



def search():
    
   
    S=input("Search: ")
    print()
    c=0
    for i,value in sorted(contact.items()):
        if S.lower() in i.lower():
            print(i,":",value)
            print()
            c+=1
        
    if c==0:
        print("No match found.")


    main()
    
def delete():
    def delsearch():
            E=input("Enter contact name:")
            if E in tempdict:
                del(contact[E])
                print("Contact deleted successfully.")
            else:
                print("Invalid Input 'Contact given is not in search list.'")
                delsearch()
    data=input("Search: ")
    print()
    c=0
    tempdict={}
    for i,value in sorted(contact.items()):
        if data.lower() in i.lower():
            print(i,":",value)
            print()
            c+=1
            tempdict[i]=value

    if c==1 :
        del(contact[data])
        print()
        print("Contact under name",data,"is deleted from Diary successfully.")

        

    elif c>1:
        print()
        print("TO DELETE")
        print()
        delsearch()
        

                
    else:
        print("No match found.")    
    
    

    main()


def commandkey():
    print("Command Keys are as follows: ")
    print()
    print("To come back to initail phase at any moment:'X'")
    print()
    print("To add new contact: 'Y'")
    print()
    print("To update existing contact: 'U'")
    print()
    print("To Search contact: 'F'")
    print()
    print("To show contact diary: 'V'")
    print()
    print("To see command keys again: 'C'")
    print()
    print("To delete any contact: 'D'")
    print()
    


commandkey()
showing()
main()

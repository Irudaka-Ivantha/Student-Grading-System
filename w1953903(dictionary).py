# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953903
#IIT ID:20211348
# Date:2022/12/13

#Initializing Variables
Total=0
option=0
symbol="-"
credit=0
Pass=0
Display_choice=""
Defer=0
Fail=0
Total_Credit=0
version=0
i=0
k=0
l=0
m=0
credit_list=[]
credit_dic={}
dictionary_list=[]
message=""
print("\n"+"*"*25,"Welcome to the University Student Progression Outcome","*"*25) 
def range_check(statement):
    '''Checks whether the user entered pass,defer,and fail credits are in range and whether they are valid or not. Finally returns the values.'''   #Checks whether the user entered pass,defer,and fail credits are in range and whether they are valid or not. Finally returns the values.
    while True:
        try:
            credit=int(input(f"\nPlease enter your total {statement} credits: ")) #checking the range and the validity
            if credit in range(0,121,20):
                break
            else:
                print("\nOut of range")
                continue
        except ValueError:
            print("\nEnter valid integer")
            continue
    return credit               #returns the credit value for further operations
while True:
    print("\nEnter '1' to continue with the student Version, enter '2' to continue with the Staff version or enter 'q' to quit.\n") #student version or staff version check
    version=input("Enter the number of the version you want to continue with: ")
    if version=="1":
        print("\n...............Welcome to the Student Version...............")
        Pass=range_check("pass")
        Defer=range_check("defer")      #calls the range_check and gets the user inputs
        Fail=range_check("Fail")
        Total_Credit=Pass+Defer+Fail
        if (Total_Credit==120):
            if Pass==120 and Defer==0 and Fail==0:
                print("\nProgress")
            elif Pass==100 and (Defer==20 or Fail==20):          #Giving the proper output according to the user inputs
                print("\nProgress (module trailer)")
            elif Fail in range(0,61,20) and Pass in range(0,81,20) and Defer in range(0,121,20):
                print("\nDo not progress and module Retriever")
            elif Pass in range(0,41,20) and Defer in range(0,41,20) and Fail in range(80,121,20):
                print("\nExclude")
        else:
            print("\nIncorrect total!")                    #Showing an error message when the total of the user inputs are not equal to 120
            continue
    elif version=="2" :
        while True:
            print("\n................Welcome to the Staff Version...............")    #Student or Staff version check
            print("\nWould you like to enter another set of data?")
            option=input("\nEnter 'y' for yes or 'q' to quit and view results: ")
            if option=="y":
                uni_id=input("\nEnter your id: ")                #Asking user to enter the student id
                uni_id.lower()                                
                if len(uni_id)==8 and uni_id[0]=="w":         #Check whether the student id user entered consist of 8 characters starting with w
                    if uni_id not in dictionary_list:     #checking whether the user entered student id is unique(whether they are not in the dictionary_list)
                        dictionary_list.append(uni_id)        #Appending the student ids user entered to the dictionary_list if the ids are unique
                    else:
                        print("\nUniversity id you entered must be unique")    #Giving an error message when the student ids user entered are not unique
                        continue
                else:
                    print("\nUniversity must consist with 8 characters and should start with 'w' or 'W'")     #Giving an error message when the student ids user entered are not in the proper form
                    continue
                Pass=range_check("pass")
                Defer=range_check("defer")             #calls the range_check and gets the user inputs
                Fail=range_check("Fail")
                Total_Credit=Pass+Defer+Fail
                if (Total_Credit==120):
                    if Pass==120 and Defer==0 and Fail==0:
                        message="Progress" 
                        print("\nProgress")                                       #Giving the proper output according to the user inputs
                        i+=1
                    elif Pass==100 and (Defer==20 or Fail==20):
                        message="Progress (module trailer)"                         
                        print("\nProgress (module trailer)")
                        k+=1
                    elif Fail in range(0,61,20) and Pass in range(0,81,20) and Defer in range(0,121,20):
                        message="Do not progress and module Retriever"
                        print("\nDo not progress and module Retriever")
                        m+=1
                    elif Pass in range(0,41,20) and Defer in range(0,41,20) and Fail in range(80,121,20):
                        message="Exclude"
                        print("\nExclude")
                        l+=1
                    credit_dic.update({uni_id:message+"-"+str(Pass)+","+str(Defer)+","+str(Fail)}) #Adding the data to the dictionary. Uni_id is the key and the rest are the value
                    credit_list.append([message,Pass,Defer,Fail])                 #appending data too the list
                    credit_file=open("credit.txt","a")                       #Opening the file in append mode
                    credit_file.write(message+"-"+str([Pass,Defer,Fail])+"\n")    #appending the data to the file
                    credit_file.close()        #closing the opened file
                else:
                    print("\nIncorrect Total!")
                    continue
            elif option=="q":
                print("\n"+"*"*25,"Here's the Menu","*"*25)
                print("\nTo access the Dictionary enter - Dictionary")          #printing a menu so user can choose what to view
                print("\nTo view the Histogram enter - Histogram")
                print("\nTo access the List enter - List")
                print("\nIf you want to view the data in the File enter - File")
                print("\n"+"*"*68)
                Display_choice=input("\nEnter what you want to view or access: ")    #Getting the user's choice
                lowered=Display_choice.lower()
                def Print_message(message):
                    '''Printing a proper message when user accessed the menu item he wants.'''
                    print(f"\nYou have successfully accessed the {message}")
                    print("\n"+symbol*100)
                if lowered=="dictionary":                      #Dictionary
                    Print_message("Dictionary.") #calls the Print_message and printing user accessed the dictionary   
                    for key in credit_dic:
                        print("\n",key,":",*credit_dic[key],sep="")      #Accessing the data in the dictionary and printing the key and the value
                    print("\n"+symbol*100)
                    break
                elif lowered=="histogram":   #Histogram
                    Print_message("Histogram.")           #calls the Print_message and printing user accessed the histogram
                    print("Progress",i," :","*"*i,"\n""Trailer",k,"  :","*"*k,"\n""Retriever",m,":","*"*m,"\n""Exclude",l,"  :","*"*l)
                    Total=i+k+m+l
                    print("\n"+str(Total),"outcomes in total.")
                    print("\n"+symbol*100)
                    break
                elif lowered=="list":        #List
                    Print_message("List.")       #calls the Print_message and printing user accessed the list
                    for item in credit_list:
                        print(item[0],"-",item[1],",",item[2],",",item[3],"\n") #Accessing data in the list(message,Pass,Defer,Fail) in order and printing them
                    print(symbol*100)
                    break
                elif lowered=="file":      #File Handling
                    Print_message("File.")          #calls the Print_message and printing user accessed the file
                    credit_file=open("credit.txt","r")#Opening the file in read mode
                    data=credit_file.read()              #Reading the data in the file and assigning those data to the data variable
                    replace_brackets_data=data.replace('[', '').replace(']', '') #replacing brackets with an emty string
                    print(replace_brackets_data)        
                    print(symbol*100)
                    print("\n"+symbol*100)
                    break
                else:
                    print("\nPlease enter Valid Input!")         #If user enetred an invalid input for option printing an error message
                    continue
            else:
               print("\nInvalid input!")                #If user enetred an invalid input for option printing an error message
    elif version=="q" or version=="Q":
        print("\n........................End of the program.....................")
        break
        
        
    

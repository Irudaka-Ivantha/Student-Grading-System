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
Defer=0
Fail=0
Total_Credit=0
version=0
i=0
k=0
l=0
m=0
credit_list=[]
message=""
print("\n"+"*"*25,"Welcome to the University Student Progression Outcome","*"*25)
print("\nPart1")
def range_check(statement):
    '''Checks whether the user entered pass,defer,and fail credits are in range and whether they are valid or not. Finally returns the values.'''  #Checks whether the user entered pass,defer,and fail credits are in range and whether they are valid or not. Finally returns the values.
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
    return credit              #returns the credit value for further operations
while True:
    print("\nEnter '1' to continue with the student Version, enter '2' to continue with the Staff version or enter 'q' to quit.") #student version or staff version check
    version=input("\nEnter the number of the version you want to continue with: ")
    if version=="1":
        print("\n...............Welcome to the Student Version...............")
        Pass=range_check("pass")
        Defer=range_check("defer")    #calls the range_check and gets the user inputs
        Fail=range_check("Fail")
        Total_Credit=Pass+Defer+Fail
        if (Total_Credit==120):
            if Pass==120 and Defer==0 and Fail==0:
                print("\nProgress")
            elif Pass==100 and (Defer==20 or Fail==20):                                                 #Giving the proper output according to the user inputs
                print("\nProgress (module trailer)")
            elif Fail in range(0,61,20) and Pass in range(0,81,20) and Defer in range(0,121,20):
                print("\nDo not progress and module Retriever")
            elif Pass in range(0,41,20) and Defer in range(0,41,20) and Fail in range(80,121,20):
                print("\nExclude")
        else:
            print("\nIncorrect total!")         #Showing an error message when the total of the user inputs are not equal to 120
            continue
    elif version=="2" :
        while True:
            print("\n................Welcome to the Staff Version...............")        #Student or Staff version check                   
            print("\nWould you like to enter another set of data?")
            option=input("\nEnter 'y' for yes or 'q' to quit and view results: ")
            if option=="y":
                Pass=range_check("pass")
                Defer=range_check("defer")      #calls the range_check and gets the user inputs
                Fail=range_check("Fail")
                Total_Credit=Pass+Defer+Fail
                if (Total_Credit==120):
                    if Pass==120 and Defer==0 and Fail==0:
                        message="Progress"
                        print("\nProgress")
                        i+=1
                    elif Pass==100 and (Defer==20 or Fail==20):                  #Giving the proper output according to the user inputs
                        message="Progress (module trailer)"
                        print("\nProgress module trailer")
                        k+=1
                    elif Fail in range(0,61,20) and Pass in range(0,81,20) and Defer in range(0,121,20):
                        message="Do not progress and module Retriever"
                        print("\nDo not progress and module Retriever")
                        m+=1
                    elif Pass in range(0,41,20) and Defer in range(0,41,20) and Fail in range(80,121,20):
                        message="Exclude"
                        print("\nExclude")
                        l+=1
                    credit_list.append([message,Pass,Defer,Fail])        #appending data too the list
                    credit_file=open("credit.txt","a")                   #Opening the file in append mode
                    credit_file.write(message+"-"+str([Pass,Defer,Fail])+"\n")  #appending the data to the file
                    credit_file.close()                                  #closing the opened file
                else:
                    print("\nIncorrect Total!")
                    continue
            elif option=="q":
                print("\nHistogram")      #Histogram
                print(symbol*100+"\n")
                print("Progress",i," :","*"*i,"\n""Trailer",k,"  :","*"*k,"\n""Retriever",m,":","*"*m,"\n""Exclude",l,"  :","*"*l)
                Total=i+k+m+l
                print("\n"+str(Total),"outcomes in total.")
                print("\n"+symbol*100)
                print("\nPart 2\n")        #List
                for item in credit_list:
                    print(item[0],"-",item[1],",",item[2],",",item[3],"\n")   #Accessing data in the list(message,Pass,Defer,Fail) in order and printing them
                print(symbol*100)
                print("\nPart3\n")         #File handling
                credit_file=open("credit.txt","r")         #Opening the file in read mode
                data=credit_file.read()             #Reading the data in the file and assigning those data to the data variable
                replace_brackets_data=data.replace('[', '').replace(']', '') #replacing brackets with an emty string
                print(replace_brackets_data)        
                print(symbol*100)
                break
            else:
               print("\nInvalid input!")        #If user enetred an invalid input for option printing an error message
    elif version=="q" or version=="Q":
        print("\n........................End of the program.....................")    
        break
        
        
    

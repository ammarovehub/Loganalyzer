#Ammar Jamous  ammmarove1993@gmail.com  ammar.jamous@edu.edugrade.se
#Last version for the project submission, os library/module is imported to check  if the logFile exist or not, Also it uses argv[0] to print the script name inside the \
#Usage variable.


import sys
import os
 
Usage=("Please write the script name followed by the logfile location and the required action. Available actions are  (statistics, error and notice)\n....\
Example:- ", sys.argv[0], "ammar.jamous\Downloads\LogFile-Parser/test.log error")
 

if len(sys.argv) !=3:
    print(Usage)
    sys.exit()

elif os.path.isfile(sys.argv[1]):
  
    with open(sys.argv[1], "r") as file:
        if str(sys.argv[2]) == ("error"):
            for line in file:
                if 'error]' in line:                    
                    print(line[:]) 
 
        elif str(sys.argv[2]) == ("notice") :
            for line in file:
                if 'notice]' in line:                    
                    print(line[:]) 
 
        elif str(sys.argv[2]) == ("statistics") :
            counter_error = 0
            counter_notice = 0
            for line in file:
                if 'error]' in line:
                   counter_error += 1
                if 'notice]' in line:
                   counter_notice += 1
            print("The Logfile contains \n", counter_error , "Errors \n", counter_notice, "Notices")
            

        else:
            print("Check your action. Available actions are  (statistics, error and notice)")
else:
    print("Check your LogFile Path!! Your file doesn't Exist")

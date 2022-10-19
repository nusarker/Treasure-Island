print("Welcome to Muslim marriage app\n")
print("In this app you will find your perfect match\n")
religion = input("Please type your religion: ").lower()
if religion == "islam":
  first_condition = input('You are eliginbe to enter. Are you 18 years or above? type "yes" or "no\n"').lower()
  if first_condition == "yes":
    second_condition = input(' you are eligible for next option. Do you pray 5 times a day? Type "yes"  or "no\n"').lower()
    if second_condition == "yes":
    	print("You are eligible to create bio data in this marrige portal\n")
    else:
    	print("Sorry you are not eligible to create biodata")
  else:
    	print("Grow older for marriage")
else:
    print("Sorry this site is only for muslim")
    
    
  
  

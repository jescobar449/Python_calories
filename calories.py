#Name: Jose Melquiades Escobar

#Declare local variables under main() program
def main():
    #make magic numbers into named constants
    multipleForFat = 9
    multipleForCarbs = 4
    
    #Prompt the user to enter gramsFat and gramsCarbs
    gramsFat = float( input( 'Enter a number for grams of fat: '))   
    gramsCarbs = float( input ('Enter a number for grams of carbs: '))
    #Calculate calories from fat
    calFromFat = gramsFat * multipleForFat
    #Calculate calories from carbs
    calFromCarbs = gramsCarbs * multipleForCarbs
    #Call the func to display results 
    showCarbs(gramsFat, gramsCarbs, calFromFat, calFromCarbs) 


#Define a function to display resulting calories
def showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs):
    print ('')
    print ('Grams of fat:', format (gramsFat, ',.2f'))
    print ('Fat calories:', format (caloriesFat, ',.2f'))
    print ('Grams of carbs:', format (gramsCarbs, ',.2f'))
    print ('Carb calories:', format (caloriesCarbs, ',.2f'))

main()

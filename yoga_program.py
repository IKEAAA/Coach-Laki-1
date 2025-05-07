
class membershipState:

    def __init__(self, name, payment):
        self.name
        self.payment

    def beginner():

        choice = int(input("What program do you want to purchase? "))

        if 1000 < choice < 2500:
            return ("You are in the beginner package. ")
        else:
            return("Invalid amount of money. ")
        
    def recreational():

        choice = int(input("What program do you want to purchase? "))

        if 1000 < choice < 2500:
            return "You are in the Beginner package."
            
        elif 2500 <= choice <= 5000:
            return ("You should be in the recreational package. ")
        
        else:
            return ("Invalid amount of money. ")
        
    def Instructor():


        choice = int(input("What program do you want to purchase? "))

        if 1000 < choice < 2500:
            return "You are in the Beginner package."
            
        elif 2500 <= choice <= 5000:
            return ("You should be in the recreational package. ")
        
        elif 1000 > choice:
            return "Welcome to Instructor package. Everything is included! "
        
        else:
            return ("Welcome to the Instructor package! Everything is included. ")

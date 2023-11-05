#!/usr/bin/env python3
# Created By: Alex M
# Date: nov 5, 2023
# This program checks if user year is a leap year
def main():
    # get age from user
    print("Enter the year  ")
    user_year_as_str = input("")
    # convert str to an int
    try:
        user_year = int(user_year_as_str)
    except ValueError:
        print (f"{user_year_as_str} is not a valid year ")
        print("")
        #check if user input is a leap year
    else: 
        if user_year % 4 == 0 :
            if user_year % 100 == 0:
                if user_year % 400 == 0 :
                    print(f"{user_year} is a leap year")
                else:
                    print(f"{user_year} is not a leap year")
            else:
                print(f"{user_year} is not a leap year")
        else:
            print(f"{user_year} is not a leap year")
            #a concluding sentence 
    finally :
        print("THANKYOU FOR USING OUR MACHINE AND HAVE A GREAT DAY :)")

if __name__ == "__main__":
    main()
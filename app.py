import helpers as validator
import template as app
def welcome(info1, info2):
    print """
    ===============================================================================

                                {} USER
                     BIGGIE ENTERPRISE BANKING SYSTEM
            WE OFFER STATE OF THE ART BANKING TECHNOLOGY THAT
            WILL MAKE YOUR LIFE EASIER
            {}


    ================================================================================
    """.format(info1, info2)

welcome("WELCOME", "SO WHY NOT ENTER THE NEXT  AND START BANKING TODAY")





while True:
    nest = str.lower(validator.validate_user_input("enter (next) to start banking today (exit to quit)", str, "please (next/exit)"))
    if (nest == "exit") or ( nest == "next"):
        print """
        """
        break
while True:
    if nest == "exit":
        welcome("GOODBYE", "HOPE YOU REMEBER TO BANK WITH US")
        break
    app.helps()
    number = validator.validate_user_input("select your banking option", int, "please enter  valid section")
    if number == 1:
        app.create_account()
    elif number == 2:
        app.deposit_amount()
    elif number == 3:
        app.withdraw_amount()
    elif number == 4:
        app.account_inquiry()
    elif number == 5:
        app.all_accounts()
    elif number == 6:
        app.close_account()
    elif number == 7:
        app.modify_account()
    elif number == 8:
        app.helps()
    elif number == 9:
        welcome("GOODBYE", "HOPE YOU REMEBER TO BANK WITH US")
        break
    else:
        print "enter from 1 - 8 "

import libraries as app
def helps():
    print(
    """
    ==============================================
        WELCOME TO BIGGIE ENTERPRISE BANK.
        WE VALUE YOUR PATRONAGE
    ==============================================

    """
    )
    print "  S/B  MAIN MENU"
    print "   "
    print "  01 . NEW ACCOUNT"
    print "  02 . DEPOSIT AMOUNT"
    print "  03 . WITHDRAW AMOUNT"
    print "  04 . BALANCE INQUIRY"
    print "  05 . ALL ACCOUNT HOLDER LIST"
    print "  06 . CLOSE AN ACCOUNT"
    print "  07 . MODIFIY AN ACCOUNT"
    print "  08 . BANKING OPTIONS"
    print "  09 . EXIT"



"""
    BIGGIE ENTERPRISE BANK TEMPLATE
"""

"""
    ACCOUNT CREATION TEMPLATE
"""
def create_account():
    print(
    """
    ==============================================
     WELCOME TO BIGGIE ENTERPRISE BANK. PLEASE
     FILL THE REQUIRED FIELDS TO CREATE A
     BANK ACCOUNT.
    ==============================================

    """
    )
    user_acc = app.new_account()
    print(
    """
                YOUR ACCOUNT DETAILS
    ===============================================
    ACC NAME : {}
    ACC NUMBER : {}
    BALANCE : {}
    ===============================================

    """.format(user_acc['name'], user_acc['account_no'], user_acc['balance'])
    )

"""
    ACCOUNT DEPOSIT TEMPLATE
"""
def deposit_amount():
    print(
    """

    =================================================
        Hi USER WELCOME TO THE DAIMOND GRACE BANK
        ENTER YOUR ACCOUNT NUMBER  TO DEPOSIT
    =================================================

    """)
    #withdraw, user_acc = app.withdraw_amount()
    initia , new_acc =  app.deposit_amount()

    print(
        """

                    YOUR LAST ACCOUT DETAILS
        ===============================================
        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}
        ===============================================

        """.format(initia['name'], initia['account_no'], initia['balance'])
        )
    print(
        """
                    YOUR NEW ACCOUT DETAILS
        ===============================================
        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}
        ===============================================

        """.format(new_acc['name'], new_acc['account_no'], new_acc['balance'])
        )

"""
    ACCOUNT WITHDRAWER TEMPLATE
"""
def withdraw_amount():
    print(
    """

    =================================================
       Hi USER WELCOME TO THE BIGGIE ENTERPRISE BANK
       ENTER YOUR ACCOUNT NUMBER  TO WITHDRAW
    =================================================

    """)
    #withdraw, user_acc = app.withdraw_amount()
    initia , new_acc =  app.withdraw_amount()

    print(
        """

                    YOUR LAST ACCOUT DETAILS
        ===============================================
        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}
        ===============================================

        """.format(initia['name'], initia['account_no'], initia['balance'])
        )
    print(
        """
                    YOUR NEW ACCOUT DETAILS
        ===============================================
        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}
        ===============================================

        """.format(new_acc['name'], new_acc['account_no'], new_acc['balance'])
        )

"""
    MODIFY ACCOUNT TEMPLATE
"""
def modify_account():
    print(
    """

    =================================================
       Hi USER WELCOME TO THE BIGGIE ENTERPRISE BANK
       ENTER YOUR ACCOUNT NUMBER  TO MODIFY
    =================================================

    """)
    #withdraw, user_acc = app.withdraw_amount()
    initia , new_acc =  app.modify_account()

    print(
        """

                    YOUR LAST ACCOUT DETAILS
        ===============================================
        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}
        ===============================================

        """.format(initia['name'], initia['account_no'], initia['balance'])
        )
    print(
        """
                    YOUR NEW ACCOUT DETAILS
        ===============================================
        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}
        ===============================================

        """.format(new_acc['name'], new_acc['account_no'], new_acc['balance'])
        )

"""
    MODIFY ACCOUNT TEMPLATE
"""
def close_account():
    print(
    """
    ====================================================
       Hi USER WELCOME TO THE BIGGIE ENTERPRISE BANK
       ENTER YOUR ACCOUNT NUMBER  TO CLOSE YOUR ACCOUNT
    ====================================================

    """)
    #withdraw, user_acc = app.withdraw_amount()
    value = app.close_account()
    if value == None:
        print(
        """
        =================================================
                thank you for staying with us
        =================================================

        """
        )
    else:
        print(
            """
                        YOUR CLOSED ACCOUT DETAILS
            ===============================================
            WE ARE UNHAPPY TO SEE YOU GO....... :)
            ACC NAME : {}
            ACC NUMBER : {}
            BALANCE : {}

            ACCOUNT CLOSED
            ===============================================

            """.format(value['name'], value['account_no'], value['balance'])
            )

def account_inquiry():
    print(
    """
    ====================================================
       Hi USER WELCOME TO THE BIGGIE ENTERPRISE BANK
       ENTER YOUR ACCOUNT NUMBER  TO GET ACCOUNT INFO
    ====================================================

    """)
    #withdraw, user_acc = app.withdraw_amount()
    value = app.account_inquiry()
    print(
        """
                    YOUR  ACCOUT DETAILS
        ===============================================

        ACC NAME : {}
        ACC NUMBER : {}
        BALANCE : {}

        ===============================================

            """.format(value['name'], value['account_no'], value['balance'])
    )
def all_accounts():
    print(
    """
            ====================================================
               Hi USER WELCOME TO THE BIGGIE ENTERPRISE BANK
                         ALL USERS ACCOUNT
            ====================================================
    """)
    holders = app.all_accounts()
    if holders ==None:
            print(
            """====================================================
                            NO ACCOUNT FOUND
            ===================================================""")
    else:
        print(

    """                            ALL USERS ACCOUNT
        ===================================================================""")
        for value in holders:
            print(
                """
            ACC NAME : {} | ACC NUMBER : {}  | BALANCE : {}
        ====================================================================""".format(value['name'], value['account_no'], value['balance'])
            )

from Bank import BankAccount
import validator
account_file = "accounts.txt"
def modify_account():
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        user_acc = validator.get_acc(account_file, acc_no)
        if user_acc == False:
            print "user with that this {} number found".format(acc_no)
        else:
            break
    acc = validator.text_to_array(account_file)
    new_acc = dict(user_acc)
    Acc_name = validator.validate_user_input("enter your new Acc name", str, "please enter  a valid name")
    new_acc['name'] = Acc_name
    acc.append(new_acc)
    validator.account_writer(account_file, '{}'.format(acc))
    return  user_acc, new_acc


def close_account():
    res = None
    while True:
        acc_no = validator.validate_user_input("enter your account No", int, "please enter  valid account")
        while True:
            ques = str.lower(validator.validate_user_input("Aar you sure You want to do this (Yes/No)", str, "please enter (Yes/No)"))
            if ques == "yes":
                res = True
                break
            elif ques == "no":
                res = False
                break
            else:
                print "you must type in (yes/no)"
        if res == False:
            break
        else:
            user_acc = validator.get_acc(account_file, acc_no)
            if user_acc == False:
                print "user with that this {} number found".format(acc_no)
                continue
            else:
                return user_acc
                break


print close_account()

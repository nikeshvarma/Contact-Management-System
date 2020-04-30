import sys
from mobile_no_dictonary import Register as reg
from mobile_no_dictonary import user_accsess as u_acc


class Main:

    def login_reg(self):

        flag = True
        while flag:
            print("\nWELCOME TO CONTACT MANAGEMENT SYSTEM")
            print(" 1. Register \n 2. Login \n 3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 3:
                flag = False

            self.req(choice)

    @staticmethod
    def req(n):
        if n == 1:
            reg.Authentication().register_user()
        elif n == 2:
            value, user = reg.Authentication().login_user()
            if value:
                u_acc.UserAccess().user_menu(user)
            else:
                print("\nWaring : Invalid username or password")
        elif n == 3:
            sys.exit()
        else:
            print("\nWaring : Invalid Option")


R_Obj = Main()

R_Obj.login_reg()

import sys
import os


class UserAccess:

    def user_menu(self, username):
        print("\nLOGIN SUCCESSFULLY AS", username)
        while True:
            print("\n 1. Create a new contact \n 2. See all contact \n 3. Update Contact")
            print(" 4. Search contact \n 5. Delete contact \n 6. Exit")
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                self.add_new_contact(username)
            elif choice == 2:
                self.show(username)
            elif choice == 3:
                self.update(username)
            elif choice == 4:
                self.search(username)
            elif choice == 5:
                self.delete_contact(username)
            elif choice == 6:
                sys.exit()
            else:
                print("\nWaring : Invalid option")
                self.user_menu(username)

    @staticmethod
    def add_new_contact(username):
        with open((username + '.txt'), 'a') as f:
            name = input("Name:")
            mobo = input("Mobile Number:")
            email_id = input("Email ID: ")
            add = input("Address:")

            f.write('\n')
            f.write('$'.join([name, mobo, email_id, add]))
            f.write('\n')

            print("\nCONTACT ADDED SUCCESSFULLY")

    @staticmethod
    def show(username):
        if os.path.exists(username + '.txt'):
            with open((username + '.txt'), 'r') as f:
                count = 0
                for _ in f:
                    count += 1
                    line = f.readline().split('$')
                    print("Contact No. -", count)
                    print("Name -", line[0])
                    print("Mobile Number -", line[1])
                    print("Email ID -", line[2])
                    print("Address -", line[3])
        else:
            print("NO CONTACTS FOUND")

    @staticmethod
    def update(username):

        if os.path.exists(username + '.txt'):

            try:
                data = input("Enter name of contact:")

                f = open(username + '.txt', 'r')
                nf = open(username + '_temp' + '.txt', 'w')

                print("\nWHAT YOU WANT TO UPDATE\n")
                print(" 1. Name \n 2. Mobile Number \n 3. Email ID \n 4. Address")
                choice = int(input("Enter your choice: "))

                flag = 0

                for _ in f:
                    line = f.readline().split('$')
                    if data.upper() != line[0].upper():
                        nf.write('\n')
                        nf.writelines('$'.join(line))
                    else:
                        flag = 1

                if flag == 1:

                    nf.write('\n')

                    if choice == 1:
                        line[0] = input("Enter new name: ")
                        nf.write('$'.join(line))
                        print("Name updated successfully")
                    elif choice == 2:
                        line[1] = input("Enter New Mobile Number:")
                        nf.write('$'.join(line))
                        print("Mobile number updated successfully")
                    elif choice == 3:
                        line[2] = input("Enter New Email ID:")
                        nf.write('$'.join(line))
                        print("Email ID updated successfully")
                    elif choice == 4:
                        line[3] = input("Enter New Address: ")
                        nf.write('$'.join(line))
                        print("Address updated successfully")
                    else:
                        print("Invalid Input")
                        try:
                            os.remove(username + '_temp' + '.txt')
                        except Exception as e:
                            print(e)

                    f.flush()
                    f.close()
                    nf.flush()
                    nf.close()

                    if os.path.exists(username + '_temp' + '.txt'):
                        os.remove(username + '.txt')
                        os.rename(username + '_temp' + '.txt', username + '.txt')

                else:
                    print("\nNO CONTACT MATCHED RELATED TO THESE NAME OR MOBILE NUMBER\n")
                    os.remove(username + '_temp' + '.txt')

            except Exception as e:
                print(e)
        else:
            print("NO CONTACTS FOUND")

    @staticmethod
    def search(username):
        if os.path.exists(username + '.txt'):
            data = input("Enter name or mobile number to search:")
            with open(username + '.txt', 'r') as f:
                for _ in f:
                    line = f.readline().split('$')
                    if data.upper() == line[0].upper() or data == line[1]:
                        print("\nCONTACT FOUND\n")
                        print("Name -", line[0])
                        print("Mobile Number -", line[1])
                        print("Email ID -", line[2])
                        print("Address -", line[3])
                        break
                else:
                    print("\nNO CONTACT MATCHED RELATED TO THESE NAME OR MOBILE NUMBER\n")
        else:
            print("NO CONTACTS FOUND")

    @staticmethod
    def delete_contact(username):
        if os.path.exists(username + '.txt'):
            data = input("Enter name delete:")
            f = open(username + '.txt', 'r')
            nf = open(username + '_temp' + '.txt', 'w')
            flag = 0
            for _ in f:
                line = f.readline().split('$')
                if data.upper() != line[0].upper():
                    nf.write('\n')
                    nf.writelines('$'.join(line))
                else:
                    flag = 1
            f.flush()
            f.close()
            nf.flush()
            nf.close()

            if flag == 0:
                print("NO MATCH FOUND IN CONTACT LIST")
                os.remove(username + '_temp' + '.txt')
            else:
                os.remove(username + '.txt')
                os.rename(username + '_temp' + '.txt', username + '.txt')
                print("CONTACT DELETED SUCCESSFULLY")
        else:
            print("NO CONTACTS FOUND")

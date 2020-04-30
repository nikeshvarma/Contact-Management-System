import os


class Authentication:
    def register_user(self):
        print("\nREGISTER USER-SELF HERE\n")
        f = open("registrations.txt", 'a')
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            f.write('\n')
            f.write(username + ' ')
            f.write(password + '\n')
            f.close()
            print("\nRegistration successful")

        except IOError as e:
            print(e)

    def login_user(self):
        if os.path.exists('registrations.txt'):
            print("\nLOGIN HERE\n")
            try:
                f = open("registrations.txt", 'r')
                username = input("Enter username: ")
                password = input("Enter password: ")

                for _ in f:
                    data = f.readline()
                    data = data.split()
                    if username in data and password in data:
                        return True, username
                return False, username

            except IOError as e:
                print(e)

            finally:
                f.flush()
                f.close()
        else:
            print("NO ACCOUNT FOUND")
            print("REGISTER YOURSELF FIRST")
from user import USERS
from simple_chalk import chalk


def login(users):
    while True:
        username = input(chalk.cyan("Username: "))
        password = input(chalk.cyan("Password: "))

        for u in users:
            if username == u[0]:
                if password == u[1]:
                    return username

        print(chalk.red("Username or password is incorrect please try again."))


users = USERS

username = login(users)

print(chalk.green(f"{username}, has been logged in."))

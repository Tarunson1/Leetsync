from leetsync.cli.commands import Commands


def main():

    while True:

        command = input("LeetSync > ").strip().lower()

        if command == "init":
            Commands.init()

        elif command == "sync":
            Commands.sync()

        elif command == "status":
            Commands.status()

        elif command == "config":
            Commands.config()

        elif command == "help":
            Commands.help()

        elif command == "exit":
            print("Good Bye ❤️")
            break

        else:
            print("Unknown Command")


if __name__ == "__main__":
    main()
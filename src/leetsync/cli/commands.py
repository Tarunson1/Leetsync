from leetsync.notifications.console import Console


class Commands:

    @staticmethod
    def init():
        Console.success("LeetSync initialized successfully.")

    @staticmethod
    def sync():
        Console.info("Sync started...")

    @staticmethod
    def status():
        Console.info("Everything is working correctly.")

    @staticmethod
    def config():
        Console.info("Configuration loaded.")

    @staticmethod
    def help():

        print("""
Available Commands

init
sync
status
config
help
""")
from leetsync.notifications.console import Console
from leetsync.services.sync_engine import SyncEngine


class Commands:

    @staticmethod
    def init():
        Console.success("LeetSync initialized successfully.")

    @staticmethod
    def sync():

        Console.info("Starting synchronization...")

        engine = SyncEngine()

        engine.sync()

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
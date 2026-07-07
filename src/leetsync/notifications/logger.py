import logging
from pathlib import Path


LOG_FILE = Path("log.txt")


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class Logger:

    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)

    @staticmethod
    def error(message: str):
        logging.error(message)


if __name__ == "__main__":

    Logger.info("LeetSync Started")

    Logger.warning("README already exists")

    Logger.error("Git Push Failed")

    print("Log file created successfully.")
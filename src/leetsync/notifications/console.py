class Console:

    @staticmethod
    def info(message: str):
        print(f"[INFO] {message}")

    @staticmethod
    def success(message: str):
        print(f"[SUCCESS] {message}")

    @staticmethod
    def warning(message: str):
        print(f"[WARNING] {message}")

    @staticmethod
    def error(message: str):
        print(f"[ERROR] {message}")


if __name__ == "__main__":

    Console.info("LeetSync Started")

    Console.success("Repository Created")

    Console.warning("README already exists")

    Console.error("GitHub Token Invalid")
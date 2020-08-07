from loguru import logger
from 03_multifile import sum


def run():
    logger.add("log_multifile.log")
    logger.info("start run")


def main():
    run()


if __name__ == "__main__":
    main()

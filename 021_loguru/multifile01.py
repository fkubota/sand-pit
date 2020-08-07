from loguru import logger
from multifile02 import sum_ab


def run():
    logger.add("log_multifile.log")
    logger.info("="*30)
    logger.info("start run")
    sum_ab(5, 7)
    logger.info("end run")


def main():
    run()
    logger.success('Complete.')


if __name__ == "__main__":
    main()

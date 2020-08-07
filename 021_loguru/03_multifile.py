from loguru import logger


def sum(logger, a, b):
    logger.info("start")
    sum_ = a + b
    logger.info(f'a + b = {sum_}')
    logger.info("end")
    return sum_


def main():
    logger.info('start main')
    sum(logger, 2, 3)
    logger.info('end main')


if __name__ == "__main__":
    main()

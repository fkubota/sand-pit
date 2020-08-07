from loguru import logger

logger.add("logtest.log")
logger.trace('トレース')
logger.debug('デバッグ')
logger.info('情報')
logger.success('成功')
logger.warning('警告')
logger.error('エラー')
logger.critical('クリティカル')

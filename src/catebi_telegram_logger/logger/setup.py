import logging

from data.logger import LoggerCreateData
from catebi_telegram_logger.logger.telegram_handler import TelegramChatHandler


def setup_logging(logger_create_data: LoggerCreateData):
    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(logging.INFO)

    logging_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(logging_format)
    root.addHandler(console)

    tg_chat_handler = TelegramChatHandler(logger_create_data)
    tg_chat_handler.setFormatter(logging_format)
    root.addHandler(tg_chat_handler)

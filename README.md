# Catebi Telegram Logger
Library to set up logging into our private TG chats. Logging setup applies on the global level logger - on the root.

## Requirements

- Python 3.10 or newer
- [Pip](https://pypi.org/project/pip/)

## Installation

```bash
pip install git+https://github.com/catebi/catebi-telegram-logger.git
```

## Usage

To set up the Telegram Logger Handler,

1. import Pydantic's Model `LoggerCreateData` and pass the data:

```python
logger_create_data = LoggerCreateData(
        app=telegram_app,
        loop=asyncio.get_running_loop(),
        logs_chat_id=logs_chat_id,
        app_name=app_name,
        ping_developers=ping_developers,
        min_level=logging.WARNING,
    )
```
where

`app: Application` - Telegram Application,

`loop: AbstractEventLoop` - asyncio loop, usually the main app's loop,

`logs_chat_id: int` - ID of the chat for sending the logs,

`ping_developers: str` - comma separated list of Telegram @username of developers to ping about errors,

`min_level: int` - minimum logging level to log, recommended logging.WARNING

2. pass logger_create_data into setup_logging:

```python
setup_logging(logger_create_data)
```

Make sure no local loggers have '[propagate](https://docs.python.org/3/library/logging.html#logging.Logger.propagate)' field set to `False`.

## Structure

`data/logger.py` contains Pydantic's Model `LoggerCreateData` to keep and validate data

`logger/telegram_handler.py` contains `TelegramChatHandler` class, extending `logging.StreamHandler` to send logs to the specified chat.

`setup.py` configures logger formatting and adds `TelegramChatHandler` to logger handlers.

## License

This project is licensed under the [MIT License](LICENSE).
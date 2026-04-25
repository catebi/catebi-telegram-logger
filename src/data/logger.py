import os
from asyncio import AbstractEventLoop
from typing import Annotated, Optional

from pydantic import AfterValidator
from pydantic.v1 import BaseModel
from telegram.ext import Application


def negative_chat_id(chat_id: int) -> int:
    if chat_id > 0:
        return -chat_id
    return chat_id

class LoggerCreateData(BaseModel):
    app: Application
    loop: AbstractEventLoop
    logs_chat_id: Annotated[int, AfterValidator(negative_chat_id)]
    app_name: str
    ping_developers: Optional[str]
    min_level: int

    class Config:
        arbitrary_types_allowed = True




from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    """
    Represents a user with an email and password.
    """

    email: EmailStr
    password: str


class ModelDetailBase(BaseModel):
    """
    Represents the details of a model including keys and user ID.
    """

    gpt_key: str
    crm_key: str
    model_name: str
    user_id: str


class TokenBase(BaseModel):
    """
    Represents a token with access token and token type.
    """

    access_token: str
    token_type: str


class ChatBotMessage(BaseModel):
    """
    Represents a message from a human to a chatbot.
    """
    human_message: str
    send_by: str

class FileMetadata(BaseModel):
    file_content: Optional[str] = None

class ChatModel(BaseModel):
    human_message: str
    chat_id: int
    date_time: datetime
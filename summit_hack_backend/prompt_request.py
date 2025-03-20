from pydantic import BaseModel


class PromptRequest(BaseModel):
    query: str
    user_id: int

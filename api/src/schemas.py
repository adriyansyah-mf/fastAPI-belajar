from pydantic import BaseModel


class CreateJobRequest(BaseModel):
    name: str

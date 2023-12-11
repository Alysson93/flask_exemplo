from pydantic import BaseModel

class DadosDTO(BaseModel):

    email: str
    file: str
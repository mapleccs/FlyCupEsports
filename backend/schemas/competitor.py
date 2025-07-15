from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class CompetitorCreateRequest(BaseModel):
    personal_name:int=Field(str)
    gameId:str=Field(str)
    main_position:str=Field(str)
    secondary_position:str=Field(str)
    highest_rank:str=Field(str)
    current_rank:str=Field(str)
    QQ:str=Field(str)
    region:str=Field(str)
    payment_method:str=Field(str)

class CompetitorCreateResponse(BaseModel):
    success:bool=Field(bool)
    playerId:int=Field(int)
    message:str=Field(str)
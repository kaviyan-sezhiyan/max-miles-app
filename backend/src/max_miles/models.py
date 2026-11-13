from datetime import datetime
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class Card(str, Enum):
    CITI_PREMIERMILES = "CITI_PREMIERMILES"
    CITI_REWARDS = "CITI_REWARDS"
    CITI_REWARDS_AMAZE = "CITI_REWARDS_AMAZE"
    HSBC_REVOLUTION = "HSBC_REVOLUTION"
    UOB_PPV = "UOB_PPV"
    DBS_YUU = "DBS_YUU"


class Transaction(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    currency: str = Field(default="SGD", min_length=3, max_length=3)
    merchant: str = Field(min_length=1, max_length=200)
    card: Card
    timestamp: datetime

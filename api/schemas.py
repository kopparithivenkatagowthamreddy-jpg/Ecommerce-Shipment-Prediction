from pydantic import BaseModel, Field
from typing import Literal

class ShipmentInput(BaseModel):
    Warehouse_block: Literal['A','B','C','D','F']
    Mode_of_Shipment: Literal['Ship','Flight','Road']
    Customer_care_calls: int = Field(ge=0)
    Customer_rating: int = Field(ge=1, le=5)
    Cost_of_the_Product: float = Field(gt=0)
    Prior_purchases: int = Field(ge=0)
    Product_importance: Literal['low','medium','high']
    Gender: Literal['F','M']
    Discount_offered: float = Field(ge=0)
    Weight_in_gms: float = Field(gt=0)

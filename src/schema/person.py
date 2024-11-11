from typing import Literal

from pydantic import BaseModel, Field, field_validator

class Person(BaseModel):
    """
    Person schema.

    Age - The person's age.
    Height - The person's height (in meters).
    Weight - The person's weight (in kilos).
    Gender - The person's gender.
    CAEC - Consumption of Food Between Meals (CAEC).
    SMOKE - Whether the person smoke or not.
    SCC - Whether the person monitors the amount of Calories Consumption (SCC).
    CALC - Consumption of Alcohol (CALC).
    MTRANS - Transportation used (MTRANS).
    FCVC - Frequency of Consumption of Vegetables (FCVC).
    FAF - Physical activity frequency (FAF).
    TUE - Time using technology devices (TUE).
    """
    Age: int = Field(ge=0, le=100)
    Height: float = Field(ge=0.0, le=2.5)
    Weight: float = Field(ge=0, le=400)
    Gender: str = Literal["Male", "Female"]
    CAEC: str = Literal["Frequently", "Sometimes", "Always", "no"]
    SMOKE: str
    SCC: str
    CALC: str = Literal["Frequently", "Sometimes", "Always", "no"]
    MTRANS: str = Literal["Public_Transportation", "Automobile", "Walking", "Motorbike", "Bike"]
    FCVC: int = Field(ge=0, le=5)
    FAF: int = Field(ge=0, le=5)
    TUE: int = Field(ge=0, le=2)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "Age": 21,
                    "Height": 1.62,
                    "Weight": 64,
                    "Gender": "Female",
                    "CAEC": "Sometimes",
                    "SMOKE": "False",
                    "SCC": "no",
                    "CALC": "no",
                    "MTRANS": "Public_Transportation",
                    "FCVC": 2,
                    "FAF": 0,
                    "TUE": 1,
                }
            ]
        }
    }

    @field_validator("Age", "Height", "Weight", "FCVC")
    def prevent_zero(cls, v):
        if v == 0:
            raise ValueError("Ensure this value is not 0.")
        return v
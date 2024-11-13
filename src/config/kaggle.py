from pathlib import Path
from pydantic import BaseModel

from .utils import read_yaml_credentials_file


class KaggleCredentials(BaseModel):
    """Creates a Pydantic's base model for the Kaggle credentials.

    Args:
        BaseModel (pydantic.BaseModel): Pydantic base model instance.
    """

    KAGGLE_USERNAME: str
    KAGGLE_KEY: str


kaggle_credentials = KaggleCredentials(
    **read_yaml_credentials_file(
        file_path=Path.joinpath(
            Path(__file__).resolve().parents[2],
            "config",
        ),
        file_name="credentials.yaml",
    )
)

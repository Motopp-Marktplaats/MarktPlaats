from pydantic import BaseModel, Field, ConfigDict


class RatingCreate(BaseModel):
    to_user_id: int
    score: int = Field(ge=1, le=5)


class RatingUpdate(BaseModel):
    score: int = Field(ge=1, le=5)


class RatingAvgOut(BaseModel):
    user_id: int
    avg_score: float | None


class RatingOut(BaseModel):
    id: int
    from_user_id: int
    to_user_id: int
    score: int

    model_config = ConfigDict(from_attributes=True)

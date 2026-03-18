from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """
    Login input from client.
    """
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=72)  # bcrypt safety


class TokenResponse(BaseModel):
    """
    Standard JWT token response.
    """
    access_token: str
    token_type: str = "bearer"

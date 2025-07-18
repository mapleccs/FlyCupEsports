# Configuration file
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str = "admin"
    DB_PASSWORD: str = "Chen%401314"
    DB_HOST: str = "182.92.127.17"
    DB_PORT: int = 3306
    DB_NAME: str = "FLY_DB"

    SECRET_KEY: str = "+gkDMNVoMr1/BuHN8FBmOMF380frQwM76ngkM8ruZs0="
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 90

    @property
    def database_url(self) -> str:
        return f"mysql+pymysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset=utf8mb4"

    class Config:
        env_file = ".env"  # 支持.env文件


settings = Settings()

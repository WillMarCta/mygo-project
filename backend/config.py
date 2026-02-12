from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    """Clase de configuración que carga las variables de entorno desde un archivo .env"""
    DATABASE_URL: str = ""

    class Config:
        """Indica que las variables de entorno se cargarán desde un archivo .env en el mismo directorio"""
        env_file = ".env"

settings = Settings()
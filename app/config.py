from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator


class Settings(BaseSettings):
    """Application configuration settings."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    # Required settings
    openai_api_key: str = Field(..., description="OpenAI API key")
    
    # Optional LangChain settings
    langchain_api_key: str | None = Field(None, description="LangChain API key for tracing")
    langchain_tracing_v2: bool = Field(False, description="Enable LangChain tracing")
    langchain_project: str = Field("AgriGPT", description="LangChain project name")
    
    # RAG configuration
    chunk_size: int = Field(800, description="Document chunk size")
    chunk_overlap: int = Field(200, description="Chunk overlap size")
    top_k_results: int = Field(5, description="Number of top results to retrieve")
    
    @field_validator("openai_api_key")
    @classmethod
    def validate_openai_key(cls, v: str) -> str:
        """Validate that OpenAI API key is present."""
        if not v or v.strip() == "":
            raise ValueError("OPENAI_API_KEY must be set")
        return v


# Create a global settings instance
settings = Settings()

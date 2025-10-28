"""
Configuration module for managing API keys and application settings.
Loads sensitive data from environment variables.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration loaded from environment variables."""
    
    # OpenAI API Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o')
    
    # Generation Parameters
    MAX_ITERATIONS = int(os.getenv('MAX_ITERATIONS', '3'))
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
    MAX_COMPLETION_TOKENS = int(os.getenv('MAX_COMPLETION_TOKENS', '12000'))
    
    # File Paths (optional, can be overridden)
    JSON_DIRECTORY = os.getenv('JSON_DIRECTORY', '')
    TXT_DIRECTORY = os.getenv('TXT_DIRECTORY', '')
    OUTPUT_DIRECTORY = os.getenv('OUTPUT_DIRECTORY', '')
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found in environment variables. "
                "Please set it in your .env file or environment."
            )
        return True


# Validate configuration on import
Config.validate()

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
    
    # Anthropic API Configuration
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    ANTHROPIC_MODEL = os.getenv('ANTHROPIC_MODEL', 'claude-sonnet-4-5')
    
    # Generation Parameters
    MAX_ITERATIONS = int(os.getenv('MAX_ITERATIONS', '3'))
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '8192'))
    
    # File Paths (optional, can be overridden)
    JSON_DIRECTORY = os.getenv('JSON_DIRECTORY', '')
    TXT_DIRECTORY = os.getenv('TXT_DIRECTORY', '')
    OUTPUT_DIRECTORY = os.getenv('OUTPUT_DIRECTORY', '')
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError(
                "ANTHROPIC_API_KEY not found in environment variables. "
                "Please set it in your .env file or environment."
            )
        return True


# Validate configuration on import
Config.validate()

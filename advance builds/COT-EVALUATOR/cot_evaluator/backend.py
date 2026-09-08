import abc
import os
import requests
import logging
from typing import List, Dict, Any, Union

logger = logging.getLogger("cot_evaluator.backend")

class ModelBackend(abc.ABC):
    @abc.abstractmethod
    def generate(self, prompt: str, temperature: float = 0.0) -> str:
        """Sends the prompt to the model and returns the text response."""
        pass

class GroqBackend(ModelBackend):
    def __init__(self, model_name: str = "llama-3.1-8b-instant", api_key: str = None):
        if api_key is None:
            try:
                from dotenv import load_dotenv
                load_dotenv()
            except ImportError:
                pass
            api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            raise KeyError("GROQ_API_KEY environment variable is not set. Please configure it in your environment or .env file.")

        self.model_name = model_name
        self.api_key = api_key
        self.endpoint = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, prompt: str, temperature: float = 0.0) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model_name,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": temperature
        }
        
        logger.info("Sending request to Groq API. Model: %s, Temp: %.2f", self.model_name, temperature)
        logger.debug("Prompt payload: %s", prompt)
        
        try:
            response = requests.post(self.endpoint, headers=headers, json=data, timeout=30.0)
            logger.info("Received Groq API response. Status: %d", response.status_code)
        except requests.exceptions.Timeout as e:
            logger.error("Groq API request timed out after 30 seconds.")
            raise RuntimeError("Request to Groq API timed out after 30 seconds.") from e
        except Exception as e:
            logger.error("Request failed: %s", e)
            raise
            
        if response.status_code != 200:
            logger.error("Groq API returned error status. Response: %s", response.text)
            raise RuntimeError(f"Groq API Request failed with status {response.status_code}. Response: {response.text}")
            
        result = response.json()
        content = result["choices"][0]["message"]["content"].strip()
        logger.debug("Groq response content: %s", content)
        return content

class MockBackend(ModelBackend):
    def __init__(self, responses: Union[str, Dict[str, str], List[str]] = ""):
        """Helper backend for testing.
        Args:
            responses: Can be:
                - a single string response.
                - a dictionary mapping prompt lookup keys/substrings to string responses.
                - a list of responses returned sequentially.
        """
        self.responses = responses
        self.call_count = 0

    def generate(self, prompt: str, temperature: float = 0.0) -> str:
        self.call_count += 1
        if isinstance(self.responses, str):
            return self.responses
        elif isinstance(self.responses, list):
            idx = min(self.call_count - 1, len(self.responses) - 1)
            return self.responses[idx]
        elif isinstance(self.responses, dict):
            for key, val in self.responses.items():
                if key in prompt:
                    return val
            return "MockBackend: No matching prompt key found."
        return ""

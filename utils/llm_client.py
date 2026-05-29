# utils/llm_client.py
import time

class OpenAIClient:
    def generate_summary(self, prompt: str) -> str:
        """Hace una llamada real a la API de OpenAI (simulada aquí con un delay)."""
        # Simulamos la latencia de red de una API real de 2 segundos
        time.sleep(2) 
        return "Respuesta cruda de la API externa"
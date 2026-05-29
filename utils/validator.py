# utils/validator.py

class LLMSummaryEvaluator:
    def __init__(self, threshold: float = 0.5):
        """
        threshold (umbral): Puntuación mínima de 0.0 a 1.0 para considerar un test como válido.
        """
        if not (0.0 <= threshold <= 1.0):
            raise ValueError("El umbral (threshold) debe estar entre 0.0 y 1.0")
        self.threshold = threshold

    def _tokenize(self, text: str) -> set[str]:
        """Método privado para limpiar el texto y convertirlo en un set de palabras únicas."""
        # Pasamos a minúsculas y limpiamos signos básicos de puntuación
        clean_text = text.lower().replace(".", "").replace(",", "").replace(";", "")
        return set(clean_text.split())

    def evaluate_similarity(self, response_text: str, expected_text: str) -> float:
        """Calcula el índice de similitud de Jaccard entre la respuesta del LLM y la esperada."""
        set_response = self._tokenize(response_text)
        set_expected = self._tokenize(expected_text)
        
        # Intersección: Palabras comunes entre ambos textos
        intersection = set_response.intersection(set_expected)
        # Unión: Total de palabras únicas entre ambos textos
        union = set_response.union(set_expected)
        
        if not union:
            return 0.0
            
        # Puntuación matemática de similitud
        return len(intersection) / len(union)

    def is_passed(self, response_text: str, expected_text: str) -> bool:
        """Determina si el test pasa comparando la puntuación obtenida contra el umbral configurado."""
        score = self.evaluate_similarity(response_text, expected_text)
        return score >= self.threshold
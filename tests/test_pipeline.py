import sys
import os
# Forzamos a Python a mirar en la raíz del proyecto pase lo que pase
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import pytest
from utils.validator import LLMSummaryEvaluator
from utils.llm_client import OpenAIClient

# 1. LEER EL CSV CON PANDAS
# read_csv carga el archivo como un DataFrame (una tabla estilo Excel).
# .to_dict(orient="records") lo convierte en una lista de diccionarios limpia para Pytest.
df = pd.read_csv("data/llm_evaluations.csv")
dataset_csv = df.to_dict(orient="records")


@pytest.mark.parametrize("caso", dataset_csv)
def test_pipeline_evaluacion_con_mock(caso, mocker):
    """
    Test que simula la llamada a la API y evalúa la respuesta del modelo
    utilizando los datos de nuestro dataset CSV.
    """
    # 2. INSTANCIAR COMPONENTES
    cliente_llm = OpenAIClient()
    evaluador = LLMSummaryEvaluator(threshold=0.4)
    
    # 3. EL MOCK (La magia para no gastar dinero ni tiempo)
    # Interceptamos el método 'generate_summary' del objeto 'cliente_llm'
    # return_value le dice qué texto exacto debe devolver cuando sea llamado
    mocker.patch.object(
        cliente_llm, 
        "generate_summary", 
        return_value=caso["llm_response"]
    )
    
    # 4. EJECUCIÓN
    # Al llamar a este método, NO tardará 2 segundos porque el mock intercepta la llamada
    respuesta_simulada = cliente_llm.generate_summary(caso["prompt"])
    
    # 5. EVALUACIÓN Y ASERCIÓN
    resultado_test = evaluador.is_passed(respuesta_simulada, caso["reference_human"])
    
    assert resultado_test is caso["expected_status"]
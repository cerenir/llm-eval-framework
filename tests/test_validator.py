import sys
import os
# Forzamos a Python a mirar en la raíz del proyecto pase lo que pase
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from utils.validator import LLMSummaryEvaluator

# 1. Cargamos el JSON una sola vez para que esté disponible para las pruebas
with open("data/test_dataset.json", "r", encoding="utf-8") as archivo:
    dataset = json.load(archivo)

# 2. Le decimos a Pytest que genere un test dinámico por cada elemento del JSON
@pytest.mark.parametrize("caso", dataset)
def test_validador_con_dataset_json(caso):
    validador = LLMSummaryEvaluator(threshold=0.4)
    
    resultado_real = validador.is_passed(caso["llm_response"], caso["reference_human"])
    assert resultado_real is caso["expected_status"]
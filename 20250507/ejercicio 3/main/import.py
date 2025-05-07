import sys
import os

# Agregar al path el directorio padre para que pueda encontrar 'modulo'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo import saludar

saludar()


# run.py
import runpy
import os
import sys
import traceback

# --- INICIO: MIGA DE PAN - KAIZEN: CAJA NEGRA (TELEMETRÍA) ---
# NOTA DE INGENIERÍA: Atrapa errores silenciosos en la interfaz (PySide)
# cuando se ejecuta compilado en modo --windowed sin consola.
def global_exception_handler(exctype, value, tb):
    error_msg = "".join(traceback.format_exception(exctype, value, tb))
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, error_msg, "Radar de Errores (Fallo Silencioso)", 0x10)
    except:
        pass
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = global_exception_handler
# --- FIN: MIGA DE PAN ---

# Añadir el directorio 'src' al path para que sea la raíz de las importaciones.
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# Ejecutar el punto de entrada principal como un módulo.
runpy.run_module("main", run_name="__main__")
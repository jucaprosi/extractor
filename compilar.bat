@echo off
echo [1/3] Instalando el motor de compilacion (PyInstaller)...
pip install pyinstaller

echo [2/3] Ensamblando la maquinaria (Modo Multi-Instancia / OneDir)...
:: Se copian los archivos YAML y Assets necesarios para que el ejecutable funcione
pyinstaller --noconfirm --onedir --windowed --name "PDA_Extractor" --add-data "src/features/pda_extractor/config_pda_extractor.yaml;features/pda_extractor" --add-data "drivers;drivers" --paths src --hidden-import main run.py

echo [3/3] ¡Compilacion terminada exitosamente!
echo Busque su programa ejecutable dentro de la nueva carpeta "dist\PDA_Extractor"
pause
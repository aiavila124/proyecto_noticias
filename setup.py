import subprocess
import sys
import os

def install_packages(packages):
    """Instala los paquetes especificados."""
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def generate_requirements():
    """Genera el archivo requirements.txt."""
    with open("requirements.txt", "w") as f:
        subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=f)

def main():
    # Lista de paquetes que quieres instalar
    # packages = ["requests", "numpy"]
    
    # Instala los paquetes
    # install_packages(packages)
    
    # Genera el archivo requirements.txt
    generate_requirements()

    print("requirements.txt generado con éxito.")

if __name__ == "__main__":
    main()

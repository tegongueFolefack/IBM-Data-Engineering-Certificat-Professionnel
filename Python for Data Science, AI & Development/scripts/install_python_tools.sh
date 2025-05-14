#!/bin/bash

# Mettre à jour le système
echo "Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

# Installer Python et pip
echo "Installation de Python et pip..."
sudo apt install -y python3 python3-pip python3-venv

# Installer Visual Studio Code
echo "Installation de Visual Studio Code..."
sudo apt install -y wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install -y code

# Installer PyCharm via Snap
echo "Installation de PyCharm..."
sudo snap install pycharm-community --classic

# Installer Jupyter Notebook
echo "Installation de Jupyter Notebook..."
pip3 install notebook

# Installer les bibliothèques Python populaires
echo "Installation des bibliothèques Python : NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn..."
pip3 install numpy pandas matplotlib seaborn scikit-learn

# Installer Django et Flask
echo "Installation de Django et Flask..."
pip3 install django flask

# Installer Git
echo "Installation de Git..."
sudo apt install -y git

# Configurer l'extension Python dans Visual Studio Code
echo "Configuration de Visual Studio Code pour Python..."
code --install-extension ms-python.python

# Créer un environnement virtuel exemple
echo "Création d'un environnement virtuel Python (myenv)..."
python3 -m venv myenv

echo "Tout est installé et configuré. Activez l'environnement virtuel avec :"
echo "source myenv/bin/activate"
echo "Ensuite, pour lancer VS Code : code ."
echo "Pour lancer Jupyter Notebook : jupyter notebook"

echo "Installation terminée."

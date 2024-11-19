# Image de Python
FROM python:3.12

# Répertoire du labo
WORKDIR /labo5

# Copier les fichiers de l'application dans le conteneur
COPY app.py requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]

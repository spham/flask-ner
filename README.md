# flask-ner

Flask + spaCy simple API for Named Entity Recognition

The Python in this repo was developed using TDD and recorded for a video series on YouTube, which [can be found here](https://youtu.be/eAPmXQ0dC7Q).

## Installation

1. Assurez-vous d'avoir Python3 et pip installés :
```bash
sudo apt update
sudo apt install python3-pip python3-venv
```

2. Créez et activez un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installez le projet et ses dépendances :
```bash
pip install -e .
```

4. Téléchargez le modèle de langue anglaise pour spaCy :
```bash
python -m spacy download en_core_web_sm
```

## Lancement du projet

1. Clonez ce dépôt (si ce n'est pas déjà fait) :
```bash
git clone https://github.com/wesdoyle/flask-ner-spacy.git
cd flask-ner-spacy
```

2. Activez l'environnement virtuel si ce n'est pas déjà fait :
```bash
source venv/bin/activate
```

3. Lancez l'application Flask :
```bash
python app.py
```

4. Ouvrez votre navigateur et accédez à `http://localhost:5000`

Pour désactiver l'environnement virtuel quand vous avez terminé :
```bash
deactivate
```

## Tests

Pour lancer les tests :

1. Assurez-vous que l'environnement virtuel est activé :
```bash
source venv/bin/activate
```

2. Lancez les tests avec pytest :
```bash
PYTHONPATH=. pytest test/
```

Note : Les tests end-to-end (e2e) nécessitent un navigateur web et Selenium WebDriver.

## Utilisation

- L'interface web vous permet d'entrer du texte en anglais
- Le système identifiera automatiquement les entités nommées (personnes, organisations, lieux, etc.)
- Les résultats sont affichés de manière interactive dans le navigateur

## API REST

Vous pouvez également utiliser l'API REST :

- Endpoint : `/ner`
- Méthode : POST
- Format de données : JSON
- Exemple de requête :
```json
{
    "sentence": "Apple is looking at buying U.K. startup for $1 billion"
}

# Projet de Comptage de Mots avec PLY

Ce projet permet de compter le nombre de fois qu'un mot spécifique apparaît dans un texte, en utilisant des expressions régulières avec la bibliothèque PLY (Python Lex-Yacc). Le texte est lu à partir d'un fichier externe, et l'utilisateur peut choisir le fichier à analyser parmi ceux présents dans le répertoire du projet.

## Fichiers

- **Text.txt** : Exemple de fichier texte (vous pouvez ajouter d'autres fichiers texte dans le répertoire si nécessaire).
- **WordCount.py** : Script Python qui affiche la liste des fichiers texte dans le répertoire, permet à l'utilisateur de choisir un fichier, demande le mot à rechercher, et affiche le nombre de fois que ce mot apparaît dans le texte.

## Installation

1. **Cloner le dépôt** :
    ```bash
    git clone <URL_DU_DEPOT>
    cd <NOM_DU_REPERTOIRE>
    ```

2. **Installer les dépendances** :
    - Assurez-vous d'avoir `pip` installé. Ensuite, installez la bibliothèque PLY :
      ```bash
      pip install ply
      ```

## Utilisation

1. **Préparer les fichiers de texte** :
   - Placez les fichiers texte que vous souhaitez analyser dans le même répertoire que `WordCount.py`. Le fichier `Text.txt` est un exemple ; vous pouvez ajouter autant de fichiers texte que vous le souhaitez.

2. **Exécuter le script** :
    ```bash
    python WordCount.py
    ```

3. **Choisir un fichier** :
    - Le script affichera la liste des fichiers texte présents dans le répertoire. Entrez le numéro correspondant au fichier que vous souhaitez analyser.

4. **Entrer le mot à chercher** :
    - Lorsque le script vous le demande, entrez le mot que vous voulez compter dans le texte du fichier sélectionné.

## Explication du Script

1. **Liste des fichiers** :
    - Le script liste tous les fichiers texte présents dans le répertoire courant et demande à l'utilisateur de choisir celui à analyser.

2. **Lecture du fichier** :
    - La fonction `read_text` lit le contenu du fichier sélectionné.

3. **Interaction avec l'utilisateur** :
    - Le script demande à l'utilisateur de spécifier le mot à rechercher dans le texte du fichier choisi.

4. **Analyse lexicale avec PLY** :
    - Le lexer de PLY analyse le texte et compte les occurrences du mot spécifié par l'utilisateur.

5. **Affichage du résultat** :
    - Le script affiche le nombre de fois que le mot apparaît dans le texte.

## Contribution

- **Jory**
- **Hichem**
- **Thibaut**
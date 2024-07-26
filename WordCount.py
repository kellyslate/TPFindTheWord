import os
import ply.lex as lex

# Définir les tokens
tokens = (
    'WORD',
)

# Définir les règles pour les tokens
def t_WORD(t):
    r'\b\w+\b'
    return t

# Gérer les erreurs
def t_error(t):
    t.lexer.skip(1)

# Fonction pour lire le texte depuis un fichier
def read_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return None

# Fonction pour afficher la liste des fichiers dans le répertoire
def list_files_in_directory(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except OSError as e:
        print(f"Erreur lors de l'accès au répertoire : {e}")
        return []

# Fonction principale
def main():
    # Afficher les fichiers disponibles dans le répertoire courant
    directory = '.'
    files = list_files_in_directory(directory)
    
    if not files:
        print("Aucun fichier trouvé dans le répertoire.")
        return
    
    print("Fichiers disponibles :")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")

    # Demander à l'utilisateur de choisir un fichier
    try:
        choice = int(input("Entrez le numéro du fichier que vous voulez analyser : "))
        if 1 <= choice <= len(files):
            file_path = files[choice - 1]
        else:
            print("Choix invalide.")
            return
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return

    # Lire le texte depuis le fichier choisi
    text = read_text(file_path)
    if text is None:
        return

    # Demander à l'utilisateur d'entrer le mot à chercher
    word_to_count = input("Entrez le mot que vous voulez compter : ").strip().lower()

    # Initialiser l'analyseur lexical
    lexer = lex.lex()

    # Compter les occurrences du mot
    count = 0
    lexer.input(text)
    for token in lexer:
        if token.type == 'WORD' and token.value.lower() == word_to_count:
            count += 1

    print(f"Le mot '{word_to_count}' apparaît {count} fois dans le texte.")

if __name__ == "__main__":
    main()

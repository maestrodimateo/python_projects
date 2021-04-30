# Api Todolist

## Fonctionnalités

1. Se connecter
2. S'inscrire
3. créer une todolist
4. Ajouter une tache
5. Supprimer une tache
6. Valider une tâche


## Tables en jeux

1. User -> id (int), name (string, unique), email (string, unique), password (string), picture (string), public_id (string)
2. Todo -> id (int), name (string), deadline, created_at
3. Task -> id (int), name (string), done (bool, default = false), when (datetime)

## Etapes à suivre

1. Création des modèles
2. Création des schemas
3. creation des ressources
4. login
5. Mot de passe oublié
# Créer un serveur MCP pour RAG à partir de documents réels complexes
Ce serveur exploite les capacités de recherche et de récupération de documents de pointe de [GroundX](https://eyelevel.ai/).
Vous pouvez le tester rapidement sur vos propres documents complexes [ici](https://eyelevel.ai/).
### Configuration
Pour synchroniser les dépendances, exécutez :
```sh
uv sync
```
### Variables d'environnement
Vous devez configurer les variables d'environnement suivantes :
```sh
GROUNDX_API_KEY=...
```
[Obtenez vos clés API GroundX ici](https://eyelevel.ai/)

Assurez-vous que ces variables sont correctement configurées avant d'exécuter l'application. Utilisez `.env.example` comme référence et créez votre propre fichier `.env`.


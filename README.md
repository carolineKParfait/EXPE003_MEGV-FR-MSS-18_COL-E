# Analyser un corpus HTR

Le corpus est disponible sur le [github](https://github.com/Masculinites-Esclavagistes/MEGV-FR-MSS-18) du projet Masculinités Esclavagistes.

Dans ce dépôt tu trouveras les programmes (prog) et les résultats pour :


- La Reconnaissance d'entités nommées (REN) avec :
    + [x] spaCy 2.3.5 ;
    + [X] spaCy 3.8.11 ;
    + [ ] Stanza ;
    + [ ] Bert ;

- Calcul de distances avec diverses métriques de similarité/distances dans les dossiers SIM :
    + [x] spaCy 2.3.5 ;
    + [X] spaCy 3.8.11 ;
    + [ ] Stanza ;
    + [ ] Bert ;
- Graphiques pour les résultats des SIM ;
    + [x] spaCy 2.3.5 ;
    + [X] spaCy 3.8.11 ;
    + [ ] Stanza ;
    + [ ] Bert ;
- Calcul des intersections et graphiques ;
    + [X] spaCy 2.3.5 ;
    + [X] spaCy 3.8.11 ;
    + [ ] Stanza ;
    + [ ] Bert ;

# Conseils de dév.

Tous les scripts on été testé sous Windows et Fedora (Linux).
    
## Installer spaCy 2.3.5

Cette version de spaCy s'utilise dans un environnement python =<3.7

```bash
pip install cymem==2.0.2 murmurhash==1.0.2 preshed==3.0.2
pip install spacy==2.3.5
```

installer les modèles de langues adaptés : exemple pour le modèle *fr_core_news_sm-2.3.0*

```bash
pip install https://github.com/explosion/spacy-models/releases/download/fr_core_news_sm-2.3.0/fr_core_news_sm-2.3.0.tar.gz
```

## Utiliser le script upstpt.py

Utiliser un environnement python 3.10 avec upsetplot 0.9.0 et matplotlib 3.9.1 les versions plus récentes de Matplotlib ne sont pas compatible avec upsetplot et Matplotlib 3.9.1 est compatible avec Python 3.8 à 3.12.

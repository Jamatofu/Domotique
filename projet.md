# Domotique

## Quelle est l'idée du projet?

1. Pouvoir minimiser la consommation électrique d'un bâtiment.

A l'aide d'un système embarqué qui pourrait être un interrupteur, on controlerait le système électrique d'un bâtiment de manière précise. Par exemple, dans une pièce, on place un OE dans une pièce précise. Cet OE va recevoir des ordres d'un ordinateur central qui le commande. Il recevra comme ordre d'éteindre les lumières à partir d'une certaine heure.

Cet appareil sera capable de communiquer avec un autre objet embarqué servant de relai à l'ordinateur central. De cet ordinateur central viendront les ordres aux objets embarqués au bout de la chaine.
Nous aurions cet hiérarchie :

ordinateur centrale <=> relayeur / répéteur <=> controleur

2. Centraliser le contrôle de toute la Domotique sur un seul poste

Ce poste doit permettre plusieurs réglages :
  - régler l'heure des extinctions et de rallumage des appareils (imprimante, ordinateur)
  - régler l'ouverture et la fermeture des volets
  - régler température du bâtiment


3. Rendre le bâtiment intelligent

L'ordinateur centrale doit pouvoir optimiser la consommation électrique en fonction de plusieurs paramètres :
  - habitude de la consommation électrique d'une pièce :
  - adapter certains système en fonction de certains paramètres :
    - adapter le chauffage en fonction de la météo
    - adapter éclairage et chauffage en fonction de la précense des gens dans la pièce

4. Gérer les appareils et avoir des statistiques sur la consommation

Pouvoir afficher des statistiques sur l'ordinateur central :
  - consommation par salle
  - consommation horaire
  - consommation en temps réel

Définir des ensembles d'appareils => pouvoir donner un nom à un étage ou à un département d'une entreprise
Exporter les résultats sous format Excel
Pouvoir définir le matériel électrique utilisé  et fournir un devis d'économie d'énergie si il y a un changement de pièce

A l'aide des dispositifs, pouvoir faire une cartographie du bâtiment


## Rôle de l'objet embarqué

- fournir à interval régulier des informations sur l'état de marche
- pouvoir se mettre en on/off

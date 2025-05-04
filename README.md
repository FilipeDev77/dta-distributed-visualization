# 🚀 Projet de Programmation Distribuée et Concurrente

## 🔧 Objectif

Développer un **système distribué en temps réel** simulant les variations du cours d’une cryptomonnaie fictive, le **DTAcoin**, en s’appuyant sur une architecture **producteur-consommateur**. Le projet utilise **Apache Kafka** pour l’échange de messages, **Docker** pour l’orchestration, et inclut une **interface web** pour la visualisation graphique instantanée du cours.

---

## 🏗️ Architecture Générale

### 🔲 Composants

- **Kafka (Broker)** : moteur de messagerie assurant la fiabilité et la scalabilité de la communication.
  
- **Producer** : simule le cours du DTAcoin en générant des valeurs toutes les 0,2 secondes.
  
- **Workers (Consumers)** : consomment et traitent les messages du topic Kafka.
  
- **Interface Web (Flask + Chart.js)** : affiche en temps réel les variations de prix via une API REST.
  
- **Docker Compose** : orchestre le déploiement de tous les services dans des conteneurs Docker.
  

---

## 🧩 Programmation Distribuée

Ce projet illustre les principes d’un système distribué :

### 1. 🖧 Composants Décentralisés

- Producteurs et consommateurs répartis dans des conteneurs indépendants.
  
- Kafka assure une **communication faiblement couplée et asynchrone**.
  

### 2. 📦 Dockerisation

- Tous les services (Kafka, Zookeeper, producer, workers, interface web) sont conteneurisés.
  
- Avantages :
  
  - **Isolation**,
    
  - **Portabilité**,
    
  - **Scalabilité horizontale** (ajout facile de workers).
    

### 3. 📨 Communication via Kafka

- Kafka joue le rôle de **bus de messages**.
  
- Producteurs publient dans un topic ; les workers les consomment.
  
- Cette architecture assure **résilience** et **extensibilité**.
  

### 4. 🔁 Résilience et Scalabilité

- Kafka stocke les messages en cas de panne d’un worker.
  
- Des workers peuvent être ajoutés sans perturber le système.
  
- Kafka gère la distribution des messages entre consommateurs.
  

---

## ⚙️ Programmation Concurrente

La **concurrence locale** optimise le traitement des messages dans les workers :

### 1. 🧵 Traitement Multi-thread

- Chaque message est traité dans un **thread dédié** :  
  → traitement parallèle, meilleure réactivité.

### 2. ⚖️ Gestion de la Charge

- Le paramètre `max_poll_records=1` limite la consommation à un message à la fois.  
  → évite la surcharge en threads.

---

## 🔄 Étapes de Réalisation

### 1. Génération de Données (Cours du DTAcoin)

- Génération aléatoire simulant les fluctuations d’un cours de cryptomonnaie.
  
- Encodage en JSON et envoi via `KafkaProducer`.
  

### 2. Déploiement Kafka avec Docker

- Utilisation d’images Docker officielles.
  
- Orchestration via `docker-compose.yml`.
  

### 3. Développement des Workers

- `KafkaConsumer` écoute et traite les données.
  
- Chaque message déclenche un thread.
  

### 4. Paramétrage Kafka

- Réglage des performances de consommation.
  
- Choix du démarrage de consommation (`earliest` ou `latest`).
  

### 5. Mise en place de la Concurrence

- Utilisation de `threading.Thread` pour traitement asynchrone.
  
- Permet l’ajout de workers à chaud.
  

---

## 🌐 Visualisation Temps Réel

### 🎯 Objectif

Afficher l’évolution du **cours du DTAcoin** en temps réel dans une page web interactive.

### 🧱 Architecture Complémentaire

- **Backend Flask** : expose l’API REST `GET /get_data` contenant le dernier prix reçu.
  
- **Frontend HTML + Chart.js** : met à jour le graphique automatiquement.
  

### 🗂️ Structure du Dossier

```
Distributed_project/
│
├── docker-compose.yml
├── producer/
│   └── producer.py
│   └── Dockerfile
│
├── worker1/
│   └── worker.py
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── templates/
│       └── index.html
│
└── worker2/
    ├── Dockerfile
    └── worker.txt
```

`worker/ ├── app.py # Serveur Flask ├── kafka_consumer.py # Thread Kafka pour alimenter les données ├── templates/ │ └── index.html # Interface web avec graphique └── static/ └── script.js # Script JS (si séparé)`

### 🔁 Fonctionnement

- Un thread Kafka met à jour la dernière valeur du DTAcoin.
  
- L’interface web interroge cette valeur toutes les 2 secondes.
  
- Le graphique se met à jour automatiquement avec Chart.js.
  

---

## ⚙️ Technologies

| Composant | Technologie |
| --- | --- |
| Messaging | Apache Kafka |
| Orchestration | Docker + Docker Compose |
| Programmation | Python (kafka-python) |
| Backend Web | Flask |
| Frontend | HTML / JS / Chart.js |
| Concurrence | Python threading |

---

## ▶️ Lancement du Projet

```
docker-compose up --build
```

---

## 📈 Résultat Attendu

- Génération de cours pour le DTAcoin toutes les 0,2 secondes.
  
- Traitement instantané par les workers.
  
- Affichage dynamique sur le graphique web.
  
- Possibilité d’ajouter de nouveaux workers sans arrêt du système.
  

---

## ✅ Conclusion

Ce projet met en œuvre les fondements de la **programmation distribuée et concurrente** :

- Système **modulaire**, **scalable** et **résilient**.
  
- **Kafka** assure la communication inter-composants.
  
- Les **threads** permettent un traitement parallèle fluide.
  
- Visualisation simple mais efficace du **cours du DTAcoin en direct**.

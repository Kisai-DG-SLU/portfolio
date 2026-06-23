# Rapport de Conduite de Projet

## Portfolio AI Engineer -- Projet 15 (P15)

**Auteur :** Damien GUESDON
**Date :** juin 2026
**Formation :** AI Engineer -- OpenClassrooms (804 heures)
**Projet technique :** SophIA -- Plateforme d'orchestration d'agents IA

---

## 1. Contexte et analyse des besoins

### 1.1 Presentation du projet

Ce rapport est le livrable final du Projet 15 de la formation AI Engineer. Il couvre la demarche de conduite de projet appliquee a la realisation d'un portfolio professionnel et d'un projet technique personnel.

Le projet technique retenu est **SophIA** (Sovereign Orchestrator Platform for Holistic Intelligence Architecture), une plateforme d'orchestration multi-agents IA deployee sur un cluster OKD SNO bare-metal avec GPU NVIDIA Tesla A2.

L'objectif professionnel vise le poste de **Head of AI Platform** (salaire cible 80-125kE), en demontrant la capacite a concevoir, deployer, industrialiser et superviser des solutions IA en environnement conteneurise de production.

Le parcours de l'apprenant s'appuie sur 20 ans d'expertise en infrastructure critique (reseau MPLS, Cisco, BGP, OSPF) et direction technique, renforces par 804 heures de formation couvrant 15 projets.

### 1.2 Contexte organisationnel

Le projet s'inscrit dans un contexte de transformation profonde du marche de l'IA. Les entreprises decouvrent massivement l'IA generative via des outils SaaS (ChatGPT, Copilot) sans gouvernance, creant un phenomene de "Shadow AI" : la propriete intellectuelle (brevets, donnees financieres, secrets industriels) est injectee sur des serveurs etrangers sans controle.

Le besoin exprime n'est pas de "faire de l'IA" mais de le faire en maitrisant sa souverainete technologique. Les parties prenantes identifiees sont :

- **Damien Guesdon** en tant qu'AI Engineer et futur Head of AI Platform
- **Les recruteurs** cibles (directions techniques, VP Engineering, directions innovation)
- **Les equipes internes** qui devront maintenir et faire evoluer la plateforme

Les contraintes du projet sont :

- **Autonomie complete** : realisation en solo de l'infrastructure a l'application
- **Infrastructure bare-metal** : cluster OKD Single Node OpenShift, GPU contraint (16Go, non fractionnable)
- **Budget maitrise** : couts energetiques et materiel, pas de budget cloud
- **Securite** : systeme air-gappe, isolation reseau par namespace

### 1.3 Parcours de formation : les 14 projets fondateurs

Les 15 projets de la formation constituent une progression pedagogique qui a directement alimente la conception de SophIA :

| Phase | Projets | Notions acquises |
|---|---|---|
| Fondamentaux (P1-P3) | Decouverte AIE, API SegFormer, Regression | Python, Git, consommation API, ML supervise |
| ML classique (P4-P6) | Classification attrition, FastAPI, Scoring credit | XGBoost, SHAP, FastAPI, MLflow, cout metier |
| MLOps & RAG (P7-P8) | Systeme RAG, Monitoring derives | LangChain, FAISS, Docker, Evidently, Ragas |
| Vision strategique (P9-P11) | Cadrage Azure, Deep Learning, RL | ROI, RGPD, ResNet, Stable-Baselines3, OpenShift |
| Architecture complexe (P12-P14) | ETL Airflow, Agents LangGraph, Fine-tuning LLM | Airflow, OKD, Milvus, LoRA, vLLM, Presidio |

Les 804 heures de formation ont permis de construire une vision systemique : un projet comme SophIA ne consiste pas seulement a entrainer un modele, mais a orchestrer l'ensemble de la chaine, de la collecte du besoin au monitoring en production. C'est cette approche qui distingue un architecte de plateforme d'un data scientist.

---

## 2. Audit de la solution data existante

### 2.1 Architecture actuelle de SophIA

SophIA est une plateforme multi-agents organisee en 5 piliers interconnectes :

```
                             Utilisateurs / API
                                    |
                                    v
                             WireGuard Access
                                    |
                                    v
+---------------------------------------------------+
| 1. Fondations : Materiel & K8s (OKD SNO)          |
|    - GPU NVIDIA Tesla A2, SCOS immutable          |
|    - 9 namespaces isoles (git, core, inference,    |
|      memory, dmz, skills, apps, sandbox, test)     |
+---------------------------------------------------+
           |                    |
           v                    v
+-------------------+  +---------------------+
| 2. Cerveau        |  | 3. Memoire RAG      |
| Hermes (orchestre)|  | Qdrant + pipeline    |
| LiteLLM (routage) |  | embeddings           |
+-------------------+  +---------------------+
           |                    |
           v                    v
+----------------------------------------------+
| 4. Pantheon Agentique                        |
| SophIA (moteur) | Dionysos (cluster)         |
| Hephaistos (dev) | Ouranos (prod/HITL)       |
| Athena (RBAC/HITL)                           |
+----------------------------------------------+
           |
           v
+-------------------+  +---------------------+
| 5. Automatisation |  | 6. Outils           |
| CI/CD BuildConfig |  | MCP, TTS, Ghost     |
+-------------------+  +---------------------+
```

### 2.2 Stack technique

| Domaine | Technologie |
|---|---|
| Orchestration | OKD (OpenShift) SNO bare-metal |
| Conteneurisation | Docker, Podman, CRI-O |
| Routage LLM | LiteLLM (proxy multimodal) |
| Base vectorielle | Qdrant |
| Monitoring | Prometheus, Grafana, node-exporter |
| Git / CI/CD | Forgejo, BuildConfig, GitOps |
| Securite reseau | EgressFirewall, namespaces air-gappes |
| Agents | Hermes (framework agentique) |

### 2.3 Evaluation de la solution existante

**Forces identifiees :**

- Souverainete totale : aucune donnee ne quitte l'infrastructure
- Agnostisme : les modeles LLM sont interchangeables (Mistral, Llama, Qwen)
- Securite : isolation reseau par namespace, pas d'acces sortant pour les zones critiques
- Cout maitrise : pas de dependance a un cloud provider

**Axes d'amelioration :**

- Complexite de maintenance : le cluster bare-metal necessite une expertise pointue
- GPU contraint : 16Go non fractionnables, limitation pour les gros modeles
- Documentation : l'architecture est documentee mais meriterait un schema C4 unifie

### 2.4 Les projets precurseurs qui ont nourri SophIA

SophIA n'est pas parti d'une page blanche. Chaque brique de l'architecture a ete experimentee dans les projets precedents :

| Brique SophIA | Projet precurseur | Notion cle |
|---|---|---|
| RAG / Qdrant | P7 (Systeme RAG Puls-Events) | LangChain, FAISS, embeddings Mistral, Ragas |
| Data Drift / Monitoring | P8 (MLOps avance) | Evidently AI, NannyML, profiling |
| Orchestration agentique | P13 (Chess Master FFE) | LangGraph, Milvus, MCP |
| Deploiement LLM local | P14 (Triage medical CHSA) | vLLM, Qwen3, LoRA, Presidio |
| Deploiement OKD | P12 (CheckIt.AI) | Airflow, Streamlit sur OKD |
| Tracking d'experiences | P6 (Scoring credit) | MLflow, Optuna, cout metier |

Cette progression montre que SophIA est l'aboutissement d'une montee en competence progressive : chaque projet a apporte une brique qui trouve sa place dans l'architecture finale.

---

## 3. Identification de la solution technique cible

### 3.1 Architecture cible

L'architecture visee est une plateforme d'orchestration d'agents IA repondant aux exigences de souverainete, de securite et de cout.

Les 9 namespaces OKD sont organises en zones fonctionnelles :

- **Zone usine (sophia-git)** : Forgejo, CI/CD, seule zone avec acces sortant (GitHub, Gmail)
- **Zone cerveau (sophia-core)** : Hermes, LiteLLM, orchestration centrale
- **Zone air-gappee (sophia-inference, sophia-memory)** : Inference LLM, Qdrant, aucun acces sortant
- **Zone SAS (sophia-dmz)** : Point d'entree utilisateur, authentification
- **Zone outils (sophia-skills)** : Outils MCP, TTS, services auxiliaires
- **Zone frontend (sophia-apps)** : Interfaces utilisateur
- **Zone dev (sophia-sandbox)** : Pods de developpement et tests
- **Zone CI/CD (sophia-test)** : Tests automatises

### 3.2 Justification des choix architecturaux

**OKD SNO vs Docker Compose**

Le choix d'OKD (plutot que Docker Compose utilise en P7, P8, P13) est motive par le besoin d'isolation et de securite. Docker Compose convient pour un developpement local ou un petit deploiement, mais ne permet pas le niveau de cloisonnement requis pour une infrastructure critique. OKD apporte :

- L'isolation reseau par namespace (EgressFirewall)
- La gestion des secrets via RBAC
- La haute disponibilite (meme en SNO, les pods sont resilients)
- L'industrialisation via BuildConfig et GitOps

**GPU local vs Cloud**

L'utilisation du GPU NVIDIA Tesla A2 en local (plutot qu'Azure en P9 ou AWS) est un choix de souverainete. Les couts d'inference sont previsibles et ne dependent pas d'un tarif cloud qui peut varier. La contrainte est la limite des 16Go, compensee par l'optimisation des modeles (quantization, vLLM).

**RAG vs Fine-tuning**

Les deux approches ont ete experimentees : le RAG en P7 (LangChain, FAISS) et le fine-tuning en P14 (LoRA, DPO). Le choix pour SophIA est le RAG, car il permet de modifier la base de connaissances sans reentrainer le modele. Le fine-tuning reste une option pour des taches specialisees, via le routage LiteLLM.

**Multi-agents vs monolithe**

L'architecture multi-agents (validee en P13 avec LangGraph) est preferee au monolithe car elle permet de specialiser chaque agent et de limiter l'impact d'une panne. Chaque agent (Dionysos pour le cluster, Hephaistos pour le dev, etc.) est independant et interchangeable.

### 3.3 Hierarchisation des cas d'usage

| Cas d'usage | Valeur | Effort | Priorite |
|---|---|---|---|
| Routage LLM (LiteLLM) | Eleve | Faible | MVP |
| Chat / assistant conversationnel | Eleve | Moyen | MVP |
| RAG sur documents internes | Eleve | Moyen | V2 |
| Agent supervision cluster (Dionysos) | Moyen | Eleve | V3 |
| Deploiement automatise (Hephaistos) | Moyen | Eleve | V3 |
| Automatisation n8n | Faible | Moyen | V4 |

---

## 4. Strategie de mise en oeuvre et d'industrialisation

### 4.1 Roadmap

**Phase MVP (Realisee)**

- Cluster OKD SNO bare-metal operationnel
- LiteLLM routeur avec modeles locaux (Mistral, Qwen)
- Hermes orchestrateur d'agents
- 5 agents du Pantheon fonctionnels
- Authentification WireGuard

**Phase V2 (En cours)**

- RAG avec Qdrant et pipeline d'ingestion
- Dashboard portfolio (projets-perso/Dashboard)
- Site vitrine SophIA (sophia.kisai.fr)
- Rapport de conduite de projet

**Phase V3 (Planifiee)**

- Agent Dionysos pour la supervision automatisee du cluster
- Agent Hephaistos pour la creation de pods de dev
- CI/CD industrialise avec BuildConfig
- Tests automatises dans sophia-test

**Phase V4 (Vision)**

- Automatisation n8n pour les workflows metier
- Outils MCP pour l'integration IDE
- Agent Athena pour la gestion RBAC
- Agent Ouranos pour le deploiement HITL en production

### 4.2 Industrialisation

**CI/CD et GitOps**

La chaine CI/CD s'appuie sur Forgejo (instance Git auto-hebergee dans le cluster) et les BuildConfig OKD. Chaque agent est defini par un Dockerfile et deploye via GitOps. Cette approche a ete validee en P5 (GitHub Actions vers HF Spaces) et P10 (Tekton/ArgoCD).

**Tests et qualite**

Trois niveaux de tests sont prevus :

1. Tests unitaires (pytest) pour les fonctions metier (valide en P5)
2. Tests API (FastAPI TestClient) pour les endpoints (valide en P5, P13)
3. Tests d'integration dans le namespace sophia-sandbox

### 4.3 Risques et opportunites

**Risques identifies :**

| Risque | Probabilite | Impact | Mitigation |
|---|---|---|---|
| Panne GPU | Faible | Critique | Monitoring Prometheus, alerting |
| Coupure electrique | Moyenne | Eleve | Alimentation stabilisee, sauvegardes |
| Obsolescence modele | Eleve | Moyen | Agnostisme LiteLLM, mise a jour reguliere |
| Securite (breche) | Faible | Critique | EgressFirewall, RBAC, audits reguliers |

**Opportunites :**

- Independance technologique totale
- Cout d'inference maitrise (pas de taxe cloud)
- Capitalisation sur les 15 projets de formation
- Positionnement unique sur le marche (AI Platform souveraine)

### 4.4 Estimation budgetaire

| Poste | Cout estime |
|---|---|
| GPU NVIDIA Tesla A2 (acquisition) | ~2000EUR |
| Serveur bare-metal | ~1500EUR |
| Alimentation, refroidissement | ~50EUR/mois |
| Stockage SSD | ~200EUR |
| Abonnements (domaine, email) | ~50EUR/an |
| Cout cloud equivalent (API GPT-4, 1M tokens/jour) | ~300EUR/mois |

L'investissement initial est amorti en moins d'un an par rapport a une solution cloud equivalente. Le cout marginal de l'inference est proche de zero une fois l'infrastructure en place.

### 4.5 KPIs

| KPI | Cible | Mesure |
|---|---|---|
| Disponibilite du cluster | 99.5% | Uptime Prometheus |
| Temps de reponse inference | < 5s | Latence LiteLLM |
| Taux d'utilisation GPU | 60-80% | Grafana / nvidia-smi |
| Temps de deploiement agent | < 10min | BuildConfig duration |
| Couverture de tests | > 80% | pytest --cov |

---

## 5. Controle et suivi du projet

### 5.1 Methodologie de gestion de projet

Le projet est gere selon une methodologie Kanban/Scrum hybride, adaptee au travail en solo :

- **Backlog** : tickets Forgejo dans le depot sophia-platform
- **Sprints** : jalons definis dans le plan d'action (/mnt/memory/PLAN_ACTION.md)
- **Revues** : validation des livrables a chaque fin de phase

Cette approche a ete eprouvee tout au long des 15 projets de la formation, avec une planification adaptee a la charge de travail (804 heures validees sur 804 heures prevues).

### 5.2 Outils de suivi

| Outil | Usage |
|---|---|
| Prometheus + Grafana | Monitoring infrastructure, alerting |
| RAGAS | Evaluation de la qualite des reponses RAG |
| Logs Hermes | Traabilite des echanges avec les agents |
| Dashboard React | Suivi des competences et progression (projets-perso/Dashboard) |

### 5.3 Tests et validation

**Environnement de test :**

- Namespace sophia-sandbox (cluster OKD) pour le developpement
- Tests unitaires avec pytest (bibliotheque installee dans le Dashboard)
- Tests API sur les endpoints des agents

**Procedure de validation :**

1. Developpement dans sophia-sandbox
2. Tests unitaires et integration
3. Revue de code (auto-revue via les regles .rules.md)
4. Deploiement en production (sophia-core, sophia-apps)

---

## 6. Conclusion et recommandations

### 6.1 Resume des choix cles

Le projet SophIA demontre la faisabilite d'une plateforme d'orchestration d'agents IA entierement souveraine, sur infrastructure bare-metal, sans dependance cloud. Les choix architecturaux (OKD SNO, LiteLLM, Qdrant, multi-agents) sont le fruit d'une progression pedagogique de 804 heures a travers 15 projets.

Les trois livrables du portfolio sont operationnels :

1. **Projet technique** : SophIA, deployee sur le cluster OKD avec 5 agents (site vitrine : sophia.kisai.fr)
2. **Carte mentale** : Integree dans le Dashboard React, egalement disponible en Markdown
3. **Portfolio en ligne** : Dashboard React deploye sur GitHub Pages, presentant l'ensemble des 15 projets

### 6.2 Perspectives d'evolution

Les axes d'amelioration identifies dans la carte mentale sont :

- **Cloud natif** : AWS SageMaker, Azure ML, Google Vertex AI (pour les entreprises qui preferent le cloud)
- **MLOps avance** : Kubeflow, DVC, Feature Store (pour industrialiser davantage)
- **LLMs** : Fine-tuning multimodal, MCP (Model Context Protocol)
- **Monitoring** : Data Drift en production, dashboards de performance

### 6.3 Prochaines etapes

1. Finaliser le rapport de conduite de projet (ce document)
2. Preparer la soutenance (presentation orale)
3. Soumettre les livrables pour validation
4. Postuler aux postes de Head of AI Platform avec ce portfolio

### 6.4 Recommandations

Pour toute organisation souhaitant internaliser une plateforme IA souveraine, la demarche proposee est :

1. **Auditer** les besoins et les flux de donnees existants
2. **Architecturer** une solution adaptee au contexte (OKD, RAG, agents)
3. **Industrialiser** avec CI/CD, monitoring et gouvernance
4. **Former** les equipes internes a la maintenance et a l'evolution
5. **Controler** avec des KPIs et un tableau de bord de pilotage

---

## 7. Annexes

### 7.1 Liens vers les livrables

- [Site vitrine SophIA](https://sophia.kisai.fr) -- Projet technique personnel
- [Dashboard Portfolio](https://kisai-dg-slu.github.io) -- Portfolio en ligne (source : projets-perso/Dashboard)
- [Depot SophIA](https://forge-sophia.kisai.fr/projets-clients/sophia-website) -- Code source du site vitrine
- [Depot plateforme SophIA](https://forge-sophia.kisai.fr/projets-clients/sophia-platform) -- Code source de la plateforme

### 7.2 Diagramme de progression des competences

```mermaid
mindmap
  root((P15 Portfolio))
    Fondamentaux (P1-P3)
      Git & Python
      API IA (SegFormer)
      ML supervise
    ML & MLOps (P4-P8)
      XGBoost / SHAP
      FastAPI / MLflow
      RAG / Docker
      Data Drift
    Vision strategique (P9-P11)
      Azure / ROI
      Deep Learning
      Reinforcement Learning
    Architecture (P12-P14)
      Airflow / OKD
      LangGraph / Agents
      Fine-tuning LLM
    Synthese (P15)
      SophIA multi-agents
      Dashboard Portfolio
      Rapport conduite projet
```

### 7.3 Glossaire des acronymes

| Acronyme | Signification |
|---|---|
| OKD | Origin Community Distribution (OpenShift) |
| SNO | Single Node OpenShift |
| HITL | Human In The Loop |
| RAG | Retrieval Augmented Generation |
| MCP | Model Context Protocol |
| RBAC | Role Based Access Control |
| SCOS | Single Common Operating System |
| MLOps | Machine Learning Operations |
| LLM | Large Language Model |
| vLLM | Virtual LLM (serveur d'inference) |
| LoRA | Low Rank Adaptation |
| DPO | Direct Preference Optimization |

---

*Document redige en juin 2026 dans le cadre de la formation AI Engineer (Projet 15).*

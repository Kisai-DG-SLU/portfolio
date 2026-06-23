---
marp: true
theme: gaia
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Montserrat:wght@600;700;800&display=swap');

  :root {
    --bg: #fdfbf7;
    --text: #2d3436;
    --primary: #2c3e50;
    --accent: #6c5ce7;
    --orange: #E65100;
  }

  section {
    background: var(--bg);
    color: var(--text);
    font-family: 'Lato', sans-serif;
    padding: 48px 64px;
  }

  h1 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    color: var(--primary);
  }

  h2 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: var(--accent);
    font-size: 36px;
  }

  h3 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    color: var(--primary);
  }

  strong { color: var(--primary); }

  a { color: var(--accent); }

  .lead h1 {
    font-size: 56px;
    margin-bottom: 8px;
  }

  .lead h2 {
    font-size: 28px;
    color: var(--accent);
  }

  .lead p {
    font-size: 20px;
    color: var(--text);
    opacity: 0.75;
  }

  .lead footer {
    position: absolute;
    bottom: 48px;
    left: 64px;
    font-size: 14px;
    color: var(--text);
    opacity: 0.5;
  }

  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 32px;
  }

  .columns-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
  }

  .card {
    background: white;
    border-radius: 8px;
    padding: 20px;
    border-left: 4px solid var(--accent);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }

  .card h3 {
    margin-top: 0;
    font-size: 18px;
  }

  .card p, .card ul {
    font-size: 15px;
    margin: 8px 0;
  }

  .card ul {
    padding-left: 18px;
  }

  .tag {
    display: inline-block;
    background: var(--accent);
    color: white;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 700;
    margin-right: 4px;
  }

  .tag-orange {
    background: var(--orange);
  }

  .tag-primary {
    background: var(--primary);
  }

  blockquote {
    border-left: 4px solid var(--accent);
    margin: 16px 0;
    padding: 12px 20px;
    background: rgba(108,92,231,0.06);
    border-radius: 0 8px 8px 0;
    font-style: italic;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
  }

  th {
    background: var(--primary);
    color: white;
    padding: 8px 12px;
    text-align: left;
  }

  td {
    padding: 6px 12px;
    border-bottom: 1px solid #eee;
  }

  .emoji-large {
    font-size: 40px;
    display: block;
    margin-bottom: 12px;
  }

  section::after {
    font-size: 12px;
    color: var(--text);
    opacity: 0.3;
  }
---

<!--
Note: Slide d'ouverture. Parler 1 min. Capter l'attention.
Présenter SophIA comme l'aboutissement de 15 projets et 1608h de formation.
Annoncer le plan : contexte, portfolio, architecture, gestion de projet, bilan.

CHALLENGE: Objectif pro. Si Charlotte demande "où vous voyez-vous dans 3 ans ?",
répondre Head of AI Platform avec les mots : "encadrer, challenger et guider 
les équipes d'ingénierie".
-->

<!-- _class: lead -->

# **SophIA**
## Portfolio AI Engineer

Damien Guesdon · P15 AI Engineer · Juin 2026

<footer>OpenClassrooms · Formation AI Engineer · 1608 heures · 15 projets</footer>

---

<!--
Note: 1 min 30. Contextualiser le marché de l'IA.
"Les entreprises découvrent ChatGPT et injectent leurs brevets sur des serveurs 
étrangers sans gouvernance. C'est le phénomène Shadow AI."
La problématique n'est pas de "faire de l'IA" mais de le faire en maîtrisant
sa souveraineté.

CHALLENGE: Choix OKD vs cloud. Justifier : OKD SNO bare-metal = souveraineté,
coût maîtrise, isolation network. Le cloud aurait été plus simple mais 
n'aurait pas répondu au besoin de cloisonnement.
-->

## Contexte & Problématique

<span class="tag">Shadow AI</span> <span class="tag tag-orange">Souveraineté</span> <span class="tag tag-primary">Air-gap</span>

<div class="columns" style="margin-top: 24px;">
<div class="card">
<h3>Le constat</h3>
<ul>
<li>Adoption massive de l'IA générative via SaaS</li>
<li>PI injectée sur des serveurs étrangers sans contrôle</li>
<li>Besoin : souveraineté technologique, pas "faire de l'IA"</li>
</ul>
</div>
<div class="card">
<h3>La réponse SophIA</h3>
<ul>
<li>Plateforme multi-agents souveraine</li>
<li>Déployée sur OKD SNO bare-metal avec GPU Tesla A2</li>
<li>Aucune donnée ne quitte l'infrastructure</li>
</ul>
</div>
</div>

<blockquote>
"Ce qui distingue un architecte de plateforme d'un data scientist, c'est la capacité 
à orchestrer toute la chaîne, de la collecte du besoin au monitoring en production."
</blockquote>

---

<!--
Note: 2 min. Parcourir la progression. Montrer la montée en compétence.
Tous les projets ne sont pas listes ici volontairement.
"De P1 à P15, chaque projet a apporté une brique qui trouve sa place 
dans l'architecture finale de SophIA."
Ne pas lire le tableau, le commenter.

CHALLENGE: Apport du portfolio. Le portfolio ne montre pas seulement les compétences,
il démontre la capacité à les intégrer dans un ensemble cohérent.
C'est la différence entre "j'ai fait 15 projets" et "voici comment ils construisent
une vision".
-->

## Les 15 Projets Fondateurs

<span class="tag">P1-P3</span> Fondamentaux <span class="tag tag-orange">P4-P8</span> ML & MLOps
<span class="tag tag-primary">P9-P11</span> Vision stratégique <span class="tag">P12-P14</span> Architecture

<div class="columns" style="margin-top: 20px;">
<div>

| Projets | Acquis |
|---|---|
| P7 RAG | LangChain, FAISS, embeddings |
| P8 MLOps | Evidently, NannyML, drift |
| P12 Airflow | ETL sur OKD |
| P13 Agents | LangGraph, MCP |
| P14 Fine-tuning | LoRA, vLLM, Presidio |

</div>
<div class="card" style="border-left-color: var(--orange);">
<h3>1608 heures de formation</h3>
<p>804 h supervisées + 804 h guidées</p>
<p>Chaque brique de SophIA a été expérimentée dans un projet précédent :</p>
<ul>
<li>RAG / Qdrant → P7</li>
<li>Déploiement OKD → P12</li>
<li>Orchestration agentique → P13</li>
<li>Inférence LLM locale → P14</li>
</ul>
</div>
</div>

---

<!--
Note: 2 min. Montrer le portfolio. Parler du Dashboard React, de la carte mentale,
de la façon dont les compétences sont organisées.
"Le portfolio ne se limite pas à une liste de projets. C'est un écosystème 
qui montre la progression, les liens entre les compétences, et la capacité
de synthèse."
Si possible, montrer les URLs rapidement.

CHALLENGE: Évolution du métier. "L'AI Engineer d'aujourd'hui ne peut plus 
se contenter d'entraîner des modèles. Il doit maîtriser l'infrastructure,
la sécurité, le coût, et la gouvernance. C'est exactement ce que ce portfolio 
démontre."
-->

## Portfolio & Compétences

<div class="columns-3" style="margin-top: 20px;">
<div class="card">
<h3>Dashboard React</h3>
<p>Portfolio en ligne déployé sur GitHub Pages</p>
<p><a href="https://kisai-dg-slu.github.io">kisai-dg-slu.github.io</a></p>
<p>15 projets présentés avec progression visible</p>
</div>
<div class="card" style="border-left-color: var(--orange);">
<h3>Carte Mentale</h3>
<p>Compétences hard skills et soft skills</p>
<p>Liens entre les projets et l'architecture SophIA</p>
<p>Axes d'amélioration identifiés</p>
</div>
<div class="card">
<h3>Site Vitrine</h3>
<p>Plateforme SophIA en ligne</p>
<p><a href="https://sophia.kisai.fr">sophia.kisai.fr</a></p>
<p>Point d'entrée de la plateforme agentique</p>
</div>
</div>

<blockquote>
"L'objectif professionnel est clair : encadrer, challenger et guider les équipes 
d'ingénierie en tant que Head of AI Platform."
</blockquote>

---

<!--
Note: 2 min. C'est le cœur technique. Expliquer l'architecture OKD,
les 9 namespaces, les 5 agents du Pantheon.
Ne pas entrer dans les détails de chaque namespace.
"9 namespaces organisés en zones fonctionnelles : usine, cerveau, 
air-gappee, SAS, outils, frontend, dev."

CHALLENGE: Gestion de projet solo. "Oui, c'est un projet solo. Mais l'architecture 
a été pensée comme si c'était une équipe : chaque agent est indépendant, 
chaque namespace isolé. C'est une architecture industrielle, pas un POC."
-->

## Architecture SophIA

<div class="columns" style="margin-top: 20px;">
<div>

### Cluster OKD SNO

- GPU NVIDIA Tesla A2 (16 Go)
- 9 namespaces isolés
- Air-gap : pas d'accès sortant pour les zones critiques
- EgressFirewall par namespace

</div>
<div>

### Pantheon Agentique

| Agent | Role |
|---|---|
| **Hermes** | Orchestrateur central |
| **Dionysos** | Supervision cluster |
| **Hephaistos** | Développement |
| **Athena** | RBAC / HITL |
| **Ouranos** | Production HITL |

</div>
</div>

<div class="card" style="margin-top: 12px; border-left-color: var(--orange);">

**Stack** : OKD SNO · LiteLLM · Qdrant · Prometheus · Grafana · Forgejo

</div>

---

<!--
Note: 1 min 30. Expliquer la démarche de gestion de projet.
Montrer la rigueur : backlog, sprints, KPIs, budget.
"Je ne me suis pas contente de développer. J'ai géré le projet comme on gère 
une plateforme en production."
Ne pas lire les chiffres, les commenter.

CHALLENGE: Gestion de projet solo (bis). "Le risque du solo, c'est le manque
de regard critique. Je l'ai compensé par des outils de monitoring,
des tests systématiques, et une documentation rigoureuse."
-->

## Gestion de Projet

<div class="columns" style="margin-top: 20px;">
<div class="card">
<h3>Méthodologie</h3>
<ul>
<li>Kanban/Scrum hybride adapté au solo</li>
<li>Backlog tickets Forgejo</li>
<li>Sprints par phase (V1 à V4)</li>
</ul>
</div>
<div class="card">
<h3>KPIs</h3>
<ul>
<li>Disponibilité cluster : 99.5%</li>
<li>Temps de réponse inférence : &lt;5s</li>
<li>Utilisation GPU : 60-80%</li>
<li>Couverture tests : &gt;80%</li>
</ul>
</div>
</div>

<div class="columns" style="margin-top: 12px;">
<div class="card" style="border-left-color: var(--orange);">
<h3>Budget</h3>
<p><strong>Investissement initial :</strong> ~3700 EUR (GPU + serveur + stockage)</p>
<p><strong>Coût mensuel :</strong> ~50 EUR (électricité, refroidissement)</p>
<p><strong>Économie vs cloud :</strong> ~300 EUR/mois (équivalent API GPT-4)</p>
<p>Amorti en moins d'un an</p>
</div>
<div class="card" style="border-left-color: var(--primary);">
<h3>Roadmap</h3>
<ul>
<li><strong>MVP</strong> : Cluster OKD, LiteLLM, 5 agents ✓</li>
<li><strong>V2</strong> : RAG, Dashboard, site vitrine ← en cours</li>
<li><strong>V3</strong> : Agents Dionysos/Hephaistos, CI/CD</li>
<li><strong>V4</strong> : n8n, MCP, Athena, Ouranos</li>
</ul>
</div>
</div>

---

<!--
Note: 1 min 30. Bilan critique. Montrer qu'on a du recul.
"Forces : souveraineté, coût, sécurité. Faiblesses : complexité, GPU contraint, 
documentation à renforcer."
Ce slide est important pour la réflexivité.

CHALLENGE: Axes d'amélioration. Charlotte va demander "que feriez-vous mieux?"
Répondre : (1) schéma C4 unifié dès l'origine, (2) tests plus tôt dans le cycle,
(3) documentation API systématique. Montrer qu'on a identifié ces points 
et qu'on les traite dans V3.
-->

## Résultats & Bilan Critique

<div class="columns" style="margin-top: 20px;">
<div class="card">
<h3>Forces</h3>
<ul>
<li>Souveraineté totale : aucune donnée ne quitte le cluster</li>
<li>Agnostisme LLM (Mistral, Llama, Qwen interchangeables)</li>
<li>Sécurité : isolation network par namespace</li>
<li>Coût maîtrise : pas de dépendance cloud</li>
</ul>
</div>
<div class="card" style="border-left-color: var(--orange);">
<h3>Axes d'amélioration</h3>
<ul>
<li>Complexité de maintenance du cluster bare-metal</li>
<li>GPU contraint (16 Go non fractionnables)</li>
<li>Documentation : schéma C4 à unifier</li>
<li>Tests à intégrer plus tôt dans le cycle</li>
</ul>
</div>
</div>

<blockquote>
"La réflexivité, c'est reconnaître que la complexité OKD est un coût 
et à l'assumer comme un choix de souveraineté."
</blockquote>

---

<!--
Note: 1 min 30. Vision et perspectives. Montrer la roadmap.
"SophIA ne s'arrête pas à la V2. V3 apporte la supervision automatisée 
du cluster, V4 l'industrialisation complète."
Conclure sur l'objectif professionnel.

CHALLENGE: Évolution du métier (approfondir). "Le métier d'AI Engineer évolue
vers plus de DevOps et de SecOps. Dans 3 ans, un AI Engineer devra savoir
déployer, sécuriser et monitorer sa plateforme. C'est là que je positionne SophIA."
-->

## Roadmap & Perspectives

<div class="columns-3" style="margin-top: 20px;">
<div class="card">
<h3>V3 · Supervision</h3>
<ul>
<li>Dionysos : supervision automatisée du cluster</li>
<li>Hephaistos : pods de dev à la demande</li>
<li>CI/CD BuildConfig industrialisé</li>
</ul>
</div>
<div class="card" style="border-left-color: var(--orange);">
<h3>V4 · Industrialisation</h3>
<ul>
<li>n8n workflows métier</li>
<li>Outils MCP pour intégration IDE</li>
<li>Athena RBAC et Ouranos HITL</li>
</ul>
</div>
<div class="card" style="border-left-color: var(--primary);">
<h3>Objectif Pro</h3>
<p><strong>Head of AI Platform</strong></p>
<p>Encadrer, challenger et guider les équipes d'ingénierie</p>
<p>Concevoir et industrialiser des plateformes IA souveraines</p>
</div>
</div>

---

<!--
Note: 30 sec. Conclusion rapide. Remercier. Ouvrir les questions.
"Voilà pour cette présentation. Je suis disponible pour vos questions 
et pour approfondir les points qui vous intéressent."

CHALLENGE: Prep pour les 10 min de discussion. Les 6 axes sont couverts 
dans les slides précédentes. Charlotte peut revenir sur n'importe lequel.
-->

<!-- _class: lead -->

# Merci

## Questions & Discussion

<footer>Damien Guesdon · sophia.kisai.fr · github.com/Kisai-DG-SLU/portfolio</footer>

---
marp: true
theme: gaia
paginate: true
backgroundImage: url('images/background.png')
style: |
  @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Montserrat:wght@600;800&display=swap');

  :root {
    --color-bg: #fdfbf7;
    --color-text: #2d3436;
    --color-primary: #2c3e50;
    --color-accent: #6c5ce7;
    --color-orange: #E65100;
  }

  section {
    font-family: 'Lato', sans-serif;
    font-size: 24px;
    color: var(--color-text);
    background-color: var(--color-bg);
  }

  h1, h2, h3, h4 {
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    width: 100%;
  }

  h1, h2, h3 {
    text-transform: uppercase;
    letter-spacing: -1px;
  }

  section:not(.lead) h1 {
    font-size: 1.3em;
    color: var(--color-primary);
    border-bottom: 3px solid var(--color-accent);
    padding-bottom: 10px;
    margin-bottom: 40px;
    margin-top: 0;
  }

  section.lead h1 {
    font-size: 2.5em;
    color: var(--color-primary);
    border: none;
    margin-bottom: 10px;
    line-height: 1.1;
  }

  h2 {
    font-size: 0.9em;
    color: var(--color-orange);
    margin-top: 0;
    margin-bottom: 20px;
  }

  h3 {
    font-size: 0.9em;
    color: var(--color-primary);
    margin-bottom: 15px;
  }

  h4 {
    font-size: 1.05em;
    color: var(--color-primary);
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 30px;
  }

  h4 strong {
    color: var(--color-orange);
    font-weight: 800;
  }

  section::before {
    content: ' ';
    position: absolute;
    top: 10px;
    left: 10px;
    width: 90px;
    height: 90px;
    background-image: url('images/logo-sophia.svg');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.8;
  }

  .intro-text-left {
    position: absolute;
    bottom: 40px;
    left: 70px;
    text-align: left;
    font-size: 0.9em;
    color: var(--color-text);
    z-index: 10;
  }

  .columns {
    display: grid;
    grid-template-columns: 40% 60%;
    gap: 0;
    width: 100%;
  }
  .columns div {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 30px;
  }
  .columns div:last-child {
    border-left: 2px solid #dcdde1;
  }

  .staff-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    margin-bottom: 30px;
    width: 100%;
  }
  .staff-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .staff-item {
    margin-bottom: 12px;
    display: flex;
    align-items: center;
  }

  .center-img {
    display: block;
    margin: 0 auto;
    text-align: center;
  }
  .center-img img {
    max-height: 250px;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }

  .tech-comparison {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 100%;
    margin-top: 20px;
  }
  .tech-header {
    padding: 15px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 1.1em;
    text-align: center;
  }
  .header-a {
    background-color: #d1e8e2;
    color: #2c3e50;
    border-right: 2px solid #2d3436;
  }
  .header-b {
    background-color: #bdc3c7;
    color: #2c3e50;
  }
  .tech-body {
    padding: 30px;
    display: flex;
    flex-direction: column;
    gap: 25px;
  }
  .tech-item {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  .tech-item span {
    font-size: 0.9em;
    line-height: 1.2;
  }
  .border-right {
    border-right: 2px solid #2d3436;
  }

  .rgpd-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 30px;
    margin-top: 40px;
    margin-bottom: 40px;
    text-align: center;
  }
  .rgpd-col {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .rgpd-title {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1em;
    font-weight: 800;
    margin-bottom: 15px;
    color: var(--color-orange);
  }
  .rgpd-text {
    font-size: 0.9em;
    line-height: 1.3;
    color: #2d3436;
  }

  .check-item {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
    text-align: left;
  }
  .check-icon {
    width: 55px;
    height: auto;
    margin-right: 20px;
    flex-shrink: 0;
  }
  .check-text {
    font-size: 1em;
    line-height: 1.2;
    color: #000;
  }

  .validation-box {
    border: 4px solid #ff8a65;
    background: linear-gradient(to bottom right, #ffffff, #fbe9e7);
    padding: 30px 20px;
    box-shadow: 0 10px 25px rgba(255, 138, 101, 0.3);
    text-align: center;
    color: #000;
    margin-bottom: 30px;
  }

  .footer-logo-block {
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .logo-fin {
    width: 280px;
    margin-bottom: 10px;
  }
  .brand-text {
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-size: 0.8em;
    color: #2c3e50;
  }

  .rgpd-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-top: 20px;
    margin-bottom: 20px;
    text-align: center;
  }

  ul {
    text-align: left;
    font-size: 0.85em;
    line-height: 1.4;
  }

  li {
    margin-bottom: 8px;
  }

  table {
    font-size: 0.7em;
    width: 100%;
    border-collapse: collapse;
    text-align: left;
  }
  th {
    background: var(--color-primary);
    color: white;
    padding: 6px 10px;
  }
  td {
    padding: 4px 10px;
    border-bottom: 1px solid #ddd;
  }

  blockquote {
    border-left: 4px solid var(--color-accent);
    margin: 16px 0;
    padding: 8px 16px;
    background: rgba(108,92,231,0.06);
    font-style: italic;
    font-size: 0.75em;
    text-align: left;
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

<div class="intro-text-left">
  <strong>Damien GUESDON</strong><br>
  AI Engineer<br>
  OpenClassrooms · Juin 2026<br>
  1608 heures · 15 projets
</div>

---

<!--
Note: 1 min 30. Contextualiser le marché de l'IA.
"Les entreprises découvrent ChatGPT et injectent leurs brevets sur des serveurs
étrangers sans gouvernance. C'est le phénomène Shadow AI."
La problématique n'est pas de "faire de l'IA" mais de le faire en maîtrisant
sa souveraineté.

CHALLENGE: Choix OKD vs cloud. Justifier : OKD SNO bare-metal = souveraineté,
coût maîtrisé, isolation réseau. Le cloud aurait été plus simple mais
n'aurait pas répondu au besoin de cloisonnement.
-->

# 1. Contexte & Problématique

#### **Le constat :** Shadow AI et besoin de <strong>souveraineté technologique</strong>

<div class="staff-grid">
  <div>
    <h3>Le phénomène Shadow AI</h3>
    <ul>
      <li>Adoption massive de l'IA générative via SaaS (ChatGPT, Copilot)</li>
      <li>PI injectée sur des serveurs étrangers sans contrôle</li>
      <li>Aucune gouvernance des données sensibles</li>
    </ul>
  </div>
  <div>
    <h3>La réponse SophIA</h3>
    <ul>
      <li>Plateforme multi-agents souveraine sur OKD SNO bare-metal</li>
      <li>GPU NVIDIA Tesla A2 (16 Go) — air-gap total</li>
      <li>Aucune donnée ne quitte l'infrastructure</li>
    </ul>
  </div>
</div>

<blockquote>
"Ce qui distingue un architecte de plateforme d'un data scientist, c'est la capacité à orchestrer toute la chaîne, de la collecte du besoin au monitoring en production."
</blockquote>

---

<!--
Note: 2 min. Parcourir la progression. Montrer la montée en compétence.
"De P1 à P15, chaque projet a apporté une brique qui trouve sa place
dans l'architecture finale de SophIA."

CHALLENGE: Apport du portfolio. Le portfolio ne montre pas seulement les compétences,
il démontre la capacité à les intégrer dans un ensemble cohérent.
-->

# 2. Les 15 Projets Fondateurs

#### **1608 heures de formation — <strong>804 h supervisées + 804 h guidées</strong>

<div class="staff-grid">
  <div>
    <h3>Briques clés de SophIA</h3>
    <table>
      <tr><th>Brique</th><th>Projet source</th></tr>
      <tr><td>RAG / Qdrant</td><td>P7 — Système RAG</td></tr>
      <tr><td>Déploiement OKD</td><td>P12 — CheckIt.AI</td></tr>
      <tr><td>Orchestration agents</td><td>P13 — Chess Master</td></tr>
      <tr><td>Inférence LLM locale</td><td>P14 — CHSA PosoLogic</td></tr>
      <tr><td>Monitoring / drift</td><td>P8 — MLOps avancé</td></tr>
    </table>
  </div>
  <div>
    <h3>Notions acquises</h3>
    <ul>
      <li><strong>P1-P3</strong> : Python, Git, API IA, ML supervisé</li>
      <li><strong>P4-P6</strong> : XGBoost, FastAPI, MLflow, SHAP</li>
      <li><strong>P7-P8</strong> : LangChain, Docker, Evidently, Ragas</li>
      <li><strong>P9-P11</strong> : Azure, Deep Learning, RL</li>
      <li><strong>P12-P14</strong> : Airflow, LangGraph, LoRA, vLLM</li>
    </ul>
  </div>
</div>

---

<!--
Note: 2 min. Montrer le portfolio. Parler du Dashboard React, de la carte mentale,
de la façon dont les compétences sont organisées.

CHALLENGE: Évolution du métier. "L'AI Engineer d'aujourd'hui doit maîtriser
l'infrastructure, la sécurité, le coût et la gouvernance."
-->

# 3. Portfolio & Compétences

#### **Trois livrables opérationnels — <strong>Objectif : Head of AI Platform</strong>

<div class="rgpd-grid">
  <div class="rgpd-col">
    <div class="rgpd-title">Dashboard React</div>
    <div class="rgpd-text">Portfolio en ligne déployé sur GitHub Pages<br><br>
      <a href="https://kisai-dg-slu.github.io">kisai-dg-slu.github.io</a><br><br>
      15 projets avec progression visible
    </div>
  </div>
  <div class="rgpd-col">
    <div class="rgpd-title">Carte Mentale</div>
    <div class="rgpd-text">Compétences hard skills et soft skills<br><br>
      Liens entre projets et architecture SophIA<br><br>
      Axes d'amélioration identifiés
    </div>
  </div>
  <div class="rgpd-col">
    <div class="rgpd-title">Site Vitrine</div>
    <div class="rgpd-text">Plateforme SophIA en ligne<br><br>
      <a href="https://sophia.kisai.fr">sophia.kisai.fr</a><br><br>
      Point d'entrée de la plateforme agentique
    </div>
  </div>
</div>

<blockquote>
"L'objectif professionnel : encadrer, challenger et guider les équipes d'ingénierie en tant que Head of AI Platform."
</blockquote>

---

<!--
Note: 2 min. C'est le cœur technique. Expliquer l'architecture OKD,
les 9 namespaces, les 5 agents du Pantheon.

CHALLENGE: Gestion de projet solo. "L'architecture a été pensée comme si
c'était une équipe : chaque agent est indépendant, chaque namespace isolé.
C'est une architecture industrielle, pas un POC."
-->

# 4. Architecture SophIA

#### **Cluster OKD SNO bare-metal — <strong>GPU NVIDIA Tesla A2</strong>

<div class="staff-grid">
  <div>
    <h3>9 namespaces isolés</h3>
    <ul>
      <li><strong>sophia-git</strong> : Forgejo, CI/CD (seule zone avec accès sortant)</li>
      <li><strong>sophia-core</strong> : Hermes, LiteLLM, orchestration</li>
      <li><strong>sophia-inference</strong> : Inférence LLM (air-gap)</li>
      <li><strong>sophia-memory</strong> : Qdrant, pipeline RAG</li>
      <li><strong>sophia-dmz</strong> : Point d'entrée utilisateur</li>
      <li><strong>sophia-skills</strong> : Outils MCP, TTS</li>
      <li><strong>sophia-apps</strong> : Frontends</li>
      <li><strong>sophia-sandbox</strong> : Développement</li>
      <li><strong>sophia-test</strong> : Tests automatisés</li>
    </ul>
  </div>
  <div>
    <h3>Pantheon Agentique</h3>
    <table>
      <tr><th>Agent</th><th>Rôle</th></tr>
      <tr><td><strong>Hermes</strong></td><td>Orchestrateur central</td></tr>
      <tr><td><strong>Dionysos</strong></td><td>Supervision cluster</td></tr>
      <tr><td><strong>Hephaistos</strong></td><td>Développement</td></tr>
      <tr><td><strong>Athena</strong></td><td>RBAC / HITL</td></tr>
      <tr><td><strong>Ouranos</strong></td><td>Production HITL</td></tr>
    </table>
    <br>
    <p style="font-size:0.75em;"><strong>Stack :</strong> OKD · LiteLLM · Qdrant · Prometheus · Grafana</p>
  </div>
</div>

---

<!--
Note: 1 min 30. Expliquer la démarche de gestion de projet.
Montrer la rigueur : backlog, sprints, KPIs, budget.

CHALLENGE: Gestion de projet solo (bis). "Le risque du solo, c'est le manque
de regard critique. Je l'ai compensé par des outils de monitoring,
des tests systématiques et une documentation rigoureuse."
-->

# 5. Gestion de Projet

#### **Méthodologie Kanban/Scrum hybride — <strong>Roadmap V1 à V4</strong>

<div class="staff-grid">
  <div>
    <h3>KPIs</h3>
    <table>
      <tr><th>KPI</th><th>Cible</th></tr>
      <tr><td>Disponibilité cluster</td><td>99.5%</td></tr>
      <tr><td>Temps réponse inférence</td><td>&lt;5s</td></tr>
      <tr><td>Utilisation GPU</td><td>60-80%</td></tr>
      <tr><td>Couverture tests</td><td>&gt;80%</td></tr>
    </table>
    <br>
    <h3>Budget</h3>
    <ul>
      <li><strong>Investissement :</strong> ~3700 EUR (GPU + serveur)</li>
      <li><strong>Coût mensuel :</strong> ~50 EUR (électricité)</li>
      <li><strong>Économie vs cloud :</strong> ~300 EUR/mois</li>
    </ul>
  </div>
  <div>
    <h3>Roadmap</h3>
    <ul>
      <li><strong>MVP ✓</strong> : Cluster OKD, LiteLLM, 5 agents</li>
      <li><strong>V2 ← en cours</strong> : RAG, Dashboard, site vitrine</li>
      <li><strong>V3</strong> : Dionysos, Hephaistos, CI/CD</li>
      <li><strong>V4</strong> : n8n, MCP, Athena, Ouranos</li>
    </ul>
    <br>
    <h3>Outils de suivi</h3>
    <ul>
      <li>Prometheus + Grafana pour le monitoring</li>
      <li>Backlog Forgejo pour les tickets</li>
      <li>Tests pytest automatisés</li>
    </ul>
  </div>
</div>

---

<!--
Note: 1 min 30. Bilan critique. Montrer qu'on a du recul.
"Forces : souveraineté, coût, sécurité. Faiblesses : complexité, GPU contraint."

CHALLENGE: Axes d'amélioration. Charlotte va demander "que feriez-vous mieux?"
Répondre : (1) schéma C4 unifié dès l'origine, (2) tests plus tôt dans le cycle,
(3) documentation API systématique.
-->

# 6. Résultats & Bilan Critique

#### **Forces et axes d'amélioration — <strong>Réflexivité</strong>

<div class="tech-comparison">
  <div class="tech-header header-a">Forces</div>
  <div class="tech-header header-b">Axes d'amélioration</div>
  <div class="tech-body border-right">
    <div class="tech-item"><span><strong>Souveraineté totale</strong> : aucune donnée ne quitte le cluster</span></div>
    <div class="tech-item"><span><strong>Agnosticisme LLM</strong> : Mistral, Llama, Qwen interchangeables</span></div>
    <div class="tech-item"><span><strong>Sécurité</strong> : isolation réseau par EgressFirewall</span></div>
    <div class="tech-item"><span><strong>Coût maîtrisé</strong> : pas de dépendance cloud</span></div>
  </div>
  <div class="tech-body">
    <div class="tech-item"><span><strong>Complexité</strong> : maintenance d'un cluster bare-metal</span></div>
    <div class="tech-item"><span><strong>GPU contraint</strong> : 16 Go non fractionnables</span></div>
    <div class="tech-item"><span><strong>Documentation</strong> : schéma C4 à unifier</span></div>
    <div class="tech-item"><span><strong>Tests</strong> : à intégrer plus tôt dans le cycle</span></div>
  </div>
</div>

<blockquote>
"La réflexivité, c'est reconnaître que la complexité OKD est un coût et l'assumer comme un choix de souveraineté."
</blockquote>

---

<!--
Note: 1 min 30. Vision et perspectives. Montrer la roadmap.
"SophIA ne s'arrête pas à la V2. V3 apporte la supervision automatisée
du cluster, V4 l'industrialisation complète."

CHALLENGE: Évolution du métier (approfondir). "Le métier d'AI Engineer évolue
vers plus de DevOps et de SecOps. Dans 3 ans, un AI Engineer devra savoir
déployer, sécuriser et monitorer sa plateforme."
-->

# 7. Roadmap & Perspectives

#### **Prochaines étapes — <strong>Objectif : Head of AI Platform</strong>

<div class="rgpd-grid">
  <div class="rgpd-col">
    <div class="rgpd-title">V3 · Supervision</div>
    <div class="rgpd-text">
      Dionysos : supervision automatisée du cluster<br><br>
      Hephaistos : création de pods de dev à la demande<br><br>
      CI/CD BuildConfig industrialisé
    </div>
  </div>
  <div class="rgpd-col">
    <div class="rgpd-title">V4 · Industrialisation</div>
    <div class="rgpd-text">
      n8n pour les workflows métier<br><br>
      Outils MCP pour intégration IDE<br><br>
      Athena RBAC et Ouranos HITL
    </div>
  </div>
  <div class="rgpd-col">
    <div class="rgpd-title">Objectif Pro</div>
    <div class="rgpd-text">
      <strong>Head of AI Platform</strong><br><br>
      Encadrer, challenger et guider<br>les équipes d'ingénierie<br><br>
      Concevoir et industrialiser des plateformes IA souveraines
    </div>
  </div>
</div>

---

<br><br>

<div class="validation-box">
  <h3 style="text-transform:none; color:var(--color-primary); margin:0;">
    Portfolio validé : 15 projets, 1608 heures de formation, une plateforme agentique souveraine déployée sur OKD bare-metal.
  </h3>
</div>

<div class="footer-logo-block">
  <img src="images/logo-sophia.svg" class="logo-fin" alt="Logo SophIA">
  <div class="brand-text">SophIA · Sovereign AI Platform</div>
</div>

<!--
Note: 30 sec. Conclusion rapide. Remercier. Ouvrir les questions.

CHALLENGE: Les 6 axes sont couverts dans les slides précédentes.
Charlotte peut revenir sur n'importe lequel.
-->

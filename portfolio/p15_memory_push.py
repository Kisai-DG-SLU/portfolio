#!/usr/bin/env python3
"""
Memory push: plan action + specs rapport conduite projet
Executed on dev-pod-portfolio in namespace sophia-sandbox.
"""

import json

# P15 memory payload
memory_entry = {
    "id": "P15",
    "type": "plan_action_specs_rapport",
    "timestamp": "2026-06-07T17:22:00Z",
    "project": "portfolio",
    "title": "Plan action + specs rapport conduite projet",
    "details": {
        "plan_objectif": "Mettre en place le plan d'action et les spécifications du rapport de conduite de projet pour le site portfolio sophia-sandbox",
        "etapes": [
            {
                "phase": "1_specs_rapport",
                "description": "Rediger les specs fonctionnelles et techniques du rapport de conduite de projet",
                "delivrables": ["specs_conduite_projet.md", "architecture_technique.md"],
                "statut": "a_lancer"
            },
            {
                "phase": "2_plan_action",
                "description": "Decouper le plan d'action en sprints avec jalons",
                "delivrables": ["plan_action_sprints.md", "jalons_calendrier.md"],
                "statut": "a_lancer"
            },
            {
                "phase": "3_implementation",
                "description": "Implementer les composants selon les specs",
                "delivrables": ["composants_frontend", "api_backend", "tests"],
                "statut": "a_lancer"
            },
            {
                "phase": "4_livraison",
                "description": "Finaliser et livrer le rapport de conduite de projet",
                "delivrables": ["rapport_conduite_projet.pdf", "presentation_soutenance"],
                "statut": "a_lancer"
            }
        ],
        "specs_rapport_contenu": {
            "section_1": "Presentation du projet (contexte, objectifs, perimetre)",
            "section_2": "Methodologie de gestion de projet",
            "section_3": "Architecture technique et choix technologiques",
            "section_4": "Plan d'action detaille et jalons",
            "section_5": "Suivi d'avancement et indicateurs de performance",
            "section_6": "Risques identifies et plans de mitigation",
            "section_7": "Livrables et validation"
        }
    },
    "tags": ["portfolio", "conduite-projet", "plan-action", "specs", "rapport", "P15"]
}

# Write to a known path on the pod
payload = json.dumps(memory_entry, indent=2, ensure_ascii=False)
print(payload)

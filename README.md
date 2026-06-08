# Martificial Souls Template

> Le template d'architecture agentique multi-agents pour solo founders augmentés par l'IA. **9 SOULs + 1 doctrine commune** — la structure exacte qui permet de remplacer une armée d'assistants observateurs par 9 agents qui se parlent et prennent des décisions.

C'est un **template adaptable**, pas une config opérationnelle prête à coller. Les placeholders `{COMPANY_NAME}`, `{PRODUCT_1}`, `{YOUR_LOCATION}` etc. sont à remplacer par ton propre contexte. La valeur n'est pas dans les noms, elle est dans l'architecture en 3 couches et la doctrine anti-hallucination.

## Architecture

```
                    Compass (CEO)
                          |
        ┌─────────────────┼─────────────────┐
        |                 |                 |
   Stewards business  Capacités transverses
   ───────────────    ──────────────────────
   • {COMPANY_NAME}   • Editor    (contenu)
   • {PRODUCT_1}      • Scout     (veille)
   • {BUSINESS_2}     • Builder   (code + SaaS)
   • {BUSINESS_3}     • Bookkeeper (KPIs + santé)
```

**1 chef + N stewards business + N capacités transverses + 1 bus partagé + 1 doctrine non-négociable.** Adapte le nombre de stewards à tes business réels (1, 3, 7, peu importe). Les capacités transverses sont génériques.

## Les 10 fichiers du template

| Fichier | Rôle | Modèle recommandé |
|---|---|---|
| `_AGENT-CORE.md` | Doctrine commune non-négociable. C'est la pièce maîtresse : anti-hallucination stricte, protocole bus inter-agents, règles d'auto-priorisation, loud failure. **À adapter à tes règles métier**, mais garde l'esprit "non-négociable". | — |
| `compass.md` | CEO unique. Voit tout, consolide, route les décisions, écrit le Daily Digest. Tu peux le garder tel quel ou affiner les workflows. | Opus 4.7+ |
| `company-steward-template.md` | Steward du "labo public" / company principale. Exemple générique. | Sonnet 4.6+ |
| `product1-steward-template.md` | Steward d'un produit SaaS. Adapte aux specs de ton produit. | Sonnet 4.6+ |
| `business2-steward-template.md` | Steward d'un 2e business (services, hospitality, etc.). | Sonnet 4.6+ |
| `business3-steward-template.md` | Steward d'un 3e business (artistique, side project, etc.). | Sonnet 4.6+ |
| `editor.md` | Capacité contenu unifiée (newsletter, posts long-form, fanout multi-canal, critic). | Opus 4.7+ |
| `scout.md` | Capacité veille intelligente avec filtre anti-monothématique (Pépite Brief). | Sonnet 4.6+ |
| `builder.md` | Capacité technique (SaaS factory + code generation + veille des frameworks IA). | Opus 4.7+ |
| `bookkeeper.md` | Capacité KPIs + coûts + santé monitoring. Échoue bruyamment. | Haiku 4.5+ |

## Installation rapide (avec Hermes Agent)

```bash
# 1. Clone
git clone https://github.com/martinoh-ai/martificial-souls-template.git
cd martificial-souls-template

# 2. Crée chaque profil Hermes et copie son SOUL
for profile in compass company-steward product1-steward business2-steward business3-steward editor scout builder bookkeeper; do
  mkdir -p ~/.hermes/profiles/$profile
  cp ${profile}-template.md ~/.hermes/profiles/$profile/SOUL.md 2>/dev/null || cp ${profile}.md ~/.hermes/profiles/$profile/SOUL.md
done

# 3. Le CORE doctrine commune, accessible par tous les profils
mkdir -p ~/.hermes/shared
cp _AGENT-CORE.md ~/.hermes/shared/_AGENT-CORE.md

# 4. Remplace les placeholders avec ton vrai contexte
# Liste des placeholders à chercher/remplacer dans chaque SOUL :
#   {COMPANY_NAME}, {PRODUCT_1}, {BUSINESS_2}, {BUSINESS_3}
#   {YOUR_NAME}, {YOUR_FIRST_NAME}, {PARTNER_NAME}, {CHILD_NAME}
#   {YOUR_LOCATION}, {NEARBY_CITY}, {YOUR_REGION}, {NEARBY_MAJOR_CITY}
#   {YOUR_LINKEDIN}, {YOUR_TWITTER}, {YOUR_EMAIL}, {YOUR_DOMAIN}
#   {PREVIOUS_VENTURE}, {PREVIOUS_REVENUE}
#   {TARGET_MRR}, {TARGET_MRR_VALUE}, {TARGET_AUDIENCE_6M}, {TARGET_AUDIENCE_LT}
#   {YOUR_LLM_BUDGET}, {YOUR_BRAIN_REPO}, {YOUR_PROJECT}, {YOUR_PROFILE}

# 5. Crée ton brain canonique
mkdir -p ~/Code/{YOUR_BRAIN_REPO}
# (versionné git, sync GitHub, source de vérité pour tous tes agents)
```

## Les 4 ingrédients qui rendent ce template tenable

Si tu retiens 4 choses de cette doctrine :

1. **Un chef qui consolide tout** (pas N agents qui crient en parallèle vers toi).
2. **Des stewards business qui pensent par activité** (pas par outil).
3. **Un cahier de bord partagé observable** où tous les agents écrivent.
4. **Un document non-négociable** qui définit "tu ne fais jamais ça" (anti-hallucination, anti-invention de chiffres).

Si tu as plus de 10 agents IA qui tournent chez toi et qu'il te manque ces 4 éléments, tu n'as pas une équipe IA. Tu as 10 personnes qui crient dans ta cuisine. Et toi tu fais le standard téléphonique au milieu.

## Le brain canonique

Cette architecture suppose que tu maintiens un **brain canonique** : un dossier de docs versionnés que tous tes agents lisent au démarrage. Recommandation :

- `STRATEGY.md` : ton plan business + KPIs
- `{YOUR_PROFILE}.md` : qui tu es, ton ton, tes audiences
- `identity/tone-of-voice.md` : voix attendue dans tes contenus
- `identity/anti-patterns-ia.md` : tout ce qu'un LLM ne doit JAMAIS écrire pour toi (chiffres inventés, anglicismes, em-dashes, etc.)
- `frameworks/` : tes scoring, tes hooks, tes templates copywriting
- `knowledge/objectifs-2026.md` (ou similaire) : tes cibles trimestrielles chiffrées

Le brain est ta source de vérité. Les SOULs sont les exécutants qui le lisent.

## Pourquoi un template plutôt qu'une config

Cette architecture vient de l'expérience réelle d'un opérateur solo (Martin Ohannessian, voir contact) qui pilote 4 business avec une équipe d'agents IA. La config originale contenait des KPIs, pricings, et stratégies business privées. Ce template offre **l'architecture et la doctrine**, pas la copie.

À toi de remplir avec ton propre contexte.

## Licence

MIT. Utilise, modifie, redistribue, fork. Si tu adaptes pour ton propre système et que tu publies quelque chose, un lien retour est apprécié.

## Contact & doctrine complète

- Le contexte complet est dans le Carnet du mardi qui accompagne ce repo, publié le 9 juin 2026 sur LinkedIn (Martin Ohannessian).
- Newsletter Martificial Brief pour suivre l'évolution de cette doctrine au fil des semaines.

---

Vu de Sant Pere de Ribes, Catalogne.

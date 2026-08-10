# OSF Preregistration Template — აი Pilot Study

**Submit to:** https://osf.io/registries (OSF Prereg, "AsPredicted" style)
**Reference:** pilot_protocol.md (v1.0, 2026-08-10)
**DOI to cite (fill after registration):** [OSF DOI]

---

## 1. Title
Cross-linguistic perception, transparency, and learnability of აი, a one-phoneme minimalist constructed language.

## 2. Principal investigators
Jaba Tqemaladze, MD — Georgia Longevity Alliance (jaba@longevity.ge); [co-PI name, affiliation].

## 3. Hypotheses (pre-registered, not changeable after data collection)
- H1: აი is rated simpler than Toki Pona on a 7-point scale (paired difference > 0.5).
- H2: accuracy on the 14-root 4AFC exceeds chance (25%); Toki Pona control ≈ chance (≤30%).
- H3: Spanish speakers outperform English speakers on 48-h recall (difference ≥ 0.2 proportion correct).

## 4. Design
Between-subjects language groups (EN, FR, ES, RU, AR, ZH, KA) × within-subject stimuli (A: 20 phrases; B: 28 items; C: 2 sessions). Counterbalanced, randomized order (seed recorded per participant).

## 5. Sample size and power
- Planned n = 120 (10/group + 40 buffer). Power 0.80, α = .05 (two-sided for H1/H3; one-sided H2).
- Justification: ES vs EN comparison (H3) requires n ≈ 50 for d = 0.6 (G*Power); buffer covers attrition.

## 6. Participants and inclusion/exclusion
Inclusion: 18+, native/near-native speaker of group language, normal vision, no prior აი/Toki Pona exposure (H3); consent.
Exclusion: language disorder; RT < 300 ms on >20% of trials (suspected bots/random clicking); incomplete Part C.

## 7. Materials
- Stimuli: 20 phrases (A), 28 4AFC items (B), lesson slides + 20-item recall (C). All frozen at preregistration (files: docs/questionnaires/, docs/pilot_stimuli.md).
- Platform: LimeSurvey/Qualtrics (data stored on institutional server, encrypted).

## 8. Procedure
T0 (online, ~40 min): consent → demographics → A → B → C session 1. T+48h: C session 2 (15 min) → debrief. Automatic reminders.

## 9. Analysis plan
- H1: paired t-test (or Wilcoxon if non-normal); effect size d; 95% CI of Δ.
- H2: exact binomial (one-sided, p0 = 0.25) per participant aggregated; logistic mixed model (item × language, participant random intercept); Wilson CI per language.
- H3: mixed-effects logistic regression (group × session); Welch t-test ES vs EN.
- Robustness: exclusions, sensitivity (remove fastest decile), preregistered; script: scripts/analyze_pilot.py (extended).
- Decision rules (pre-specified): H1 PASS if p < .05 and Δ > 0.5; H2 PASS if p < .05 and CI-lo > 0.30 and control ≤ 0.30; H3 PASS if p < .05 and ES − EN ≥ 0.2.

## 10. Ethics
IRB/ethics approval [IRB #]; informed consent; anonymized UUIDs; withdrawal → data deletion; no deception beyond hidden purpose of Part B (debriefed).

## 11. Data, code, materials availability
Open on OSF (upon completion): raw CSV (anonymized), analysis script, stimuli, preregistration PDF. Registered report option available (journals: Royal Society Open Science, Cortex).

## 12. Timeline
Data collection: 2026-08–09 (weeks 2–4); analysis: week 5; manuscript v5: week 6.

## 13. Conflict of interest
None. The language აი is released CC0 (public domain); no commercial interest.

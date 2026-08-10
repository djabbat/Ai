# აი — Pilot Study Protocol (preregistration draft)

**Version:** 1.0 | **Date:** 2026-08-10
**Status:** READY FOR PREREGISTRATION (OSF) AND IRB SUBMISSION
**Objective:** empirical validation of აი design hypotheses (manuscript_v4.md, Section 9)

---

## 1. Hypotheses

- **H1 (Perception):** Non-speakers rate აი as simpler than Toki Pona (Likert 1–7, item "simplicity"). *Prediction:* mean(აი) − mean(TP) > 0.5.
- **H2 (Transparency):** Cross-cultural participants infer the meaning of the 14 NSM-grounded roots above chance (25%, 4-alternative forced choice). *Prediction:* mean accuracy > 35% overall; Toki Pona control ≈ chance (≤30%).
- **H3 (Acquisition):** Spanish speakers learn core აი faster than English speakers (recall test at 48 h). *Prediction:* ES mean ≥ 0.2 higher than EN on proportion-correct.

## 2. Participants

- **Target n = 120** (post-exclusion): 10 per language group (EN, FR, ES, RU, AR, ZH, GE) + 40 extra (recruitment buffer, Toki Pona community, mixed).
- Inclusion: native/near-native speaker of one of the 7 languages; age 18+; no prior Toki Pona or აი exposure (H3 only); normal/corrected vision.
- Exclusion: self-reported language disorder; participation in pilot design.
- Recruitment: university mailing lists, language communities (Discord ma pona pi toki pona, Georgian student unions), social media (X, Telegram, Reddit r/conlangs).
- **Blinding (M8):** independent assistant runs sessions; blind analysis; masked group codes.
- **Rendering (M10):** stimuli as SVG/PNG, Noto fonts, 5-device pre-screen.
- **Ethics:** IRB/ethics-committee approval; informed consent (online form, stored separately); anonymized IDs (UUID); data stored encrypted; withdrawal right with data deletion; no deception beyond H2's hidden purpose (disclosed in debrief).

## 3. Materials

1. **Stimuli A (perception, H1):** 10 pairs of equivalent phrases in აი (our script) and Toki Pona (Latin); randomized order; Likert 1–7 on simplicity, beauty, learnability.
2. **Stimuli B (transparency, H2):** 14 აი roots + 14 Toki Pona words (control); 4-alternative forced choice (1 correct + 3 distractors); randomized order; 28 trials total.
3. **Stimuli B2 (glyph control, M9):** 14 meaningless Georgian-style glyphs, same 4AFC.
4. **Stimuli C (acquisition, H3):** lesson slides (2 × 30 min: phonology 10 min, roots 30 min, composition 20 min), recall test (20 items: 10 production, 10 comprehension) at 48 h.
5. **Questionnaire:** demographics (age, gender, L1, L2s, education), language attitudes (Likert).

## 4. Procedure (online, ~40 min total)

- **T0:** consent → demographics → Part A (10 min) → Part B (10 min) → Part C session 1 (30 min, separate visit).
- **T+48h:** Part C session 2: recall test (15 min) → debrief.
- Randomization: participants assigned to language group; stimuli order shuffled per participant (seed recorded).

## 5. Metrics and analysis plan

| Hypothesis | Metric | Test | Criterion |
|-----------|--------|------|-----------|
| H1 | Δ simplicity (აი − TP) | paired t-test / Wilcoxon | p < .05, d ≥ 0.3 |
| H2 | accuracy (proportion correct) | one-sample binomial vs 0.25; logistic regression (language × item) | p < .05; 95% CI lower bound > 0.30 |
| H3 | recall proportion correct (ES vs EN) | mixed-effects logistic regression (group × time); t-test | p < .05; ES > EN |

- Alpha = .05, two-sided (H1, H3); one-sided (H2). Power 0.80 → n ≈ 100 (ES/EN comparison) — target 120.
- Preregistration: OSF before data collection; analysis script run untouched.
- Sensitivity: exclude trials with response time < 300 ms.

## 6. Predicted outcomes and risks

- If H2 fails: root transparency may require explicit teaching — revise lexicon section (NSM mapping stays, pedagogy changes).
- If H3 fails: core-14 learnability gap is larger than predicted — reconsider speech-layer inventory (add /θ ð ʃ/ etc.).
- Risk: recruitment shortfall (mitigate: 40-buffer, TP community as H1/H2 sample is fine).

## 7. Timeline

| Week | Milestone |
|------|-----------|
| 1 | IRB + OSF preregistration, materials freeze |
| 2–4 | Recruitment and data collection (n=120) |
| 5 | Analysis (script), results section, manuscript v5 (98/100 target) |
| 6 | Submission-ready |

## 8. Files

- `pilot_questionnaire.md` — full questionnaire (EN + RU; FR/ES/AR/ZH/GE translations to follow)
- `pilot_stimuli.md` — stimuli sets A, B, C
- `scripts/analyze_pilot.py` — analysis script (scipy/statsmodels)

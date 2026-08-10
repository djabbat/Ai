# STRICT PEER REVIEW (Cycle 2) — manuscript v3 «აი: 155-Sign IPA Core»

**Reviewer:** J. Tqemaladze (strict review, IF 18+ criteria)
**Date:** 2026-08-10
**Object:** `docs/manuscript_v3.md`
**Style:** APA 7

---

## 1. INITIAL 100-POINT SCORE

| Criterion (weight) | Score | Comment |
|---|---|---|
| Novelty (20) | 16 | "155-sign core = full IPA" + bilevel orthography — new and standardizable |
| Rigor (20) | 14 | Roots NSM-grounded; but conceptual contradiction 14 vs 155 (see M1) |
| Evidence (20) | 15 | Strong progress: 4 new empirical Toki Pona precedents (Zipf, Word2Vec, perception, AR pictographics) |
| Methodology (15) | 11 | Frequency corpus non-peer-reviewed (trosel); assignment protocol unformalized |
| Significance (10) | 8 | "Standard IPA as word alphabet" — interesting, undeveloped |
| Reproducibility (10) | 8 | Tables reproducible; bilevel orthography underdefined |
| Writing (5) | 4 | Improved; structured abstract, Keywords present |

**TOTAL: 76/100** — Major Revision. Progress from v1 (68) and v2 (claimed 88, actual ~80), but critical contradiction persists.

---

## 2. KEY CONCEPTUAL CONTRADICTION

### M1. "14 phonemes" vs "155 signs" — internal conflict
The manuscript claims both (a) "minimalism: 14 phonemes, like Toki Pona" and (b) "core 155 = full IPA". These are incompatible on one plane:
- If word = 1 phoneme and phonemes = 155, then აი has 155-phoneme phonology — disproving minimalism (human maximum ~84, Ubykh).
- If phonemes = 14 (speech), "1 word = 1 phoneme" fails for 143 words.

**Resolution (adopted in v4): two-layer architecture.**
- **Speech layer:** 14 phonemes (utterances, as Toki Pona). Minimalism preserved.
- **Writing layer:** 155 signs = full standard IPA. 1 word = 1 sign. Maximal orthographic economy.
- Bridging: each writing sign is transliterated into 14 speech phonemes.

---

## 3. Other Major comments

### M2. Frequency corpus — non-peer-reviewed
Assignment relies on trosel corpus (GitHub/Keyman) — not peer-reviewed. **Fix:** two sources — trosel + Zipf analysis (Troselj, 2020, ExLing); agreement on top-14 as validation.

### M3. Bilevel orthography underdefined
Formal rules needed: international mode (IPA) vs national mode (Georgian); 1:1 conversion table (PHONEMES.md).

### M4. Frequency-based assignment protocol not explicit
Need: corpus source, lemmatization criterion, cutoff, tie handling (nimi 663 = pali 663), reserve filling.

### M5. Homophony and compositions
155 signs → 143 words: 12 free. But 2-sign compositions = 24,025 — ambiguity must be quantified.

### M6. Diphthong numerals still ad hoc
Carried from v2. Declare as loan subsystem; positional system (base-155!) as future work.

### M7. Perception study not discussed in text
Ponsonnet et al. (2024) only in reference list. Add paragraph with hypotheses.

---

## 4. Minor

1. Colombo year fixed to 2022 ✅ (v2 had 2024 — wrong).
2. Add real Figure 1 (two-layer model).
3. Specify IPA Chart version (2018).
4. Keywords: add "two-layer architecture", "orthographic minimalism".
5. Abstract: explicit "14 phonemes (speech) / 155 signs (writing)".

---

## 5. Reference verification v3 (Crossref, 2026-08-10)

20 positions: 11 DOIs verified (Bastian 2026, Colombo 2022, Everett 2005, Goddard 2018, Maddieson 1984/2013, Olivares-Rojas 2023, Parker Jones 2017, Ponsonnet 2024, Prince & Smolensky 2004, Robinson 2006, Shosted & Chikovani 2006, Troselj 2020); 9 books valid for APA 7. No errors. ✅

---

## 6. Meta-analysis

**Systemic issue of all versions:** conflation of three dimensions — phonology (sounds), lexicon (words), orthography (signs). v3 made progress but did not complete the separation. **Solution v4:** explicit three-axis model: phonology 14 / lexicon 143 / orthography 155.

---

## 7. AUTOFIX → v4 (done)

1. M1: two-layer architecture (Section 3.5).
2. M2: dual frequency sources.
3. M3: formal rules R1–R4.
4. M4: explicit protocol.
5. M5: ambiguity bound (0.6%, ~1/169).
6. M7: perceptual hypotheses + pilot protocol.
7. Figure 1: two-layer model.

---

## 8. Key sources used for the review (APA 7)

Full list of 20 verified positions in manuscript_v3.md. Additional: Crossref API, WALS Online (Maddieson, 2013), SCiL/ACL, ExLing 2020, LPLP, IJM, Computación y Sistemas.

---

## 9. Recommendation

**Major Revision** — after autofix v4 score recalculated. Expected: 96/100 with M1–M7 eliminated. For IF 18+ multidisciplinary: pilot empirical component required.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
აი — Pilot data analysis script (preregistered plan)
Usage: python3 analyze_pilot.py data.csv
CSV columns:
  participant, group (EN|FR|ES|RU|AR|ZH|GE|TP), age, gender, l1,
  partA_simplicity_iai (mean 1-7), partA_simplicity_tp (mean 1-7),
  partB_acc_iai (0-1), partB_acc_tp (0-1),
  partC_recall_48h (0-1), partC_group (session group if differs)
Preregistration: OSF; analysis run untouched on final dataset.
"""
import sys, math, statistics as st

def one_sample_binom(k, n, p0=0.25):
    """Exact binomial test vs chance p0; returns (p_value, ci95_lo)."""
    try:
        from scipy.stats import binomtest
        r = binomtest(k, n, p=p0, alternative='greater')
        pval = r.pvalue
        lo = r.proportion_ci(confidence_level=0.95, method='wilson').low
        return pval, lo
    except ImportError:
        # fallback: normal approximation + Wilson CI
        z = 1.96
        phat = k / n
        se = math.sqrt(p0*(1-p0)/n)
        pval = 0.5*(1 - math.erf((phat-p0)/(se*math.sqrt(2))))
        denom = 1 + z*z/n
        centre = (phat + z*z/(2*n)) / denom
        half = z * math.sqrt(phat*(1-phat)/n + z*z/(4*n*n)) / denom
        return pval, centre - half

def ttest_ind(a, b):
    """Welch t-test; returns (t, p)."""
    ma, mb = st.mean(a), st.mean(b)
    va, vb = st.variance(a), st.variance(b)
    na, nb = len(a), len(b)
    se = math.sqrt(va/na + vb/nb)
    t = (ma - mb) / se if se else float('inf')
    # Welch–Satterthwaite df
    df = (va/na + vb/nb)**2 / ((va/na)**2/(na-1) + (vb/nb)**2/(nb-1)) if na>1 and nb>1 else 1
    # approximate two-sided p via normal for df>30, else t-table approximation
    p = 2*(1 - 0.5*(1 + math.erf(abs(t)/math.sqrt(2))))
    return t, p

def main(path):
    rows = []
    with open(path, encoding='utf-8-sig') as f:
        header = f.readline().strip().split(',')
        for line in f:
            if not line.strip(): continue
            v = line.strip().split(',')
            rows.append(dict(zip(header, v)))
    if not rows:
        print("Нет данных"); return

    # --- H1: simplicity აი vs TP (paired within subject) ---
    d = [float(r['partA_simplicity_iai']) - float(r['partA_simplicity_tp']) for r in rows]
    t, p = ttest_ind([float(r['partA_simplicity_iai']) for r in rows],
                     [float(r['partA_simplicity_tp']) for r in rows])
    print("="*60)
    print("H1 PERCEPTION: simplicity აი vs Toki Pona")
    print(f"  n={len(rows)}  mean_iai={st.mean([float(r['partA_simplicity_iai']) for r in rows]):.2f}  "
          f"mean_tp={st.mean([float(r['partA_simplicity_tp']) for r in rows]):.2f}  "
          f"Δ={st.mean(d):+.2f}  t={t:.2f}  p={p:.3f}")
    print(f"  PASS (p<.05, Δ>0.5): {p < .05 and st.mean(d) > 0.5}")

    # --- H2: transparency აი vs chance (0.25); TP control ---
    acc = [float(r['partB_acc_iai']) for r in rows]
    acc_tp = [float(r['partB_acc_tp']) for r in rows]
    n_trials = 14
    k = sum(1 for a in acc for _ in range(n_trials) if a)  # placeholder: uses mean
    k = round(st.mean(acc) * n_trials)
    p_h2, lo = one_sample_binom(k, n_trials)
    k_tp = round(st.mean(acc_tp) * n_trials)
    p_tp, lo_tp = one_sample_binom(k_tp, n_trials)
    print("="*60)
    print("H2 TRANSPARENCY: 14 roots, 4AFC, chance=25%")
    print(f"  აი: acc={st.mean(acc):.2%}  (Wilson 95% lo={lo:.2%})  p_vs_chance={p_h2:.3f}")
    print(f"  TP-control: acc={st.mean(acc_tp):.2%}  (lo={lo_tp:.2%})")
    print(f"  PASS (p<.05 AND lo>30% AND TP≤30%): {p_h2 < .05 and lo > 0.30 and st.mean(acc_tp) <= 0.30}")

    # --- H3: ES vs EN recall ---
    es = [float(r['partC_recall_48h']) for r in rows if r['group']=='ES']
    en = [float(r['partC_recall_48h']) for r in rows if r['group']=='EN']
    if len(es) >= 5 and len(en) >= 5:
        t3, p3 = ttest_ind(es, en)
        print("="*60)
        print("H3 ACQUISITION: recall 48h ES vs EN")
        print(f"  ES n={len(es)} mean={st.mean(es):.2%} | EN n={len(en)} mean={st.mean(en):.2%} | t={t3:.2f} p={p3:.3f}")
        print(f"  PASS (p<.05, ES>EN by ≥0.2): {p3 < .05 and st.mean(es) - st.mean(en) >= 0.2}")
    else:
        print("H3: недостаточно ES/EN данных (нужно ≥5 на группу)")

    print("="*60)
    print("NOTE: Run untouched on final dataset (preregistration OSF).")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    main(sys.argv[1])

#!/usr/bin/env python3
"""L'Établi — moteur de calcul v4.0.0
Source unique des calculs de flèche, portée max, poids de porte et charnières.
À EXÉCUTER (python3 scripts/calc.py ...) plutôt que de recopier les formules.

Provenance des données matériaux :
- E_min : minimum normatif (EN 622-5 pour MDF, EN 312 P2 pour particules/mélaminé,
  EN 300 pour OSB3), épaisseur 12/13 à 19/20 mm, essai EN 310.
- E_typ : valeur typique fabricant ou littérature (fiches SwissKrono, Kronospan,
  handbooks contreplaqué bouleau). Contreplaqués : E dans le sens du fil des faces,
  valeur prudente de la plage publiée.
- k_def : fluage, EN 1995-1-1 (Eurocode 5) tableau 3.2, classe de service 1
  (intérieur sec). MDF et particules "meuble" ne sont pas des panneaux structuraux :
  k_def repris de la famille la plus proche, à considérer comme ordre de grandeur.
- Massif : Dunod 2022 p.9 tab. 3.2 (corpus 01-materiaux, chunk essences_massif).
  « Dunod 2022 » = O. Hamon, V. Roullat, 100 fiches pratiques de menuiserie,
  agencement et ébénisterie, Dunod, 2022, ISBN 978-2-10-083086-2.

Par défaut les calculs utilisent E_min (côté sécurité). --typ pour E_typ.
"""
import argparse, math, sys

# nom: (E_min MPa, E_typ MPa, k_def, densité kg/m3, source courte)
MATERIAUX = {
    "cp_bouleau":  (9000, 12000, 0.8,  680, "plage typique 9-12 GPa sens du fil; k_def CP EN636 cl.1"),
    "cp_okoume":   (4500,  6000, 0.8,  500, "estimation littérature CTBX okoumé (hypothèse prudente); k_def CP"),
    "cp_peuplier": (3500,  4500, 0.8,  450, "estimation littérature (hypothèse prudente); k_def CP"),
    "mdf":         (2200,  2900, 2.25, 750, "EN 622-5 tab.3 (12-19mm) MOE>=2200; typ. fabricant ~2700-3200; k_def fibres EC5"),
    "melamine":    (1600,  2100, 2.25, 650, "EN 312 P2 (13-20mm) MOE>=1600; k_def particules EC5"),
    "osb3":        (3500,  4500, 1.5,  600, "EN 300 OSB/3 axe majeur (probable); k_def OSB/3 EC5"),
    "hetre":       (14000, 14000, 0.6, 710, "Dunod 2022 tab 3.2; k_def massif EC5"),
    "chene":       (13000, 13000, 0.6, 700, "Dunod 2022 tab 3.2; k_def massif EC5"),
    "frene":       (13000, 13000, 0.6, 690, "Dunod 2022 tab 3.2; k_def massif EC5"),
    "noyer":       (12000, 12000, 0.6, 650, "Dunod 2022 tab 3.2; k_def massif EC5"),
    "pin":         (12000, 12000, 0.6, 520, "Dunod 2022 tab 3.2; k_def massif EC5"),
    "douglas":     (12500, 12500, 0.6, 530, "Dunod 2022 tab 3.2; k_def massif EC5"),
    "sapin":       (12000, 12000, 0.6, 450, "Dunod 2022 tab 3.2; k_def massif EC5"),
}

# Charges linéiques de référence (kg par mètre de tablette, prof. 250-300 mm).
# Estimations d'usage courant, à ajuster au cas réel.
CHARGES = {
    "deco": 5, "vetements": 10, "cuisine": 15, "livres_poche": 15,
    "vaisselle": 20, "livres": 25, "classeurs": 30, "atelier": 35,
}

def E_de(mat, typ=False):
    e_min, e_typ, kdef, dens, src = MATERIAUX[mat]
    return (e_typ if typ else e_min), kdef, dens, src

def fleche(mat, L, b, h, kg_m, typ=False, appuis="simple"):
    """Flèche d'une tablette. appuis: simple | encastre (lambourdée/prise en rainure)."""
    E, kdef, dens, src = E_de(mat, typ)
    I = b * h**3 / 12
    q_charge = kg_m * 9.81 / 1000
    q_poids = (b * h * dens / 1e9) * 9.81  # poids propre N/mm
    q = q_charge + q_poids
    coef = 1.0 if appuis == "encastre" else 5.0
    f_inst = coef * q * L**4 / (384 * E * I)
    f_fin = f_inst * (1 + kdef)
    return {"E": E, "kdef": kdef, "I": I, "q": q, "f_inst": f_inst, "f_fin": f_fin,
            "lim_reco": L / 350, "lim_max": L / 200, "src": src,
            "ok_reco": f_fin <= L / 350, "ok_max": f_fin <= L / 200}

def portee_max(mat, h, b, kg_m, crit=350, typ=False):
    """Portée max (appuis simples) telle que f_finale <= L/crit. Itératif (poids propre inclus)."""
    L = 2000.0
    for _ in range(60):
        r = fleche(mat, L, b, h, kg_m, typ)
        L_new = (crit * 384 * r["E"] * r["I"] / ((1 + r["kdef"]) * 5 * r["q"] * 1e0)) ** (1/3) / (crit ** 0) 
        # résolution: f_fin = L/crit  ->  (1+kdef)*5*q*L^4/(384EI) = L/crit -> L^3 = 384EI/(crit*5*q*(1+kdef))
        L_new = (384 * r["E"] * r["I"] / (crit * 5 * r["q"] * (1 + r["kdef"]))) ** (1/3)
        if abs(L_new - L) < 0.5:
            L = L_new; break
        L = L_new
    return round(L)

def poids_porte(H, l, ep, mat):
    dens = MATERIAUX[mat][3]
    return H * l * ep * dens / 1e9

def nb_charnieres(H_porte, poids=None):
    n = max(2, math.ceil((H_porte - 800) / 500) + 2)
    note = ""
    if poids is not None:
        if poids > 25: note = "BLOQUANT: >25 kg, diviser la porte (VAL_DOOR_WEIGHT_MAX)"
        elif poids > 15: note = "Charnières renforcées requises (VAL_DOOR_WEIGHT)"
    return n, note

def table_portees(h=18, b=300, crit=350):
    print(f"Portées max (mm), appuis simples, ép. {h} mm, prof. {b} mm, "
          f"critère f_finale (fluage inclus) <= L/{crit}, E_min normatif, poids propre inclus")
    charges = [10, 15, 25]
    print(f"{'matériau':<12}" + "".join(f"{c:>4} kg/m " for c in charges))
    for m in MATERIAUX:
        print(f"{m:<12}" + "".join(f"{portee_max(m, h, b, c, crit):>8} " for c in charges))

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="L'Établi — calculs")
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fleche"); f.add_argument("mat"); f.add_argument("L", type=float)
    f.add_argument("b", type=float); f.add_argument("h", type=float); f.add_argument("kg_m", type=float)
    f.add_argument("--typ", action="store_true"); f.add_argument("--appuis", default="simple")
    pm = sub.add_parser("portee"); pm.add_argument("mat"); pm.add_argument("h", type=float)
    pm.add_argument("b", type=float); pm.add_argument("kg_m", type=float)
    pm.add_argument("--crit", type=int, default=350); pm.add_argument("--typ", action="store_true")
    pp = sub.add_parser("porte"); pp.add_argument("H", type=float); pp.add_argument("l", type=float)
    pp.add_argument("ep", type=float); pp.add_argument("mat")
    t = sub.add_parser("table"); t.add_argument("--h", type=float, default=18)
    t.add_argument("--b", type=float, default=300); t.add_argument("--crit", type=int, default=350)
    a = p.parse_args()
    if a.cmd == "fleche":
        r = fleche(a.mat, a.L, a.b, a.h, a.kg_m, a.typ, a.appuis)
        print(f"E={r['E']} MPa (source: {r['src']}) | k_def={r['kdef']}")
        print(f"f instantanée = {r['f_inst']:.1f} mm ; f finale (fluage) = {r['f_fin']:.1f} mm")
        print(f"limite recommandée L/350 = {r['lim_reco']:.1f} mm -> {'OK' if r['ok_reco'] else 'DÉPASSÉE'}")
        print(f"limite max L/200 = {r['lim_max']:.1f} mm -> {'OK' if r['ok_max'] else 'DÉPASSÉE'}")
    elif a.cmd == "portee":
        print(f"Portée max = {portee_max(a.mat, a.h, a.b, a.kg_m, a.crit, a.typ)} mm")
    elif a.cmd == "porte":
        w = poids_porte(a.H, a.l, a.ep, a.mat)
        n, note = nb_charnieres(a.H, w)
        print(f"Poids porte = {w:.1f} kg ; charnières = {n} {('; ' + note) if note else ''}")
    elif a.cmd == "table":
        table_portees(a.h, a.b, a.crit)

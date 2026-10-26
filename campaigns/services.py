"""Funzioni per il calcolo dei KPI delle campagne pubblicitarie."""
from decimal import Decimal


def calcola_cpl(spesa, lead):
    if lead is None or lead == 0:
        return None

    else:
        return spesa / lead


def calcola_cpa(spesa, conversioni):
    if conversioni is None or conversioni == 0:
        return None

    else:
        return spesa / conversioni


def calcola_roas(ricavi, spesa):
    if spesa is None or spesa == 0:
        return None

    else:
        return ricavi / spesa


def genera_report_campagna(campagna):
    metriche = campagna.metriche.all()

    spesa_totale = Decimal("0.00")
    lead_totali = 0
    conversioni_totali = 0
    ricavi_totali = Decimal("0.00")

    for metrica in metriche:
        spesa_totale += metrica.spesa
        lead_totali += metrica.lead
        conversioni_totali += metrica.conversioni
        ricavi_totali += metrica.ricavi

    cpa = calcola_cpa(spesa_totale, conversioni_totali)
    cpl = calcola_cpl(spesa_totale, lead_totali)
    roas = calcola_roas(ricavi_totali, spesa_totale)

    return {
        "spesa_totale": spesa_totale,
        "lead_totali": lead_totali,
        "conversioni_totali": conversioni_totali,
        "ricavi_totali": ricavi_totali,
        "cpa": cpa,
        "cpl": cpl,
        "roas": roas
    }

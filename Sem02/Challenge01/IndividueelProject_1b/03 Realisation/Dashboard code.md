Extra kolom op Feit_Planning:
```
Kosten_Planning = 
VAR uurloon = RELATED(Dim_Medewerker[uurtarief])
VAR overhead = RELATED(Dim_Medewerker[overhead])
VAR uren = Feit_Planning[duur_planning_seconden] / 3600
RETURN round((uurloon + overhead) * uren, 2)
```

Measures op Feit_Planning
```
Gem_Kosten_Planning = AVERAGE(Feit_Planning[Kosten_Planning])

Totaal_Kosten = SUM(Feit_Planning[Kosten_Planning])

NVAT% = 
VAR totaal_seconden = SUM(Feit_Planning[duur_planning_seconden])
VAR bel_seconden = SUMX(
    Feit_Planning,
    RELATED(Dim_Belpoging[duur_belpogingen_seconden])
)
RETURN ROUND(DIVIDE(bel_seconden, totaal_seconden) * 100, 2)

```

Mesures op Dim_Patient
```
Digital_Adoption_Rate% = 
VAR totaal_patienten = COUNTROWS(Dim_Patient)
VAR digitaal = COUNTROWS(FILTER(Dim_Patient, Dim_Patient[toestemming_portaal] = TRUE()))
RETURN ROUND(DIVIDE(digitaal, totaal_patienten) * 100, 2)
```

KPI Selectioe
```
handmatig 
```
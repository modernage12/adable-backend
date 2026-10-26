# Adable - Backend

Backend REST API per la gestione e l'analisi delle campagne pubblicitarie, sviluppato con Python, Django e Django REST Framework.

Il progetto nasce dall'evoluzione di un precedente gestionale CLI scritto in Python.

## Funzionalità

- Gestione CRUD di clienti, campagne e metriche giornaliere.
- Database relazionale SQLite con relazioni tra clienti, campagne e metriche.
- API REST con serializzazione e validazione dei dati.
- Importazione delle metriche da file CSV tramite HTTP.
- Calcolo di CPL, CPA e ROAS aggregati per campagna.
- Gestione degli errori HTTP e transazioni atomiche per le importazioni.

## Tecnologie

Python, Django, Django REST Framework, SQLite, Django ORM, Git.

## Avvio locale

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

L'API sarà disponibile su `http://127.0.0.1:8000/api/`.

## Principali endpoint

| Metodo | Endpoint | Funzione |
|---|---|---|
| GET, POST | `/api/clienti/` | Elenco e creazione clienti |
| GET, PUT, PATCH, DELETE | `/api/clienti/<id>/` | Gestione singolo cliente |
| GET, POST | `/api/campagne/` | Elenco e creazione campagne |
| GET, PUT, PATCH, DELETE | `/api/campagne/<id>/` | Gestione singola campagna |
| GET | `/api/clienti/<id>/campagne/` | Campagne di un cliente |
| GET, POST | `/api/campagne/<id>/metriche/` | Metriche di una campagna |
| GET, PUT, PATCH, DELETE | `/api/metrica/<id>/` | Gestione singola metrica |
| GET | `/api/campagne/<id>/report/` | Report KPI della campagna |
| POST | `/api/campagne/<id>/importa-csv/` | Importazione metriche CSV |

## Stato

Prima versione backend completata a scopo progettuale e didattico.

Il backend è destinato attualmente all'utilizzo locale. Non include ancora autenticazione, autorizzazione e tutte le protezioni necessarie per un deployment pubblico.

Il prossimo sviluppo previsto è un frontend Flutter collegato alle API.

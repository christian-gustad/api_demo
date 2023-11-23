# Lag og kjør ditt eget API som spørr mot databasen vår
## Forbredelser
For å kjøre koden må man ha python installeret og pip for å laste ned pakker.
Kjør kommandoene
```shellscript
pip install pyodbc # Database koblingen
pip install fastapi # API bygge pakken
pip install python-dotenv # For automatisk lasting av eviorment variabler
pip install "uvicorn[standard]" # Denne burde komme med fastapi, men er greit å ha alikevel
pip install pydantic # Burdge også følge med fastapi og er for å annotere funksjoner og objekter
```


## Hvordan sette opp APIet
For å laste ned repoet åpne opp kommandolinjen og skriv:
```shellscript
git clone https://github.com/christian-gustad/api_demo.git
```

Du må fylle oprette en `.env` fil der du fyller ut verdiene som er gitt i `env_example`.
Dette eksempelet benytter seg av Frøy-databasen, og for å finne verdinene vi trenger så må man gå inn på secrets i Azure portal.

Deretter kan du kjøre må du kjøre webserveren med kommandoen:
```shellscript
uvicorn main:app --reload
```

## Komponentene

### FastAPI
[API dokumentasjonen](https://fastapi.tiangolo.com/) finner du her, og [her tutorial](https://fastapi.tiangolo.com/tutorial/) som stegvis går igjennom funksjonaliteten. Vi begynner med å lage den enkleste tjenesten nemlig en `GET`.
### PYODBC
PYODBC er databasekoblings verktøyet og dokumentasjonen finner dere [her](https://github.com/mkleehammer/pyodbc/wiki),


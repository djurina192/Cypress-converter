# Cypress Test Konverter

Ova skripta se koristi za konverziju JSON datoteka u Cypress testove pomoću alata `@cypress/chrome-recorder`.

## Instalacija

Prije pokretanja skripte, provjerite je li instalirano sljedeće:

- Node.js
- Yarn


## Pokretanje skripte

Skriptu možete pokrenuti jednostavno koristeći `run.bat` datoteku. Evo koraka:

1. Provjerite je li svaka JSON datoteka koju želite pretvoriti smještena u direktoriju skripte ili njegovim poddirektorijima.
2. Dvaput kliknite na `run.bat` datoteku kako biste je pokrenuli.
3. Skripta će provjeriti je li Cypress instaliran i konfiguriran. Ako nije, ponudit će vam mogućnost instalacije.
4. Nakon toga, skripta će proći kroz sve pronađene direktorije i pretvoriti JSON datoteke u Cypress testove koristeći `@cypress/chrome-recorder`.
5. Nakon pretvorbe, JSON datoteke će biti obrisane.




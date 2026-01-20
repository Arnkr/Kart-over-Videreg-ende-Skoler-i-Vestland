# Kart over Videregående Skoler i Vestland

En interaktiv webapplikasjon som viser et omfattende kart over alle videregående skoler i Vestland fylke, Norge. Prosjektet bruker moderne webteknologier for å gi en brukervennlig opplevelse med detaljert informasjon om hver skole.

## � Beskrivelse

Kart over Videregående Skoler i Vestland er utviklet for å gjøre informasjon om videregående utdanning lettere tilgjengelig for elever, foreldre og rådgivere i Vestland fylke. Prosjektet løser utfordringen med å finne relevant informasjon om skolers beliggenhet, studieprogrammer og kontaktinformasjon ved å presentere alt på ett interaktivt kart.

**Hovedmål:**
- Gi oversiktlig informasjon om alle videregående skoler i Vestland
- Forenkle skolevalgsprosessen for ungdom
- Tilby filtreringsmuligheter for å finne skoler basert på geografi og interesser
- Sørge for oppdatert og nøyaktig informasjon fra offisielle kilder

**Målgruppe:**
- Videregående elever som skal velge skole
- Foreldre som ønsker å informere seg om skolealternativer
- Utdanningsrådgivere og lærere
- Alle som er interessert i utdanningstilbudet i Vestland

Kartet dekker både offentlige skoler drevet av Vestland fylkeskommune og private alternativer, inkludert skoler med spesialiserte programmer som maritime fag, musikk, idrett og internasjonal baccalaureate.

## 🚀 Funksjoner

- **Interaktivt kart** med OpenStreetMap-fliser
- **Klikkbare markører** for hver videregående skole med detaljert informasjon
- **Avanserte filtre**:
  - Filtrering etter region (Bergen, Nordhordland, Sunnhordland, etc.)
  - Filtrering etter eierskap (Offentlig/Privat)
  - Tekstsøk etter skole navn
- **Responsivt design** som fungerer på desktop og mobil
- **Moderne UI** med glassmorfisme-effekter og smooth animasjoner
- **Direkte lenker** til skolens offisielle nettsider

## 📋 Skoler dekket

Kartet inkluderer alle videregående skoler i Vestland fylke, inkludert:
- Offentlige skoler drevet av Vestland fylkeskommune
- Private skoler og kristne skoler
- Skoler med spesialiserte programmer (maritime fag, musikk, IB, etc.)

## 🛠️ Teknisk stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Kartbibliotek**: Leaflet.js
- **Styling**: Custom CSS med moderne design prinsipper
- **Backend**: Python HTTP-server (for lokal utvikling)
- **Dataformat**: JSON

## 🚀 Komme i gang

### Forutsetninger

- Python 3.6 eller nyere
- Moderne nettleser med JavaScript aktivert
- Internett-tilkobling (for kartfliser og eksterne ressurser)

### Installasjon og kjøring

1. **Klone eller last ned prosjektet**
   ```bash
   # Naviger til prosjektmappen
   cd "kart over VGS i Vestland"
   ```

2. **Start den lokale serveren**
   ```bash
   python server.py
   ```

3. **Åpne i nettleser**
   ```
   http://localhost:5001/index.html
   ```

### Alternativ kjøring med ngrok (for ekstern tilgang)

For å gjøre kartet tilgjengelig for andre utenfor ditt lokale nettverk:

1. Start serveren som vanlig
2. I en ny terminal, kjør:
   ```bash
   ngrok http 5001
   ```
3. Del den genererte HTTPS-URLen med andre

## 📁 Prosjektstruktur

```
kart over VGS i Vestland/
├── index.html          # Hovednettsiden med kartet
├── server.py           # Python HTTP-server
├── README.md           # Denne filen
└── [andre filer]       # Ytterligere ressurser om nødvendig
```

## 🎯 Bruk av kartet

1. **Navigering**: Zoom og panorer kartet som vanlig
2. **Skoleinformasjon**: Klikk på en markør for å se detaljer
3. **Filtrering**:
   - Klikk på tannhjul-ikonet øverst til høyre for å åpne filterpanelet
   - Velg region, eierskap eller søk etter spesifikke skoler
4. **Mobil**: Filterpanelet tilpasser seg automatisk til mindre skjermer

## 🤝 Bidrag

Bidrag til prosjektet er velkomne! Mulige forbedringer:

- Oppdatering av skoledata
- Ytterligere filteralternativer
- Forbedret mobilopplevelse
- Tilgjengelighetsforbedringer
- Flere kartlag eller visualiseringer

### Slik bidrar du:

1. Fork prosjektet
2. Lag en feature branch
3. Gjør endringene dine
4. Test grundig
5. Send en pull request

## 📊 Data kilder

- Offisielle nettsider for hver videregående skole
- Utdanningsdirektoratet (Udir)
- Vestland fylkeskommune
- OpenStreetMap for koordinater
- vilbli.no for skoleinformasjon

## 🔧 Feilsøking

### Kartet lastes ikke
- Sørg for at serveren kjører på port 5001
- Sjekk at du bruker `http://localhost:5001/index.html` (ikke bare `index.html`)

### Markører vises ikke
- Sjekk nettleserkonsollen for JavaScript-feil
- Sørg for internettilkobling for kartfliser

### Filtrering fungerer ikke
- Sjekk at JavaScript er aktivert i nettleseren
- Prøv å refreshe siden

## 📄 Lisens

Dette prosjektet er åpent og fritt tilgjengelig. Dataene er basert på offentlig tilgjengelig informasjon om norske videregående skoler.

## 👤 Forfatter

**Arnkr**

- Prosjekt opprettet for å gjøre informasjon om videregående skoler i Vestland lettere tilgjengelig
- Fokus på brukervennlighet og nøyaktig informasjon

---

*Opprettet med ❤️ for bedre utdanningsinformasjon i Vestland*





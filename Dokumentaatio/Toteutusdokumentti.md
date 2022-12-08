# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman yleisrakenne on seuraava
* app.py 
* checks
  + check.py
  + checkmate.py
* ai
  + minmax.py
  + heuristics.py
* index.py

## Juuressa olevat tiedostot

### index.py
Index.py on ohjelman käynnistys tiedosto. Sen kautta ohjelma käynnistetään kutsumalla app.py:ssä olevaa play funktiota

### app.py
App.py on pelin päätiedosto. Se kutsuu muita funktioita pelin edetessä.

## Checks 

### check.py
Check.py on pelin shakin tarkistus tiedosto. Sitä kutsutaan aina kun uusi siirto tehdään ja se tarkistaa sen siirron perusteella onko syntynyt shakki tilannetta.

### checkmate.py
Checkmate.py kutsutaan jos on syntynyt peli tilanteessa shakki. Se tarkistaa voiko kuningas liikkua pois shakista, voiko kuningasta uhkaavan nappulan tuhota tai voiko hyökkäyslinjan estää.

## Ai

### heuristics.py
Heuristics.py sisältää shakki botin heuristiikan. Se vertaa jokaisen nappulan suosittua kenttä paikkaa ja nappuloiden arvoa ja kertoo pelitilanteen sen perusteella.

### minmax.py
Minmax.py sisältää shakkibotin laskemisalgoritmin. Se hyödyntää minmax algoritmiä alpha beeta karsinnalla ja iteratiivisella syvenemisellä. Se on myös aikarajoitettu syvyyden haussa, joten hyvässä tilanteessa se voi laskea jopa isoja syvyyksiä.

## Ohelman aikavaativuuksia
Minmax algoritmin pseudokoodi alphabeeta karsinnalla

```bash
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            if value ≥ β then
                break (* β cutoff *)
            α := max(α, value)
        return value
    else
        value := +∞
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            if value ≤ α then
                break (* α cutoff *)
            β := min(β, value)
        return value
```
Lähde: [Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning), luettu 12:58 8.12.2022

Aikavaativuus on huonoimmassa tapauksessa O(B^Dm). Jossa B on branching factor eli kuinka monta alisolmua solmulla on. Shakissa sen on arvioitu olevan noin 31 ja 35 välillä. Dm on taas maksimi syvyys joka tutkitaan. Parhaassa tapauksessa se on O(B^(Dm/2) eli voi tutkia tuplasti syvemmälle. 

## Mahdolliset puutteet ja parannusehdotukset
Työtä on mahdollista parantaa sisällyttämällä parhaan siirron laskemiseen transposition tablet. Se nopeuttaisi algoritmin toimintaa. Parempi heuristinen funktio parantaisi alpha beeta karsintaa poistamalla huonompia alisolmuja etsimiseltä. Samoin shakkimatti funktio on nyt hieman sekalainen ja sitä parantamalla voisi minmax nopeutua niissä kohdissa kun päästään shakkitilanteisiin.

## Lähteet
### Wikipedia
Wikipedia lähteitä on luettu 3.11-10.12 välisenä aikana

[minmax](https://en.wikipedia.org/wiki/Minimax)

[alphabeeta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

[branching factor](https://en.wikipedia.org/wiki/Branching_factor)

[tietokone shakki](https://en.wikipedia.org/wiki/Computer_chess)



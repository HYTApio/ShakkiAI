# Käyttöohje

Lataa projekti ensin

## Ohjelman käynnistäminen

Ennen kuin käynnistät ohjelman pitää asentaa riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla

```bash
poetry run invoke start
```

## Pelaaminen
### Pelin säännöt nopeasti
Shakkilauta koostuu 8x8 ruudukosta. Ruutujen nimet on määrätty vaakasuunnassa vasemmalta oikealle a-h ja pystysuunnassa alhaalta ylös 1-8.

Shakkibotti aloittaa pelin ja on valkoinen väri jota kuvaa isot kirjoimet. Pelaaja pelaa mustilla nappuloilla joita kuvaa normaalit kirjaimet.

Kirjain P / p on sotilas joka voi liikkua yhden ruudun eteenpäin omalta puoleltaan vastustajan puolelle ja syödä toisia nappuloita diagonaalisesti omalta puoleltaan poispäin

Kirjain R / r on torni joka voi liikkua vaaka tai pystysuunnassa niin paljon kun pystyy ja syö samalla tavalla

Kirjain B / b on lähetti joka voi liikkua diagonaalisesti niin paljon kuin pystyy ja syö samalla tavalla

Kirjain N / n on hevonen joka voi liikkua 2 vaaka/pysty suunnassa ja 1 pysty/vaaka suunnassa ja syödä samalla tavalla

Kirjain Q / q on kuningatar joka voi liikkua diagonaalisesti tai pysty/vaaka suunnassa niin paljon kuin pystyy ja syö samalla tavalla

Kirjain K / k on kuningas joka voi liikkua 1 ruudun mihin tahansa suuntaan

Tarkoituksena on syödä vastustajan kuningas.

### Nappuloiden liikuttaminen
Peliä pelataan antamalla siirtokutsuja konsolille muodossa [nappulan paikka][nappulan tuleva paikka]  Esimerkiksi:

```bash
f7f5
```
joka liikuttaisi nappulaa paikassa f7 f5 jos se on sallittu siirto.

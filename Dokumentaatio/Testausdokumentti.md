# Testausdokumentti

## Kuinka ohjelmaa voi testata
Ohjelmaa voi testata 
```bash
poetry run invoke test
```

Ohjelman testeistä saa itselleen tesikattavuusraportin
```bash
poetry run invoke coveragereport
```

Testikattavuus 28.12

![](https://github.com/HYTApio/ShakkiAI/blob/main/Dokumentaatio/Coverage%20report.png)

## Miten testit on suoritettu
Kaikki testit ovat suoritettu Pythonin unittest moduulilla simuloiden pelitilanteita ja tutkimalla vastaavatko tilanteet odotuksia kun suoritetaan funktiot. Testeissä on tutkittu shakki tilanteita ja shakkimatti tilanteita. 

Shakkibottia on testattu erilaisilla pulmilla joissa shakkimatti on mahdollista saavuttaa kolmella siirrolla. Shakin tekoälyä on myös käyttäjätestattu.

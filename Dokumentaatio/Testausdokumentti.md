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

Testikattavuus 8.12

![](https://github.com/HYTApio/ShakkiAI/blob/main/Dokumentaatio/Kuvat/ShakkiAI_coverage_report.png)

## Miten testit on suoritettu
Kaikki testit ovat suoritettu Pythonin unittest moduulilla simuloiden pelitilanteita ja tutkimalla vastaavatko tilanteet odotuksia kun suoritetaan funktiot. Testeissä on tutkittu shakki tilanteita ja shakkimatti tilanteita. Shakkibottia on testattu, että se osaa tehdä shakkimatin testeillä vain kerran, koska sen testit vievät aikaa. Shakin tekoälyä ja sitä miten se saa tehtyä shakkimatin on kuitenkin tutkittu kattavasti testaamalla sen liikkeitä ihmispelaajaa vastaan kokeilemalla shakin peluuta. 

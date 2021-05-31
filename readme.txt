Aufgabe der Wetterstation ist es, die aktuellen und in der Vergangenheit aufgezeichneten Wetterdaten auf einem Web-Interface darzustellen.
Dabei werden folgende Daten erfasst und gespeichert: Datum, Uhrzeit, Lufttemperatur, Luftfeuchte, Luftdruck und Windgeschwindigkeit.

Die Daten werden in einer CSV-Datei gespeichert und zur Zeit über ein Gnuplot-Script ausgelesen. Ziel ist es, die Daten in einer SQL-Daten-
bank abzulegen und über eine Javascript-Weboberfläche interaktiv anzuzeigen.

Die Energieversorgung erfolgt vorerst über Akkus, später sollen diese über eine Solarzelle wieder aufgeladen werden bzw. die Laufzeit
verlängert werden.

To-Do-Liste:

Software:
- Windmesser in Datenerfassung integrieren, alle Daten in CSV-Datei schreiben
- Erfassungszeitraum auf 1 Minute anpassen - Winddaten in Durchschnitt und Spitzenwert getrennt
- LED-Blinkmuster vorbereiten (aus - an - alle blinken - Umlauflicht) - eigene LED include vorbereiten
- SQL-Server installieren (MariaDB und Lighttpd?)
- PHPMyAdmin installieren und DB vorbereiten
- Daten in DB schreiben
- Webserver installieren
- Daten auslesen und darstellen über JS
- Schalter für "Daten Echtzeit - 1 Stunde - 3 Stunden - 6 Stunden - 12 Stunden - 24 Stunden - 48 Stunden - 72 Stunden - 1 Woche - 1 Monat
- Software-SChalter für LED (aus - Dauerlicht - alle blinken - Umlauflicht)


Hardware-Module:
- Mastverbinder (Status: Entwurf auf Papier)
- Powerpack (Status: Entwurf auf Papier)
- LED-Ring (Status: Entwurf auf Papier)
- Controller (Status: Entwurf auf Papier)
- Sensorkopf (Status: Entwurf auf Papier)
- Verbindung der Module untereinander
- Verkabelung der Module
- Befestigung auf Mast

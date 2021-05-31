# !/usr/bin/env python3
# Test der Wetterstation
import bme280
import smbus2
from time import strftime
from time import sleep
from os import system
import sys

# Adresse und Port des BME280 setzen
port = 1
address = 0x76
bus = smbus2.SMBus(port)

# Fenstertitel setzen
sys.stdout.write('\33]0;Wetterdaten\a')
sys.stdout.flush()

# Setzen von Variablen
# druck = 1013.3 kommt von BME280
# tempLuft = 20.0 kommt von BME280
tempBoden = 18.1
wind = 3.8
# luftfeucht = 80.0 kommt von BME280

intervall = 5


try:
	while True :
		tempLuft,druck,luftfeucht = bme280.readBME280All() #Hole Daten vom BME280
		system("clear") #Start des Hauptprogrammes, sende "clear" an Konsole
		zeit = strftime("%d.%m.%Y %H:%M") #generiere Anzeig-Zeit-String
		dbzeit = strftime("%d.%m.%Y %H:%M:%S") #generiere Datenbank-Zeit-String 
		print("Datum und Uhrzeit:", zeit)
		
		dtg = strftime("%d%H%M%b%y") # generiere Taktische Zeit-String
		print("Taktische Zeit:   ", dtg)
		
		print("\nWetterdaten:") # rufe Wetterdaten ab und zeige sie an
		print("Luftdruck:        %6.2f mBar" % druck)
		print("Lufttemperatur:     %6.2f °C" % tempLuft)
		# print("Bodentemperatur:  ", tempBoden, "°C (Beispielwert!)")
		print("Luftfeuchtigkeit:   %6.2f " % luftfeucht)
		# print("Windstärke:       ", wind, "m/s (Beispielwert!)")
		
		# Schreibe Wetterdaten und Uhrzeit in eine Datei
		speicherdaten = dbzeit+";"+str("%6.2f" % druck)+";"+str("%6.2f" % tempLuft)+";"+str("%6.2f" % tempBoden)+";"+str("%6.2f" % luftfeucht)+";"+str(wind)+"\n"
		with open("wetter.dat", "a") as datei:
			datei.write(speicherdaten)
			datei.closed
		
		druck = druck + 0.1
		
		sleep(intervall) #warte das definierte Intervall ab
		
except KeyboardInterrupt: #Ausnahme: Programm aus Dauerschleife werfen mit Strg + C 
		print("Programm beendet!")

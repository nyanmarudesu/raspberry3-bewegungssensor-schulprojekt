# Import der notwendigen Bibliotheken
import RPi.GPIO as GPIO
import time
import requests
import json

# Setzen des GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Setzen der PIN-Nummer
PIR_PIN = 23

# Setzen des PINs als Eingangspin
GPIO.setup(PIR_PIN, GPIO.IN)

def initialize_sensor():
    """
    Initialisiert den Bewegungssensor und überprüft, ob er korrekt angeschlossen ist.
    """
    try:
        time.sleep(2) # Wait for sensor to stabilize
        # Erstes Lesen vom PIN zum Überprüfen der Verbindung
        if GPIO.input(PIR_PIN) == 0: 
            print("Sensor verbunden und betriebsbereit")
            return True
        else:
            print("Fehler bei der Initialisierung des Sensors")
            return False
    except Exception as e:
        print(f"Es trat ein Fehler auf: {e}")
        return False


def detect_movement():
    """
    Überprüft kontinuierlich, ob eine Bewegung erkannt wird.
    """
    while True:
        if GPIO.input(PIR_PIN):
            print("Bewegung erkannt!")
            requests.post("https://ntfy.sh/monitoringmovement",
            data="Bewegung erkannt!",
            headers={
                "Title": "Sensor Bewegung erkannt!",
                "Priority": "urgent",
                "Tags": "warning,skull"
            })
            time.sleep(4)

def main():
    """
    Hauptfunktion, die die Initialisierung und Bewegungserkennung durchführt.
    """
    if initialize_sensor():
        detect_movement()

# Ausführung der Hauptfunktion
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programm durch Benutzer beendet")
    finally:
        # Aufräumen der GPIO-Einstellungen
        GPIO.cleanup()

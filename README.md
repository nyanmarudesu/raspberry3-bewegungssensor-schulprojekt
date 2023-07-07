# Bewegungserkennung mit dem HC-SR501 und Raspberry Pi

Dieses Python-Script verwendet den HC-SR501 Bewegungssensor in Verbindung mit einem Raspberry Pi, um Bewegungen zu erkennen. Bei Erkennung einer Bewegung wird eine Benachrichtigung an die URL https://ntfy.sh/monitoringmovement-
## Hardware-Setup
Die Hardware-Komponenten für dieses Projekt sind:
1.	Raspberry Pi
2.	HC-SR501 Bewegungssensor
3.	Jumper-Kabel

Der Sensor HC-SR501 wird folgendermaßen mit dem Raspberry Pi verbunden:
•	Der VCC-Pin des Sensors wird mit dem 5V-Pin des Raspberry Pi verbunden.
•	Der GND-Pin des Sensors wird mit einem der GND-Pins des Raspberry Pi verbunden.
•	Der OUT-Pin des Sensors wird mit dem GPIO 23 des Raspberry Pi verbunden.

## Software-Setup
### Python und pip
Zunächst müssen wir die notwendigen Softwarepakete installieren. Dazu gehören Python (Version 3.5 oder höher), das Python-Paketverwaltungssystem pip und die benötigten Python-Bibliotheken.

Wenn Python und pip noch nicht auf Ihrem System installiert sind, können Sie diese wie folgt installieren:
### Für Linux und macOS:
1. Öffnen Sie ein Terminalfenster.
2. Führen Sie den Befehl ``python --version`` oder ``python3 --version`` aus, um zu überprüfen, ob Python bereits installiert ist.
3. Führen Sie den Befehl ``pip --version`` oder ``pip3 --version`` aus, um zu überprüfen, ob pip bereits installiert ist.
4. Wenn Python oder pip nicht installiert sind, können Sie Python hier herunterladen und installieren. Pip wird zusammen mit Python installiert

### Für Windows:
1. Öffnen Sie die Befehlszeile (cmd).
2. Führen Sie den Befehl ``py --version`` oder ``python --version``aus, um zu überprüfen, ob Python bereits installiert ist.
3. Führen Sie den Befehl ``py -m pip --version`` aus, um zu überprüfen, ob pip bereits installiert ist.
4. Wenn Python oder pip nicht installiert sind, können Sie Python hier herunterladen und installieren. Pip wird zusammen mit Python installiert.

### Python-Bibliotheken
Das Python-Script verwendet die RPi.GPIO-Bibliothek, um die GPIO-Pins des Raspberry Pi zu steuern, und die requests-Bibliothek, um HTTP-Requests zu senden. Beide Bibliotheken können mit pip installiert werden:
``pip install RPi.GPIO requests``
Das Modul time und json sind in der Python Standardbibliothek enthalten und benötigen keine separate Installation.

## NTFY
NTFY ist eine einfache, effektive und kostenlose Benachrichtigungs-Dienstleistung. Es erlaubt Nutzern, Echtzeit-Benachrichtigungen auf einer Vielzahl von Plattformen zu empfangen. Darunter fallen iOS und Android, aber auch Desktop-Betriebssysteme und Webbrowser. In dieser Anwendung wird ntfy dazu verwendet, um Benachrichtigungen auszusenden, wenn unser Bewegungssensor Bewegung erkennt.

In unserem Skript verwenden wir NTFY, um eine Benachrichtigung an die URL https://ntfy.sh/monitoringmovement zu senden, wenn eine Bewegung erkannt wird. Diese Benachrichtigung kann dann von anderen Diensten oder Anwendungen, die mit NTFY verbunden sind, abgerufen und angezeigt werden.
NTFY hat auch mobile Anwendungen für iOS und Android. Die Apps sind kostenlos und ermöglichen es Ihnen, Benachrichtigungen direkt auf Ihr Mobilgerät zu erhalten. Dies kann besonders nützlich sein, wenn Sie Ihr Skript auf einem Server oder einem anderen entfernten System ausführen und Benachrichtigungen über Ereignisse oder Zustände direkt auf Ihr Mobilgerät erhalten möchten.

## Script-Beschreibung
Das Script beginnt mit der Initialisierung des Sensors. Wenn die Initialisierung erfolgreich ist, beginnt es, kontinuierlich auf Bewegungen zu prüfen. Bei Erkennung einer Bewegung sendet es eine HTTP POST-Anfrage an https://ntfy.sh/monitoringmovement und an einen Microsoft Teams-Webhook.

### Ausführung des Scripts
Das Script kann mit Python 3 ausgeführt werden:
``python3 app.py`` oder ``python app.py``
### Fehlerbehandlung
Das Script behandelt zwei Arten von Fehlern:
•	Wenn beim Initialisieren des Sensors ein Fehler auftritt, wird eine Fehlermeldung gedruckt und das Script beendet.
•	Wenn das Script durch einen KeyboardInterrupt beendet wird (z.B. durch Drücken von CTRL+C), wird eine Meldung gedruckt und die GPIO-Einstellungen werden bereinigt.


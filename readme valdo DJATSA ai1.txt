                          Meine KI für das normale Vier gewinnt (Valdo Djatsa)

Dieses Projekt implementiert das Spiel Vier Gewinnt (Connect Four) mit einem KI-Spieler, der den Minimax-Algorithmus verwendet, um den besten Zug zu berechnen.
 
Der Code in der Datei ai1.py ist eine KI, welche für eine gegebene Spielsituation  den Funktion ´??``ai´´ benutzt, um selbstständig den nächsten Zug zu  planen und auszuführen.

## Voraussetzungen

- Python ( Version 3.8 oder höhre Versionen)
- Numpy-Bibliothek für die Verarbeitung von Arrays
- Time-Bibliothek für die Berechnung der Ausführungszeit
- logging-Bibliothek für die Berechnung der Ausführungszeit


## Dateistruktur

- `vier_gewinnt.py`: Hauptprogramm mit dem Vier-Gewinnt-Spiel
- `helper.py`: Hilfsfunktionen, die von `vier_gewinnt.py` verwendet werden.
- `log.txt`: Log-Datei, in der der Spielfortschritt protokolliert wird.
- `config.py`: Enthält wichtige Konstante und Parameter (durch Einkommentieren der Zeile         "logging.basicConfig(level=logging.DEBUG, format='%(message)s')" können Sie das Spielfeld anzeigen)
- `ai1.py`: Der Datei, meiner stärktersten  KI  
- `ai2.py`: Der Datei, mit der KI, die ich genutzt habe, um meiner zu testen   
- `ai3`:Der Datei, indem ich die anderen KIs (leichsten) gespeichert habe.

## Spiel starten

Führen Sie das Programm `vier_gewinnt.py` aus und folgen Sie den Anweisungen auf der Konsole, um das Spiel zu spielen.

## Konfiguration der KI

Die KI verwendet den Minimax-Algorithmus für die Berechnung der Züge. Die Suchtiefe kann in der Funktion `ai` in `vier_gewinnt.py` angepasst werden.

## Funktionen

- `evaluate_window(window, player)`: Bewertet den Punktestand eines Fensters für einen bestimmten Spieler.
- `score_position(arr, player)`: Bewertet das gesamte Spielfeld für einen bestimmten Spieler.
- `get_next_empty_row(arr, col)`: Gibt die nächste leere Reihe in einer Spalte zurück.
- `drop_piece(arr, row, col, player)`: Setzt einen Spielstein in das Spielfeld.
- `is_winner(arr)`: Überprüft, ob ein Spieler gewonnen hat.
- `is_winning_move(arr, move, player)`: Überprüft, ob ein Zug zu einem Gewinn führt.
- `minimax(arr, depth, maximizing_player, alpha, beta, player)`: Implementiert den Minimax-Algorithmus.
- `log_progress(arr)`: Schreibt den Spielfortschritt in die Datei `log.txt`.
- `ai(arr, player)`: KI-Funktion, die den besten Zug für den KI-Spieler berechnet und ausführt.

## Log-Datei

Der Spielfortschritt wird in der Datei `log.txt` protokolliert. Diese Datei enthält den aktuellen Spielstand in Form einer Spieltafel.

## 

- [Valdo DJATSA]

Genießen Sie das Spiel!

 ## Resourcen
  Benotete Aufgabe 2  und die angegeben Frameworks von Herr Prof Thomas Nierhoff
  Python Standard Library
  https://www.javatpoint.com/mini-max-algorithm-in-ai
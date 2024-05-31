vier_gewinnt.py startet das Hauptprogramm (z.B. mittels "python vier_gewinnt.py")

config.py enthält wichtige Konstante und Parameter, welche (zumindest vor der finalen Einreichung) geändert werden dürfen
- durch Einkommentieren der Zeile "logging.basicConfig(level=logging.DEBUG, format='%(message)s')" können Sie das Spielfeld anzeigen
- N_GAMES_PLAYED legt fest, wieviele Spiele insgesamt gespielt werden
- PLAYER_1_TYPE / PLAYER_2_TYPE legt fest, wer gegeneinander spielt. So können Sie z.B. Spiele KI vs. KI oder KI vs. human spielen

helper.py enthält Hilfsfunktionen wie "Stein legen", "Status anzeigen", etc... Sie dürfen die Funktionen in dieser Datei gerne für ihre eigene KI verwenden

ai1.py und ai2.py sind die Dateien, in denen Sie ihre verschiedenen Versionen der KI implementieren und gegeneinander antreten lassen können
- der Code in der Funktion "ai" in ai1.py und ai2.py soll durch ihre eigene Implementierung überschrieben werden

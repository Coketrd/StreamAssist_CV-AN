@service
async def download_and_get_duration_streamassist(mp3_url=None):
    import aiohttp
    import io
    import os
    from mutagen.mp3 import MP3

    output_path = "/config/pyscript/url_streamassist.mp3"

    async def debug_print(message):
        print(message)  # Verwende print für Protokollausgaben

    if not mp3_url:
        debug_print("Keine MP3-URL bereitgestellt.")
        return

    try:
        # Herunterladen der MP3-Datei
        async with aiohttp.ClientSession() as session:
            async with session.get(mp3_url) as response:
                if response.status == 200:
                    debug_print("Datei erfolgreich heruntergeladen.")
                    content = response.read()  # Lese die Daten aus der Antwort

                    # Schreib die Datei auf die Festplatte
                    with io.open(output_path, 'wb') as f:
                        f.write(content)

                    # Überprüfen, ob die Datei gespeichert wurde
                    if os.path.exists(output_path):
                        debug_print(f"Temporäre Datei wurde erfolgreich unter {output_path} gespeichert.")
                    else:
                        debug_print(f"Temporäre Datei wurde nicht gefunden unter {output_path}.")
                        return

                    # Auslesen der Dauer der MP3-Datei
                    try:
                        audio = MP3(output_path)
                        duration_seconds = audio.info.length
                        debug_print(f"Die Dauer der MP3-Datei beträgt {duration_seconds} Sekunden.")

                        # Zusätzliche Sekunden basierend auf der Länge hinzufügen
                        if duration_seconds < 10:
                            duration_seconds += 2
                        elif 10 <= duration_seconds < 20:
                            duration_seconds += 3
                        elif 20 <= duration_seconds < 30:
                            duration_seconds += 4

                        debug_print(f"Die angepasste Dauer beträgt {duration_seconds} Sekunden.")

                        # Setzen der Dauer im Timer
                        service.call("timer", "start", entity_id="timer.extract_mp3_time_streamassist", duration=duration_seconds)
                    except Exception as e:
                        debug_print(f"Fehler beim Auslesen der MP3-Dauer: {e}")
                else:
                    debug_print(f"Fehler beim Herunterladen der Datei. Statuscode: {response.status}")
    except Exception as e:
        debug_print(f"Fehler im Skript: {e}")

"""Runs the actual extracted detector with synthetic level frames; no microphone."""
from turns import TurnDetector


def scenario(frames):
    detector = TurnDetector()
    events = []
    for level, milliseconds in frames:
        event = detector.feed(level, milliseconds)
        if event is not None:
            events.append(event)
    return events


SCENARIOS = {
    'Ruido corto: descartar': [(0.001, 100), (0.1, 100), (0.001, 900)],
    'Voz suficiente: cerrar turno': [(0.001, 100), (0.1, 100), (0.1, 200), (0.001, 900)],
    'Silencio: no enviar': [(0.001, 100)] * 20,
    'Limite temporal: cerrar': [(0.001, 100), (0.1, 100), (0.1, 29900)],
}

if __name__ == '__main__':
    print('KarpezVoz: componente real; niveles sinteticos; sin microfono, ASR, LLM ni TTS.')
    for label, frames in SCENARIOS.items():
        print(f'{label}: {scenario(frames)}')

import random
from major_chord_generator import generate_major_chords
from minor_chord_generator import generate_minor_chords

def search(symbol):
    # Dictionary mapping note symbols to MIDI note numbers for major and minor keys
    note_mapping = {
        'C': 48, 'Cm': 48, 'C#': 49, 'C#m': 49,
        'Db': 49, 'Dbm': 49, 'D': 50, 'Dm': 50,
        'D#': 51, 'D#m': 51, 'Eb': 51, 'Ebm': 51,
        'E': 52, 'Em': 52, 'F': 53, 'Fm': 53,
        'F#': 54, 'F#m': 54, 'Gb': 54, 'Gbm': 54,
        'G': 55, 'Gm': 55, 'G#': 56, 'G#m': 56,
        'Ab': 56, 'Abm': 56, 'A': 45, 'Am': 45,
        'A#': 46, 'A#m': 46, 'Bb': 46, 'Bbm': 46,
        'B': 47, 'Bm': 47
    }
    return note_mapping.get(symbol, None)


def generate_chords(scale_chords, num_bars):
    chords = []
    maxi = search(scale_chords[0])
    for symbol in scale_chords:
        if len(symbol) == 1: 
            root = search(symbol)
            if root is not None:
                chords.extend(generate_major_chords(root,maxi))
            else:
                print(f"Ignoring invalid chord symbol: {symbol}")
        elif len(symbol) >= 2:
            root = search(symbol)
            if root is not None:
                chords.extend(generate_minor_chords(root,maxi))
            else:
                print(f"Ignoring invalid chord symbol: {symbol}")
        else:
            print(f"Ignoring invalid chord symbol: {symbol}")
    
    # Extend chords list until it reaches the desired number of bars
    while len(chords) < num_bars:
        random_chord = random.choice(chords)
        chords.append(random_chord)
    
    return chords[:num_bars]  # Truncate to the desired number of bars

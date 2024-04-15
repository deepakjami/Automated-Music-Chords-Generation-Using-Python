import random

# Define the keys and their respective major and minor scales in the circle of fifths
circle_of_fifths = {
    "C": [["C", "Dm", "Em", "F", "G", "Am"], ["Cm", "Eb", "Fm", "Gm", "Ab"]],
    "G": [["G", "Am", "Bm", "C", "D", "Em"], ["Gm", "Am", "Bb", "Cm", "Dm", "Eb"]],
    "D": [["D", "Em", "F#m", "G", "A", "Bm"], ["Dm", "Em", "F", "Gm", "Am", "Bb"]],
    "A": [["A", "Bm", "C#m", "D", "E", "F#m"], ["Am", "Bm", "C", "Dm", "Em", "F"]],
    "E": [["E", "F#m", "G#m", "A", "B", "C#m"], ["Em", "F#m", "G", "Am", "Bm", "C"]],
    "B": [["B", "C#m", "D#m", "E", "F#", "G#m"], ["Bm", "C#m", "D", "Em", "F#m", "G"]],
    "F#": [["F#", "G#m", "A#m", "B", "C#", "D#m"], ["F#m", "G#m", "A", "Bm", "C#m", "D"]],
    "C#": [["C#", "D#m", "Fm", "F#", "G#", "A#m"], ["C#m", "D#m", "E", "F#m", "G#m", "A"]],
    "D#" :[["D#", "Fm", "Gm", "A#", "Cm", "Dm"],["D#m", "Fm", "G#", "A#m", "C#", "D#"]],
    "G#" :[["G#", "A#m", "Cm", "D#", "Fm", "Gm"],["G#m", "A#m", "B", "D#m", "F#m", "G#"]],
    "A#" :[["A#", "Cm", "Dm", "F", "Gm", "Am"],["A#m", "Cm", "C#", "D#m", "Fm", "G#"]],
    "F": [["F", "Gm", "Am", "A#", "C", "Dm"], ["Fm", "Gm", "Ab", "Bbm", "Cm", "Db"]],
    "Bb": [["Bb", "Cm", "Dm", "Eb", "F", "Gm"], ["Bbm", "Cm", "Db", "Ebm", "Fm", "Gb"]],
    "Eb": [["Eb", "Fm", "Gm", "Ab", "Bb", "Cm"], ["Ebm", "Fm", "Gb", "Abm", "Bb", "Cb"]],
    "Ab": [["Ab", "Bbm", "Cm", "Db", "Eb", "Fm"], ["Abm", "Bbm", "Cb", "Dbm", "Ebm", "Fb"]],
    "Db": [["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm"], ["Dbm", "Ebm", "E", "Fbm", "Gbm", "Ab"]],
    "Gb": [["Gb", "Abm", "Bbm", "B", "Db", "Ebm"], ["Gbm", "Abm", "A", "Bbm", "Cbm", "Db"]],
    "Cb": [["Cb", "Dbm", "Ebm", "E", "Gb", "Abm"], ["Cbm", "Dbm", "D", "Ebm", "Fbm", "Gb"]],
}

def generate_scale_chords(key, scale_type, num_bars):
    scale = circle_of_fifths.get(key)[scale_type]
    main_key_chord = scale[0]
    
    # For 4 bars
    if num_bars == 4:
        chords = [main_key_chord]
        while len(chords) < 4:
            chord = random.choice(scale[1:])
            if chord not in chords:
                chords.append(chord)
    
    # For 8 bars
    elif num_bars == 8:
        chords = [main_key_chord]
        repeat_chords = random.sample(scale[1:], 3)
        for i in range(3):
            chords.append(repeat_chords[i])
        chords.extend(chords[:3])
        unique_chords = set(chords)
        while len(chords) < 8:
            random_chord = random.choice(scale[1:])
            if random_chord not in unique_chords:
                chords.append(random_chord)
            unique_chords.add(random_chord)
    
    return chords

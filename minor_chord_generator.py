def generate_minor_chords(root_note,maximum):
    minor_chords = []
    root_note -= 12
    minor_third = root_note + 3
    perfect_fifth = root_note + 7
    f = True
    if root_note + 12 <= maximum:
        f = False
        root_note += 12
    elif ((minor_third + 12) <= maximum) and f:
        minor_third_third += 12
        f = False
    if f :
        perfect_fifth -= 12
    minor_chord = [root_note -12,root_note + 12, minor_third + 12, perfect_fifth + 12
    minor_chords.append(minor_chord)
    return minor_chords

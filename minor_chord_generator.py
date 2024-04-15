def generate_minor_chords(root_note,maximum):
    minor_chords = []
    # Calculate the minor third and perfect fifth relative to the root note
    root_note -= 12
    minor_third = root_note + 3
    perfect_fifth = root_note + 7
    # Construct the minor chord using the root note, minor third, and perfect fifth
    f = True
    if root_note + 12 <= maximum:
        f = False
        root_note += 12
    elif ((minor_third + 12) <= maximum) and f:
        minor_third_third += 12
        f = False
    if f :
        perfect_fifth -= 12

    minor_chord = [root_note -12,root_note + 12, minor_third + 12, perfect_fifth + 12]
    # Append the minor chord to the list of minor chords
    minor_chords.append(minor_chord)
    return minor_chords

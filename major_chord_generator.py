def generate_major_chords(root_note,maximum):
    major_chords = []
    # Calculate the major third and perfect fifth relative to the root note
    root_note -= 12
    major_third = root_note + 4
    perfect_fifth = root_note + 7
    # Construct the major chord using the root note, major third, and perfect fifth

    f = True
    if root_note + 12 <= maximum:
        f = False
        root_note += 12
    elif ((major_third + 12) <= maximum) and f:
        major_third += 12
        f = False
    if f:
        perfect_fifth -= 12
    
    major_chord = [root_note -12,root_note + 12, major_third + 12, perfect_fifth + 12]
    # Append the major chord to the list of major chords
    major_chords.append(major_chord)
    return major_chords

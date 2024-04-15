import random
from midiutil import MIDIFile

def create_midi_file(note_list, output_file):
    # Create a MIDI file with one track
    midi_file = MIDIFile(1)

    # Add track name and tempo
    track = 0
    time = 0
    midi_file.addTrackName(track, time, "Track 0")
    midi_file.addTempo(track, time, 120)  # 120 BPM (beats per minute)

    # Define notes and their duration
    duration = 4  # 4 beats for 1 bar
    channel = 0  # MIDI channel (0-15)

    # Add notes to the MIDI file
    for chord_notes in note_list:
        for note in chord_notes:
            velocity = random.randint(70, 90)  # Random velocity between 60 to 100 for each note
            midi_file.addNote(track, channel, note, time, duration, velocity)
        time += duration  # Move time forward by 4 beats for each chord

    # Write the MIDI data to a file
    with open(output_file, "wb") as f:
        midi_file.writeFile(f)

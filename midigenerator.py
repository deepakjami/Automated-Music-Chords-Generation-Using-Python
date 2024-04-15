import random
from midiutil import MIDIFile

def create_midi_file(note_list, output_file):
    midi_file = MIDIFile(1)
    track = 0
    time = 0
    midi_file.addTrackName(track, time, "Track 0")
    midi_file.addTempo(track, time, 120)
    duration = 4  
    channel = 0  
    for chord_notes in note_list:
        for note in chord_notes:
            velocity = random.randint(70, 90)  
            midi_file.addNote(track, channel, note, time, duration, velocity)
        time += duration
    with open(output_file, "wb") as f:
        midi_file.writeFile(f)

import random
from circle_of_fifth import circle_of_fifths, generate_scale_chords
from generator import generate_chords
from midigenerator import create_midi_file

def main():
    print("Welcome to the Scale Chord Generator!")
    print("-------------------------------------")

    key = input("Enter your favorite key (e.g., C, G, D): ").strip().capitalize()
    scale_type = int(input("Enter 0 for major scale, 1 for minor scale: "))
    num_bars = int(input("Enter the number of bars (4 or 8): "))

    if key in circle_of_fifths:
        scale_chords = generate_scale_chords(key, scale_type, num_bars)
        scale_name = "major" if scale_type == 0 else "minor"
        print(f"The generated {key} {scale_name} scale chords with {num_bars} bars are: {', '.join(scale_chords)}")
    else:
        print("Invalid key. Please enter a valid key from the circle of fifths.")
    chords = generate_chords(scale_chords,num_bars)
    print("Generated Chords:")
    print(chords)
    output_file = "output.mid"
    create_midi_file(chords, output_file) 


if __name__ == "__main__":
    main()

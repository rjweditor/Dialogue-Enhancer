import separation_anxiety

def main():
    # Example file paths (update these paths to actual files on your system)
    input_file = 'path/to/input/audiofile.wav'
    output_directory = 'path/to/output/directory'

    # Call the function from the shared object file
    try:
        # Assuming separation_anxiety has a function named 'separate_audio'
        result = separation_anxiety.separate_audio(input_file, output_directory)
        print(f"Separation completed successfully. Output is saved in: {output_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

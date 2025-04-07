import sys

def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False
    
    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def edit_input_file(file_path):
    """Allow the user to modify the contents of the input file."""
    print("\n***** Interactive Mode *****")
    print("Enter your new content below. Press Enter twice to finish.\n")

    new_lines = []
    while True:
        line = input()
        if line == "":
            break
        new_lines.append(line)

    try:
        with open(file_path, 'w') as file:
            file.write("\n".join(new_lines))
        print(f"\n Successfully updated {file_path}\n")
    except Exception as e:
        print(f"Error updating file: {e}")

def main(input_file="input.txt", output_file="output.txt"):
    """Main function to process a text file."""

    if sys.stdin.isatty():
        print("Do you want to edit the input file before processing? (y/n): ", end="")
        choice = input().strip().lower()

        if choice == 'y':
            input_file = "custom-input.txt"
            output_file = "custom-output.txt"
            edit_input_file(input_file)

    text = read_file(input_file)
    if text:
        results = process_text(text)
        if results:
            success = write_results(results, output_file)
            if success:
                print(f"Processing complete. Results written to {output_file}")
                return True
    
    print("Processing failed.")
    return False

if __name__ == "__main__":
    main()
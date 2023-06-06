# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line

import sys

def main():
    # Read text from stdin
    text = sys.stdin.read().strip()

    # Filter character given as an argument from the text
    if len(sys.argv) < 2:
        print("Usage: python main.py <character>", file=sys.stderr)
        return
    
    char = sys.argv[1]
    filtered_text = text.replace(char, '')

    # Print the result to stdout
    print(filtered_text)

    # Print the total number of removed characters to stderr
    removed_count = len(text) - len(filtered_text)
    print(removed_count, file=sys.stderr)


if __name__ == "__main__":
    main()


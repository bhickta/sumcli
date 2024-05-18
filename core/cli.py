import sys
from .document import Document
import os
import pyperclip

def main():
    if len(sys.argv) < 2:
        print("Usage: mycli <path>")
        sys.exit(1)

    path_from_cli = sys.argv[1]

    summary = Document(os.path.join(path_from_cli))
    summary_text = summary.summary

    pyperclip.copy(summary_text)

    print("Summary copied to clipboard:")
    print(summary_text)

if __name__ == "__main__":
    main()

import sys
from .document import Document
import os
import pyperclip

def main():
    summary = Document()
    summary_text = summary.summary

    pyperclip.copy(summary_text)

    print("Summary copied to clipboard:")

if __name__ == "__main__":
    main()

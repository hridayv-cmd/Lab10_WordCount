"""
Program: Word Count Analyzer
Author: Your Name
Purpose: An OOP-based program that reads a user-selected text file, filters out 
         punctuation and normalizes text, counts word frequencies, and prints 
         an alphabetical report.
Starter Code: None (Built entirely based on Lab 10 requirements)
Date: July 3, 2026
"""

import string
from pathlib import Path

class WordAnalyzer:
    def __init__(self, filepath: str):
        """
        Initializes the analyzer with a private Path object 
        and a private dictionary for frequencies.
        """
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self) -> bool:
        """
        Main logic to read and parse the file. Uses a try-except block,
        removes all standard and smart punctuation, and updates counts.
        """
        try:
            # Check if file exists using pathlib
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            # Combine standard punctuation with custom smart quotes/bullets
            extra_punctuation = "“”‘’•—’‘"
            all_punctuation = string.punctuation + extra_punctuation
            
            # Create a translation table to strip out all punctuation completely
            translator = str.maketrans('', '', all_punctuation)
            
            # Open and process line by line
            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    # Replace double hyphens with a space to prevent fused words
                    cleaned_line = line.replace('--', ' ')
                    
                    # Clean line: convert to lowercase and remove punctuation strings
                    cleaned_line = cleaned_line.lower().translate(translator)
                    words = cleaned_line.split()
                    
                    for word in words:
                        # Extra protection to clean individual trailing/leading strays
                        word = word.strip()
                        if word:
                            self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            return True
            
        except FileNotFoundError:
            print(f"Error: The file '{self.__filepath.name}' was not found.")
            return False

    def print_report(self):
        """
        Sorts the words alphabetically and prints them in the specified format.
        """
        if not self.__frequencies:
            print("No data to report.")
            return

        # Sort keys alphabetically
        sorted_words = sorted(self.__frequencies.keys())
        
        for word in sorted_words:
            # Matches the exact spacing format from the example output: word  :: count
            print(f"{word:<15} :: {self.__frequencies[word]}")


def main():
    # File dictionary mapping menu keys to Path objects
    files_menu = {
        "1": Path("tarzan.txt"),
        "2": Path("princess_mars.txt"),
        "3": Path("monte_cristo.txt"),
        "4": Path("treasure_island.txt")
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. Tarzan")
        print("2. Princess of Mars")
        print("3. Monte Cristo")
        print("4. Treasure Island")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice in files_menu:
            target_path = files_menu[choice]
            
            # Print the header exactly matching assignment instructions
            print(f"\nProcessing '{target_path.name}'...\n")
            
            # Instantiate the OOP Class
            analyzer = WordAnalyzer(str(target_path))
            
            # If successful, print the report
            if analyzer.process_file():
                analyzer.print_report()
                
            print() # Clear line for look
            input("Press Enter to return to the menu... ")
            
        elif choice == '5':
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu... ")

if __name__ == "__main__":
    main()
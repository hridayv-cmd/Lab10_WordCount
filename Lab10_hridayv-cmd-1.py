"""
Program: Word Count Analyzer
Author: Your Name
Purpose: An OOP-based program that reads a user-selected text file, filters out 
         punctuation and normalizes text, counts word frequencies, and prints 
         an alphabetical report.
Starter Code: None (Built entirely based on Lab 10 requirements)
Date: July 3, 2026
"""
from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath: str):
        """
        Initializes the WordAnalyzer with a private Path object and an empty
        dictionary for tracking word frequencies.
        """
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self) -> bool:
        """
        Main data processing logic. Reads the file line by line, cleans text,
        and updates the word frequency dictionary.
        
        Returns:
            bool: True if processing succeeded, False if FileNotFoundError occurred.
        """
        try:
            # Explicitly checking for existence using Path.exists()
            if not self.__filepath.exists():
                raise FileNotFoundError
            # Creating a translation table to strip punctuation
            # string.punctuation contains characters like !, ., ?, etc.
            translator = str.maketrans('', '', string.punctuation)

            # Using Path.open() to read line by line safely
            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    # Convert to lowercase and remove punctuation
                    cleaned_line = line.lower().translate(translator)
                    # Split line into an array of individual words
                    words = cleaned_line.split()
                    
                    for word in words:
                        # Increment or set word count
                        self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
                # Mission success: returns True after the loops finish reading everything
            return True
            
        except FileNotFoundError:
            print(f"\nError: The file '{self.__filepath.name}' could not be found.")
            return False

    def print_report(self):
        """
        Sorts the accumulated frequencies alphabetically and prints them 
        in a clean, readable column format.
        """
        if not self.__frequencies:
            print("No data to report.")
            return

        # Sort the dictionary keys alphabetically
        sorted_words = sorted(self.__frequencies.keys())

        print(f"\n--- Word Frequency Report: {self.__filepath.name} ---")
        for word in sorted_words:
            # Using left alignment formatting to mimic the assignment layout
            print(f"{word:<15} :: {self.__frequencies[word]}")
        print("-" * 40)
        def main():
    # Constructing paths safely using pathlib
    # Assumes text files sit in the same directory as this script
            file_options = {
                "1": {"name": "Princess of Mars", "path": Path("princess_mars.txt")},
                "2": {"name": "Tarzan", "path": Path("Tarzan.txt")},
                "3": {"name": "Treasure Island", "path": Path("treasure_island.txt")},
                "4": {"name": "Count of Monte Cristo", "path": Path("monte_cristo.txt")}
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        # Displaying menu dynamically without file extensions (.txt)
        for key, item in file_options.items():
            print(f"{key}. {item['name']}")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break
        
        elif choice in file_options:
            selected_file = file_options[choice]
            print(f"\nProcessing '{selected_file['path'].name}'...")
            
            # Instantiating the OOP object with the path string
            analyzer = WordAnalyzer(str(selected_file['path']))
            
            if analyzer.process_file():
                analyzer.print_report()
            
            input("\nPress Enter to return to the menu... ")
        
        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu... ")


if __name__ == "__main__":
    main()
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
                        return True
        except FileNotFoundError:
            print(f"\nError: The file '{self.__filepath.name}' could not be found.")
            return False
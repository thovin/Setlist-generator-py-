#Setlist generator

This is a python program that takes a series of ballroom dance song lists and generates a setlist for a dance. The setlist generated contains the name of the song and the name of the artist. The dance associated with any given song is intentionally omitted, as they are only suggestions; a number of dances can be danced to any given song. It will have no duplication unless the amount of songs requested is greater than the amount provided, dances are evenly distributed throughout, and the same dance will never play twice in a row. This program works in 4 steps:


Step 1: Import song and artist information from text files and convert it into lists


Step 2: Get the desired length of the setlist from the user


Step 3: Create a song and artist list, and fill them to the desired length using a random number generator. Keep a list of used dances and songs to ensure no duplication and even distribution of dances.


Step 4: Output song and artist lists to a text file, with songs and artists separated by semicolons and one song per line for easy importation into a spreadsheet

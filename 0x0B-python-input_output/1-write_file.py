#!/usr/bin/python3
def write_file(filename="", text=""):
    # Open the file in write mode, creating it if it doesn't exist
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file
        file.write(text)
        # Return the number of characters written
        return len(text)

# Example usage:
filename = "example.txt"
text_to_write = "Hello, this is a sample text."

characters_written = write_file(filename, text_to_write)
print(f"Number of characters written: {characters_written}")

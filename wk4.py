def modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to lowercase)
        modified_content = content.lower()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Cannot read/write the file.")

# Run the function
modify_file()


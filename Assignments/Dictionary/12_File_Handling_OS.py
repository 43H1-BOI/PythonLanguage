print("File Handling Program using OS Module")
print("=" * 70)

import os

# Get current working directory
current_dir = os.getcwd()
print(f"\nCurrent Working Directory: {current_dir}")

# Create a directory for file operations
directory_name = "test_files"
directory_path = os.path.join(current_dir, directory_name)

print(f"\n1. Creating Directory")
print("-" * 70)
if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory created: {directory_path}")
else:
    print(f"Directory already exists: {directory_path}")

# Create a file and write content
file_path = os.path.join(directory_path, "sample.txt")

print(f"\n2. Creating and Writing to File")
print("-" * 70)
try:
    with open(file_path, "w") as file:
        file.write("Hello World!\n")
        file.write("This is a file handling example.\n")
        file.write("Using OS module in Python.\n")
    print(f"File created and written: {file_path}")
except Exception as e:
    print(f"Error writing to file: {e}")

# Check if file exists
print(f"\n3. Checking File Existence")
print("-" * 70)
if os.path.exists(file_path):
    print(f"File exists: {file_path}")
else:
    print(f"File does not exist: {file_path}")

# Get file stats
print(f"\n4. File Statistics")
print("-" * 70)
if os.path.exists(file_path):
    stats = os.stat(file_path)
    print(f"File size: {stats.st_size} bytes")
    print(f"Last modified: {stats.st_mtime}")

# Read file content
print(f"\n5. Reading File Content")
print("-" * 70)
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:")
        print(content)
except Exception as e:
    print(f"Error reading file: {e}")

# Append content to file
print(f"\n6. Appending to File")
print("-" * 70)
try:
    with open(file_path, "a") as file:
        file.write("This line is appended.\n")
    print("Content appended successfully")
except Exception as e:
    print(f"Error appending to file: {e}")

# Read file line by line
print(f"\n7. Reading File Line by Line")
print("-" * 70)
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")
except Exception as e:
    print(f"Error reading file: {e}")

# List files in directory
print(f"\n8. Listing Files in Directory")
print("-" * 70)
if os.path.exists(directory_path):
    files = os.listdir(directory_path)
    print(f"Files in {directory_name}:")
    for file in files:
        print(f"  - {file}")

# Create another file
file_path2 = os.path.join(directory_path, "sample2.txt")

print(f"\n9. Creating Second File")
print("-" * 70)
try:
    with open(file_path2, "w") as file:
        file.write("Second sample file\n")
    print(f"File created: {file_path2}")
except Exception as e:
    print(f"Error: {e}")

# List all files again
print(f"\n10. Updated File List")
print("-" * 70)
files = os.listdir(directory_path)
print(f"Files in {directory_name}:")
for file in files:
    full_path = os.path.join(directory_path, file)
    if os.path.isfile(full_path):
        print(f"  - {file} (File)")
    elif os.path.isdir(full_path):
        print(f"  - {file} (Directory)")

# Get file extension
print(f"\n11. File Path Operations")
print("-" * 70)
print(f"File name: {os.path.basename(file_path)}")
print(f"Directory name: {os.path.dirname(file_path)}")
print(f"File extension: {os.path.splitext(file_path)[1]}")
print(f"File name without extension: {os.path.splitext(file_path)[0]}")

# Rename file
new_file_path = os.path.join(directory_path, "renamed_file.txt")

print(f"\n12. Renaming File")
print("-" * 70)
if os.path.exists(file_path2):
    os.rename(file_path2, new_file_path)
    print(f"File renamed from {os.path.basename(file_path2)} to {os.path.basename(new_file_path)}")

# Check absolute path
print(f"\n13. Absolute Path")
print("-" * 70)
print(f"Absolute path: {os.path.abspath(file_path)}")

# Delete file
print(f"\n14. Deleting File")
print("-" * 70)
if os.path.exists(new_file_path):
    os.remove(new_file_path)
    print(f"File deleted: {new_file_path}")

# List remaining files
print(f"\n15. Final File List")
print("-" * 70)
files = os.listdir(directory_path)
print(f"Remaining files in {directory_name}:")
for file in files:
    print(f"  - {file}")

print("\n" + "=" * 70)
print("\nFile Handling Operations Completed!")
print(f"Note: Directory '{directory_name}' and its contents remain for reference")

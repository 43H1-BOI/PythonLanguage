print("File Handling Program using OS Module")
# Output: File Handling Program using OS Module

print("=" * 70)
# Output: ======================================================================

import os

# Get current working directory
current_dir = os.getcwd()
print(f"\nCurrent Working Directory: {current_dir}")
# Output: Current Working Directory: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary

# Create a directory for file operations
directory_name = "test_files"
directory_path = os.path.join(current_dir, directory_name)

print(f"\n1. Creating Directory")
# Output: 1. Creating Directory

print("-" * 70)
# Output: ----------------------------------------------------------------------

if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory created: {directory_path}")
    # Output: Directory created: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files
else:
    print(f"Directory already exists: {directory_path}")
    # Output: Directory already exists: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files

# Create a file and write content
file_path = os.path.join(directory_path, "sample.txt")

print(f"\n2. Creating and Writing to File")
# Output: 2. Creating and Writing to File

print("-" * 70)
# Output: ----------------------------------------------------------------------

try:
    with open(file_path, "w") as file:
        file.write("Hello World!\n")
        file.write("This is a file handling example.\n")
        file.write("Using OS module in Python.\n")
    print(f"File created and written: {file_path}")
    # Output: File created and written: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files\sample.txt
except Exception as e:
    print(f"Error writing to file: {e}")

# Check if file exists
print(f"\n3. Checking File Existence")
# Output: 3. Checking File Existence

print("-" * 70)
# Output: ----------------------------------------------------------------------

if os.path.exists(file_path):
    print(f"File exists: {file_path}")
    # Output: File exists: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files\sample.txt
else:
    print(f"File does not exist: {file_path}")

# Get file stats
print(f"\n4. File Statistics")
# Output: 4. File Statistics

print("-" * 70)
# Output: ----------------------------------------------------------------------

if os.path.exists(file_path):
    stats = os.stat(file_path)
    print(f"File size: {stats.st_size} bytes")
    # Output: File size: 71 bytes
    # print(f"Last modified: {stats.st_mtime}")

# Read file content
print(f"\n5. Reading File Content")
# Output: 5. Reading File Content

print("-" * 70)
# Output: ----------------------------------------------------------------------

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:")
        # Output: File Content:
        print(content)
        # Output: Hello World!
        # Output: This is a file handling example.
        # Output: Using OS module in Python.
except Exception as e:
    print(f"Error reading file: {e}")

# Append content to file
print(f"\n6. Appending to File")
# Output: 6. Appending to File

print("-" * 70)
# Output: ----------------------------------------------------------------------

try:
    with open(file_path, "a") as file:
        file.write("This line is appended.\n")
    print("Content appended successfully")
    # Output: Content appended successfully
except Exception as e:
    print(f"Error appending to file: {e}")

# # Read file line by line
# print(f"\n7. Reading File Line by Line")
# print("-" * 70)
# try:
#     with open(file_path, "r") as file:
#         lines = file.readlines()
#         for i, line in enumerate(lines, 1):
#             print(f"Line {i}: {line.strip()}")
# except Exception as e:
#     print(f"Error reading file: {e}")

# List files in directory
print(f"\n7. Listing Files in Directory")
# Output: 7. Listing Files in Directory

print("-" * 70)
# Output: ----------------------------------------------------------------------

if os.path.exists(directory_path):
    files = os.listdir(directory_path)
    print(f"Files in {directory_name}:")
    # Output: Files in test_files:
    for file in files:
        print(f"  - {file}")
        # Output:   - sample.txt

# Create another file
file_path2 = os.path.join(directory_path, "sample2.txt")

print(f"\n8. Creating Second File")
# Output: 8. Creating Second File

print("-" * 70)
# Output: ----------------------------------------------------------------------

try:
    with open(file_path2, "w") as file:
        file.write("Second sample file\n")
    print(f"File created: {file_path2}")
    # Output: File created: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files\sample2.txt
except Exception as e:
    print(f"Error: {e}")

# # List all files again
# print(f"\n10. Updated File List")
# print("-" * 70)
# files = os.listdir(directory_path)
# print(f"Files in {directory_name}:")
# for file in files:
#     full_path = os.path.join(directory_path, file)
#     if os.path.isfile(full_path):
#         print(f"  - {file} (File)")
#     elif os.path.isdir(full_path):
#         print(f"  - {file} (Directory)")

# Get file extension
print(f"\n9. File Path Operations")
# Output: 9. File Path Operations

print("-" * 70)
# Output: ----------------------------------------------------------------------

print(f"File name: {os.path.basename(file_path)}")
# Output: File name: sample.txt

print(f"Directory name: {os.path.dirname(file_path)}")
# Output: Directory name: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files

print(f"File extension: {os.path.splitext(file_path)[1]}")
# Output: File extension: .txt

# print(f"File name without extension: {os.path.splitext(file_path)[0]}")

# Rename file
new_file_path = os.path.join(directory_path, "renamed_file.txt")

print(f"\n10. Renaming File")
# Output: 10. Renaming File

print("-" * 70)
# Output: ----------------------------------------------------------------------

if os.path.exists(file_path2):
    os.rename(file_path2, new_file_path)
    print(f"File renamed from {os.path.basename(file_path2)} to {os.path.basename(new_file_path)}")
    # Output: File renamed from sample2.txt to renamed_file.txt

# # Check absolute path
# print(f"\n13. Absolute Path")
# print("-" * 70)
# print(f"Absolute path: {os.path.abspath(file_path)}")

# Delete file
print(f"\n11. Deleting File")
# Output: 11. Deleting File

print("-" * 70)
# Output: ----------------------------------------------------------------------

if os.path.exists(new_file_path):
    os.remove(new_file_path)
    print(f"File deleted: {new_file_path}")
    # Output: File deleted: c:\Users\Abhishek\Languages\Python\Assignments\Dictionary\test_files\renamed_file.txt

# List remaining files
print(f"\n12. Final File List")
# Output: 12. Final File List

print("-" * 70)
# Output: ----------------------------------------------------------------------

files = os.listdir(directory_path)
print(f"Remaining files in {directory_name}:")
# Output: Remaining files in test_files:

for file in files:
    print(f"  - {file}")
    # Output:   - sample.txt

print("\n" + "=" * 70)
# Output: ======================================================================

print("\nFile Handling Operations Completed!")
# Output: File Handling Operations Completed!

# print(f"Note: Directory '{directory_name}' and its contents remain for reference")

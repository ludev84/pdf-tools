import os
import heapq


def find_largest_files(directory, num_files=20):
    """
    Finds and lists the 'num_files' largest files within a directory and its subdirectories.

    Args:
        directory (str): The path to the directory to search.
        num_files (int): The number of largest files to find.

    Returns:
        list: A list of tuples, where each tuple contains (size, filepath).
    """

    file_sizes = []  # List to store (size, filepath) tuples
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                size = os.path.getsize(filepath)
                file_sizes.append((size, filepath))
            except OSError:
                # Handle potential errors (e.g., permission denied, broken symlinks)
                print(f"Warning: Could not get size of {filepath}")

    # Use a min-heap to efficiently keep track of the largest files
    largest_files = heapq.nlargest(num_files, file_sizes)

    return largest_files


if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    path = os.path.join(current_directory, "Calibre")
    largest_files = find_largest_files(current_directory)

    if largest_files:
        print(f"The {len(largest_files)} largest files are:")
        for size, filepath in largest_files:
            print(f"{size} bytes - {filepath}")
    else:
        print("No files found in the specified directory.")

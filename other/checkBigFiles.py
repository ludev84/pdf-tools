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
                # Convert size to MB
                file_size_kb = size / 1024
                file_size_mb = file_size_kb / 1024
                file_sizes.append((file_size_mb, filename))
            except OSError:
                # Handle potential errors (e.g., permission denied, broken symlinks)
                print(f"Warning: Could not get size of {filepath}")

    # Use a min-heap to efficiently keep track of the largest files
    largest_files = heapq.nlargest(num_files, file_sizes)

    return largest_files


if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    path = os.path.join(current_directory, "Calibre")
    largest_files = find_largest_files(path)

    if largest_files:
        print(f"The {len(largest_files)} largest files are:")
        for size, filename in largest_files:
            print(f"{size:.2f} MB - {filename}")
    else:
        print("No files found in the specified directory.")

import os
import sys

def mapper(search_string):
    file_name = os .environ.get('map_input_file')
    for line in sys.stdin:
        if search_string in line:
            print(f"found in {file_name}")
            break
if __name__ == "__main__":
    search_string = sys.argv[1]
    mapper(search_string)       
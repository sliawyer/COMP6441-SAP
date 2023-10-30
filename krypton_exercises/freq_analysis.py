# Outputs the frequency of groupings of characters in a text file
# Use as part of a chosen plaintext attack - See Krypton level 3

import sys

if __name__ == "__main__":
    
    char_dict = {}
    groupsize = 0
    lines = ""

    if len(sys.argv) != 3:
        print("Usage: python3 freq_analysis.py filename groupsize")
        exit(1)
    
    try:
        groupsize = int(sys.argv[2])
    except:
        print("Cannot read in groupsize. Groupsize must be an integer")
        exit(1)
        
    try:
        f = open(sys.argv[1], "r")
        file_lines = f.readlines()
    
    except:
        print("Cannot read in file. File must exist")
        exit(1)

    for line in file_lines:
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        lines = lines + line
    
    for i in range(len(lines) - groupsize):
        group = lines[i:i+groupsize]
        if group in char_dict:
            char_dict[group] += 1
        else:
            char_dict[group] = 1
            
    char_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    
    for char in char_dict:
        print(char[0] + "\t" + str(char[1]))
        
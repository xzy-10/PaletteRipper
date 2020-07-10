# PaletteRipper
 A Python program I wrote as practice with Pillow.

### Usage

________

`python3 PaletteRipper.py [MODE] [INPUTFILE] [OUTPUTFILE] [QUALITY/NUMBER] (SORTED)`  

Modes:
--fullset --> Isolates all unique colours and reassembles them in a new image.
    |
    --> QUALITY --> The number of times to divide the picture width and height by. A higher number corresponds to fewer colours. 
    |               Use 1 for maximum quality.
    --> SORTED (Y/N) --> Determines whether the full palette should be sorted.

--simplified --> Chooses the most common colours and reassembles them in a new image.
    |
    --> NUMBER --> The maximum number of colours to put in the new image. Note that this may not be possible for large numbers.

INPUTFILE --> The name of the picture to extract the colour palette from.

OUTPUTFILE --> The name of the picture where the colour palette will be placed. Please save as PNG to avoid compression.
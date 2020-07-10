from PIL import Image
from colorgram import extract
import sys
if len(sys.argv) >= 5:
    mode = sys.argv[1]
    inputfile = sys.argv[2]
    outputfile = sys.argv[3]
    NUMQUA = int(sys.argv[4])
    
    if mode == "--simplified":
        try:
            colors = extract(inputfile, NUMQUA)
            im = Image.new('RGB', (1, NUMQUA))
            im.putdata([v.rgb for v in colors])
            im.save(outputfile)
            print(f"Extracted the common colours (with NUMBER = {sys.argv[4]}) from {inputfile} and saved to {outputfile}.")
        except FileNotFoundError:
            print("Error: File Not Found.")
        except ValueError as err:
            print("Error: " + str(err))
        except OSError:
            print("Error: Incompatible File.")
        except ZeroDivisionError:
            print("Error: Division by zero.")            
    
    elif mode == "--fullset":
        try:
            with Image.open(inputfile) as im:
                width, height = im.size
                imgpixelated = im.resize((int(width/NUMQUA)+1, int(height/NUMQUA)+1),resample=Image.BILINEAR)
                swidth, sheight = imgpixelated.size
                palette = set()
                i = 0
                for x in range(0, swidth, 1):
                    for y in range(0, sheight, 1):
                            pixel = tuple(imgpixelated.getpixel((x, y)))
                            palette.add(pixel)
                totalc = len(palette)
                if totalc > 1000000:
                    nwidth = 3000
                elif totalc > 100000:
                    nwidth = 2000
                elif totalc > 10000:
                    nwidth = 1000
                elif totalc > 1000:
                    nwidth = 500
                else:
                    nwidth = 100
                nheight = int((len(palette)/nwidth))+1
                output = Image.new('RGB', (nwidth, nheight), color = (255, 255, 255))
                index = 0
                nx = 0
                ny = 0
                sortedc = sys.argv[5]
                if sortedc == "Y":
                    spalette = sorted(palette)
                elif sortedc == "N":
                    spalette = palette
                else:
                    raise ValueError("Invalid Option.")
                for pix in spalette:
                    if nx < nwidth:
                        output.putpixel((nx,ny), pix)
                        nx += 1
                    else:
                        nx = 0
                        ny += 1
                        output.putpixel((nx,ny), pix)
                        nx += 1
                output.save(outputfile)
                print(f"Extracted all colours (with QUALITY = {sys.argv[4]} and sorted = {sortedc}) from {inputfile} and saved to {outputfile}.")
        except FileNotFoundError:
            print("Error: File Not Found.")
        except ValueError as err:
            print("Error: " + str(err))
        except OSError:
            print("Error: Incompatible File.")
        except ZeroDivisionError:
            print("Error: Division by zero.")    
else:
    print(f'''
USAGE: python3 {sys.argv[0]} --fullset/--simplified INPUTFILE OUTPUTFILE QUALITY/NUMBER(determines how many colors) (SORTED (Y/N))    
OPTIONS:
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
    ''')
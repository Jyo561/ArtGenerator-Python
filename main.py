from PIL import Image

def get_str_ascii(intent):
    index = intent // 32
    ascii_chars = [" ", ".", "+", "=", "@", "$", "#", "%"]
    return ascii_chars[index]

def get_image(dir, scale):
    img = Image.open(dir)
    width, height = img.size
    for y in range(0, height, scale * 2):
        for x in range(0, width, scale):
            plx = img.getpixel((x, y))
            intent = (plx[0]+plx[1]+plx[2]) / 3
            if plx[3] == 0:
                intent = 0
            print(get_str_ascii(intent), end="")
        print("")

def main():
    get_image("418c74d3758a045bd29a3da57893ab6c.jpg", 10)

if __name__ == "__main__":
    main()

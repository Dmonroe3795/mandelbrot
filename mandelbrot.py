from PIL import Image

def isInMandelbrotSet(c,n):
    try:
        for x in range(n):
            if abs(mandelbrotFunc(c,x)) > 2:
               return x
    except :
        return n
    return 0
def mandelbrotFunc(c,n):
    if n == 0:
        return 0
    x = mandelbrotFunc(c,n-1)
    return (x*x)+c
def scale(x,y,min,max):
    scale = x/y
    diff = max - min
    return min+(diff*scale)
def isPixWanted(x,y,col,row,n,lowerBoundX,upperBoundX,lowerBoundY,upperBoundY):
    z = scale(x,col,lowerBoundX,upperBoundX)
    p = scale(y,row,lowerBoundY,upperBoundY)
    c = z+ p*1j
    return isInMandelbrotSet(c,n)
def drawMandelbrot(choice):
    n = 25
    col = 3840
    row = 3840
    if choice == 1:
        lx = .25
        ux = .35
        ly = -0.05
        uy = .05
    elif choice == 2:
        lx = -1.0
        ux = -0.5
        ly = .05
        uy = .55
    elif choice == 3:
        col = int(1000)
        row =int(666)
        lx = -2
        ux = 1
        ly = -1
        uy = 1
    else:
        col = int(input("Enter the width in pixels "))
        row = int(input("Enter the height in pixels"))
        lx = float(input("Enter the lower bound of the x-axis "))
        ux = float(input("Enter the upper bound of the x-axis "))
        ly = float(input("Enter the lower bound of the y-axis "))
        uy = float(input("Enter the upper bound of the y-axis "))
    img = Image.new("RGB",(col,row),(0,0,0))
    for x in range(col):
        for y in range(row):
            color = isPixWanted(x,y,col,row,25,lx,ux,uy,ly)
            percent = color/n
            green = int(percent*255)
            img.putpixel((x,y),(0,green,0))
    img.show()
    print("DONE!")
    
drawMandelbrot(int(input("If you want to see elephant valley enter 1 \nIf you want to see sea horse valley enter 2\nIf you want to see the Standard image enter 3:\nIf you want to set custom values enter anything else:\nBeware that the presets are at 1000x1000 pixels so it might take a moment to draw your image:\n")))


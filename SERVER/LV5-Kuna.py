import string
from tkinter import Frame, Menu, Canvas, filedialog as fd, Tk
import socket
import threading as thr

def selectReadFile():
    openWindow = fd.askopenfilename()
    openFile = open(openWindow, 'r')
    for line in openFile:
        line = line.rstrip()
        drawCommands = line.split(' ')
        if drawCommands[0] == "Line":
            line = Line(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], xcoordinate2 = drawCommands[4],  ycoordinate2 = drawCommands[5])
            line.draw(c)
        if drawCommands[0] == "Triangle":
            triangle = Triangle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], xcoordinate2 = drawCommands[4],  ycoordinate2 = drawCommands[5], xcoordinate3 = drawCommands[6], ycoordinate3 = drawCommands[7])
            triangle.draw(c)
        if drawCommands[0] == "Rectangle":
            rectangle = Rectangle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], height = drawCommands[4],  width = drawCommands[5])
            rectangle.draw(c)
        if drawCommands[0] == "Circle":
            circle = Circle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], radius = drawCommands[4])
            circle.draw(c)
        if drawCommands[0] == "Ellipse":
            ellipse = Ellipse(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], radius1 = drawCommands[4],  radius2 = drawCommands[5])
            ellipse.draw(c)
        if drawCommands[0] == "Polygon":
            polygonColor = drawCommands[1]
            polygonX1 = drawCommands[2]
            polygonY1 = drawCommands[3]
            del drawCommands[0:2]
            polygon = Polygon(polygonColor, polygonX1, polygonY1, drawCommands)
            polygon.draw(c)

def newThread():
    connectionThread = thr.Thread(target=startServer)
    connectionThread.daemon = True
    connectionThread.start()

def startServer():
    listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8000
    maxConnections = 10
    name = socket.gethostname()
    listensocket.bind(('localhost', port))
    listensocket.listen(maxConnections)
    statusText = "Started server at " + name + " on port " + str(port)
    c.create_text(680, 580, text=statusText, fill="white")
    while True:
        (cs, address) = listensocket.accept()
        print("Connection address: ", address)
        t = thr.Thread(target = drawFromMessage, args =(cs,))
        t.daemon = True
        t.start()

def drawFromMessage(cs):
    while True:
        message = cs.recv(1024).decode()
        message = message.rstrip()
        drawCommands = message.split(' ')
        if drawCommands[0] == "Line":
            line = Line(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], xcoordinate2 = drawCommands[4],  ycoordinate2 = drawCommands[5])
            line.draw(c)
        if drawCommands[0] == "Triangle":
            triangle = Triangle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], xcoordinate2 = drawCommands[4],  ycoordinate2 = drawCommands[5], xcoordinate3 = drawCommands[6], ycoordinate3 = drawCommands[7])
            triangle.draw(c)
        if drawCommands[0] == "Rectangle":
            rectangle = Rectangle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], height = drawCommands[4],  width = drawCommands[5])
            rectangle.draw(c)
        if drawCommands[0] == "Circle":
            circle = Circle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], radius = drawCommands[4])
            circle.draw(c)
        if drawCommands[0] == "Ellipse":
            ellipse = Ellipse(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], radius1 = drawCommands[4],  radius2 = drawCommands[5])
            ellipse.draw(c)
        if drawCommands[0] == "Polygon":
            polygonColor = drawCommands[1]
            polygonX1 = drawCommands[2]
            polygonY1 = drawCommands[3]
            del drawCommands[0:2]
            polygon = Polygon(polygonColor, polygonX1, polygonY1, drawCommands)
            polygon.draw(c)


class GrafickiLik():  #Klasa GrafLik pored svojeg inicijalizatora mora još imati funkcije: SetColor, GetColor i Draw. Također mora imati i dva atributa odnosno varijable: boja (pogledati prethodni opis kako se koriste boje u Tkinter-u) i tocka
    Color: string
        
    def __init__(self, color, xcoordinate1, ycoordinate1):
        self.Color = color
        self.xcoordinate1 = xcoordinate1
        self.ycoordinate1 = ycoordinate1

    def draw(self, canvas):
        pass

class Line(GrafickiLik):

    def __init__(self, color, xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.xcoordinate2 = xcoordinate2
        self.ycoordinate2 = ycoordinate2

    def draw(self, canvas):
        canvas.create_line((self.xcoordinate1, self.ycoordinate1, self.xcoordinate2, self.ycoordinate2), fill = self.Color)

class Triangle(Line):

    def __init__(self, color, xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2, xcoordinate3, ycoordinate3):
        super().__init__(color, xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2)
        self.xcoordinate3 = xcoordinate3
        self.ycoordinate3 = ycoordinate3

    def draw(self,canvas):
        canvas.create_line((self.xcoordinate1, self.ycoordinate1, self.xcoordinate2, self.ycoordinate2), fill=self.Color)
        canvas.create_line((self.xcoordinate2, self.ycoordinate2, self.xcoordinate3, self.ycoordinate3), fill=self.Color)
        canvas.create_line((self.xcoordinate3, self.ycoordinate3, self.xcoordinate1, self.ycoordinate1), fill=self.Color)

class Rectangle(GrafickiLik):

    def __init__(self, color, xcoordinate1, ycoordinate1, height, width):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.height = height
        self.width = width

    def draw(self,canvas):
        canvas.create_rectangle((self.xcoordinate1, self.ycoordinate1, float(self.xcoordinate1) + float(self.width), float(self.ycoordinate1) + float(self.height)), 
        outline = self.Color, fill = '')


class Circle(GrafickiLik):

    def __init__(self, color, xcoordinate1, ycoordinate1, radius):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.radius = radius

    def draw(self,canvas):
        canvas.create_oval((float(self.xcoordinate1) - float(self.radius), float(self.ycoordinate1) - float(self.radius), float(self.xcoordinate1) + 
        float(self.radius), float(self.ycoordinate1) + float(self.radius)), outline=self.Color, fill='')

class Ellipse(Circle):
    def __init__(self, color, xcoordinate1, ycoordinate1, radius1, radius2):
        super().__init__(color, xcoordinate1, ycoordinate1, radius1)
        self.radius2 = radius2

    def draw(self,canvas):
        canvas.create_oval((self.xcoordinate1, self.ycoordinate1, float(self.xcoordinate1) + float(self.radius), 
        float(self.ycoordinate1) + float(self.radius2)), outline=self.Color, fill="")

class Polygon(GrafickiLik):
    def __init__(self, color, xcoordinate1, ycoordinate1, coordinates = []):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.coordinates = coordinates
        self.coordinates.insert(0, xcoordinate1)
        self.coordinates.insert(1, ycoordinate1)

    def getCoordinates(self):
        return self.coordinates

    def setCoordinates(self, coordinates):
        self.coordinates = coordinates

    def draw(self, canvas):
        canvas.create_polygon(self.coordinates, outline = self.Color, fill = '')
    


if __name__ == "__main__":
    root = Tk()

    root.title("LV5 Objektno Programiranje - Renato Kuna")
    c = Canvas( bg="#999999", height=600, width=800)
    c.pack()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    servermenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label = "Open", command=selectReadFile)
    filemenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="Server", menu=servermenu)
    servermenu.add_command(label = "Start Server", command=newThread)
    root.config(menu=menubar)

    root.mainloop()
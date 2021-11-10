ton = ["c1","d1","e1","f1","g1","a1","h1","c2","d2","e2","f2","g2","a2","h2","c3"]
#globale Variabel

#def mousePressed():


#def mouseReleased():
    

def setup():
    size(900, 350)
    background(255,255,255)
    frameRate(30)
 
def draw(): #wird einmal pro Frame ausgeführt
    background(255,255,255)
    img = loadImage("violinschluessel_background.png")
    image(img,100,20, 690, 288)
    #Position (x, y) und Grösse (Breite, Höhe) des Bildes
    b = 1
    #wenn b=1, dann ist die Mausposition noch unbekannt
    for i in range(15):        
        if mouseY < 60 + 16*i and b == 1:
            #16 ist ca. Abstand in px zwischen zwei Tönen auf Notenlinien
            a = 14 -i
            b = 0
        elif b == 1:
            a = 0
    note = loadImage(ton[a]+".png")
    #jeweiliges Bild wird geladen
    image(note,300,20, 60, 288)
    textSize(64)
    #Schriftgrösse
    fill(236,64,122)
    #Schriftfarbe
    text(ton[a],20,64)
    #fixe Position des Notennamens
    

    #print mouseY

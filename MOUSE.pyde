
def setup():
    size(600,400)
    fill(200,30,40)
    rect(30,50,50,50)
    fill(90,150,60)
    rect(100,200,50,50)
    fill(250,250,90)
    rect(150,50,50,50)
    fill(255,255,255)
    rect(250,100,300,250)
def draw():
   if mousePressed and mouseX >200:
            line(pmouseX,pmouseY,mouseX,mouseY)

   
   
def mouseClicked():
   if mouseX>200:
       stroke(90,150,60)
   if mouseY <300:
      stroke(250,250,90)
   if mouseX<150:
        stroke(255,0,0)
     
    

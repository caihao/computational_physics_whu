from visual import *


print"""
Interactive Superposition of Coherent Sources (ver 2/16/2004)
Rob Salgado (salgado@physics.syr.edu)
"""
### ver 2/16/2004   tested on Windows 2000
###                 with Python-2.3.3.exe and VPython-2003-10-05.exe
###                 Navigation needs work. The mouse should be able to
###                    drag each of the three points along the xz-plane.
###                    The relation between the dragged point and mouse
###                    cursor look unnatural.

#phase=arange(0,1,.1)
#print len(phase)
#sinphase=sin(phase)
#print phase, sinphase
#eqn =raw_input('formula')
#x=arange(0,10,0.1)
#c=curve(x=x,y=eval(eqn))

scene.autoscale=0
scene.range=(12,12,12)
scene.title="Wave Superposition"

t=0

AA=1
Ak=2.*pi/5
Aw=1
Ap=0

wavelength=2.*pi/Ak

Ax0=0; Ay0=0
Ax1=10;Ay1=0
Adx=Ax1-Ax0
Ady=Ay1-Ay0
Ar=arange(0,sqrt(Adx*Adx+Ady*Ady)+0.01,0.01)

Ax=Ax0+Adx*Ar/Ar[-1]
Ay=Ay0+Ady*Ar/Ar[-1]

Ac=curve(x=Ax,z=Ay,y=AA*sin(Ak*Ar-Aw*t+Ap),color=color.cyan,radius=0.2)
As0=sphere(pos=vector([Ax0,0,Ay0]),radius=0.1,color=color.cyan)
As1=sphere(pos=vector([Ax1,0,Ay1]),radius=0.1,color=color.cyan)

Alabel=label(pos=vector([Ax0,0,Ay0]),text="Ar=%4.2f" % (Ar[-1]),color=color.cyan,yoffset=-60,opacity=0)

Asource=arrow(pos=As0.pos,axis=vector(0,Ac.y[0],0),color=color.cyan)
Atarget=arrow(pos=As1.pos,axis=vector(0,Ac.y[-1],0),color=color.cyan)



BA=1
Bk=Ak
Bw=1
Bp=0

Bx0=0; By0=0
Bx1=10;By1=0
Bdx=Bx1-Bx0
Bdy=By1-By0
Br=arange(0,sqrt(Bdx*Bdx+Bdy*Bdy)+0.01,0.01)

Bx=Bx0+Bdx*Br/Br[-1]
By=By0+Bdy*Br/Br[-1]

Bc=curve(x=Bx,z=By,y=BA*sin(Bk*Br-Bw*t+Bp),color=color.green,radius=0.2)
Bs0=sphere(pos=vector([Bx0,0,By0]),radius=0.1,color=color.green)
Bs1=sphere(pos=vector([Bx1,0,By1]),radius=0.1,color=color.green)

Blabel=label(pos=vector([Bx0,0,By0]),text="Br=%4.2f" % (Br[-1]),color=color.green,yoffset=-100,opacity=0)

Bsource=arrow(pos=Bs0.pos,axis=vector(0,Bc.y[0],0),color=color.green)
Btarget=arrow(pos=Bs1.pos,axis=vector(0,Bc.y[-1],0),color=color.green)


Xtarget=arrow(pos=Bs1.pos,axis=vector(0,Ac.y[-1]+Bc.y[-1],0),color=color.magenta)

Xlabeld=label(pos=Bs1.pos,text="delta_r=%4.2f" % (Br[-1]-Ar[-1]),color=color.magenta,xoffset=-30,yoffset=100,opacity=0)
Xlabell=label(pos=Bs1.pos,text="lambda=%4.2f" % wavelength,color=color.magenta,xoffset=-30,yoffset=60,opacity=0)
Xlabelr=label(pos=Bs1.pos,text="ratio=%4.2f" % ((Br[-1]-Ar[-1])/wavelength),color=color.magenta,xoffset=-30,yoffset=-60,opacity=0)


n=None
drag=0    

#scene.forward=vector([0.021853,-0.923144,-0.383834])
while 1:
    rate(40)
#    print scene.center, scene.forward, scene.range
    t += 0.1
    
    Ac.y=AA*sin(Ak*Ar-Aw*t+Ap)
    Asource.axis=vector(0,Ac.y[0],0)
    Atarget.axis=vector(0,Ac.y[-1],0)
    
    Bc.y=BA*sin(Bk*Br-Bw*t+Bp)
    Bsource.axis=vector(0,Bc.y[0],0)
    Btarget.axis=vector(0,Bc.y[-1],0)

    Xtarget.axis=vector(0,Ac.y[-1]+Bc.y[-1],0)

    if scene.mouse.clicked:
        m=scene.mouse.getclick()
        newPick=scene.mouse.pick

        if newPick==As0:
            print " A"
        elif newPick==Bs0:
            print " B"
        elif newPick==Bs1:
            print " X"
        else:
            print " none"
            #scene.center=(As0.pos+Bs0.pos+As1.pos+Bs1.pos)/4.
            #scene.center=scene.mouse.pos


        print newPick
        if m.click == "none":
            drag=0; print drag
            scene.mouse.getclick()
            scene.center=scene.mouse.pos
        elif m.click == "left":
            n=newPick
            drag=1; print drag
            
    if drag==1:
        #print "Drag ",
        #print scene.mouse.button
        if n!=None:
            n.pos[0]=scene.mouse.pos[0]
            n.pos[2]=scene.mouse.pos[2]

            newpos=n.pos
            if n==As0:
                Ax0=newpos[0]
                Ay0=newpos[2]
                As0.pos=vector([Ax0,0,Ay0])

            elif n==Bs0:
                Bx0=newpos[0]
                By0=newpos[2]
                Bs0.pos=vector([Bx0,0,By0])
            elif n==Bs1:
                Ax1=newpos[0]
                Ay1=newpos[2]
                Bx1=newpos[0]
                By1=newpos[2]
                As1.pos=vector([Ax1,0,Ay1])
                Bs1.pos=vector([Bx1,0,By1])

            else:
                print "none"


            Adx=Ax1-Ax0
            Ady=Ay1-Ay0
            Ar=arange(0,sqrt(Adx*Adx+Ady*Ady)+0.01,0.01)
            Alabel.pos=vector([Ax0,0,Ay0])
            Alabel.text="Ar=%4.2f" % (Ar[-1])


            Ax=Ax0+Adx*Ar/Ar[-1]
            Ay=Ay0+Ady*Ar/Ar[-1]
            Aold=Ac
            Ac=curve(x=Ax,z=Ay,y=AA*sin(Ak*Ar-Aw*t+Ap),color=color.cyan,radius=.2)
            Aold.visible=0

            Asource.pos=vector([Ax0,0,Ay0])
            Atarget.pos=vector([Ax1,0,Ay1])

            Bdx=Bx1-Bx0
            Bdy=By1-By0
            Br=arange(0,sqrt(Bdx*Bdx+Bdy*Bdy)+0.01,0.01)
            Blabel.pos=vector([Bx0,0,By0])
            Blabel.text="Br=%4.2f" % (Br[-1])

            Bx=Bx0+Bdx*Br/Br[-1]
            By=By0+Bdy*Br/Br[-1]
            Bold=Bc
            Bc=curve(x=Bx,z=By,y=BA*sin(Bk*Br-Bw*t+Bp),color=color.green,radius=.2)
            Bold.visible=0

            Bsource.pos=vector([Bx0,0,By0])
            Btarget.pos=vector([Bx1,0,By1])

            Xtarget.pos=vector([Bx1,0,By1])
            Xlabeld.pos=Bs1.pos
            Xlabeld.text="delta_r=%4.2f" % (Br[-1]-Ar[-1])
            Xlabell.pos=Bs1.pos
            Xlabell.text="lambda=%4.2f" % wavelength
            Xlabelr.pos=Bs1.pos
            Xlabelr.text="ratio=%4.2f" % ((Br[-1]-Ar[-1])/wavelength)


            

### EMWave-Maxwell.py
### Electromagnetic Plane Wave visualization (requires VPython)
### Rob Salgado
### salgado@physics.syr.edu     http://physics.syr.edu/~salgado/

#needs a code clean-up (seems buggy on 2.4) 


### v0.5  2001-11-07 tested on Windows 2000
### v0.51 2003-02-16 tested on Windows 2000
###         with Python-2.1.1.exe and VPython-2001-10-31.exe
### v1.00 2004-03-21 tested on Windows 2000
###         with Python-2.3.3.exe and VPython-2003-10-15.exe
### v2.00 2006-04-30 tested on Windows 2000
### v2.50 2006-06-01 tested on Windows 2000/XP-TabletPC
###         with Python-2.3.4.exe and VPython-2003-10-15.exe
### v2.51 2006-06-13 tested on Windows 2000/XP-TabletPC
###         with Python-2.3.4.exe and VPython-2003-10-15.exe #fixed minor loop color problem

### v2.75 2008-01-18 tested on Windows XP
###         with Python-2.3.4.exe and VPython-2003-10-15.exe #colors adjusted (key 'n'), keys 'e' and 'b'


from visual import *

calculus=1             #key c
verbose=1              #key v

showNeighboringWaves=0 #key s
showWavefronts=0       #key w
showAmpere=1           #key a
showFaraday=1          #key f
showGauss=0            #key g
showE=1            #key e
showB=1            #key b

dimFields=0            #key d
colorScheme=0          #key n (negative background color)

highlightAmpere=1
highlightFaraday=1
highlightField=1

print"""
Electromagnetic Plane Wave visualization (v2.75) 2008-01-20
Rob Salgado (salgado@physics.syr.edu)

Electric Field vectors are blue. Magnetic Field vectors are red.
  The thick green vector representing
d|E|/dt ("time-rate-of-change-of-the-magnitude-of-the-electric-field")
is associated with the spatial arrangement of the magnetic field according to
the AMPERE-MAXWELL Law (as evaluated on the green loop).
[The sense of circulation on the green loop (by the RightHandRule) determines
the direction of change of the electric field... determined by your thumb.]
  The thick yellow vector representing
d|B|/dt ("time-rate-of-change-of-the-magnitude-of-the-magnetic-field")
is associated with the spatial arrangement of the electric field according to
the FARADAY Law (as evaluated on the yellow loop).
[The sense of circulation on the yellow loop (by the RightHandRule) determines
the direction of change of the magnetic field... OPPOSITE to your thumb.]
  Intuitively, d|E|/dt tells the current value of E at that point to look like
the value of E at the point to its left (in this example).
In other words, the pattern of the electric field moves to the RIGHT.
  Similarly, d|B|/dt tells the current value of B at that point to look like
the value of B at the point to its left (in this example).
In other words, the pattern of the magnetic field moves to the RIGHT.
  Thus, this electromagnetic plane wave moves to the RIGHT.
      MOVE the mouse to reposition the loops
      CLICK the mouse or SPACEBAR to start and stop the animation
      TOGGLE: (a)mpere     (f)araday  (g)auss  (w)avefronts
              (d)im-fields (s)how-neighboring-waves
              (c)alculus   (v)erbose  (n) color-scheme"""

scene=display(
    width=800,height=600,
    x=0, y=0,
    title="EM Wave v2.75 (Rob Salgado)")
scene.autoscale=0
scene.range=(6,6,6)
scene.forward=(-1.0, -1.250, -4)
scene.newzoom=1

scene.forward=(-3.401075,-1.172172,-2.370908) ; scene.range=(16,16,16) #for plane wave introduction *perspective

scene.forward=(-2.218882,-1.142878,-3.511822) ; scene.range=(16,16,16) #for plane wave introduction

scene.forward=(-1.720152,-2.383154,-3.150263) ; scene.range=(10,10,10)  #for detailed view

scene.forward=(-1.720152,-2.383154,-3.150263) ; scene.range=(20,20,20)  #for detailed view


colorBackground=[color.black,color.white]
labelBackground=[0.66, 0.5]
label_epsV=vector(.1,.1,.1)

Ecolor=[color.blue, (0,0,.4) ,color.yellow, (0.5,0.5,0) ]
Bcolor=[color.red, (.4,0,0) ,color.green, (0,0.75,0)]
ddtcolor=[Bcolor[2+colorScheme], Ecolor[2+colorScheme]]

Gcolor1=(0.0,0.27e-9,0.0);Gcolor2=Gcolor1; Gcolor_boundary=[color.cyan, color.black] #GAUSS
Frontcolor=[(0.5,0.5,0.5), (0.3,0.3,0.3)]

ambient=[0.3,0.7]
scene.ambient=.4
scene.background=colorBackground[colorScheme]

EField=[]
EField2=[]

BField=[]
BField2=[]
Emax=4.
sep=10.

magnify=2.5
S=20
omega=0.1
wavelength=S
k=2*pi/wavelength

t=0
t=1
trun=0
fi=0

prefixAmpere=["","Ampere says\n",""]
prefixFaraday=["","Faraday says\n",""]

dBdtpos_text=["  |B| is increasing","  d|B|/dt >0"]
dBdtneg_text=["|B| is decreasing  ","d|B|/dt <0  "]
dBdtzer_text=[" |B| is maintained "," d|B|/dt =0 "]

dEdtpos_text=["  |E| is increasing","  d|E|/dt >0"]
dEdtneg_text=["|E| is decreasinge ","d|E|/dt <0  "]
dEdtzer_text=["  |E| is maintained"," d|E|/dt =0 "]

## gauss
fi=0
gaussSurface=[]
gc=0
##gtilesize=2
##gtilehalf=gtilesize/2.
##gaussX=3.

########
gt=2
gh=gt/2.
gaussX=3.

gaussSurface.append( curve(height=0,width=0,pos=[(fi-gaussX, -sep,-sep),(fi-gaussX,-sep,sep),  (fi-gaussX,sep,sep), (fi-gaussX,sep,-sep),(fi-gaussX,-sep,-sep)], color=Gcolor_boundary[colorScheme] ,visible=showGauss) )
gaussSurface.append( curve(height=0,width=0,pos=[(fi+gaussX, -sep,-sep),(fi+gaussX,-sep,sep),  (fi+gaussX,sep,sep), (fi+gaussX,sep,-sep),(fi+gaussX,-sep,-sep)], color=Gcolor_boundary[colorScheme] ,visible=showGauss) )
gaussSurface.append( curve(height=0,width=0,pos=[(fi-gaussX, -sep,-sep),(fi+gaussX, -sep,-sep)],color=Gcolor_boundary[colorScheme], visible=showGauss ) )
gaussSurface.append( curve(height=0,width=0,pos=[(fi-gaussX, -sep, sep),(fi+gaussX, -sep, sep)],color=Gcolor_boundary[colorScheme], visible=showGauss ) )
gaussSurface.append( curve(height=0,width=0,pos=[(fi-gaussX,  sep,-sep),(fi+gaussX,  sep,-sep)],color=Gcolor_boundary[colorScheme], visible=showGauss ) )
gaussSurface.append( curve(height=0,width=0,pos=[(fi-gaussX,  sep, sep),(fi+gaussX,  sep, sep)],color=Gcolor_boundary[colorScheme], visible=showGauss ) )

gaussPos=[]
gaussPos0=[]
gaussPos1=[]
gaussNor=[] #for coloring
gaussCol=[]
gauss_dA=[] #for flux

for ax in arange(-gaussX+gh,gaussX,gt):
    gc +=1
    for az in arange(-sep+gh,sep,gt):
        Cx=fi+ax;Cz=az
        A1=Cx-gh;A2=Cz-gh
        B1=Cx+gh;B2=Cz+gh
        if gc%2 ==0:
            #outward is upward-y
            gaussPos1.append( vector(A1, sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(A1, sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0, 1) );gaussCol.append( Gcolor1 );gauss_dA.append( (0,1,0) ) #OUT

            #inward is downward-y
            gaussPos1.append( vector(A1, sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(B1, sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(A1, sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0, 0, 1) );gaussCol.append( Gcolor2 );gauss_dA.append( (0,-1,0) ) #IN               
        else:
            #outward is downward-y
            gaussPos1.append( vector(A1, -sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(B1, -sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, -sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, -sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, -sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(A1, -sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0, 0, 1) );gaussCol.append( Gcolor1 );gauss_dA.append( (0,-1,0) ) #OUT
            #inward is upward-y                
            gaussPos1.append( vector(A1, -sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(A1, -sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, -sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, -sep, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, -sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, -sep, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0, 0, 1) );gaussCol.append( Gcolor2 );gauss_dA.append( (0,1,0) ) #IN                

#            gaussSurface.append( box(phase=fi,pos=(fi+ax, sep,az),axis=(0,.001,0),height=gtilesize,width=gtilesize,color=color.cyan, visible=showGauss) )
        gc +=1
gc +=1
for ax in arange(-gaussX+gh,gaussX,gt):
    gc +=1
    for ay in arange(-sep+gh,sep,gt):
        Cx=fi+ax;Cy=ay
        A1=Cx-gh;A2=Cy-gh
        B1=Cx+gh;B2=Cy+gh
        if gc%2 ==0:
            #inward
            gaussPos1.append( vector(A1, A2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(A1, B2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )   
            gaussPos1.append( vector(B1, B2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )   
            gaussPos1.append( vector(B1, B2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, A2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, A2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor2 );gauss_dA.append( (0,0,-1) ) #IN

            #outward
            gaussPos1.append( vector(A1, A2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(B1, A2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, B2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )   
            gaussPos1.append( vector(B1, B2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, B2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )   
            gaussPos1.append( vector(A1, A2, sep) ) ;gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor1 );gauss_dA.append( (0,0,1) ) #OUT                
        else:
            #inward
            gaussPos1.append( vector(A1, A2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(B1, A2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, B2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, B2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, B2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(A1, A2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor2 );gauss_dA.append( (0,0,1) ) #IN
            #outward                
            gaussPos1.append( vector(A1, A2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(A1, B2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, B2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(B1, B2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(B1, A2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(A1, A2, -sep) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor1 );gauss_dA.append( (0,0,-1) ) #OUT

        
##        if gc%2 ==0:
##            gaussSurface.append( box(phase=fi,pos=(fi+ax,ay,-sep),axis=(0,0,.001),height=gtilesize,width=gtilesize,color=(0,0.5,0.5), visible=showGauss ) )
##        else:
##            gaussSurface.append( box(phase=fi,pos=(fi+ax,ay, sep),axis=(0,0,.001),height=gtilesize,width=gtilesize,color=(0,0.5,0.5), visible=showGauss ) )
        gc +=1
gc +=1
for ay in arange(-sep+gh,sep,gt):
    gc +=1
    for az in arange(-sep+gh,sep,gt):
        Cy=ay;Cz=az
        A1=Cy-gh;A2=Cz-gh
        B1=Cy+gh;B2=Cz+gh
        if gc%2 ==0:
            #outward
            gaussPos1.append( vector(fi+gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(fi+gaussX,B1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,A1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor1 );gauss_dA.append( (1,0,0) ) #OUT
            #inward                
            gaussPos1.append( vector(fi+gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(fi+gaussX,A1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,B1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi+gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor2 );gauss_dA.append( ( -1,0,0) ) #IN
        else:
            #inward
            gaussPos1.append( vector(fi-gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(fi-gaussX,A1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )    
            gaussPos1.append( vector(fi-gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,B1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor1 );gauss_dA.append( ( -1,0,0) ) #OUT

            #outward
            gaussPos1.append( vector(fi-gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos1[-1] )
            gaussPos1.append( vector(fi-gaussX,B1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,B1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,A1, B2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            gaussPos1.append( vector(fi-gaussX,A1, A2) );gaussPos.append( gaussPos1[-1]);gaussPos0.append( gaussPos0[-1] )
            for i in arange(0,6):
                gaussNor.append( (0,0,1) );gaussCol.append( Gcolor2 );gauss_dA.append( ( 1,0,0) ) #IN                
        
##        if gc%2 ==0:
##            gaussSurface.append( box(phase=fi,pos=(fi-gaussX,ay,az),axis=(.001,0,0),height=gtilesize,width=gtilesize,color=color.cyan, visible=showGauss ) )
##        else:
##            gaussSurface.append( box(phase=fi,pos=(fi+gaussX,ay,az),axis=(.001,0,0),height=gtilesize,width=gtilesize,color=color.cyan, visible=showGauss ) )
        gc +=1

gaussElements=faces(pos=gaussPos,normal=gaussNor,color=gaussCol,visible=showGauss)
#gaussSurface.append(gaussElements)
##########


## WAVEFRONT
fi=wavelength/4
a=1.
front=[]
front2=[]
ftilesize=0.3

phase0=0
phase1=fi
phase2=fi+wavelength
framefront1=frame(pos=(phase1,0,0))
framefront2=frame(pos=(phase2,0,0))

#front.append( curve(phase=fi,pos=[(fi, -sep*a,-sep*a),(fi,-sep*a,sep*a),  (fi,sep*a,sep*a), (fi,sep*a,-sep*a),(fi,-sep*a,-sep*a)], color=color.white ) )
front.append( curve(frame=framefront1,pos=[(phase0, 0,0),(phase0,0,Emax),  (phase0,Emax,Emax), (phase0,Emax,0),(phase0,0,0)], color=[(0.5,0.5,0.5),color.red,color.magenta,color.blue,color.white], visible=showWavefronts ) )
for ay in arange(-a*sep,a*sep+1):
    for az in arange(-a*sep,a*sep+1):
        front.append( box(frame=framefront1, pos=(phase0,ay,az),axis=(.001,0,0),height=ftilesize,width=ftilesize,color=Frontcolor[colorScheme], visible=showWavefronts))

front2.append( curve(frame=framefront2, pos=[(phase0, 0,0),(phase0,0,Emax),  (phase0,Emax,Emax), (phase0,Emax,0),(phase0,0,0)], color=[(0.5,0.5,0.5),color.red,color.magenta,color.blue,color.white], visible=showWavefronts ) )
for ay in arange(-a*sep,a*sep+1):
    for az in arange(-a*sep,a*sep+1):
        front2.append( box(frame=framefront2, pos=(phase0,ay,az),axis=(.001,0,0),height=ftilesize,width=ftilesize,color=Frontcolor[colorScheme], visible=showWavefronts))


## FIELDS
for i in arange(-S,S):
    Ev=arrow(pos=(i,0,0),axis=(0,0,0),color=Ecolor[dimFields],shaftwidth=0.2, fixedwidth=1,nbw=0)
    EField.append(Ev)

for i in arange(-S,S):
    Bv=arrow(pos=(i,0,0),axis=(0,0,0),color=Bcolor[dimFields],shaftwidth=0.2, fixedwidth=1,nbw=0)
    BField.append(Bv)


if showNeighboringWaves>=0:
    for i in arange(-S,S):
        Ev=arrow(pos=(i,sep,0),axis=(0,0,0),color=Ecolor[0],shaftwidth=0.2, fixedwidth=1,nbw=3, visible=showNeighboringWaves)
        EField.append(Ev)
    for i in arange(-S,S):
        Bv=arrow(pos=(i,sep,0),axis=(0,0,0),color=Bcolor[0],shaftwidth=0.2, fixedwidth=1,nbw=3, visible=showNeighboringWaves)
        BField.append(Bv)

    for i in arange(-S,S):
        Ev=arrow(pos=(i,-sep,0),axis=(0,0,0),color=Ecolor[0],shaftwidth=0.2, fixedwidth=1,nbw=3, visible=showNeighboringWaves)
        EField.append(Ev)
    for i in arange(-S,S):
        Bv=arrow(pos=(i,-sep,0),axis=(0,0,0),color=Bcolor[0],shaftwidth=0.2, fixedwidth=1,nbw=3, visible=showNeighboringWaves)
        BField.append(Bv)

    for j in arange(1,3):
        for i in arange(-S,S):
            Ev=arrow(pos=(i,0,j*sep),axis=(0,0,0),color=Ecolor[dimFields],shaftwidth=0.2, fixedwidth=1, nbw=1, visible=showNeighboringWaves)
            EField.append(Ev)
        for i in arange(-S,S):
            Bv=arrow(pos=(i,0,j*sep),axis=(0,0,0),color=Bcolor[dimFields],shaftwidth=0.2, fixedwidth=1, nbw=1, visible=showNeighboringWaves)
            BField.append(Bv)

        for i in arange(-S,S):
            Ev=arrow(pos=(i,0,-j*sep),axis=(0,0,0),color=Ecolor[dimFields],shaftwidth=0.2, fixedwidth=1, nbw=1, visible=showNeighboringWaves)
            EField.append(Ev)
        for i in arange(-S,S):
            Bv=arrow(pos=(i,0,-j*sep),axis=(0,0,0),color=Bcolor[dimFields],shaftwidth=0.2, fixedwidth=1, nbw=1, visible=showNeighboringWaves)
            BField.append(Bv)


height=sep/2.
FaradayLoop=curve(pos=[(-1,-height,0),(-1,height,0),  (1,height,0), (1,-height,0),(-1,-height,0)],color=ddtcolor[0], visible=showFaraday)
AmpereLoop= curve(pos=[(-1,0,-height),(-1,0,height),  (1,0,height), (1,0,-height),(-1,0,-height)],color=ddtcolor[1], visible=showAmpere)

dBdt=arrow(pos=vector(fi,0,0),axis=(0,0,0),color=ddtcolor[0],shaftwidth=0.35,headwidth=0.7, fixedwidth=1, visible=showFaraday)
dEdt=arrow(pos=vector(fi,0,0),axis=(0,0,0),color=ddtcolor[1],shaftwidth=0.35,headwidth=0.7, fixedwidth=1, visible=showAmpere)
dBdtlabel = label(pos=vector(fi,0,0)+label_epsV, text='dB/dt',color=Bcolor[2], opacity=labelBackground[colorScheme], xoffset=20, yoffset=12, height=16, border=6, visible=showFaraday, font="arial bold")
dEdtlabel = label(pos=vector(fi,0,0),            text='dE/dt',color=Ecolor[2], opacity=labelBackground[colorScheme], xoffset=20, yoffset=12, height=16, border=6, visible=showAmpere,  font="arial bold")


fi=0
while 1:
        
    newfi=int(scene.mouse.pos.x)
    newfi=max(min(newfi,S-2),-(S-2))


    phase=k*(newfi-S)-omega*t
    if fi <> newfi:  #MOVE THE LOOPS
        EField[S+fi-1].color=EField[S+fi+1].color=Ecolor[dimFields]
        BField[S+fi-1].color=BField[S+fi+1].color=Bcolor[dimFields]

        if highlightField==1:
            if showFaraday==1: BField[S+fi].color=Bcolor[dimFields]
            if showAmpere==1:  EField[S+fi].color=Ecolor[dimFields]
        fi=newfi        
        if showFaraday==1: EField[S+fi-1].color=EField[S+fi+1].color=ddtcolor[0]
        if showAmpere==1:  BField[S+fi-1].color=BField[S+fi+1].color=ddtcolor[1]

        if highlightField==1 and showFaraday==1: BField[S+fi].color=Bcolor[0]
        if highlightField==1 and showAmpere==1:  EField[S+fi].color=Ecolor[0]

        FaradayLoop.x[0]=fi-1
        FaradayLoop.x[1]=fi-1
        FaradayLoop.x[2]=FaradayLoop.x[3]=fi+1
        FaradayLoop.x[4]=FaradayLoop.x[0]

        AmpereLoop.x[0]=fi-1
        AmpereLoop.x[1]=fi-1
        AmpereLoop.x[2]=AmpereLoop.x[3]=fi+1
        AmpereLoop.x[4]=AmpereLoop.x[0]

        for i in arange(0,len(gaussPos)):
            gaussPos0[i][0]+=(newfi-fi)            
            gaussPos1[i][0]+=(newfi-fi)            

    #UPDATE THE FIELDS
    for i in arange(0,len(EField)):
        amp=Emax*sin(k*(i%(2*S)-S)-omega*t)
        EField[i].axis.y=amp
        BField[i].axis.z=amp
#        print (i%(2*S)-S), EField[i].pos[0]

    #UPDATE THE FLUX
    if showGauss>0:
##        px=take(gaussPos, (0,), 1)
##        amp0=sin(k*px-omega*t)
##        dA_y=take(gauss_dA, (1,), 1)
##        dA_z=take(gauss_dA, (2,), 1)
##        Eflux_=amp*dA_y
##        Bflux_=amp*dA_z
##        col_g=array([0]*len(gaussPos)) #gaussCol[:,1]
##        col_r=((0.5+Bflux_)/2.)*abs(dA_z)
##        col_b=((0.5+Eflux_)/2.)*abs(dA_y)
###        put(gaussElements.color, [0,2], [col_r, col_b])

        for i in arange(0,len(gaussPos),6):
            colorcheck=vector(0,0,0)
            #print
            for ii in arange(0,6):
                #print i+ii, gaussPos[i+ii][0], gauss_dA[i+ii][1], gauss_dA[i+ii][2]
                amp=sin(k*gaussPos[i+ii][0]-omega*t)
                g_dA1=gauss_dA[i+ii][1]*showE #for Eflux
                g_dA2=gauss_dA[i+ii][2]*showB #for Bflux
                #Eflux=amp*g_dA[1];E_on=abs(gauss_dA[i][1])
                #Bflux=amp*g_dA[2];B_on=abs(gauss_dA[i][2])
                ###col_g=gaussCol[i][1]
                #gaussElements.color[i]= ( (0.5+amp*g_dA1/2.)*abs(g_dA1) , col_g, (0.5+amp*g_dA2/2.)*abs(g_dA2) )
                gaussElements.color[i+ii][2]= (0.5+amp*g_dA1/2.)*abs(g_dA1)
                gaussElements.color[i+ii][0]= (0.5+amp*g_dA2/2.)*abs(g_dA2) 
                colorcheck+=vector(gaussElements.color[i+ii])
            #print colorcheck
            if mag2(colorcheck)<2.9:
                for ii in arange(0,6):
                    gaussElements.pos[i+ii]=gaussPos0[i+ii]
            else:
                for ii in arange(0,6):
                    gaussElements.pos[i+ii]=gaussPos1[i+ii]
                    

#    for i in front:
#        i.x=(i.phase+(omega/k)*t )%(2*S)-S        #kx-wt=constant

    framefront1.x=(phase1+(omega/k)*t )%(2*S)-S        #kx-wt=constant
    framefront2.x=(phase2+(omega/k)*t )%(2*S)-S        #kx-wt=constant

    #UPDATE THE dB/dt
    dBdt.axis.z=magnify*omega*Emax*abs(cos(phase))*-sign( dot(EField[S+newfi+1].axis-EField[S+newfi-1].axis,vector(0,1,0)) )
    dBdtlabel.text=prefixFaraday[verbose]
    if dot(dBdt.axis,BField[S+newfi].axis)>0:
        dBdtlabel.text += dBdtpos_text[calculus]
        dBdt.pos=vector(newfi,0,BField[S+newfi].axis.z)+0*label_epsV
    elif dot(dBdt.axis,BField[S+newfi].axis)<0:
        dBdtlabel.text += dBdtneg_text[calculus]
        dBdt.pos=vector(newfi,0,BField[S+newfi].axis.z-dBdt.axis.z)+0*label_epsV
    else:
        dBdtlabel.text += dBdtzer_text[calculus]
        dBdt.pos=vector(newfi,0,BField[S+newfi].axis.z)
    dBdtlabel.pos=BField[S+newfi].pos+BField[S+newfi].axis+0*label_epsV
       
    #UPDATE THE dE/dt    
    dEdt.axis.y=magnify*omega*Emax*abs(cos(phase))*sign( dot(BField[S+newfi+1].axis-BField[S+newfi-1].axis,vector(0,0,-1)) )
    dEdtlabel.text=prefixAmpere[verbose]
    if dot(dEdt.axis,EField[S+newfi].axis)>0:
        dEdtlabel.text += dEdtpos_text[calculus]
        dEdt.pos=vector(newfi,EField[S+newfi].axis.y,0)
    elif dot(dEdt.axis,EField[S+newfi].axis)<0:
        dEdtlabel.text += dEdtneg_text[calculus]
        dEdt.pos=vector(newfi,EField[S+newfi].axis.y-dEdt.axis.y,0)
    else:
        dEdtlabel.text += dEdtzer_text[calculus]
        dEdt.pos=vector(newfi,EField[S+newfi].axis.y,0)
    dEdtlabel.pos=EField[S+newfi].pos+EField[S+newfi].axis
            



    if scene.kb.keys: # is there an event waiting to be processed?
        s = scene.kb.getkey() # obtain keyboard information
        if s=='a':
            showAmpere +=1; showAmpere %=2; AmpereLoop.visible=dEdt.visible=showAmpere; dEdtlabel.visible=showAmpere*verbose
            if showAmpere==1:
                BField[S+fi-1].color=ddtcolor[0]
                BField[S+fi+1].color=ddtcolor[0]
            else:
                BField[S+fi-1].color=Bcolor[dimFields]
                BField[S+fi+1].color=Bcolor[dimFields]

        if s=='f':
            showFaraday +=1; showFaraday %=2; FaradayLoop.visible=dBdt.visible=showFaraday;dBdtlabel.visible=showFaraday*verbose
            if showFaraday==1:
                EField[S+fi-1].color=ddtcolor[1]
                EField[S+fi+1].color=ddtcolor[1]
            else:
                EField[S+fi-1].color=Ecolor[dimFields]
                EField[S+fi+1].color=Ecolor[dimFields]

        if s=='d':
            dimFields +=1; dimFields %=2; 

            for i in EField:
                i.color=Ecolor[dimFields]
            for i in BField:
                i.color=Bcolor[dimFields]


        if s=='e':
            showE +=1; showE %=2; 

            for i in EField:
                i.visible=showE*(1-showNeighboringWaves*(i.nbw%2))
        if s=='b':
            showB +=1; showB %=2; 

            for i in BField:
                i.visible=showB*(1-showNeighboringWaves*(i.nbw%2))


        if s=='v':
            verbose +=1; verbose %=3;
            dBdtlabel.visible=showFaraday*min(verbose,1);dEdtlabel.visible=showAmpere*min(verbose,1)

        if s=='c':
            calculus +=1; calculus %=2; 

        if s=='s':
            for i in arange(0,len(EField)):
                EField[i].visible=1-showNeighboringWaves*(EField[i].nbw%2)
                BField[i].visible=1-showNeighboringWaves*(BField[i].nbw%2)
            showNeighboringWaves +=1; showNeighboringWaves %=2;
            

        if s=='w':
            showWavefronts +=1; showWavefronts %=2;
            for i in front:
                i.visible=showWavefronts
            for i in front2:
                i.visible=showWavefronts
                
            
        if s=='g':
            showGauss +=1; showGauss %=2;
            for i in gaussSurface:
                i.visible=showGauss
            gaussElements.visible=showGauss
        if s=='n':
            colorScheme = (colorScheme+1)%2 #TOGGLE colorScheme
            scene.background=colorBackground[colorScheme]
            dEdtlabel.opacity=labelBackground[colorScheme]
            dBdtlabel.opacity=labelBackground[colorScheme]
            ddtcolor[0]=Bcolor[2+colorScheme]
            ddtcolor[1]=Ecolor[2+colorScheme]

            FaradayLoop.color=ddtcolor[0]
            dBdt.color=ddtcolor[0]
            dBdtlabel.color=Bcolor[2]  # using ddtcolor[1] will have darker text
            AmpereLoop.color=ddtcolor[1]
            dEdt.color=ddtcolor[1]
            dEdtlabel.color=Ecolor[2]  #using ddtcolor[0] will have darker text

            for gS in gaussSurface:
                for gsC in arange(len(gS.color)):
                    gS.color[gsC]=vector(Gcolor_boundary[colorScheme])

            for f in arange(1,len(front)):
                front[f].color=Frontcolor[colorScheme]
            for f in arange(1,len(front2)):
                front2[f].color=Frontcolor[colorScheme]

            scene.ambient=1-scene.ambient

        if s=='z':
            print "scene.center=(%f,%f,%f)"  % tuple(scene.center)
            print "scene.forward=(%f,%f,%f)"  % tuple(scene.forward)
            print "scene.range=(%f,%f,%f)"  % tuple(scene.range)
            print "t=%f\n" %t

        if s==' ':
            trun = (trun+1)%2 #TOGGLE PAUSE


        if showFaraday==1: EField[S+fi-1].color=EField[S+fi+1].color=ddtcolor[0]
        if showAmpere==1:  BField[S+fi-1].color=BField[S+fi+1].color=ddtcolor[1]

        if highlightField==1:
            if showFaraday==1: BField[S+fi].color=Bcolor[0]
            else:              BField[S+fi].color=Bcolor[dimFields]

            if showAmpere==1:  EField[S+fi].color=Ecolor[0]
            else:              EField[S+fi].color=Ecolor[dimFields]

    if scene.mouse.clicked:  #CLICK TOGGLE PAUSE
        scene.mouse.getclick()
        trun = (trun+1)%2
        
    if trun>0:
        t+=0.1

    rate(60) #v0.51 suggested by Jonathan Brandmeyer to reduce mouse polling when idle
    


from pydobot import Dobot 
import time 

dev = Dobot(port= "/dev/ttyUSB0")

F1 = -45
F2 = -20 
F3 = 4
F4 = 28


def centerDrop_1(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_2(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)
    

def centerDrop_3(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_4(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_5(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_6(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_7(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_8(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def centerDrop_9(x1,y1,z1,H):
    r=0
    gap = 5
    z = -48
    dev.move_to(x =x1 , y=y1 , z = z+gap,r=r)
    dev.move_to(x =x1 , y =y1 , z=z , r=r)
    dev.suck(True)
    dev.move_to(x=x1 , y= y1, z=H ,r=r)
    dev.move_to(230,44,H,r=r)
    dev.move_to(230,44,z1,r)
    dev.suck(False)
    dev.move_to(230,44,H,r=r)

def Home():
    dev.move_to(x=200,y =0 ,z = 100 ,r =0)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#((x,y,z,r ), (j1,j2,j3,j4)) = dev.get_pose()
#print(dev.get_pose())
#dev.move_to(x=200,y=0,z=-45)
#dev.suck(False)

#def test_autocenterDrop(cx,cy,H):
    #gap = 6 

    #dev.move_to(x =cx , y=cy , z = z+gap,r=r)
    #dev.move_to(x =cx , y =cy , z=z , r=r)
    #dev.suck(True)
    #dev.move_to(x=x1 , y= y1, z=H ,r=r)
    #dev.move_to(230,44,H,r=r)
    #dev.move_to(230,44,z1,r)
    #dev.suck(False)
    #dev.move_to(230,44,H,r=r)




#def SD(x1,y1,x2,y2):
    #r = 0 
    #z =-45
    #gap  = 6
    #dev.move_to(x=x1 , y = y1 , z= z+gap ,r=r)
    #dev.move_to(x =x1 , y =y1 , z=z , r=r)
    #dev.suck(True)
    #dev.move_to(x=x1 , y= y1, z=z+gap ,r=r)
    #dev.move_to(x=x2 , y = y2 , z= z+gap ,r=r)
    #dev.move_to(x =x2 , y =y2 , z=z , r=r)
    #dev.suck(False)
    #dev.move_to(x=x2 , y= y2, z=z+gap ,r=r)


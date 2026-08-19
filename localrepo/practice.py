print("please enter the colour of light :")
colour = input("colour : ")
if(colour=="RED" or colour=="red"):
    print("Traffic Light is RED")
    print("Please don't move")
elif(colour=="YELLOW" or colour ==  "yellow"):
    print("Traffic light is yellow please wait for a minute ")
elif(colour=="GREEN" or colour =='green'):
    print("Traffic light is green you can move now")
else:
    print("Traffic light is broken")
    print("NEEDED REPAIR")
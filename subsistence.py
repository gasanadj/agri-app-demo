import cabbage
import cassava
import greens

while True:
 def subsistence():    
    #START
        print("You have selected Subsistence farming ")
        print("General farming tips")
        print("Which Crop are you interested in?")
        print("1.Cabbage")
        print("2.Cassava")
        print("3.Greens")
        print("0.To quit APP")
    #user iput    
        choice=int(input("Select the crop(1-3) : "))
        if (choice == 1):#cabbage
           cabbage.cabbage() 
        elif (choice == 2):#cassava
            cassava.cassava()
        elif (choice==3):#greens
            greens.greens()
        else:
            print("INVALID INPUT")        
    #end  
    
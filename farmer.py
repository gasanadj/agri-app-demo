import largescale
import smallscale
import subfarming
def farmer():
     print("What type of farmer are you")
     print("1.Large scale farmer")
     print("2.Small scale farmer")
     print("3.Subsistence farmer")
     type=int(input("Select the type of farmer(1-3: )"))
     if (type == 1):
       print("You selected Largescale farmer")
       largescale.largescale()
     elif (type == 2):
       print("You selected Smallscale farmer")
       smallscale.smallscale 
     elif (type == 3):
       print("You selected Subsistence farmer")
       subfarming.subsistence() 
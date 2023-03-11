import farmer
import crops
import rice
import Tea
import sugarcane
import small
import Potatoes
import Beans
import Maize
import Banana
def english():
    farmer.farmers()
    farmer_choice = int(input("Enter choice of Farmer: "))
    if (farmer_choice == 1) :
        crops.large()
        crop_choice = int(input("Enter choice of crop: "))
        if (crop_choice == 1):
            rice.rice()
        elif (crop_choice == 2):
            Tea.tea()
        elif (crop_choice == 3):
            sugarcane.sugarcane()
    elif (farmer_choice == 2):
        small.small_scale()
        crop_choice = int(input("Enter crop choice "))
        if (crop_choice == 1):
            Potatoes.potatoes()
        elif (crop_choice == 2):
            Beans.beans()
        elif (crop_choice == 3):
            Maize.maize()
        elif (crop_choice == 4):
            Banana.banana()


        



def cabbage(): 
    print("You selected Cabbage")
    print("Which type of information are you looking for?")
    print("1.Best farming practices")
    print("2.Best fertilizers and insecticides")
    print("3.Best harvesting and storage practices")
    print("0.To quit APP")
    info=int(input("Select information of interest(1-3) : "))
    if (info == 1):
                    print("You selected Best farming practices")
                    print("*THE BEST FARMING PRACTICES*")
    elif (info == 2):
                    print("You selected Best fertilizers and insecticides")
                    print("*THE BEST FERTILIZERS AND INSECTICIDES*") 
    elif (info == 3):
                    print("You selected Best harvesting and storage practices")
                    print("*THE BEST HARVESTING AND STORAGE PRACTICES*")  
   # elif (info == 0):
                    #break   
    else:
                    print("invalid input")
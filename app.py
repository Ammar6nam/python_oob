# #!/usr/bin/env python


class aquarium_app:
    def __init__(self, totalNumFish, EyeColor, skinColor):
        self.SkinColor = skinColor
        self.roundOfLife = 0
        self.eyeColor = EyeColor
        self.deadFish = 0
        self.totalNumFish = totalNumFish

    def _start(self):
        if self.totalNumFish == 0:
            print("There are no alive fish left.")
            #return
        self.roundOfLife += 1

        print(f"{str(self.totalNumFish)} fish are swimming. Their eyes are {self.eyeColor} and their skin is {self.SkinColor}.",f"There are {str(self.deadFish)}  dead fish with them in the aquarium.",f"The fish have now been swimming {str(self.roundOfLife)} times.",sep='\n')

    def __numOfnewDeadFish(__self, _newDeadFish):
        __self.totalNumFish -= _newDeadFish
        __self.deadFish += _newDeadFish
        if _newDeadFish > 1:
            print(f"{str(_newDeadFish)} fish have died.")
        else:
            print("A fish has died.")
        if __self.totalNumFish == 0:
            print("All fish are dead.","GAME OVER","=====",sep='\n')


i=0
totalNum=int(input('Enter teh total number of the Fish: '))
eyeColor=str(input('Enter the color of eye: '))
skinColor=str(input('Enter the color of the skin: '))
print('\n')
MyAquariumApp = aquarium_app(totalNum, eyeColor, skinColor)
while i<1:
    MyAquariumApp._start()
    print('\n')
    newDeadFish=int(input('Enter the number of new dead fish! '))
    print('\n')
    MyAquariumApp._aquarium_app__numOfnewDeadFish(newDeadFish)
    totalNum-=newDeadFish
    if totalNum !=0:
        continue
    else:
        break


    # MyAquariumApp._start()
    # MyAquariumApp._aquarium_app__numOfnewDeadFish(1)
    # MyAquariumApp._start()
    # MyAquariumApp._aquarium_app__numOfnewDeadFish(2)
    # MyAquariumApp._start()
    # MyAquariumApp._aquarium_app__numOfnewDeadFish(1)



# def numOfnewDeadFish(totalNum,newDeadFish):
#     if totalNum == 0:
#         print("All fish are dead.","GAME OVER","=====",sep='\n')
#     totalNum -= newDeadFish
#     if _newDeadFish > 1:
#         print(f"{str(_newDeadFish)} fish have died.")
#     else:
#         print("A fish has died.")
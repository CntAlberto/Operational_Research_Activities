#----------------------------------------------------------------------------------
#-- Students: Alberto Cantele (10766393), Biagio Cancelliere (10713858)
#-- First Activity Task from Foundations of Operational Research: "A dangerous Hiking"
#----------------------------------------------------------------------------------

import array as arr

foodWeight= arr.array('i', [5,8,12])
waterWeight= arr.array('i', [3,5,8])
shelterWeight= arr.array('i', [5,8,12])
foodPt= arr.array('i', [10,20,25])
waterPt= arr.array('i', [10,20,25])
shelterPt= arr.array('i', [5,15,20])
total=[]
coordinateI=[]
coordinateJ=[]
coordinateK=[]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if foodWeight[i]+waterWeight[j]+shelterWeight[k]+3<=25:
                total.append(20+foodPt[i]+waterPt[j]+shelterPt[k])
                coordinateI.append(i)
                coordinateJ.append(j)
                coordinateK.append(k)

maxElement= max(total)
maxIndex=total.index(maxElement)
print("points: ",maxElement," food: ",
      foodPt[coordinateI[maxIndex]]," water: ",
      waterPt[coordinateJ[maxIndex]]," shelter: ",
      shelterPt[coordinateK[maxIndex]]," defense: 20")
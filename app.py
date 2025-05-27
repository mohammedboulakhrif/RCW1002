myList=[2,4,6,8,10,12]
i,j=0,len(myList)-1
while(i<j):
    temp=myList[1]
    myList[i]=myList[j]
    myList[j]=temp
    i+=1
    j-=1
print (f'ma list finale est {myList}')    

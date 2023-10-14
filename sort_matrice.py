mylist = [[-9,8,45,-6,21,20,14] ,
          [45,2,-1,30,2,1,3,4] ,
          [5,9,63,1,4,5,3,10,45] ,
          [45,32,10,25,32,6,32] ,
          [14,20,23,56,95,2]
          ]
def display(list) : 
    for  _ , n in enumerate(list) :
        print(  _ , " -> ", n )
l = 0   
m = 0 
n = 0 
                
display(mylist)
print('\n-------------------------------\n')
 
def tri_row(list):
    
    line = 0 
    while line<= len(list) - 1 :
        
        for  m  in range(len(list[line])):
            for  n  in range(m + 1 ) :
                if list[line][m] < list[line][n]:
                    #print('True -- >' , mylist[line][n] , ' more than ' , mylist[line][m])
                    list[line][n]  ,  list[line][m] =  list[line][m] ,  list[line][n]   
                            
        print(list[line] , '\n--------------------------------------\n')
        
        line += 1
        return list
    
    
           
    
        
         
     
   
     
 
 
 
  
            


            
        
        
        
    
    
    
    
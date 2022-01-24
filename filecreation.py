import numpy as np

def createFile(decisionvector, A, filetitle, costlist, durationlist): # A = matrix with RMP duties, filetitle must be string
    
    file = open(filetitle + '.txt', "a")
    
    for i in range(len(decisionvector)): # we gaan alle elementen van de decision vector af
        lst_to_add_to_file = []
        if decisionvector[i] != 0:       # als deze niet gelijk is aan nul, zijn we geinteresseerd
            # Find value in decision vector x_d    
            lst_to_add_to_file.append(decisionvector[i])
            
            # Costs task
            lst_to_add_to_file.append(costlist[i])
            
            # Duration task
            lst_to_add_to_file.append(durationlist[i])
            
            # Find tasks in column
            B = np.array(A)
            column = B[:,i]
            tasks = []
            for elt in range(len(column)):
                if column[elt] == 1:
                    tasks.append(elt)
            lst_to_add_to_file.append(tasks)
            
            towrite = '\n'
            for i in range(len(lst_to_add_to_file) -1):
                
                towrite += str(lst_to_add_to_file[i])
                towrite += ' '
            for j in range(len(lst_to_add_to_file[-1])):
                towrite += str(lst_to_add_to_file[-1][j])
                towrite += ' '
                
            #towrite += '\n'
            
            file.write(towrite)
    
    file.close()
            
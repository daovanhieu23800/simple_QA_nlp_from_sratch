file_path = 'queries.txt'
file = open(file_path, 'r')
i=0
for x in file:
    new_f = open(f"./Input/input_{i}.txt", "w")
    new_f.write(x)
    new_f.close()
    
        
    i+=1



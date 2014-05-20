#add following line in place of your code. It is exercise last question of 4th lectures in which we have to combine related records 
# This is actually mapper code, 
for line in reader:
        newLine = []
        if len(line) == 5:# main table        
              newLine = [line[0], "A", line[1], line[2], line[3], line[4]]
        if len(line) == 19: # related table 
               newLine = [line[3], "B", line[0], line[1], line[2], line[5], line[6], line[7], line[8], line[9]]
        
       writer.writerow(newLine)
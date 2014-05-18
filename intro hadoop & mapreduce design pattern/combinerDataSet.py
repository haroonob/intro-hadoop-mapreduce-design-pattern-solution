for line in reader:
        newLine = []
        if len(line) == 5:       
              newLine = [line[0], "A", line[1], line[2], line[3], line[4]]
        if len(line) == 19: 
               newLine = [line[3], "B", line[0], line[1], line[2], line[5], line[6], line[7], line[8], line[9]]
        
       writer.writerow(newLine)
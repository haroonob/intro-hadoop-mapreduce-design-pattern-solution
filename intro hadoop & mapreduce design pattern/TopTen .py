linesWithIndexValue = [] # Have the length of the body as the first element in the array and the line as the 2nd element
    bodyLength = 0

    for line in reader:
       bodyLength = len(line[4]) # get the size of the body
       linesWithIndexValue.append([bodyLength, line])

    linesWithIndexValue.sort(key = lambda x: x[0]) #x is the length of the body for each line[4]
    for line in linesWithIndexValue[-10:]:
        writer.writerow(line[1])
        
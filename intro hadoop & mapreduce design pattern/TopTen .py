#Your mapper function should print out 10 lines containing longest posts, sorted in
#ascending order from shortest to longest.
#Please do not use global variables and do not change the "main" function.

linesWithIndexValue = [] # Have the length of the body as the first element in the array and the line as the 2nd element
    bodyLength = 0

    for line in reader:
       bodyLength = len(line[4]) # get the size of the body
       linesWithIndexValue.append([bodyLength, line])

    linesWithIndexValue.sort() #x is the length of the body for each line[4]
    for line in linesWithIndexValue[-10:]:
        writer.writerow(line[1])
        
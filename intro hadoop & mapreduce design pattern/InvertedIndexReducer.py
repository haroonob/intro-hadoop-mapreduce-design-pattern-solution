#!/usr/bin/python
# fantastically count 17583,1007765,1025821,7004477,9006895
# # fantastic appear in 345

import sys

nodeIds=""
oldKey = None

#combine question ids for each words

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, nodeId= data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", nodeIds
        oldKey = thisKey
        nodeIds = ""

    oldKey = thisKey
    nodeIds += nodeId+","

if oldKey != None:
    print oldKey, "\t", nodeIds


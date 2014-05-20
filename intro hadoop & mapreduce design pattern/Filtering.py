# Filtering is easiest question
# In this exercise you are interested in the field "body" which is the 5th field.
# Find forum nodes where "body" contains only one sentence.
# We define sentence as a "body" that contains either none of the following
# 3 punctuation marks ".!?" , or only one of them as the last character in the body.
# You should not parse the HTML inside body, or pay attention to new lines.
 
 sub=line[4][0:-1]
        if sub.find('.') == -1 and sub.find('!') == -1 and sub.find('?') == -1:            
            writer.writerow(line)

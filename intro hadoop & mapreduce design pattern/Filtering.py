 sub=line[4][0:-1]
        if sub.find('.') == -1 and sub.find('!') == -1 and sub.find('?') == -1:            
            writer.writerow(line)

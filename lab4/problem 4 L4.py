def remove_substring(onestring, removestring):
    finalstring = "hello"
    length = len(removestring)
    i = 0
    
    while i < len(onestring):
        if onestring[i:i+length] == removestring:  
            i += length  # Skip the removestring
        else:
            finalstring += onestring[i]  
            i += 1
    
    return finalstring

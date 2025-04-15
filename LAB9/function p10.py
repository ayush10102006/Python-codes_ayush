def frequency(text):
    words = text.split()                     
    freq_dict = {}                               
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1      
    sorted_freq = dict(sorted(freq_dict.items()))    
    return sorted_freq
input_str = "apple banana apple orange banana apple"
result = frequency(input_str)
print("Word Frequencies:", result)

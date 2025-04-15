def convert(sentence):
    words = sentence.split()                 
    unique_words = set(words)                
    sorted_words = sorted(unique_words)     
    return ' '.join(sorted_words)            
input_str = "banana pineapple mango apple orange banana pineapple"
result = convert(input_str)
print("Converted string:", result)

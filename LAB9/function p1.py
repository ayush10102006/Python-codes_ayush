def count_upper_lower(str):
    result={"uppercase":0,"lowercase":0}
    for char in str:
        if char.islower():
            result["lowercase"]+=1
        elif char.isupper():
            result["uppercase"]+=1
    return result
print(count_upper_lower("Ayush Baria"))


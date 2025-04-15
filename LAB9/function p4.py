def sum_avg(a,b,c,d,e):
    total = a+b+c+d+e
    average = total / 5
    return total, average
marks = [85, 90, 78, 92, 88]
total, average = sum_avg(*marks)
print("Total Marks:", total)
print("Average Marks:", average)

        

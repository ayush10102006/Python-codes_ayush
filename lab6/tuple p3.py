from datetime import date
date1=(5, 4, 2023)  
date2=(10, 4, 2023)
d1=date(date1[2], date1[1], date1[0])
d2=date(date2[2], date2[1], date2[0])
difference=abs((d2-d1).days)
print("Number of days between {date1} and {date2}: {difference} days",difference)

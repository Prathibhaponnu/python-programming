from datetime import datetime
current_Year=datetime.today().year
final_Year=int(input("Enter the final year:"))
print("List of leap years")
for year in range(current_Year,final_Year):
    if(year%4==0) and (year%100!=0) or(year%400==0):
        print(year)

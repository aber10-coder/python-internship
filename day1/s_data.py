sales = [1200, 1500, 900, 1800, 2200, 1700, 1300]
high=0
low=10000000000000000000
total=0
avg=0
count=0
for item in sales:
    total=total+item
    if high<item:
        high=item
    if low>item:
        low=item
for i in sales:
    if i>1500:
        count=count+1
avg=total/7
print(f'Average sales is: {avg}')
print(f'Highest sales is: {high}')
print(f'Lowest sales is: {low}')
print(f"Number of days where sales exceeded 1500: {count}")

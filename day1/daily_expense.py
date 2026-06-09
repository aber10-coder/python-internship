total_exp=0
avg_dexp=0
h_exp=0
l_exp=1000000000000
exp=[]
print('enter your day by day for 7 days:')
for i in range(0,7):
    inp=int(input())
    exp.append(inp)
for item in exp:
    total_exp=total_exp+item
    if item>h_exp:
        h_exp=item
    if item<l_exp:
        l_exp=item
avg_dexp=(total_exp/7)
print(f"average daily expense is {avg_dexp}")
print(f"Highest expense: {h_exp}")
print(f"Lowest exp: {l_exp}")


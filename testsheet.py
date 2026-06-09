list=[10,8,5,9,5,20,26]
count=0
for item in list:
    index=[]
    app=list.index(item)
    index.append(app)
    for i in index:
        count=count+1
        if count>1:
            for j in range(0,count-1):
                list.pop(i)
print(list)

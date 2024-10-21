
dict = ["cat", "bat", "cft", "xyz"]
search = "c*t"

local = []
indexes=[]
count=0
for i in range(len(search)):
    if search[i]!="*":
        count+=1
        indexes.append(i)
[search]*(26^count)

queue=[]
for i in range(count):
    p=""
    queue.pop(0)
    if search[i]!="*":
        p.append(search[i])
    else:
        for j in range(0,26):
            
            p.append(i+'a')
            queue.append(p)

    
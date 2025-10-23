from collections import deque 

queueLS = deque(["Jako", "Annah", "Jrima", "Bamit"])
queueLS.append("X-man")




print(type(queueLS), queueLS)
print(queueLS, "\n")


pL = queueLS.popleft()

print("popleft() : ", pL)

print("queueLS : ", queueLS)


# we can't pop from right!!!
#pR = queueLS.popright()


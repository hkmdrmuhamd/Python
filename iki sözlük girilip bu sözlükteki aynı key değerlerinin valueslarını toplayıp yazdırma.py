dic1 = {"a":100,"b":400,"c":700}
dic2 = {"a":500,"b":100,"d":200}
dic3 = dict()

for i in dic1:
    for j in dic2:
        if i == j:
            a = dic1[i]
            b = dic2[j]
            c = a + b
            dic3.update({i:c})
        else:
            dic3.update({j: dic2[j]})
            dic3.update({i:dic1[i]})
print(dic3)






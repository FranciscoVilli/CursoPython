
list2 = ["R1","R2","R3","S1","S2","S4","S5","FW1","OLT1"]
for i in list2:
    if "R" in i:  
        print(f"Los valores R son: {i}")
    elif "S" in i:
        print(f"Los valores S son: {i}")
    else:
        print(f"Los valores distintos son: {i}")

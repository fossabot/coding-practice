def direction_reduction(arr):
    stack = []
    for d in arr:
        if len(stack) > 0:
            if (d=="NORTH" and stack[-1]=="SOUTH") or (d=="SOUTH" and stack[-1]=="NORTH")  or (d=="EAST" and stack[-1]=="WEST") or (d=="WEST" and stack[-1]=="EAST"):
                stack.pop()
                continue
        stack.append(d)
        print("stack = ", stack)
    return stack
            
print(direction_reduction(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
def move_zeros(array):
    l = [a for a in array if a is False or a!=0]
    return l+[0]*(len(array)-len(l))

print("Input: ", (["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
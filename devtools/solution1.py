
def solution():
    # 2단 부터 5단까지 
    for j in range(1,10):
        for i in range(2,6):
            space = ""
            if(i*j < 10): 
                space += " "
            print(" "+str(i) + " * " + str(j) + " = "+ str(i*j),end= "  "+space)
        print()
    print()  
    # 6단 부터 9단까지 
    for j in range(1,10):
        for i in range(6,10):
            space = ""
            if(i*j < 10): 
                space += " "
            print(" "+str(i) + " * " + str(j) + " = "+ str(i*j),end= "  "+space)
        print()
    return 

solution()

# for i in range(1, 10):
#     for j in range(2, 10):
#         print(f"{j} * {i} = {j*i}", end="   " if j % 5 != 0 else "\n")
#     if i % 9 != 0:
#         print("\n")


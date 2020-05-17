def convert(left_operand):
    lo_byte=list(bin(left_operand))  #turns left operand into binary
    lo_byte=lo_byte[2:]              #strips the part 0b
    lis_32b=list()
    i=0
    while i<=31-len(lo_byte):
        lis_32b.append(0)
        i+=1
    for num in lo_byte:
        lis_32b.append(int(num))
    return lis_32b    

import binary
import complement
import msbshift
left_operand=int(input("Input the left operand  for the shift '>>>' operation:"))
right_operand=int(input("Input the right operand  for the shift '>>>' operation:"))
lis_32b=binary.convert(left_operand)        #conert decimal to 32 bit binary
comp1s=complement.complement1s(lis_32b)     # Turning into i's complement
comp2s=complement.complement2s(comp1s)      #Turning into 2's complement
msb_l=msbshift.shift(right_operand,comp2s)  #msb shifting and putting zero
#sum
iterate=31
a=1
sum=0
while iterate>=0:
    sum=sum+a*msb_l[iterate]
    b=a
    a+=b
    iterate-=1
print(left_operand,">>>",right_operand,":",sum)

list_word=[ 'hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','tail','domestic','catsize']
a=input('''Enter the specifications of the animal from the following-:
'hair','feathers','eggs','milk','airborne','aquatic','predator','toothed',
'backbone','breathes','venomous','fins','tail','domestic','catsize'-: ''')
word=a.split(',')
print(word)
num=[]
for i in list_word:
    if i in word:
       num.append('1')
    else:
        num.append('0')        
print(num)
with open('zoo.data','r') as u:
     for line in u:
         line=line.replace('\n',' ')
         words=line.split(',')
         print(words)
         j1=words[1:13]
         for i in range(14,17):
             j1.append(words[i])
         print(j1)    
         if j1==num:
             print('The name of animal is',words[0])
         
    

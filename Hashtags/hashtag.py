unique_hashtags=list()
name_dict=dict()
with open('data.txt','r') as u:
     for line in u:
         line=line.split('-')
         #print(a)
         mid_sentence=line[1]
         #print(word)
         for i in range(0,len(mid_sentence)):
             if mid_sentence[i]=='#':
                 hashtag=' '
                 for j in range(i,len(mid_sentence)):
                    if mid_sentence[j]!=' ':
                       hashtag+=mid_sentence[j]
                    else:
                        if hashtag not in unique_hashtags:
                            unique_hashtags.append(hashtag)
                            i=j
                            break
                        else:
                            i=j
                            break
                         
print("List of unique hashtag is: \n",unique_hashtags)                        
for hashtag in unique_hashtags:
    name_list=list()
    with open("data.txt",'r') as s:
        for line in s:
            #print(line)
            line=line.replace('\n',' ')
            mid_line=line.split('-')
            #print(word)
            #print(lis)
            if hashtag in mid_line[1]:
                #print(word[2])
                name_list.append(mid_line[2])
        name_dict[hashtag]=name_list
print("hashtags used by the people are :")
print(name_dict)         

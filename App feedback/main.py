import os
class appreview:
    def __init__(self,fileName):
        appreview.path=fileName
        
    def openfile(self):
        """

        Defining the dictonary with the category and its values.


        """
        cat_dict={'cat1':"User rating of Instagram",'cat2':"User rating of Whatsapp",'cat3':"User rating of Facebook",
        'cat4':"User rating of snapchat",'cat5':"User rating of Twitter",'cat6':"User rating of Telegram"
        ,'cat7':"User rating of Hike",'cat8':"User rating of Skype",'cat9':"User rating of Hangout by Google",'cat10':"User rating of Google duo"}
        cat_key=list(cat_dict.keys())
        """

        retriving the data in dictionary as users review of every category

        """
        main_dict=dict()
        with open(self.path,'r') as u:
            for line in u:
                temp_dict=dict()
                line=line.replace('\n','')
                line=line.split(',')
                a=line[1:11]
                for i in range(0,10):
                    temp_dict[cat_key[i]]=a[i]
                main_dict[line[0]]=temp_dict
        value_list=list(main_dict.values())
        value_list=value_list[1:]
        """

        Making of empty dictionary for the cateogry rating with empty list as values

        """
        review=dict()
        for i in cat_key:
            review[i]=list()
        """

        Appending the data to dict values that correspond to the specific key of the dictionary.

        """
        for j in value_list:
            for k,v in review.items():
                for x,y in j.items():
                    if x==k:
                        v.append(float(y))
        """

        Printing the average result of the specific category here in case (Average review of the apps).

        """
        for k,y in cat_dict.items():
            for k1,v1 in review.items():
                if k==k1:
                    print(y,round(sum(v1)/len(v1),2))
       
# main
fileName=input("Enter the file name with .csv extension")
filename,file_extension=os.path.splitext(fileName)
count=0
"""
Checking the file format is correct or not

"""
while(count!=2):
    if file_extension=='.csv':
        users=appreview(fileName)
        users.openfile()
        break
    else: 
        count+=1
        print("you entered wrong file extension")
        fileName=input("Enter the file name with .csv extension")
        filename,file_extension=os.path.splitext(fileName)







                 

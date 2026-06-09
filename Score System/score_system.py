#!/usr/bin/python3
import csv
from student import student
from os import listdir


#Read & Process

    #Input
names=[]
subjects=[]
score_data=[]

exam_name=input('Please enter the exam name (corresponding to the CSV file name):')
while exam_name+'.csv' not in listdir():
    exam_name=input('Please enter the correct exam name! ：')

    #Read the CSV file
with open(exam_name+'.csv','r',encoding='utf-8') as file:
    csv_reader=csv.reader(file)

    line=1
    for row in csv_reader:
        if line==1:
            subjects=row[1:]
            line+=1
        elif line!=1:
            names.append(row[0])
            score_data.append(list(map(int,row[1:])))

    #Create an instance for each student and store it in a dictionary.
stu_dict={name : student(name,scores) for name,scores in zip(names,score_data)}

    #Create a list of scores for each subject and store it in a dictionary.
score_dict={}
for pos in range(len(subjects)):
    sub_score=[]
    for name in names:
        sub_score.append(stu_dict[name].scores[pos])
    score_dict.update({subjects[pos]:sub_score})

    #Ranking
sum_list=[stu_dict[name].sum_score for name in names]
sum_list.sort()
sum_list.reverse()
for name in names:
    stu_dict[name].rank=sum_list.index(stu_dict[name].sum_score)+1


#Store

    #Confirm
confirm=input('Record the details of this exam? (Y/N):')
while confirm not in ('yYnN'):
    confirm=input('Please enter Y or N !:')
print('\n')

if confirm in ('yY'):
    with open('report.txt','a+',encoding='utf-8') as file:
        
        file.write('*'*5+exam_name+'*'*5+'\n\n')
        
    #Store student data
        file.write(f'{'name':<16}')
        for sub in subjects:
            file.write(f'{sub:<8}')
        file.write(f'{'Total':<7}{'Avg':<6}{'Level':<6}{'Rank':<6}\n')
        file.write('-'*8*(5+len(subjects))+'\n')

        for name in names:
            file.write(f'{stu_dict[name].name:<16}')
            for score in stu_dict[name].scores:
                file.write(f'{score:<8}')
            file.write(f'{stu_dict[name].sum_score:<7}{stu_dict[name].ave:<7.1f}{stu_dict[name].level:<5}{stu_dict[name].rank}\n')

        file.write('-'*8*(5+len(subjects))+'\n')
    
    #Store subject data
        file.write(f'{'Subj':<10}{'Max':<8}{'Min':<8}{'Avg'}\n')
        file.write('-'*32+'\n')

        for sub in subjects:
            file.write(f'{sub:<10}{max(score_dict[sub]):<8}{min(score_dict[sub]):<8}{sum(score_dict[sub])*1.0/len(names):.1f}\n')

        file.write('-'*32+'\n\n\n\n')  

else: pass

'''For Notepad, please use the Consolas, Courier New or Cascadia Code font.'''


#Terminal output

    #Output student data
print(f'{'Name':<16}',end='')
for sub in subjects:
    print(f'{sub:<8}',end='')
print(f'{'Total':<7}{'Avg':<6}{'Level':<6}{'Rank':<6}')
print('-'*8*(5+len(subjects)))

for name in names:
    print(f'{stu_dict[name].name:<16}',end='')
    for score in stu_dict[name].scores:
        print(f'{score:<8}',end='')
    print(f'{stu_dict[name].sum_score:<7}{stu_dict[name].ave:<7.1f}{stu_dict[name].level:<5}{stu_dict[name].rank}')

print('-'*8*(5+len(subjects)))

    #Output subject data
print(f'{'Subj':<10}{'Max':<8}{'Min':<8}{'Avg'}')
print('-'*32)

for sub in subjects:
    print(f'{sub:<10}{max(score_dict[sub]):<8}{min(score_dict[sub]):<8}{sum(score_dict[sub])*1.0/len(names):.1f}')

print('-'*32+'\n')

wait=input('Press "Enter" to exit.')
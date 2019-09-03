#import libraries
import numpy as np
import pandas as pd
import math
#import matplotlib.pyplot as plt

def level_of_attainment(avg_greater,co_title):
    coattainment_list=[]
    for n in avg_greater:
        if n >= 0.7:
            coattainment_list.append(3)
        elif n>=0.6:
            coattainment_list.append(2)
        else:
            coattainment_list.append(1)
    #converting list into dictionary
    coattainment_dict={}
    coattainment_dict['AAT']=coattainment_list[0]
    co=co_title[0]
    dict_key = 'Assignment: ' + co
    coattainment_dict[dict_key]=coattainment_list[1]
    # co=co_title[1]
    # coattainment_dict[co]=coattainment_list[2]
    coattainment_dict['SEE']=coattainment_list[2]
    return coattainment_dict

def calc(aat,a1,see,co_title):
    #calculating lengths
    aat_count=len(aat)
    a1_count=len(a1)
    # a2_count=len(a2)
    see_count=len(see)
    #calculating average
    aat_avg=math.floor(sum(aat)/aat_count)
    a1_avg=math.floor(sum(a1)/a1_count)
    # a2_avg=math.floor(sum(a2)/a2_count)
    
    # removing the nans
    for i in range(0, see_count):
        if isinstance(see[i], int):
            continue
        see[i] = 0
            
  
    print("\n\nSEE:", see, "\n\n")
    see_avg=math.floor(sum(see)/see_count)

    print('see_avg', see_avg)
    #number of students who scored more than average
    aat_n=len(list(filter(lambda n:n >= aat_avg,aat)))
    a1_n=len(list(filter(lambda n:n >= a1_avg,a1)))
    # a2_n=len(list(filter(lambda n:n >= a2_avg,a2)))
    see_n=len(list(filter(lambda n:n >= see_avg,see)))
    print('see_n', see_n, 'see_n/see_count', see_n/see_count)
    #list of percentage of people who got more than average(scale of 0-1)
    avg_greater=[]
    avg_greater.append(aat_n/aat_count)
    avg_greater.append(a1_n/a1_count)
    # avg_greater.append(a2_n/a2_count)
    avg_greater.append(see_n/see_count)
    #finding attainment of co's
    coattainment_dict=level_of_attainment(avg_greater,co_title)
    return coattainment_dict

def Cal2(pathf):
    # Importing the dataset
    dataset = pd.read_excel(pathf, 10)
    # filteredDataset = dataset.iloc[:, 24:29]
    filteredDataset = dataset.iloc[:, 24:28]
    
    #subjectDetails = pd.read_excel('C:\\Users\\tharu\\Desktop\\doc.xls', 1, header=None)
    

    aat = np.array(filteredDataset.iloc[6:, 0].values).tolist()
    assignmentq1 = np.array(filteredDataset.iloc[6:, 1].values).tolist()
    
    see = filteredDataset.iloc[6:, 2]
    # aat = np.array(filteredDataset.iloc[6:, 0].values).tolist()
    # assignmentq1 = np.array(filteredDataset.iloc[6:, 1].values).tolist()
    # assignmentq2 =  np.array(filteredDataset.iloc[6:, 2].values).tolist()
    # see = filteredDataset.iloc[6:, 3]

    #getting all titles of co's
    # co_title=np.array(filteredDataset.iloc[0, 1:3].values).tolist()
    co_title=np.array(filteredDataset.iloc[0, 1:2].values).tolist()



    #grademap
    # grademap={'S+':95,'S':85,'A':75,'B':65,'C':55}

    #converting SEE grades to marks format
    # for index, grade in enumerate(see, start=1):
    #     grade=grade.strip()
    #     see[index]=grademap[grade]
        
    see=see.tolist()
    #aat_n=len(list(filter(lambda n:n >= 8.92,aat)))

    #call to the funtion
    # extradict=calc(aat,assignmentq1,assignmentq2,see,co_title)
    extradict=calc(aat,assignmentq1,see,co_title)

    print(extradict)
    return extradict

'''
Cal2('C:\\Users\\tharu\\Desktop\\doc.xls')
'''
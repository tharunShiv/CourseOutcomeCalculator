import pandas as pd
import numpy as np
def Cal(pathf):
    
        students = pd.read_excel(pathf, 10)
        course_detail = pd.read_excel(pathf, 1, header=None)

        c_d = course_detail
        # print("c_d", c_d[0:])
        # print("\n\nCD:", c_d[0:].iloc[0, 1], "\n\n")
        course_name = c_d[0:].iloc[0, 1]
        stud = students[6:]     # getting only the student marks

        iat1 = stud.iloc[:, 2:8]   # marks of iat1 only
        iat2 = stud.iloc[:, 9:15]  # marks of iat2 only
        iat3 = stud.iloc[:, 16:22]  # marks of iat3 only



        coiat1 = np.reshape(students.iloc[0, 2:8].values, (1, 6))  # the cos of each question for iat 1
        coiat2 = students.iloc[0, 9:15].values.reshape(1, 6)  # the cos of each question for iat 2
        coiat3 = students.iloc[0, 16:22].values.reshape(1, 6)  # the cos of each question for iat 3

        # total of iat1
        coTotalDict1 = dict()
        # count of iat1
        coCountDict1 = dict()
        coTotalDict2 = dict()
        coCountDict2 = dict()
        coTotalDict3 = dict()
        coCountDict3 = dict()

        coStudentMarks = dict()  # the marks of respective cos

        cols = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        z = 0

        # to find the max values
        coMaxValueDict1 = dict()
        coMaxValueDict2 = dict()
        coMaxValueDict3 = dict()

        # to find the min values
        coMinValueDict1 = dict()
        coMinValueDict2 = dict()
        coMinValueDict3 = dict()

        for x in cols:
            if z < 6:
                z += 1
                # print(coiat1[0][(x)] + "\n\n")
                # print(len(stud))
                for y in range(len(stud)):
                    if coiat1[0][x] in coTotalDict1 and str(iat1.iloc[y, x]) != 'nan':
                        # print(coTotalDict1[coiat1[0][x]])
                        coTotalDict1[coiat1[0][x]] += iat1.iloc[y, x]
                        coCountDict1[coiat1[0][x]] += 1
                        coStudentMarks[coiat1[0][x]].append(iat1.iloc[y, x])
                        if coMaxValueDict1[coiat1[0][x]] < iat1.iloc[y, x]:
                            coMaxValueDict1[coiat1[0][x]] = iat1.iloc[y, x]
                        if coMinValueDict1[coiat1[0][x]] > iat1.iloc[y, x]:
                            coMinValueDict1[coiat1[0][x]] = iat1.iloc[y, x]
                    elif str(iat1.iloc[y, x]) != 'nan':
                        coTotalDict1[coiat1[0][x]] = 0
                        coTotalDict1[coiat1[0][x]] += iat1.iloc[y, x]
                        coCountDict1[coiat1[0][x]] = 1
                        coMaxValueDict1[coiat1[0][x]] = iat1.iloc[y, x]
                        coMinValueDict1[coiat1[0][x]] = iat1.iloc[y, x]
                        if coiat1[0][x] not in coStudentMarks:
                            coStudentMarks[coiat1[0][x]] = [iat1.iloc[y, x]]
                        else:
                            coStudentMarks[coiat1[0][x]].append(iat1.iloc[y, x])
            elif z < 13:
                z += 1
                # print(coiat2[0][x] + "\n\n")
                # print(len(stud))
                for y in range(len(stud)):
                    if coiat2[0][x] in coTotalDict2 and str(iat2.iloc[y, x]) != 'nan':
                        # print(coTotalDict2[coiat2[0][x]])
                        coTotalDict2[coiat2[0][x]] += iat2.iloc[y, x]
                        coCountDict2[coiat2[0][x]] += 1
                        coStudentMarks[coiat2[0][x]].append(iat2.iloc[y, x])
                        if coMaxValueDict2[coiat2[0][x]] < iat2.iloc[y, x]:
                            coMaxValueDict2[coiat2[0][x]] = iat2.iloc[y, x]
                        if coMinValueDict2[coiat2[0][x]] > iat2.iloc[y, x]:
                            coMinValueDict2[coiat2[0][x]] = iat2.iloc[y, x]
                    elif str(iat2.iloc[y, x]) != 'nan':
                        coTotalDict2[coiat2[0][x]] = 0
                        coTotalDict2[coiat2[0][x]] += iat2.iloc[y, x]
                        coCountDict2[coiat2[0][x]] = 1
                        coMaxValueDict2[coiat2[0][x]] = iat2.iloc[y, x]
                        coMinValueDict2[coiat2[0][x]] = iat2.iloc[y, x]
                        if coiat2[0][x] not in coStudentMarks:
                            coStudentMarks[coiat2[0][x]] = [iat2.iloc[y, x]]
                        else:
                            coStudentMarks[coiat2[0][x]].append(iat2.iloc[y, x])
            else:
                # print(coiat3[0][x] + "\n\n")
                # print(len(stud))
                for y in range(len(stud)):
                    if coiat3[0][x] in coTotalDict3 and str(iat3.iloc[y, x]) != 'nan':
                        # print(coTotalDict3[coiat3[0][x]])
                        coTotalDict3[coiat3[0][x]] += iat3.iloc[y, x]
                        coCountDict3[coiat3[0][x]] += 1
                        coStudentMarks[coiat3[0][x]].append(iat3.iloc[y, x])
                        if coMaxValueDict3[coiat3[0][x]] < iat3.iloc[y, x]:
                            coMaxValueDict3[coiat3[0][x]] = iat3.iloc[y, x]
                        if coMinValueDict3[coiat3[0][x]] > iat3.iloc[y, x]:
                            coMinValueDict3[coiat3[0][x]] = iat3.iloc[y, x]

                    elif str(iat3.iloc[y, x]) != 'nan':
                        coTotalDict3[coiat3[0][x]] = 0
                        coTotalDict3[coiat3[0][x]] += iat3.iloc[y, x]
                        coCountDict3[coiat3[0][x]] = 1
                        coMaxValueDict3[coiat3[0][x]] = iat3.iloc[y, x]
                        coMinValueDict3[coiat3[0][x]] = iat3.iloc[y, x]
                        if coiat3[0][x] not in coStudentMarks:
                            coStudentMarks[coiat3[0][x]] = [iat3.iloc[y, x]]
                        else:
                            coStudentMarks[coiat3[0][x]].append(iat3.iloc[y, x])

        # print(coTotalDict1)
        # print(coCountDict1)
        # print(coTotalDict2)
        # print(coCountDict2)
        # print(coTotalDict3)
        # print(coCountDict3)

        # finding the final total dictionary
        finalTotalDict = dict()

        for x in coTotalDict1.keys():
            if x in finalTotalDict:
                finalTotalDict[x] += coTotalDict1[x]
            else:
                finalTotalDict[x] = coTotalDict1[x]

        for x in coTotalDict2.keys():
            if x in finalTotalDict:
                finalTotalDict[x] += coTotalDict2[x]
            else:
                finalTotalDict[x] = coTotalDict2[x]

        for x in coTotalDict2.keys():
            if x in finalTotalDict:
                finalTotalDict[x] += coTotalDict3[x]
            else:
                finalTotalDict[x] = coTotalDict3[x]

        # finding the final count dictionary
        finalCountDict = dict()

        for x in coCountDict1.keys():
            if x in finalCountDict:
                finalCountDict[x] += coCountDict1[x]
            else:
                finalCountDict[x] = coCountDict1[x]

        for x in coCountDict2.keys():
            if x in finalCountDict:
                finalCountDict[x] += coCountDict2[x]
            else:
                finalCountDict[x] = coCountDict2[x]

        for x in coCountDict2.keys():
            if x in finalCountDict:
                finalCountDict[x] += coCountDict3[x]
            else:
                finalCountDict[x] = coCountDict3[x]

        # finding the average
        finalAvgDict = dict()

        for x in finalTotalDict:
            finalAvgDict[x] = finalTotalDict[x] / finalCountDict[x]

        # finding the course attainment
        coAttainment = dict()

        import math

        for co in coStudentMarks:
            nStudentCount = 0 #number of student
            print("Avg is", finalAvgDict[co])
            for x in range(len(coStudentMarks[co])):
                if coStudentMarks[co][x] >= math.floor(finalAvgDict[co]):
                    nStudentCount+=1
            print(nStudentCount)

            #finding the percentage of students
            percentage = nStudentCount/math.floor(finalCountDict[co])
            print(co, " percentage = ", percentage, "\n")

            '''
            For eg, if you get 70% as an average mark for that question, find the count of students who scored 70% marks and above.

            If 80% or more students have scored 70% of marks for that particular question or here CO1 for eg, then we attain level 3.

            If 70% or more students have scored 70% of marks for that particular question or here CO1 for eg, then we attain level 2.

            If 60% or more students have scored 70% of marks for that particular question or here CO1 for eg, then we attain level 1
            '''

            if percentage >= 0.80:
                coAttainment[co] = 3
            elif percentage >= 0.70:
                coAttainment[co] = 2
            else:
                coAttainment[co] = 1

        # finding the maximum marks of that CO
        finalMaxValueDict = dict()
        for x in coMaxValueDict1.keys():
            if x in finalMaxValueDict:
                if finalMaxValueDict[x] < coMaxValueDict1[x]:
                    finalMaxValueDict[x] = coMaxValueDict1[x]
            else:
                finalMaxValueDict[x] = coMaxValueDict1[x]

        for x in coMaxValueDict2.keys():
            if x in finalMaxValueDict:
                if finalMaxValueDict[x] < coMaxValueDict2[x]:
                    finalMaxValueDict[x] = coMaxValueDict2[x]
            else:
                finalMaxValueDict[x] = coMaxValueDict2[x]

        for x in coMaxValueDict3.keys():
            if x in finalMaxValueDict:
                if finalMaxValueDict[x] < coMaxValueDict3[x]:
                    finalMaxValueDict[x] = coMaxValueDict3[x]
            else:
                finalMaxValueDict[x] = coMaxValueDict3[x]

        # finding the minimum marks of that CO
        finalMinValueDict = dict()
        for x in coMinValueDict1.keys():
            if x in finalMinValueDict:
                if finalMinValueDict[x] < coMinValueDict1[x]:
                    finalMinValueDict[x] = coMinValueDict1[x]
            else:
                finalMinValueDict[x] = coMinValueDict1[x]

        for x in coMinValueDict2.keys():
            if x in finalMinValueDict:
                if finalMinValueDict[x] < coMinValueDict2[x]:
                    finalMinValueDict[x] = coMinValueDict2[x]
            else:
                finalMinValueDict[x] = coMinValueDict2[x]

        for x in coMinValueDict3.keys():
            if x in finalMinValueDict:
                if finalMinValueDict[x] < coMinValueDict3[x]:
                    finalMinValueDict[x] = coMinValueDict3[x]
            else:
                finalMinValueDict[x] = coMinValueDict3[x]

        # finding the number of students with max marks
        cols = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        z = 0

        coNumberOfMaxDict1 = dict()
        coNumberOfMaxDict2 = dict()
        coNumberOfMaxDict3 = dict()

        for x in cols:
            if z < 6:
                z += 1
                for y in range(len(stud)):
                    if coiat1[0][x] in coNumberOfMaxDict1 and str(iat1.iloc[y, x]) != 'nan':
                        if iat1.iloc[y, x] == finalMaxValueDict[coiat1[0][x]]:
                            coNumberOfMaxDict1[coiat1[0][x]] += 1
                    elif str(iat1.iloc[y, x]) != 'nan':
                        if iat1.iloc[y, x] == finalMaxValueDict[coiat1[0][x]]:
                            coNumberOfMaxDict1[coiat1[0][x]] = 1
            elif z < 13:
                z += 1
                for y in range(len(stud)):
                    if coiat2[0][x] in coNumberOfMaxDict2 and str(iat2.iloc[y, x]) != 'nan':
                        if iat2.iloc[y, x] == finalMaxValueDict[coiat2[0][x]]:
                            coNumberOfMaxDict2[coiat2[0][x]] += 1
                    elif str(iat2.iloc[y, x]) != 'nan':
                        if iat2.iloc[y, x] == finalMaxValueDict[coiat2[0][x]]:
                            coNumberOfMaxDict2[coiat2[0][x]] = 1
            else:
                z += 1
                for y in range(len(stud)):
                    if coiat3[0][x] in coNumberOfMaxDict3 and str(iat3.iloc[y, x]) != 'nan':
                        if iat3.iloc[y, x] == finalMaxValueDict[coiat3[0][x]]:
                            coNumberOfMaxDict3[coiat3[0][x]] += 1
                    elif str(iat3.iloc[y, x]) != 'nan':
                        if iat3.iloc[y, x] == finalMaxValueDict[coiat3[0][x]]:
                            coNumberOfMaxDict3[coiat3[0][x]] = 1

        # final the final number of max students
        finalNumberOfMaxDict = dict()
        for x in coNumberOfMaxDict1.keys():
            if x in finalNumberOfMaxDict:
                finalNumberOfMaxDict[x] += coNumberOfMaxDict1[x]
            else:
                finalNumberOfMaxDict[x] = coNumberOfMaxDict1[x]

        for x in coNumberOfMaxDict2.keys():
            if x in finalNumberOfMaxDict:
                finalNumberOfMaxDict[x] += coNumberOfMaxDict2[x]
            else:
                finalNumberOfMaxDict[x] = coNumberOfMaxDict2[x]


        for x in coNumberOfMaxDict3.keys():
            if x in finalNumberOfMaxDict:
                finalNumberOfMaxDict[x] += coNumberOfMaxDict3[x]
            else:
                finalNumberOfMaxDict[x] = coNumberOfMaxDict3[x]


        # finding the number of students with min marks
        cols = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        z = 0

        coNumberOfMinDict1 = dict()
        coNumberOfMinDict2 = dict()
        coNumberOfMinDict3 = dict()

        for x in cols:
            if z < 6:
                z += 1
                for y in range(len(stud)):
                    if coiat1[0][x] in coNumberOfMinDict1 and str(iat1.iloc[y, x]) != 'nan':
                        if iat1.iloc[y, x] == finalMinValueDict[coiat1[0][x]]:
                            coNumberOfMinDict1[coiat1[0][x]] += 1
                    elif str(iat1.iloc[y, x]) != 'nan':
                        if iat1.iloc[y, x] == finalMinValueDict[coiat1[0][x]]:
                            coNumberOfMinDict1[coiat1[0][x]] = 1
            elif z < 13:
                z += 1
                for y in range(len(stud)):
                    if coiat2[0][x] in coNumberOfMinDict2 and str(iat2.iloc[y, x]) != 'nan':
                        if iat2.iloc[y, x] == finalMinValueDict[coiat2[0][x]]:
                            coNumberOfMinDict2[coiat2[0][x]] += 1
                    elif str(iat2.iloc[y, x]) != 'nan':
                        if iat2.iloc[y, x] == finalMinValueDict[coiat2[0][x]]:
                            coNumberOfMinDict2[coiat2[0][x]] = 1
            else:
                z += 1
                for y in range(len(stud)):
                    if coiat3[0][x] in coNumberOfMinDict3 and str(iat3.iloc[y, x]) != 'nan':
                        if iat3.iloc[y, x] == finalMinValueDict[coiat3[0][x]]:
                            coNumberOfMinDict3[coiat3[0][x]] += 1
                    elif str(iat3.iloc[y, x]) != 'nan':
                        if iat3.iloc[y, x] == finalMinValueDict[coiat3[0][x]]:
                            coNumberOfMinDict3[coiat3[0][x]] = 1

        # final the final number of min students
        finalNumberOfMinDict = dict()
        for x in coNumberOfMinDict1.keys():
            if x in finalNumberOfMinDict:
                finalNumberOfMinDict[x] += coNumberOfMinDict1[x]
            else:
                finalNumberOfMinDict[x] = coNumberOfMinDict1[x]

        for x in coNumberOfMinDict2.keys():
            if x in finalNumberOfMinDict:
                finalNumberOfMinDict[x] += coNumberOfMinDict2[x]
            else:
                finalNumberOfMinDict[x] = coNumberOfMinDict2[x]


        for x in coNumberOfMinDict3.keys():
            if x in finalNumberOfMinDict:
                finalNumberOfMinDict[x] += coNumberOfMinDict3[x]
            else:
                finalNumberOfMinDict[x] = coNumberOfMinDict3[x]


        '''The result dict will have the final return dictionary to the frontend'''

        resultDict = dict(coAttainment)
        resultDict = dict()
        resultDict['attainment'] = dict(coAttainment)

        resultDict['finalTotalCount'] = dict(finalCountDict)

        resultDict['finalMaxValueDict'] = dict(finalMaxValueDict)

        resultDict['finalNumberOfMaxDict'] = dict(finalNumberOfMaxDict)

        resultDict['finalMinValueDict'] = dict(finalMinValueDict)

        resultDict['finalNumberOfMinDict'] = dict(finalNumberOfMinDict)


        # plotting the result
        import matplotlib.pyplot as plt
        imagedictionary = dict()
        for x in finalCountDict.keys():
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = ['N students with Max', 'N students with Min', 'N students with average']
            sizes = [finalNumberOfMaxDict[x], finalNumberOfMinDict[x], finalCountDict[x] - finalNumberOfMaxDict[x] - finalNumberOfMinDict['CO1']]
            explode = (0, 0.3, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            wedges, texts, autotexts = ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.set_title(x + " Pie Chart")
            ax1.legend(wedges, labels,
                  title="Labels",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
            plt.savefig("static/"+x+".png", bbox_inches='tight')
            imagedictionary[x] = x+".png"
            #plt.show()
        resultDict['imagedictionary'] = dict(imagedictionary)
        resultDict['courseName'] = course_name
        return resultDict

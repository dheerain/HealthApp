import pickle
from config import disease_config


userData=[]


# def createPdf(data):
#     pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
#     pdf.add_page()
#     pdf.set_font("Arial", 'B' ,15) 
#     # pdf.set_text_color(255, 255, 255)
#     pdf.set_line_width(0.0)
#     pdf.line(5.0,5.0,205.0,5.0) # top one
#     pdf.line(5.0,292.0,205.0,292.0) # bottom one
#     pdf.line(5.0,5.0,5.0,292.0) # left one
#     pdf.line(205.0,5.0,205.0,292.0) # right one
#     pdf.cell(200, 10, txt = f"Name: {data['name']}", ln = 1, align = 'C') 
#     pdf.set_font("Arial", 'B' ,11) 
#     pdf.cell(200, 10, txt = f"Age: {data['age']}", ln = 1, align = 'C') 
#     pdf.cell(200, 10, txt = f"Sex: {data['gender']}", ln = 1, align = 'C') 
#     pdf.cell(200, 10, txt = f"Weight: {data['weight']}", ln = 1, align = 'C') 
#     pdf.cell(200, 10, txt = f"Date: {data['date']}", ln = 1, align = 'C') 
    
#     medicalCond =[]
#     for i in disease_config.keys():
#         if data.get(i):
#             medicalCond.append(i)
#     if medicalCond:
#         pdf.cell(200, 10, txt = f"Any Medical Condition: {'/'.join(medicalCond)}", ln = 1, align = 'C') 
#     pdf.set_font('arial', 'B', 9)
#     pdf.cell(0, 0, '', 0, 2, 'C',fill=1)

#     columnNameList = ['ItemName', 'Quantity', 'Protien', 'Fiber', 'Fat','Carbs']
#     # # for header in columnNameList:
    
#     # pdf.cell(0, 0, 'ItemName', 1, 0, 'C',fill=1)
#     # pdf.cell(0, 0, 'Quantity', 1, 0, 'C')
#     # pdf.cell(0, 0, 'Protien', 1, 0, 'C')
#     # pdf.cell(0, 0, 'Fiber', 1, 0, 'C')
#     # pdf.cell(0, 0, 'Fat', 1, 0, 'C')
#     # pdf.cell(0, 0, 'Carbs', 1, 0, 'C')
#     # # pdf.cell(200, 10, 'Carbs', 1, 0, 'C')



#     pdf.cell(-140)
#     # pdf.set_font('arial', '', 11)
#     # for row in range(0, len(iris_grouped_df)):
#     #     for col_num, col_name in enumerate(columnNameList):
#     #         if col_num != len(columnNameList)-1:
#     #             pdf.cell(35,10, str(iris_grouped_df['%s' % (col_name)].iloc[row]), 1, 0, 'C')
#     #         else:
#     #             pdf.cell(35,10, str(iris_grouped_df['%s' % (col_name)].iloc[row]), 1, 2, 'C')  
#     #             pdf.cell(-140)
#     # pdf.output('iris_grouped_df_0.pdf', 'F')    
    
    

    

#     pdf.output(data['name']+'_diet_plan.pdf')

#     return data['name']+'_diet_plan.pdf'

def storeData():
    # initializing data to be stored in db  
    # Its important to use binary mode
    userDataDBfile = open('userData.db', 'wb')  
    # source, destination
    global userData
    pickle.dump(userData, userDataDBfile)                     
    userDataDBfile.close()
    loadData()
  
def loadData():
    # for reading also binary mode is important
    global userData
    dbfile = open('userData.db', 'rb')     
    userData = pickle.load(dbfile)
    dbfile.close()
    return userData


def saveNewUser(data,update=False,index=0):
    data_dict= {'name':data['name'][0],
                'weight':data['weight'][0],
                'gender':data['gender'][0],
                'age':data['age'][0],
                'date':data['date'][0],
                }
    # for disease in disease_config.keys():
    #     data_dict.update({disease:True if data.get(disease) else False})
    diseases = [ disease for disease in disease_config.keys() if data.get(disease)]
    data_dict.update({'disease':diseases})



    dietList =[]
    for idx, item in enumerate(data['item']):
        dietList.append([data['item'][idx],int(data['quantity'][idx]),data['time'][idx]])

    # print(dietList)
    global userData
    data_dict.update({'diet':dietList})
    userData = loadData()
    if not update:
        userData.append(data_dict)
    else:
        if isinstance(userData[index]['weight'],list):
            weightList = userData[index]['weight']
            weightList.append(data_dict['weight'])
            data_dict['weight']= weightList
        else:
            weightList=[userData[index]['weight']]
            data_dict['weight']= weightList
            
        userData[index]= data_dict
    print(data_dict['weight'])
    storeData()
    # pdfpath = createPdf(data_dict)
    return data_dict
    

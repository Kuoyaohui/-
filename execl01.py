import xlwt  
import xlrd  
try:  
    
    filename=xlwt.Workbook()  #新增excel
    sheet=filename.add_sheet("test")  #命名excel
    hello='123'
    sheet.write(3,2,hello) #第四行第三列填入123  
    filename.save("D:/test1.xls") #絕對路徑
except Exception,e:  
    print(str(e))
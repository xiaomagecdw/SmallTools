# coding:utf-8
'''
Created on 2017年9月23日

@author: chendaiwu
'''
import xlwt

def writeExcel(sheetname, r , c, d, name):

    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('sheetname', cell_overwrite_ok=True)
    sheet1.write(r, c, d)

    workbook.save("name.xls")
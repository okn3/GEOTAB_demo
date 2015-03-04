# -*- coding: utf-8 -*-
#-------------------------
#
# excelからデータ呼び出し
#
#-------------------------

import xlrd
import time

# 読み込みファイルの指定
book = xlrd.open_workbook('logs/0304aquia.xlsm')

# シートの指定(summary)
sheet_1 = book.sheet_by_index(1)

# セルデータの登録
log_date = 2
log_time = 3
log_record_type = 4
log_speed = 5
log_longitude = 6
log_latitude = 7
log_location = 8
log_reason = 9
log_ignition = 10
log_engin_diagnostic = 11
log_engin_status = 14

if __name__ == "__main__":

    print "電力残量"
    # データタイプから絞り込み
    for row in range(sheet_1.nrows):
        if sheet_1.cell(row,log_engin_diagnostic).value == "Charge state":
            #print "time: ", float(sheet_1.cell(row,log_time).value)
            energy = int(sheet_1.cell(row,log_engin_status).value[:1])
            print "[",
            for var in range(energy):
                print "■",
            for other in range(10-energy):
                print " ",
            print "]",
            print sheet_1.cell(row,log_engin_status).value

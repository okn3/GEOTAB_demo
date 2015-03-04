# -*- coding: utf-8 -*-
#-------------------------
#
# excelからデータ呼び出し
# 燃費データの算出
#
#-------------------------

import xlrd

# 読み込みファイルの指定
book = xlrd.open_workbook('../logs/0227note.xlsx')

# シートの指定(summary)
sheet_1 = book.sheet_by_index(0)

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

    print "今回の走行"
# データタイプから絞り込み
    for row in range(sheet_1.nrows):
        if sheet_1.cell(row,log_engin_diagnostic).value == "Trip fuel used":
            fuel_used = sheet_1.cell(row,log_engin_status).value
            print "[消費燃料]:", fuel_used
        if sheet_1.cell(row,log_engin_diagnostic).value == "Trip idle fuel used":
            fuel_idle = sheet_1.cell(row,log_engin_status).value
            print "[アイドリングで消費]:", fuel_idle
            
            dlt = float(fuel_used[:-1]) - float(fuel_idle[:-1])
            print "[燃費効率]:",int(dlt/float(fuel_used[:-1])*100),"%"

# -*- coding: utf-8 -*-
#-------------------------
#
# excelからデータ呼び出し
# 燃費データの算出
#
#-------------------------

import xlrd
import time
import json
import time

# 読み込みファイルの指定
book = xlrd.open_workbook('../logs/0223BMW116i.xlsx')

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

line = "====================="

if __name__ == "__main__":

    stop_point = []
    print "今回の走行"
    # 止まっている状態のGPS情報を取得
    for row in range(sheet_1.nrows):
        if sheet_1.cell(row,log_speed).value < 10 and sheet_1.cell(row,log_record_type).value == "GpsRecord":
            point_get = {"lat":sheet_1.cell(row,log_latitude).value,"lng":sheet_1.cell(row,log_longitude).value}
            json_point = {
                    "no":row,
                    "speed":sheet_1.cell(row,log_speed).value,
                    "point":point_get,
                   }
            stop_point.append(json_point)
    f = open("log_data.json", "w")            
    print stop_point
    f.write(str(json.dumps(stop_point)))
    
    f.close()

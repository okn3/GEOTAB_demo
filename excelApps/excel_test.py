# -*- coding: utf-8 -*-
#-------------------------
#
# excelからデータ呼び出し
#
# -record typeがGpsRecordのログデータを全部抜き出す-
#
#-------------------------

import xlrd

# 読み込みファイルの指定
book = xlrd.open_workbook('../logs/geotab_log.xlsm')

# シートの指定(summary)
sheet_1 = book.sheet_by_index(2)

# ファイルの行列数表示(デバッグ用)
print sheet_1.ncols
print sheet_1.nrows

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
log_engin_status = 13


#行の表示
def showRow():
    
    # 列の全データ表示
    for col in range(sheet_1.ncols):
        print sheet_1.cell(row,col).value,
    
    # データを選択して表示
    #print sheet_1.cell(row,log_time)
    #print sheet_1.cell(row,log_location)


if __name__ == "__main__":
            
    # データタイプから絞り込み
    for row in range(sheet_1.nrows):
        if sheet_1.cell(row,log_record_type).value == "GpsRecord":
            print "[",row,"]:", sheet_1.cell(row,log_record_type).value
            showRow()
            print "\n"

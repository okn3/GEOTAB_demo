# GEOTAB


## /stopMap

excelデータからjsonでデータ書き出し
jsonをgooglemapで表示

車のスピードが遅くなるポイントの特定

#### 使用方法

`python stop_point.py`

`open index.html -a Firefox`

* firefox 限定

### api_test.py

GEOTABのAPIをpythonからたたく

* apiの挙動がおかしい

## /excelApps

excelファイルを使った簡単なアプリケーション

### excel_test.py

excelデータを抜き取って表示

statusがGpsRecordの行のデータを全て表示

### ilde_status.py

（未完成）アイドリングの状態を分析→（本来は信号の位置の特定使う予定でした）

### fuel_efficiency.py

使用燃料とアイドリング燃料から効率を計算

### battery_log.py

電気自動車のバッテリー残量を可視化

## logs/

myGEOTABからexcelデータをdownloadし車種別にデータを分割した

******

開発はpython2.7.6でやっております

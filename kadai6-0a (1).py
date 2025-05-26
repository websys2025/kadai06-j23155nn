import requests
import json

# アプリケーションID（自分のIDを記入）
APP_ID = "44685c506506b692cfb96ef6c5be07722529504d"

# API エンドポイント
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# リクエストパラメータ
params = {
    "appId": APP_ID,
    "lang": "J",                      # 日本語
    "statsDataId": "0003349247",     # 若者の生活に関する調査 本人票 Q1
    "metaGetFlg": "Y",               # メタ情報を取得
    "cntGetFlg": "N",                # 件数不要
    "explanationGetFlg": "Y",        # 説明を取得
    "annotationGetFlg": "Y",         # 注釈を取得
    "sectionHeaderFlg": "1",
    "replaceSpChars": "0"
}
#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)
# kadai6-1.py
# e-Stat APIを使用して「若者の生活に関する調査（本人票）」の性別に関するデータを取得する
# statsDataId: 0003349247
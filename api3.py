import requests
import urllib
import pandas as pd


def get_api(url, param):
    result = requests.get(url, params=param)
    return result.json()


def main():
    gen_input = input("ジャンルIDを入力>>")
    APP_ID = 1019079537947262807
    list = []
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    param = {
        "format":"json",
        "genreId":gen_input,
        "applicationId":[APP_ID]
    }
    result = get_api(url, param)
    for i in result['Items']:
        item = i['Item']
        ranking = item['rank']
        itemName = item['itemName']
        print(f"{ranking}位")
        print(f"商品名:{itemName}")
        list.append(f"{ranking}位")
        list.append(itemName)
    df = pd.DataFrame(list, columns=["順位"])
    df.to_csv("data.csv", encoding='utf_8_sig', index=False)


main()
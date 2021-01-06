import requests
import urllib


def get_api(url, param):
    result = requests.get(url, params=param)
    return result.json()


def main():
    keyword = input("キーワードを入力してください>>")
    APP_ID = 1019079537947262807
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
    param = {
        "format":"json",
        "keyword":keyword,
        "applicationId":[APP_ID]
    }
    result = get_api(url, param)
    for i in result['Products']:
        item = i['Product']
        name = item['productName']
        print(name)
        num = item['itemCount']
        print(f"{num}個")
        max_price = item['maxPrice']
        min_price = item['minPrice']
        print(f"最高価格:{max_price}円")
        print(f"最低価格:{min_price}円")




main()
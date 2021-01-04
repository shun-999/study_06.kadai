import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = input("キーワードを入力してください>>")
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    result = get_api(url)
    for i in result['Products']:
        item = i['Product']
        name = item['productName']
        print(name)
        num = item['itemCount']
        print(f"{num}個")
        max_price = item['minPrice']
        print(f"最高価格:{max_price}円")
        min_price = item['minPrice']
        print(f"最低価格:{min_price}円")




main()

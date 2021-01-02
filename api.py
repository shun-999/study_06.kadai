import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = input("キーワードを入力してください>>")
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    result = get_api(url)
    for i in result['Items']:
        item = i['Item']
        name = item['itemName']
        price = item['itemPrice']
        print(name)
        print(price, '円')


main()

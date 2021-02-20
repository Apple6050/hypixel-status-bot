apikey = "hypixel api key"
uuid = "your uuid"
url = 'https://api.hypixel.net/status?key=' + apikey + '&uuid=' + uuid
import urllib.request
import asyncio

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()

async def main():
    if (rescode == 200):
        print("request success")
        response_body = response.read()
        with open('result.json', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)


asyncio.get_event_loop().run_until_complete(main())
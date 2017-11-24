import requests

url = "http://schedule.iitu.kz/rest/user/get_timetable_block.php"

for i in range(13765, 14246):
    querystring = {"block_id": str(i)}
    response = requests.request("GET", url, params = querystring)
    e = response.text.encode('utf-8')
    with open(f"data/{i}.json", "ab") as f:
        f.write(e)




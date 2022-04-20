import os,requests,json,time,sys,random,threading



class Discord():
    
    
    
    
    def createthread(token,name,channelid):
        payload = json.dumps({
        "name": name,
        "type": 11,
        "auto_archive_duration": 60,
        "location": "Thread Browser Toolbar"
        })
        headers = {
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.42 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*'
        }
        url = f"https://canary.discord.com/api/v9/channels/{channelid}/threads"
        while True:
            x = requests.post(url,headers=headers,data=payload)
            print(x.text)
            if x.status_code == 201:
                print("Thread Created Successfully :) By H4xton & Yaboi")
            if x.text == "The resource is being rate limited.":                
                bypasslimit = x.json()['retry_after']
                time.sleep(bypasslimit)
                print("Bypassed rate-limit, retrying...")

                
                
if __name__ == "__main__":
    token = input("Enter your token: ")
    ThreadName = input("Enter your thread name: ")
    channelid = input("Enter your channel id: ")
    i = input("How Many threads skid (RUNTIME) : ")
    t = []

    for i in range(int(i) + 1):
        thread = threading.Thread(target=Discord.createthread(token,ThreadName,channelid), daemon=True)
        t.append(thread)
        thread.start()
        for thread in t:
            thread.join()

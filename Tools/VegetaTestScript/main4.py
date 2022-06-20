import os
import time
import json


def saveToFile(fileName, data):
    data = data.split('\n')

    with open(fileName, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    print(os.popen("echo \"GET http://0.0.0.0:80/stream/100\" | vegeta attack -duration=5m -rate=0 -max-workers=32 | vegeta encode > vegeta4.json").read())
    saveToFile("vegeta4.json", os.popen("cat vegeta4.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)
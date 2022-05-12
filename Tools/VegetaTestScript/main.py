import os
import time
import json


def saveToFile(fileName, data):
    data = data.split('\n')

    with open(fileName, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    print(os.popen("echo \"GET http://0.0.0.0:80/get\" | vegeta attack -duration=5m -rate=0 -max-workers=32 | vegeta encode > vegeta1.json").read())
    saveToFile("vegeta1.json", os.popen("cat vegeta1.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/get\" | vegeta attack -duration=5m -rate=0 -max-workers=250 | vegeta encode > vegeta2.json").read())
    saveToFile("vegeta2.json", os.popen("cat vegeta2.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/get\" | vegeta attack -duration=5m -rate=0 -max-workers=500 | vegeta encode > vegeta3.json").read())
    saveToFile("vegeta3.json", os.popen("cat vegeta3.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/stream/100\" | vegeta attack -duration=5m -rate=0 -max-workers=32 | vegeta encode > vegeta4.json").read())
    saveToFile("vegeta4.json", os.popen("cat vegeta4.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/stream/100\" | vegeta attack -duration=5m -rate=0 -max-workers=250 | vegeta encode > vegeta5.json").read())
    saveToFile("vegeta5.json", os.popen("cat vegeta5.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/stream/100\" | vegeta attack -duration=5m -rate=0 -max-workers=500 | vegeta encode > vegeta6.json").read())
    saveToFile("vegeta6.json", os.popen("cat vegeta6.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/drip?numbytes=5000&status=200&duration=0&delay=0\" | vegeta attack -duration=5m -rate=0 -max-workers=32 | vegeta encode > vegeta7.json").read())
    saveToFile("vegeta7.json", os.popen("cat vegeta7.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/drip?numbytes=5000&status=200&duration=0&delay=0\" | vegeta attack -duration=5m -rate=0 -max-workers=250 | vegeta encode > vegeta8.json").read())
    saveToFile("vegeta8.json", os.popen("cat vegeta8.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

    print(os.popen("echo \"GET http://0.0.0.0:80/drip?numbytes=5000&status=200&duration=0&delay=0\" | vegeta attack -duration=5m -rate=0 -max-workers=500 | vegeta encode > vegeta9.json").read())
    saveToFile("vegeta9.json", os.popen("cat vegeta9.json | jq -c 'delpaths([[\"attack\"], [\"body\"],[\"seq\"],[\"timestamp\"],[\"bytes_out\"],[\"bytes_in\"],[\"error\"],[\"method\"],[\"url\"],[\"headers\"]])'").read())
    time.sleep(60)

import vt
import time

def main():
    # Enter your own API key as parameter
    client = vt.client.Client("51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca")

    analysis = client.scan_url('https://www.google.com/')
    
    while True:
        analysis = client.get_object("/analyses/{}", analysis.id)
        print(analysis.status)
        if analysis.status == "completed":
            break
        time.sleep(30)


if __name__ == '__main__':
    main()
import vt

def main():
    client = vt.client.Client("51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca")

    url_id = vt.url_id("https://www.google.com")
    url = client.get_object('/urls/{}', url_id)

    print(url.times_submitted)
    print(url.last_analysis_stats)

if __name__ == "__main__":
    main()
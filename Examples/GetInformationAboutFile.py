import vt

def main():
    # Enter your own API key as parameter
    client = vt.client.Client("51bd951cd29384782a40f883531b182a06adb725331ea8c38b7b1f00e45826ca")

    # Ask for the file you are interested in, you can replace the hash in the example with some other SHA-256, SHA-1 or MD5
    file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")

    print(file.size)
    print(file.sha256)
    print(file.type_tag)


if __name__ == '__main__':
    main()
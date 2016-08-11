import requests
import time


class GetYZM:

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

    def __init__(self):
        pass

    @staticmethod
    def get_image():
        for i in range(500):
            t = str(int(time.time() * 1000))
            captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
            r = requests.get(captcha_url, headers=GetYZM.header)
            with open('image/4'+str(i)+'.jpg', 'wb') as f:
                f.write(r.content)
                f.close()
            time.sleep(1)


if __name__ == u"__main__":
        GetYZM.get_image()

import pytest
import requests
import base64

from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil


#fixture
#@pytest.fixture(scope="function",autouse=False,params=["wuhan","changsha","chongqing"])
#def execute_sql(request):
#    print("sql connect")
#    yield request.param
#    print("sql close")


class TestApi:

    #class var
    access_token = "WWgtONSlNTY55"
    sess = requests.session()

    def setup(self):
        print("setup")

    def teardown(self):
        print("tear down")

    def test_token(self):
        dic = {"access_token":"WWgtONSlNTY55"}
        YamlUtil().write_yaml(dic)

    def test_yiyan(self):
        url="http://api.txapi.cn/v1/hitokoto"
        params = {
            #"token":TestApi.access_token
            "token":YamlUtil().read_yaml("access_token")
        }
        #res = requests.get(url=url,params=params)
        #res = TestApi.sess.request(method="get", url=url, params=params)
        res = RequestUtil().all_send_request(method="get", url=url, params=params)
        print(res.json())

    def test_weather(self,execute_sql):
        print("execute_sql %s" % execute_sql)
        url = "http://api.txapi.cn/v1/weather"
        data = {
            #"token":TestApi.access_token
            "token":YamlUtil().read_yaml("access_token"),
            "city":"Wuhan"
        }
        #res = requests.post(url=url, data=data)
        #res = TestApi.sess.request(method="post",url=url, data=data)
        res = RequestUtil().all_send_request(method="post",url=url, data=data)
        print(res.json()["code"])
        #raise Exception("error")

    def img64(self):
        file = open("E:/TestApi/img_data.png","rb")
        image_data = file.read()
        base64_data = base64.b64encode(image_data)
        return base64_data

    @pytest.mark.smoke
    def test_imageVerifyCode(self):
        url = "http://api.txapi.cn/v1/aim/ocr/img_code"
        files = {
            #"token":TestApi.access_token
            "token":YamlUtil().read_yaml("access_token"),
            "img_data": TestApi.img64(self)
        }
        #res = requests.post(url=url, data=files)
        #res = TestApi.sess.request(method="post", url=url, data=files)
        res = RequestUtil().all_send_request(method="post", url=url, data=files)
        print(res.json())
import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import YamlUtil


class TestWeather:
    @pytest.mark.parametrize("caseinfo",YamlUtil().read_testcase_yaml("/TestCase/get_city.yaml"))
    def test_weather(self,caseinfo):
        #print(caseinfo)
        url = caseinfo["request"]["url"]
        method = caseinfo["request"]["method"]
        params = caseinfo["request"]["params"]
        #data = {
        #    "token":YamlUtil().read_yaml("access_token"),
        #    "city":"Wuhan"
        #}
        res = RequestUtil().all_send_request(method="post",url=url, data=params)
        print(res.json()["code"])
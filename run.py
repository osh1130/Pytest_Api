import os
import time

from TestCase.test_api import TestApi
import pytest

from TestCase.test_weather import TestWeather
from commons.yaml_util import YamlUtil

#if __name__=='__main__':
#    TestApi().test_yiyan()
#    TestApi().test_weather()
#    TestApi().test_imageVerifyCode()

if __name__=='__main__':
    pytest.main()
#    TestApi().test_token()
#    print(YamlUtil().read_yaml("access_token"))
#    TestWeather().test_weather()
    time.sleep(5)
    os.system("allure generate ./temps -o ./reports --clean")
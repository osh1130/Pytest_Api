import pytest

from commons.yaml_util import YamlUtil


@pytest.fixture(scope="session",autouse=True)
    #function
def execute_sql():
    #print("sql connect")
    #before session
    #yield
    #print("sql close")
    #after all session have done
    YamlUtil().clean_yaml()
    #always keep the lasted cookies
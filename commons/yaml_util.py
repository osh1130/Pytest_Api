import os
import yaml


class YamlUtil:

    #read yaml file
    def  read_yaml(self,key):
        #os.getcwd()
        with open(os.getcwd()+'/extract.yaml' , encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

    #write data
    def write_yaml(self,data):
        with open(os.getcwd()+'/extract.yaml' , encoding="utf-8",mode="a") as f:
            yaml.dump(data, stream=f,allow_unicode=True)

    def clean_yaml(self):
        with open(os.getcwd()+'/extract.yaml' , encoding="utf-8",mode="w") as f:
            f.truncate()

    def read_testcase_yaml(self, yaml_path):
        with open(os.getcwd()+yaml_path , encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

#if __name__=='__main__':
#    YamlUtil().read_yaml()
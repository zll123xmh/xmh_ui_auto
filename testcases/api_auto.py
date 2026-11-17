# import json
# from pickle import GET
#
# import requests
# from requests import post
#
#
# class SendMethod:
#     def send_method(self,url=None,method=None,params=None,data=None):
#         if method == "GET":
#             response = requests.get(url=url,params=params)
#         elif method == "POST":
#             response = requests.post(url=url,data=data)
#         else:
#             response = None
#
#         result = {}
#         if response != None:
#             result['status_code'] = response.status_code
#             result['body'] = response.text
#             return result
#         else:
#             return None
#
# if __name__ == '__main__':
#     url = "https://www.baidu.com"
#     method = "POST"
#     data = {
#
#     }
#
# result = SendMethod().send_method(url=url,method=method)
# #new_result = json.dumps(result,ensure_ascii=False,indent=4)
# print(result)


# -*- coding: utf-8 -*-
import requests
import allure

# 基础地址，你的flask服务
BASE_URL = "http://127.0.0.1:5000"

# 全局变量，存登录之后拿到的token，后面其他接口用
token = ""

@allure.feature("用户认证模块")
@allure.story("登录接口")
@allure.title("正常账号密码登录，获取JWT Token")
def test_login_success():
    url = f"{BASE_URL}/api/auth/login"
    # 请求体，换成你项目真实账号密码
    req_data = {
        "username": "admin",
        "password": "123456"
    }
    resp = requests.post(url, json=req_data)

    # 断言：响应状态码200代表成功
    assert resp.status_code == 200
    resp_json = resp.json()
    # 断言返回体包含access_token
    assert "access_token" in resp_json

    # 把token存到全局变量，给后面接口用
    global token
    token = resp_json["access_token"]
    print("✅ 登录成功，token=", token)


@allure.feature("用户认证模块")
@allure.story("登录接口")
@allure.title("错误密码登录，登录失败")
def test_login_wrong_password():
    url = f"{BASE_URL}/api/auth/login"
    req_data = {
        "username": "admin",
        "password": "wrongpwd"
    }
    resp = requests.post(url, json=req_data)
    # 状态码不是200，代表登录失败
    assert resp.status_code != 200


@allure.feature("接口信息管理模块")
@allure.story("查询接口列表")
@allure.title("携带token，查询接口列表成功")
def test_get_api_list():
    # 先判断token是否拿到，必须先执行登录用例
    assert token != "", "请先执行登录用例获取token"
    url = f"{BASE_URL}/api/info/list"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    print("✅ 查询接口列表成功：", resp.json())
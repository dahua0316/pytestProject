# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pytest
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # json_data = {
    #     "password": "dahua",
    #     "username": "123456"
    # }
    # header = {
    #     "Content-Type": "application/json"
    # }
    # result = requests.post("http://192.168.50.30:8086/api/user/login", json=json_data, headers=header)
    # print(result.json())
    pytest.main()



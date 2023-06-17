import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Room(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Room, self).__init__(api_root_url, **kwargs)

    def get_room_list(self, **kwargs):
        return self.get("/cloud/room/page", **kwargs)

    def create_room(self, **kwargs):
        return self.post("/cloud/room/save", **kwargs)

    def get_room_detail(self, **kwargs):
        return self.get("/cloud/room/get", **kwargs)


room = Room(api_root_url)

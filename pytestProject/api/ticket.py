import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Ticket(RestClient):

    def __int__(self, api_root, **kwargs):
        super(Ticket, self).__int__(api_root_url, **kwargs)

    def get_ticket_list(self, **kwargs):
        return self.get("/ticket/page", **kwargs)

    def genarate_ticket(self, **kwargs):
        return self.post("/ticket/genarate", **kwargs)

    def set_aside_ticket(self, ticketId, **kwargs):
        return self.put("/ticket/banned/{}".format(ticketId), **kwargs)


ticket = Ticket(api_root_url)

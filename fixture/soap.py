from suds.client import Client
from suds import WebFault
from model.projects import Project
import re
import os.path
import json


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_list_using_soap(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "../target.json")) as f:
            target = json.load(f)
        client = Client(f'{target["web"]["baseUrl"]}api/soap/mantisconnect.php?wsdl')
        list_from_soap = client.service.mc_projects_get_user_accessible(username=target['webadmin']["username"],
                                                                        password=target['webadmin']["password"])
        list = []
        for row in list_from_soap:
            list.append(Project(id=row[0], name=row[1], description=row[7]))
        return list

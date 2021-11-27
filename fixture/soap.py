from suds.client import Client
from suds import WebFault
from model.projects import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_list_using_soap(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        list_from_soap = client.service.mc_projects_get_user_accessible(username, password)
        list = []
        for row in list_from_soap:
            list.append(Project(id=row[0], name=row[1], description=row[7]))
        return list

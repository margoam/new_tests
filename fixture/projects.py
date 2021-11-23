import re
import os.path
import json
from model.projects import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/my_view_page.php") and len(wd.find_elements_by_css_selector("a.subtle")[0].text) > 0):
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../target.json")) as f:  # .. -на один уровень выше
                target = json.load(f)
            wd.get(target['web']["baseUrl"])

    def open_manage_project_page(self):
        wd = self.app.wd
        wd.find_elements_by_link_name("Manage").click()
        wd.find_elements_by_link_name("Manage Projects").click()

    def fill_project_form(self, name, description):
        wd = self.app.wd
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_name("description").send_keys(description)

    def create_new_project(self):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create new project']").click()
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def get_projects_list(self):
        wd = self.app.wd
        contact_list = []
        self.open_manage_project_page()
        for element in wd.find_elements_by_css_selector("body > table:nth-child(6) tr.row")[3:]:
            name = element.find_element_by_xpath("td[1]").text
            status = element.find_element_by_xpath("td[2]").text
            view_status = element.find_element_by_xpath("td[4]").text
            description = element.find_element_by_xpath("td[5]").text
            contact_list.append(Project(name=name, status=status, view_status=view_status,
                                        description=description))
        return list(contact_list)


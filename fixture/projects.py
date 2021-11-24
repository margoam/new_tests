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
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        self.edit_fields("name", project.name)
        self.edit_fields("description", project.description)

    def edit_fields(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def get_projects_list(self):
        wd = self.app.wd
        contact_list = []
        self.open_manage_project_page()
        for element in wd.find_elements_by_css_selector("body > table:nth-child(6) tr.row-1"):
            name = element.find_element_by_xpath("td[1]").text
            status = element.find_element_by_xpath("td[2]").text
            view_status = element.find_element_by_xpath("td[4]").text
            description = element.find_element_by_xpath("td[5]").text
            contact_list.append(Project(name=name, status=status, view_status=view_status,
                                        description=description))
        for element in wd.find_elements_by_css_selector("body > table:nth-child(6) tr.row-2"):
            name = element.find_element_by_xpath("td[1]").text
            status = element.find_element_by_xpath("td[2]").text
            view_status = element.find_element_by_xpath("td[4]").text
            description = element.find_element_by_xpath("td[5]").text
            contact_list.append(Project(name=name, status=status, view_status=view_status,
                                        description=description))
        return list(contact_list)


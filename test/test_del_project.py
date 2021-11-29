from model.projects import Project
import random


def test_delete_project(app):
    if len(app.projects.get_projects_list()) == 0:
        app.projects.create_new_project(Project(name="Test2123", description="For testing"))
    old_list = app.soap.get_list_using_soap()
    project = random.choice(old_list)
    app.projects.delete_project_by_index(project.name)
    new_list = app.soap.get_list_using_soap()
    old_list.remove(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)

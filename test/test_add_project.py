from model.projects import Project
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("name", 10), description=random_string("header", 15))]


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    old_list = app.projects.get_projects_list()
    app.projects.create_new_project(project)
    new_list = app.projects.get_projects_list()
    old_list.append(project)
    assert sorted(old_list) == sorted(new_list)

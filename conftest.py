import json
import pytest
import os.path
from fixture.application import Application
import ftputil

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:  # f - содержит объект, указывающий на открытый файл
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config['web']['baseUrl'], username=config['webadmin']['username'],
                              password=config['webadmin']['password'])  # Инициализация фикстуры
    fixture.session.ensure_login(username=config["webadmin"]['username'], password=config["webadmin"]['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)  # Как должна быть разрушена фикстура
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


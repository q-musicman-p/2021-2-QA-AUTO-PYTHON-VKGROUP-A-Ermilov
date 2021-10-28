import os.path
import shutil
import sys
from random import randint
import pytest

from static_variables import EMAIL, PASSWORD
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.header_page import HeaderPage


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.makedirs(base_dir)

    config.base_temp_dir = base_dir

@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir,
                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')  # ??? why?
def root_dir():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))
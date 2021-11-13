import pytest
import os.path
import shutil
import sys

from ui.fixtures import *


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


def pytest_addoption(parser):
    parser.addoption('--debug-log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    debug_log = request.config.getoption('--debug-log')

    return {'debug-log': debug_log}

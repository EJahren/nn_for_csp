import glob
import subprocess
from os import scandir
from os.path import dirname, join

import pytest


@pytest.fixture(scope="session")
def data_dir():
    return join(dirname(dirname(__file__)), "data")


@pytest.fixture(autouse=True, scope="session")
def fetch_dataset(data_dir):
    subprocess.call(join(data_dir, "get.sh"), cwd=data_dir)


@pytest.fixture(scope="session")
def big_data_set_files(data_dir):
    return list(scandir(join(data_dir, "ProblemDataSet200to400")))


@pytest.fixture(scope="session")
def param_files(data_dir):
    return glob.glob(join(data_dir, "*.param"))

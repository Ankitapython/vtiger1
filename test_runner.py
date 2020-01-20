import pytest

from test_scripts.test_case.test_login import *


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_VtigerProj():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.hs = Login(self.driver)

    def test_tc_001_home_login(self):
        self.hs.home()



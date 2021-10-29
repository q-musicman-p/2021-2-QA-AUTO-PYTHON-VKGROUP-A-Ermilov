import pytest

from time import sleep
from base import Base

class TestNegativeLogin(Base):

    def test_uncorrect_credentials(self):
        # self.login_page.try_to_login(email='vasya_pupkin@mail.ru', password='1234567890')
        # assert "Error" in self.driver.page_source  # BAD!!!
        pass

    def test_some_neg_login(self):  # ???
        pass


class TestUI(Base):

    def test_create_company(self, login):
        pass

    def test_create_segment(self, login):
        pass

    def test_delete_segment(self, login):
        pass

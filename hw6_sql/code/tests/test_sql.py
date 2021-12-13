from tests.base import BaseTest


class TestSql(BaseTest):
    def test_task1(self):
        self.builder.create_task1_data()
        assert len(self.get_result_task(1)) == 1

    def test_task2(self):
        self.builder.create_task2_data()
        assert len(self.get_result_task(2)) == 5

    def test_task3(self):
        self.builder.create_task3_data()
        assert len(self.get_result_task(3)) == 10

    def test_task4(self):
        self.builder.create_task4_data()
        assert len(self.get_result_task(4)) == 5

    def test_task5(self):
        self.builder.create_task5_data()
        assert len(self.get_result_task(5)) == 5

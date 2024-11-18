from rt_with_exceptions import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            maks = Runner('Макс', -5)
            for i in range(10):
                maks.walk()
            self.assertEqual(maks.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            denis = Runner(5)
            for i in range(10):
                denis.run()
            self.assertEqual(denis.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                        format="%(levelname)s | %(message)s",
                        encoding="utf-8")

    unittest.main()

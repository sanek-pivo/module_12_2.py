import runner_and_tournament # импортируем модуль runner_and_tournament
from unittest import TestCase # импортируем TestCase из unittest


class TournamentTest(TestCase): # Создаем класс который наследуем его от TestCase

    @classmethod
    def setUpClass(cls): # Метод который вызывается перед всеми тестами в этом классе
        cls.all_results = {} # Создаем словарь для хранения результатов всех тестов

    def setUp(self): # Метод который производится перед каждым тестированием
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls): # Метод который вызывается после всего тестирования
        for test_key, test_value in cls.all_results.items(): #
            position = 1
            for key, value in test_value.items():
                position += 1

    def test_Begun_1(self):
        Begun_1 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        result = Begun_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    def test_Begun_2(self):
        Begun_2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        result = Begun_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')

    def test_Begun_3(self):
        Begun_3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = Begun_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        print(f'{result}')


TournamentTest()
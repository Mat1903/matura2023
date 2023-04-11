import unittest

from matura_2019_czerwiec import Matura2019czerwiec


class MyTestCase(unittest.TestCase):
    def test_zadanie_4_1(self):
        expected_Odp_1 = [563, 2087, 163, 2423, 3581, 911, 997, 113, 1049, 1511, 2467, 283,
                                                       3559, 521, 4201, 877, 1301, 2749, 4919, 1213, 2039, 4111, 3331,
                                                       401, 2221]

        Odp_1 = Matura2019czerwiec().zadanie4_1()

        self.assertEqual(expected_Odp_1, Odp_1)

    def test_zadanie_4_2(self):
        expected_Odp_2 = [31, 37, 101, 1009, 1021, 113, 1499, 1213, 1217,
                                                                     1229, 1231, 1237, 1487, 1223, 7027, 7043, 3821,
                                                                     31873, 1511, 140527, 151169, 151189, 193261,
                                                                     1297001, 1061, 100267, 100271, 100279, 181957, 13,
                                                                     112163, 112181, 3803, 76001, 160183, 160201,
                                                                     160243, 17, 907, 701, 383, 389, 1103, 1109, 31721,
                                                                     1583, 1597, 1601, 1619, 3571, 112111]

        Odp_2 = Matura2019czerwiec().zadanie4_2()

        self.assertEqual(expected_Odp_2, Odp_2)

    def test_zadanie_4_3(self):
        expected_Odp_3 = 27

        Odp_3 = Matura2019czerwiec().zadanie4_3()

        self.assertEqual(expected_Odp_3, Odp_3)
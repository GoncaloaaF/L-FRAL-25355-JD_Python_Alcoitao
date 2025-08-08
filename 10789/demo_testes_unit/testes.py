import unittest


def soma(a:float, b:float) -> float:
    """
    a fun deve somar <a> e  <b> e devolver o valor da soma

    :param a: float correspondente ao 1 valor da soma
    :param b: float correspondente ao 1 valor da soma
    :return: float com o valor da soma

    """


    return float(a+b)


"""





"""



class TestSoma(unittest.TestCase):


    def setUp(self):
        print("setUp - corre antes")

    def tearDown(self):
        print("tearDown - corre depois")


    def test_teste1(self):
        self.assertEqual(soma(0,0),0, "o resultado da soma de 0 + 0 deve ser 0")

    def test_soma_int_int(self):
        res = soma(3,3)

        self.assertEqual(6,res, "erro no calculo de soma")
        self.assertIs(float, type(res),  "Erro no tipo do resultado")


    def test_Erros_tipos(self):
        self.assertRaises(TypeError, soma,0,"0")

    def test_Erros_tipos2(self):
        self.assertRaises(TypeError, soma,"0",0)

    def test_in(self):
        self.assertNotIn(9, [1,3,4,5])



    def test_tempo(self):
        soma = 0
        for i in range(1_000_000):
            soma = soma + i

        self.assertEqual(499999500000, soma)
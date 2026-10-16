import unittest
from nucleo.lista_simple import ListaSimple
from nucleo.lista_doble import ListaDoble

class TestListaSimple(unittest.TestCase):

    def setUp(self):
        self.lista = ListaSimple()

    def test_lista_inicia_vacia(self):
        self.assertTrue(self.lista.esta_vacia())
        self.assertEqual(len(self.lista), 0)
        self.assertIsNone(self.lista.cabeza)
        self.assertIsNone(self.lista.cola)

    def test_agregar_final(self):
        self.lista.agregar_final("A")
        self.lista.agregar_final("B")
        self.lista.agregar_final("C")

        self.assertEqual(list(self.lista), ["A", "B", "C"])
        self.assertEqual(len(self.lista), 3)
        self.assertEqual(self.lista.cabeza.dato, "A")
        self.assertEqual(self.lista.cola.dato, "C")

    def test_eliminar_inicio(self):
        self.lista.agregar_final("A")
        self.lista.agregar_final("B")

        eliminado = self.lista.eliminar_inicio()

        self.assertEqual(eliminado, "A")
        self.assertEqual(list(self.lista), ["B"])
        self.assertEqual(len(self.lista), 1)

    def test_eleminar_ultimo_elemento(self):
        self.lista.agregar_final("A")

        self.assertEqual(self.lista.eliminar_inicio(), "A")
        self.assertTrue(self.lista.esta_vacia())
        self.assertIsNone(self.lista.cabeza)
        self.assertIsNone(self.lista.cola)

    def test_eliminar_lista_vacia(self):
        with self.assertRaises(IndexError):
            self.lista.eliminar_inicio()

    def test_buscar_existente(self):
        self.lista.agregar_final("Ana")
        self.lista.agregar_final("Luis")

        resultado = self.lista.buscar(lambda dato: dato == "Luis")
        self.assertEqual(resultado, "Luis")

    def test_buscar_inexistente(self):
        self.lista.agregar_final("Ana")

        resultado = self.lista.buscar(lambda dato: dato == "Pedro")
        self.assertIsNone(resultado)

    def test_ultimos(self):
        for numero in [1, 2, 3, 4, 5]:
            self.lista.agregar_final(numero)

        self.assertEqual(list(self.lista.ultimos(3)), [3, 4, 5])
        self.assertEqual(list(self.lista.ultimos(0)), [])
        self.assertEqual(list(self.lista.ultimos(10)), [1, 2, 3, 4, 5])

class TestListaDoble(unittest.TestCase):

    def setUp(self):
        self.lista = ListaDoble()

    def test_lista_inicia_vacia(self):
        self.assertTrue(self.lista.esta_vacia())
        self.assertEqual(len(self.lista), 0)
        self.assertIsNone(self.lista.cabeza)
        self.assertIsNone(self.lista.cola)

    def test_insertar_final(self):
        self.lista.insertar_final("A")
        self.lista.insertar_final("B")
        self.lista.insertar_final("C")

        self.assertEqual(list(self.lista), ["A", "B", "C"])
        self.assertEqual(len(self.lista), 3)
        self.assertEqual(self.lista.cabeza.dato, "A")
        self.assertEqual(self.lista.cola.dato, "C")

    def test_recorrer_adelante_y_atras(self):
        for dato in ["A", "B", "C"]:
            self.lista.insertar_final(dato)

        self.assertEqual(list(self.lista.recorrer_adelante()), ["A", "B", "C"])
        self.assertEqual(list(self.lista.recorrer_atras()), ["C", "B", "A"])

    def test_insertar_antes(self):
        nodo_b = self.lista.insertar_final("B")
        self.lista.insertar_antes(nodo_b, "A")

        self.assertEqual(list(self.lista), ["A", "B"])
        self.assertIsNone(self.lista.cabeza.anterior)
        self.assertIs(self.lista.cabeza.siguiente, nodo_b)
        self.assertIs(nodo_b.anterior, self.lista.cabeza)

    def test_insertar_despues(self):
        nodo_a = self.lista.insertar_final("A")
        self.lista.insertar_despues(nodo_a, "B")

        self.assertEqual(list(self.lista), ["A", "B"])
        self.assertIs(self.lista.cola.anterior, nodo_a)
        self.assertIs(nodo_a.siguiente, self.lista.cola)

    def test_eliminar_nodo_intermedio(self):
        self.lista.insertar_final("A")
        nodo_b = self.lista.insertar_final("B")
        self.lista.insertar_final("C")

        eliminado = self.lista.eliminar(nodo_b)

        self.assertEqual(eliminado, "B")
        self.assertEqual(list(self.lista), ["A", "C"])
        self.assertEqual(len(self.lista), 2)
        self.assertIs(self.lista.cabeza.siguiente, self.lista.cola)
        self.assertIs(self.lista.cola.anterior, self.lista.cabeza)
        self.assertIsNone(nodo_b.lista)
        self.assertIsNone(nodo_b.anterior)
        self.assertIsNone(nodo_b.siguiente)

    def test_eliminar_cabeza_y_colas(self):
        nodo_a = self.lista.insertar_final("A")
        nodo_b = self.lista.insertar_final("B")
        nodo_c = self.lista.insertar_final("C")

        self.assertEqual(self.lista.eliminar(nodo_a), "A")
        self.assertEqual(self.lista.eliminar(nodo_c), "C")

        self.assertEqual(list(self.lista), ["B"])
        self.assertIs(self.lista.cabeza, nodo_b)
        self.assertIs(self.lista.cola, nodo_b)
        self.assertIsNone(nodo_b.anterior)
        self.assertIsNone(nodo_b.siguiente)

    def test_eliminar_ultimo_nodo(self):
        nodo = self.lista.insertar_final("A")

        self.assertEqual(self.lista.eliminar(nodo), "A")
        self.assertTrue(self.lista.esta_vacia())
        self.assertIsNone(self.lista.cabeza)
        self.assertIsNone(self.lista.cola)

    def test_buscar_existentes(self):
        self.lista.insertar_final("Ana")
        self.lista.insertar_final("Luis")

        nodo = self.lista.buscar(lambda dato: dato == "Luis")

        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.dato, "Luis")

    def test_buscar_inexistente(self):
        self.lista.insertar_final("Ana")

        resultado = self.lista.buscar(lambda dato: dato == "Pedro")
        self.assertIsNone(resultado)

    def test_rechazar_nodo_de_otra_lista(self):
        otra_lista = ListaDoble()
        nodo = otra_lista.insertar_final("A")

        with self.assertRaises(ValueError):
            self.lista.eliminar(nodo)

    def test_rechazar_ndo_nulo(self):
        with self.assertRaises(ValueError):
            self.lista.eliminar(None)

if __name__ == "__main__":
    unittest.main()
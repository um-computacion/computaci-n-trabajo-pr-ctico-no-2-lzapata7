import unittest
from src.palindromos import is_palindrome

class TestPalindromesSimples(unittest.TestCase):
    
    def test_palindrome_sometemos(self):
        self.assertTrue(is_palindrome("sometemos"))
    
    def test_palindrome_neuquen(self):
        self.assertTrue(is_palindrome("neuquen"))
    
    def test_palindrome_arañara(self):
        self.assertTrue(is_palindrome("arañara"))
        
class TestPalindromesFrases(unittest.TestCase):
    
    def test_palindrome_amaplan(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    
    def test_palindrome_adan(self):
        self.assertTrue(is_palindrome("Adán no cede con nada"))
    
    def test_palindrome_nolemon(self):
        self.assertTrue(is_palindrome("No lemon, no melon"))
    
    def test_palindrome_anallevaaloso(self):
        self.assertTrue(is_palindrome("Ana lleva al oso la avellana"))
    
    def test_palindrome_oiradario(self):
        self.assertTrue(is_palindrome("oir a Darío"))
    
    def test_palindrome_nodeseo(self):
        self.assertTrue(is_palindrome("No deseo yo ese don"))
    
    def test_palindrome_amorroma(self):
        self.assertTrue(is_palindrome("Amor, Roma"))

class TestFrasesNoPalindromas(unittest.TestCase):

    def test_frase_comun(self):
        self.assertFalse(is_palindrome("esto es una simulacion"))

    def test_frase_con_mayusculas(self):
        self.assertFalse(is_palindrome("Respenten Los Rangos"))

    def test_frase_con_simbolos(self):
        self.assertFalse(is_palindrome("comprar $ un auto"))

    def test_frase_larga(self):
        self.assertFalse(is_palindrome("ir al supermercado a comprar fideos"))

    def test_frase_casi_palindromo(self):
        self.assertFalse(is_palindrome("Amar, Roma"))
        
class TestPalindromesEdgeCases(unittest.TestCase):

    def test_cadena_vacia(self):
        self.assertTrue(is_palindrome(""))

    def test_una_letra_minuscula(self):
        self.assertTrue(is_palindrome("s"))

    def test_una_letra_mayuscula(self):
        self.assertTrue(is_palindrome("L"))

    def test_solo_espacios(self):
        self.assertTrue(is_palindrome("      "))

    def test_simbolos_no_letras(self):
        self.assertTrue(is_palindrome("!&$"))

    def test_numero_unico(self):
        self.assertTrue(is_palindrome("5"))

    def test_palabra_con_acentos(self):
        self.assertFalse(is_palindrome("automóvil"))

    def test_frase_con_acentos(self):
        self.assertFalse(is_palindrome("Juancito juega al fútbol"))


if __name__ == '__main__':
    unittest.main()
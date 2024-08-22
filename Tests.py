#Camilo Andres Quintero Rodriguez
import libreriaComplejos as lc
import unittest

class TestCplOperations(unittest.TestCase):

    #Tests para la suma de numeros complejos
    def test_cplsum(self):
        valor = lc.sumar((-4,2),(2,1)) 
        self.assertAlmostEqual(valor[0],-2) 
        self.assertAlmostEqual(valor[1],3)
    
    def test_cplsum2(self):
        valor = lc.sumar((1,0),(2,1)) 
        self.assertAlmostEqual(valor[0],3) 
        self.assertAlmostEqual(valor[1],1)

    #Tests de resta de numeros complejos
    def test_cplresta(self):
        valor = lc.resta((1,2),(2,1))
        self.assertAlmostEqual(valor[0],-1) 
        self.assertAlmostEqual(valor[1],1)
    
    def test_cplresta2(self):
        valor = lc.resta((0,2),(2,0))
        self.assertAlmostEqual(valor[0],-2) 
        self.assertAlmostEqual(valor[1],2)
    
    #Tests de producto de numeros complejos
    def test_cplproducto(self):
        valor = lc.producto((2,3),(4,2))
        self.assertAlmostEqual(valor[0],2) 
        self.assertAlmostEqual(valor[1],16)
    
    def test_cplproducto2(self):
        valor = lc.producto((3,9),(1,2))
        self.assertAlmostEqual(valor[0],-15) 
        self.assertAlmostEqual(valor[1],15)
    
    #Tests de division de numeros complejos
    def test_cpldivision(self):
        valor = lc.division((1,2),(2,1))
        self.assertAlmostEqual(valor[0],0.8) 
        self.assertAlmostEqual(valor[1],0.6)
    
    def test_cpldivision2(self):
        valor = lc.division((5,5),(1,1))
        self.assertAlmostEqual(valor[0],5.0) 
        self.assertAlmostEqual(valor[1],0.0)

    #Tests del conjugado de numeros complejos
    def test_cplconjungado(self):
        valor = lc.conjugado((1,2))
        self.assertAlmostEqual(valor[0],1) 
        self.assertAlmostEqual(valor[1],-2)
    
    def test_cplconjugado2(self):
        valor = lc.conjugado((5,5))
        self.assertAlmostEqual(valor[0],5) 
        self.assertAlmostEqual(valor[1],-5)

    #Tests del modulo de numeros complejos
    def test_cplmodulo(self):
        valor = lc.modulo((0,2))
        self.assertAlmostEqual(valor,2.0)
    
    def test_cplconmodulo2(self):
        valor = lc.modulo((5,5))
        self.assertAlmostEqual(valor,7.0710678118654755) 
        
    #Tests de convertir un cartesiano a polar
    def test_cplconvertirCar(self):
        valor = lc.conversion((5,-3),False)
        self.assertAlmostEqual(valor[0],5.830951894845301) 
        self.assertAlmostEqual(valor[1],5.742765806909002)
    
    def test_cplconvertirPol(self):
        valor = lc.conversion((5,-1.0472),True)
        self.assertAlmostEqual(valor[0],2.4999893963627287) 
        self.assertAlmostEqual(valor[1],-4.330133140917716)
    
    #Tests de la fase de un numero complejo
    def test_cplfase(self):
        valor = lc.fase((5,-3))
        self.assertAlmostEqual(valor,5.742765806909002) 
        
    
    def test_cplfase2(self):
        valor = lc.fase((5,3))
        self.assertAlmostEqual(valor,0.5404195002705842) 
        

    
def main():
    unittest.main()
main()

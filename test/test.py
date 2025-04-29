from src.main import *
from unittest.mock import patch



def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def test_funcaoteste():
    with patch(target='random.randint', return_value=12345) :
        result = funcaoteste() 
        yield result
    
    assert result == {"teste": True, "num_aleatorio": random.randint(0,12345)}


def test_create_estudante():
    estudante_test = Estudante(name='Rodolfo', curso="ADM", ativo=False)
    result = create_estudante(estudante_test)
    yield result
    assert estudante_test == result

def test_update_estudante_nagativo():
    result = update_estudante(-5) 
    yield result
    assert not result
    
def test_update_estudante_positivo():
    result = update_estudante(8) 
    yield result
    assert result

def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result

def test_delete_estudante_positivo():
    result = delete_estudante(10)
    yield result
    assert not result
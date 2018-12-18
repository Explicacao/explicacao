def juntar_listas(lista):
    pass





# Codigo para correr testes
def test(inp, out):
    result = ""
    try:
        result = juntar_listas(list(inp))
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format(inp, out, result))
        exit(1)
    except Exception as e:
        print("A funcão \"crashou\" para o input {}".format(inp))
        print("Erro: " + str(e))
        exit(1)

test([[1,2],[3,4,5],[6,4]], [1,2,3,4,5,6,4])
test([[1,2],[]], [1,2])
test([], [])
print("Todos os testes passaram!")

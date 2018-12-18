def maior(lista):
    pass





# Codigo para correr testes
def test(inp, out):
    result = ""
    try:
        result = maior(list(inp))
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format(inp, out, result))
        exit(1)
    except Exception as e:
        print("A funcão \"crashou\" para o input {}".format(inp))
        print("Erro: " + str(e))
        exit(1)

test([1,3,2], 3)
test(list(range(5)), 4)
test([1,5,2,4,6,5,3,-1,-5], 6)
print("Todos os testes passaram!")

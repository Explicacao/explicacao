def encontrar(lista, item):
    pass




# Codigo para correr testes
def test(inp, inp2, out):
    result = ""
    try:
        result = encontrar(list(inp), inp2)
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format((inp, inp2), out, result))
        exit(1)
    except Exception as e:
        print("A funcão \"crashou\" para o input {}".format((inp, inp2)))
        print("Erro: " + str(e))
        exit(1)

test([1,3,2], 3, 1)
test([1,5,-4,3,-6,5], -6, 4)
test([-4,-6], 1, None)
print("Todos os testes passaram!")

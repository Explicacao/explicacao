def alterar_indice(lista, indice, item):
    pass




# Codigo para correr testes
def test(inp, inp2, inp3, out):
    result = ""
    try:
        result = alterar_indice(list(inp), inp2, inp3)
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format((inp, inp2, inp3), out, result))
        exit(1)
    except Exception as e:
        print("A funcão \"crashou\" para o input {}".format((inp, inp2, inp3)))
        print("Erro: " + str(e))
        exit(1)

test([1,3,2], 2, 1, [1,3,1])
test([1,5,-4,3,-6,5], 3, -1, [1,5,-4,-1,-6,5])
test([-4,-6], 50, 20, [-4, -6])
print("Todos os testes passaram!")

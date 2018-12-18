def inverter(lista):
    pass





# Codigo para correr testes
def test(inp, out):
    result = ""
    try:
        result = inverter(list(inp))
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format(inp, out, result))
        exit(1)
    except Exception as e:
        print("A funcão \"crashou\" para o input {}".format(inp))
        print("Erro: " + str(e))
        exit(1)

test([1,2,3], [3,2,1])
test(list(range(5)), [4,3,2,1,0])
print("Todos os testes passaram!")

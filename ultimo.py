def ultimo(lista):
    pass





# Codigo para correr testes
def test(inp, out):
    result = ""
    try:
        result = ultimo(list(inp))
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format(inp, out, result))
        exit(1)
    except Exception:
        print("A funcão \"crashou\" para o input {}".format(inp))
        exit(1)

test([1,2,3], 3)
test(list(range(5)), 4)
print("Todos os testes passaram!")

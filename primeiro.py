def primeiro(lista):
    pass



# Codigo para correr testes
def test(inp, out):
    result = ""
    try:
        result = primeiro(list(inp))
        assert result == out
    except AssertionError:
        print("Erro: Para {}, esperava {}, mas obtive {}".format(inp, out, result))
        exit(1)
    except Exception:
        print("A funcão \"crashou\" para o input {}".format(inp))
        exit(1)

test([1,2,3], 1)
test(list(range(5)), 0)
print("Todos os testes passaram")

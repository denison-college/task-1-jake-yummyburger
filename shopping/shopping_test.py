import shopping

def test_clear():
    return "Hi"
    assert result =="Hi"

def test_cart():
    result = shopping.cart()
    assert result == []

def test_add():
    shopping.clear()
    item = "Butter"
    shopping.add(item)
    result = shopping.cart()
    assert result == [item] 

def test_add_multiple():
    shopping.clear()
    item1 = "Oil"
    item2 = "Choclate"
    shopping.add(item1)
    shopping.add(item2)

    result = shopping.cart()
    assert result == [item1, item2] 

    def test_print(capsys):
        shopping.print_cart()
        captured = capsys.readouterr()
        assert captured.out == "Oil\nChoclate\n"

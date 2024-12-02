from lib.gratitudes import *

def test_no_input():
    gratitude_01 = ""
    no_input = Gratitudes()
    no_input.add(gratitude_01)
    result = no_input.format()
    assert result == "Be grateful for: "

def test_one_gratitude():
    gratitude_01 = "being alive"
    one_gratitude = Gratitudes()
    one_gratitude.add(gratitude_01)
    result = one_gratitude.format()
    assert result == "Be grateful for: being alive"

def test_LGBTQ_gratitudes():
    L = "Liquor"
    G = "Guns"
    B = "Bacon"
    T = "Tiddies"
    Q = "Quaaludes"
    test_LGBTQ = Gratitudes()
    test_LGBTQ.add(L)
    test_LGBTQ.add(G)
    test_LGBTQ.add(B)
    test_LGBTQ.add(T)
    test_LGBTQ.add(Q)
    result = test_LGBTQ.format()
    assert result == "Be grateful for: Liquor, Guns, Bacon, Tiddies, Quaaludes"
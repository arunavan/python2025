def getEmi(amount):  # method
    return amount/12

def test_getEmi():  # test method
    assert getEmi(60000) == 8000



# pytest test.py
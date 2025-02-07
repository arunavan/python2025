#pip install -U pytest  => to install pytest library
#pytest pytest1.py    => to run testcases
#py -m pytest  app.py  => to run pytest cases in current folder
# MAC- python3 -m pip install --upgrade pip
# python3 -m pip install unittest
# python3 -m pip install pytest
def increment(x):
    return x + 1
#print (increment(int(input("Enter x"))))
def test_increment():  # test function
    assert increment(5)==6

'''
def test_answer():
    assert inc(3) == 4
    assert inc(5) == 6
    assert inc(-4) == 3

def hello():
    return "welcome"

def test_hello():
    assert hello()=="welcome"
'''
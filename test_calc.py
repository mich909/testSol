import calc
def test_inc():
    assert calc.inc(5)==6
def test_dec():
    assert calc.dec(3)==2
    
def test_calc():
    assert calc.inc(calc.dec(0)) == 0
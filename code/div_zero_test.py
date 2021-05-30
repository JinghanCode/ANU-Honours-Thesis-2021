@given(st.integers(0, 100000))
def test_div_zero(x):
   1 / (x - 13242)
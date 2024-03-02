import pytest
from converter import fahrenheit

class TestCelsius:
    def test_temperature(self):
        assert fahrenheit(27) == 27*(9/5)+32
        assert fahrenheit(0) == 32
        assert fahrenheit(-4) == (-4)*(9/5)+32
        with pytest.raises(TypeError): 
            fahrenheit(True)
        with pytest.raises(TypeError):
            fahrenheit("34")

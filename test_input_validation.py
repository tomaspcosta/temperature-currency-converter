import pytest
from converter import Converter

# Test for validating that the temperature is a valid number and within a reasonable range (absolute zero).
@pytest.mark.input_validation
def test_validate_temperature_input_schema():
    assert Converter.validate_temperature_input(100) == 100
    assert Converter.validate_temperature_input(-273.15) == -273.15
    
    with pytest.raises(ValueError):
        Converter.validate_temperature_input("not_a_number")
    
    with pytest.raises(ValueError):
        Converter.validate_temperature_input(-500) 

# Test for validating that the currency input is numeric and positive
@pytest.mark.currency_input_validation
def test_validate_currency_input_schema():
    # Valid inputs (must be numeric and positive)
    assert Converter.validate_currency_input(100) == 100  # Valid positive currency value
    assert Converter.validate_currency_input(0.01) == 0.01  # Very small but valid value
    
    # Invalid inputs (must throw ValueError for non-numeric or non-positive)
    with pytest.raises(ValueError):
        Converter.validate_currency_input("not_a_number")  # String input instead of numeric
    
    with pytest.raises(ValueError):
        Converter.validate_currency_input(-100)  # Negative currency value is invalid
    
    with pytest.raises(ValueError):
        Converter.validate_currency_input(0)  # Zero is considered invalid as per the validation logic

import pytest
from converter import Converter

# Unit Tests for Temperature Conversions
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert Converter.celsius_to_fahrenheit(0) == 32  # Passes (0°C = 32°F)
    assert round(Converter.celsius_to_fahrenheit(30), 1) == 86.0  # Corrected to 86.0°F

@pytest.mark.celsius_to_kelvin
def test_celsius_to_kelvin():
    assert Converter.celsius_to_kelvin(0) == 273.15  # Passes (0°C = 273.15K)
    assert Converter.celsius_to_kelvin(30) == 303.15  # Corrected (Expected 303.15K)

@pytest.mark.fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert Converter.fahrenheit_to_celsius(32) == 0  # Passes (32°F = 0°C)
    assert round(Converter.fahrenheit_to_celsius(50), 2) == 10  # Passes (50°F = 10.0°C)

@pytest.mark.fahrenheit_to_kelvin
def test_fahrenheit_to_kelvin():
    assert Converter.fahrenheit_to_kelvin(32) == 273.15  # Passes (32°F = 273.15K)
    assert round(Converter.fahrenheit_to_kelvin(10), 2) == 260.93  # Corrected (Expected 260.93K)

@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert Converter.kelvin_to_celsius(273.15) == 0   # Passes (273.15K = 0°C)
    assert Converter.kelvin_to_celsius(303.15) == 30  # Corrected (Expected 30°C)

@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert Converter.kelvin_to_fahrenheit(273.15) == 32  # Passes (273.15K = 32°F)
    assert round(Converter.kelvin_to_fahrenheit(303.15), 2) == 86.0  # Corrected (Expected 86.0°F)

# Currency Conversion Tests
@pytest.mark.eur_to_usd
def test_eur_to_usd():
    assert round(Converter.eur_to_usd(100), 2) == 105.0  # Passes (100 EUR = 105 USD)

@pytest.mark.eur_to_gbp
def test_eur_to_gbp():
    assert round(Converter.eur_to_gbp(100), 2) == 88.0   # Passes (100 EUR = 88 GBP)

@pytest.mark.eur_to_inr
def test_eur_to_inr():
    assert round(Converter.eur_to_inr(100), 2) == 8765.0  # Passes (100 EUR = 8765 INR)

# Test for validating that the temperature is a valid number and within a reasonable range (absolute zero).
@pytest.mark.input_validation
def test_validate_temperature_input_schema():
    # Valid inputs (must be numeric and >= absolute zero)
    assert Converter.validate_temperature_input(100) == 100  # Valid positive temperature
    assert Converter.validate_temperature_input(-273.15) == -273.15  # Absolute zero is valid

    # Invalid inputs (must throw ValueError for non-numeric and below absolute zero)
    with pytest.raises(ValueError, match="The temperature value must be a numeric value."):
        Converter.validate_temperature_input("not_a_number")  # String input instead of numeric

    with pytest.raises(ValueError, match="Temperature cannot be below absolute zero (-273.15°C)."):
        Converter.validate_temperature_input(-500)  # Below absolute zero, invalid
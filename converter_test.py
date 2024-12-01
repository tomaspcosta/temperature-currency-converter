import pytest
from converter import Converter, validate_temperature_input, validate_currency_input


# Unit Tests for Temperature Conversions
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert Converter.celsius_to_fahrenheit(0) == 32     # Passes (0°C = 32°F)
    assert Converter.celsius_to_fahrenheit(25) == 77.0  # Passes (25°C = 77°F)


@pytest.mark.celsius_to_kelvin
def test_celsius_to_kelvin():
    assert Converter.celsius_to_kelvin(0) == 273.15   # Passes (0°C = 273.15K)
    assert Converter.celsius_to_kelvin(25) == 298.15  # Passes (25°C = 298.15K)


@pytest.mark.fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert Converter.fahrenheit_to_celsius(32) == 0  # Passes (32°F = 0°C)
    assert round(Converter.fahrenheit_to_celsius(100), 2) == 37.78  # Passes (100°F = 37.78°C)


@pytest.mark.fahrenheit_to_kelvin
def test_fahrenheit_to_kelvin():
    assert Converter.fahrenheit_to_kelvin(32) == 273.15   # Passes (32°F = 273.15K)
    assert round(Converter.fahrenheit_to_kelvin(212), 2) == 373.15  # Passes (212°F = 373.15K)


@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert Converter.kelvin_to_celsius(273.15) == 0   # Passes (273.15K = 0°C)
    assert Converter.kelvin_to_celsius(298.15) == 25  # Passes (298.15K = 25°C)


@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert Converter.kelvin_to_fahrenheit(273.15) == 32  # Passes (273.15K = 32°F)
    assert Converter.kelvin_to_fahrenheit(298.15) == 77  # Passes (298.15K = 77°F)

# Input Validation Tests
@pytest.mark.inoput_validation
def test_validate_temperature_input():
    assert validate_temperature_input(100) == 100  # Valid temperature
    assert validate_temperature_input(-273.15) == -273.15  # Absolute zero is valid
    with pytest.raises(ValueError):
        validate_temperature_input(-300)  # Below absolute zero is invalid


@pytest.mark.validation
def test_validate_currency_input():
    assert validate_currency_input(100) == 100  # Valid positive amount
    assert validate_currency_input(10.50) == 10.50  # Valid decimal amount
    with pytest.raises(ValueError):
        validate_currency_input("xyz")  # Non-numeric input
    with pytest.raises(ValueError):
        validate_currency_input(-50)  # Negative value
    with pytest.raises(ValueError):
        validate_currency_input(0)  # Zero value
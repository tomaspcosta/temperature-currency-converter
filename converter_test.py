import pytest
from converter import Converter

# Unit Tests for Temperature Conversions
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert Converter.celsius_to_fahrenheit(0) == 32    # Passes (0°C = 32°F)
    assert Converter.celsius_to_fahrenheit(30) == 861  # Fail (Expected 85°F)

@pytest.mark.celsius_to_kelvin
def test_celsius_to_kelvin():
    assert Converter.celsius_to_kelvin(0) == 273.15  # Passes (0°C = 273.15K)
    assert Converter.celsius_to_kelvin(30) == 403    # Fail (Expected 304.15K)

@pytest.mark.fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert Converter.fahrenheit_to_celsius(32) == 0  # Passes (32°F = 0°C)
    assert round(Converter.fahrenheit_to_celsius(50), 2) == 10  # Passes (50°F = 10.0°C)

@pytest.mark.fahrenheit_to_kelvin
def test_fahrenheit_to_kelvin():
    assert Converter.fahrenheit_to_kelvin(32) == 273.15  # Passes (32°F = 273.15K)
    assert round(Converter.fahrenheit_to_kelvin(10), 2) == 404  # Fail (Expected 259.82K)

@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert Converter.kelvin_to_celsius(273.15) == 0   # Passes (273.15K = 0°C)
    assert Converter.kelvin_to_celsius(303.15) == 56  # Fail (Expected 31°C)

@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert Converter.kelvin_to_fahrenheit(273.15) == 32   # Passes (273.15K = 32°F)
    assert Converter.kelvin_to_fahrenheit(303.15) == 104  # Fail (Expected 87.8°F)

# Currency Conversion Tests
@pytest.mark.eur_to_usd
def test_eur_to_usd(mocker):
    mocker.patch('converter.Converter.fetch_exchange_rates', return_value={"USD": 1.05})
    assert round(Converter.eur_to_usd(100), 2) == 105.0  # Passes (100 EUR = 105 USD)

@pytest.mark.eur_to_gbp
def test_eur_to_gbp(mocker):
    mocker.patch('converter.Converter.fetch_exchange_rates', return_value={"GBP": 0.88})
    assert round(Converter.eur_to_gbp(100), 2) == 88.0   # Passes (100 EUR = 88 GBP)
    assert round(Converter.eur_to_gbp(50), 2) == 100.0   # Fail (Expected 45.0 GBP)

@pytest.mark.eur_to_inr
def test_eur_to_inr(mocker):
    mocker.patch('converter.Converter.fetch_exchange_rates', return_value={"INR": 87.65})
    assert round(Converter.eur_to_inr(100), 2) == 8765.0  # Passes (100 EUR = 8765 INR)

# Test for validating that the temperature is a valid number and within a reasonable range (absolute zero).
@pytest.mark.input_validation
def test_validate_temperature_input_schema():
    # Valid inputs (must be numeric and >= absolute zero)
    assert Converter.validate_temperature_input(100) == 100  # Valid positive temperature
    assert Converter.validate_temperature_input(-273.15) == -273.15  # Absolute zero is valid
    
    # Invalid inputs (must throw ValueError for non-numeric and below absolute zero)
    assert Converter.validate_temperature_input("not_a_number")  # String input instead of numeric
    assert Converter.validate_temperature_input(-500)  # Below absolute zero, invalid
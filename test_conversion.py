import pytest
from unittest.mock import patch
from converter import Converter

# Unit Tests for Temperature Conversions
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert Converter.celsius_to_fahrenheit(0) == 32 
    assert round(Converter.celsius_to_fahrenheit(30), 1) == 86.0 

@pytest.mark.celsius_to_kelvin
def test_celsius_to_kelvin():
    assert Converter.celsius_to_kelvin(0) == 273.15  # 0°C = 273.15K
    assert Converter.celsius_to_kelvin(30) == 303.15  # 30°C = 303.15K

@pytest.mark.fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert Converter.fahrenheit_to_celsius(32) == 0  # 32°F = 0°C
    assert round(Converter.fahrenheit_to_celsius(50), 2) == 10.0  # 50°F = 10.0°C

@pytest.mark.fahrenheit_to_kelvin
def test_fahrenheit_to_kelvin():
    assert Converter.fahrenheit_to_kelvin(32) == 273.15  # 32°F = 273.15K
    assert round(Converter.fahrenheit_to_kelvin(10), 2) == 260.93  # 10°F = 260.93K

@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert Converter.kelvin_to_celsius(273.15) == 0   # 273.15K = 0°C
    assert Converter.kelvin_to_celsius(303.15) == 30  # 303.15K = 30°C

@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert Converter.kelvin_to_fahrenheit(273.15) == 32  # 273.15K = 32°F
    assert round(Converter.kelvin_to_fahrenheit(303.15), 2) == 86.0  # 303.15K = 86.0°F

# Currency Conversion Tests with Mocking
@pytest.mark.eur_to_usd
@patch('converter.Converter.fetch_exchange_rates')
def test_eur_to_usd(mock_fetch_rates):
    mock_fetch_rates.return_value = {"USD": 1.05}  # Mocked exchange rate
    assert round(Converter.eur_to_usd(100), 2) == 105.0  # 100 EUR = 105 USD

@pytest.mark.eur_to_gbp
@patch('converter.Converter.fetch_exchange_rates')
def test_eur_to_gbp(mock_fetch_rates):
    mock_fetch_rates.return_value = {"GBP": 0.88}  # Mocked exchange rate
    assert round(Converter.eur_to_gbp(100), 2) == 88.0  # 100 EUR = 88 GBP

@pytest.mark.eur_to_inr
@patch('converter.Converter.fetch_exchange_rates')
def test_eur_to_inr(mock_fetch_rates):
    mock_fetch_rates.return_value = {"INR": 87.65}  # Mocked exchange rate
    assert round(Converter.eur_to_inr(100), 2) == 8765.0  # 100 EUR = 8765 INR

# Test for validating that the temperature input is valid
@pytest.mark.input_validation
def test_validate_temperature_input_schema():
    # Valid inputs
    assert Converter.validate_temperature_input(100) == 100  # Valid positive temperature
    assert Converter.validate_temperature_input(-273.15) == -273.15  # Absolute zero is valid

    # Invalid inputs
    with pytest.raises(ValueError, match=r"Temperature must be between -273.15°C and 1000°C."):
        Converter.validate_temperature_input(-500)

    with pytest.raises(ValueError, match="The temperature value must be a numeric value."):
        Converter.validate_temperature_input("not_a_number")  # String input

# Test for validating that the currency input is numeric and positive
@pytest.mark.currency_input_validation
def test_validate_currency_input_schema():
    # Valid inputs
    assert Converter.validate_currency_input(100) == 100  # Positive value
    assert Converter.validate_currency_input(0.01) == 0.01  # Small positive value

    # Invalid inputs
    with pytest.raises(ValueError):
        Converter.validate_currency_input("not_a_number")  # Non-numeric input

    with pytest.raises(ValueError):
        Converter.validate_currency_input(-100)  # Negative value

    with pytest.raises(ValueError):
        Converter.validate_currency_input(0)  # Zero value
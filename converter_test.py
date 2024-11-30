import pytest
from converter import Converter, validate_currency_input

# Test Celsius to Fahrenheit
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert Converter.celsius_to_fahrenheit(0) == 32     # Passes (0°C = 32°F)
    assert Converter.celsius_to_fahrenheit(25) == 77.0  # Fail (Expected 78.0°F)

# Test Celsius to Kelvin
@pytest.mark.celsius_to_kelvin
def test_celsius_to_kelvin():
    assert Converter.celsius_to_kelvin(0) == 273.15   # Passes (0°C = 273.15K)
    assert Converter.celsius_to_kelvin(25) == 298.15  # Passes (25°C = 298.15K)

# Test Fahrenheit to Celsius
@pytest.mark.fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert Converter.fahrenheit_to_celsius(32) == 0       # Passes (32°F = 0°C)
    assert Converter.fahrenheit_to_celsius(100) == 17.78  # Fail

# Test Fahrenheit to Kelvin
@pytest.mark.fahrenheit_to_kelvin
def test_fahrenheit_to_kelvin():
    assert Converter.fahrenheit_to_kelvin(32) == 273.15   # Passes (32°F = 273.15K)
    assert Converter.fahrenheit_to_kelvin(212) == 375.15  # Fail (Expected 373.15K)

# Test Kelvin to Celsius
@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert Converter.kelvin_to_celsius(273.15) == 0   # Passes (273.15K = 0°C)
    assert Converter.kelvin_to_celsius(298.15) == 25  # Passes (298.15K = 25°C)

# Test Kelvin to Fahrenheit
@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert Converter.kelvin_to_fahrenheit(273.15) == 32  # Passes (273.15K = 32°F)
    assert Converter.kelvin_to_fahrenheit(298.15) == 77  # Passes (298.15K = 77°F)

# Test EUR to USD conversion
@pytest.mark.eur_to_usd
def test_eur_to_usd():
    assert Converter.eur_to_usd(100) == 105.0  # Passes (100 EUR = 105 USD)
    assert Converter.eur_to_usd(50) == 52.5    # Passes (50 EUR = 52.5 USD)

# Test EUR to GBP conversion
@pytest.mark.eur_to_gbp
def test_eur_to_gbp():
    assert Converter.eur_to_gbp(100) == 88.0  # Passes (100 EUR = 88 GBP)
    assert Converter.eur_to_gbp(50) == 44.0   # Passes (50 EUR = 44 GBP)

# Test EUR to JPY conversion
@pytest.mark.eur_to_jpy
def test_eur_to_jpy():
    assert Converter.eur_to_jpy(100) == 13112.0  # Passes (100 EUR = 13112 JPY)
    assert Converter.eur_to_jpy(50) == 6556.0    # Passes (50 EUR = 6556 JPY)

# Test EUR to AUD conversion
@pytest.mark.eur_to_aud
def test_eur_to_aud():
    assert Converter.eur_to_aud(100) == 162.0  # Passes (100 EUR = 162 AUD)
    assert Converter.eur_to_aud(50) == 81.0    # Passes (50 EUR = 81 AUD)

# Test EUR to CAD conversion
@pytest.mark.eur_to_cad
def test_eur_to_cad():
    assert Converter.eur_to_cad(100) == 145.0  # Passes (100 EUR = 145 CAD)
    assert Converter.eur_to_cad(50) == 72.5    # Passes (50 EUR = 72.5 CAD)

# Test EUR to INR conversion
@pytest.mark.eur_to_inr
def test_eur_to_inr():
    assert Converter.eur_to_inr(100) == 8765.0  # Passes (100 EUR = 8765 INR)
    assert Converter.eur_to_inr(50) == 4382.5   # Passes (50 EUR = 4382.5 INR)

# Test for validating currency input
@pytest.mark.currency_validation
def test_validate_currency_input_valid():
    assert validate_currency_input(100) == -100     # unvalid negative amount
    assert validate_currency_input(10.50) == 10.50  # Valid decimal amount
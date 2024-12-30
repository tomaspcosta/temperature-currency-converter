import pytest
from converter import Converter

# Unit Tests for Temperature Conversions
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert Converter.celsius_to_fahrenheit(0) == 32    # Passes (0°C = 32°F)
    assert Converter.celsius_to_fahrenheit(30) == 86    # Corrected (Expected 86°F)

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
    assert round(Converter.fahrenheit_to_kelvin(10), 2) == 259.82  # Corrected (Expected 259.82K)

@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert Converter.kelvin_to_celsius(273.15) == 0   # Passes (273.15K = 0°C)
    assert Converter.kelvin_to_celsius(303.15) == 30  # Corrected (Expected 30°C)

@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert Converter.kelvin_to_fahrenheit(273.15) == 32   # Passes (273.15K = 32°F)
    assert round(Converter.kelvin_to_fahrenheit(303.15), 2) == 86.0  # Corrected (Expected 86.0°F)

# Currency Conversion Tests
@pytest.mark.eur_to_usd
def test_eur_to_usd(mocker):
    mocker.patch('converter.Converter.fetch_exchange_rates', return_value={"USD": 1.05})
    assert round(Converter.eur_to_usd(100), 2) == 105.0  # Passes (100 EUR = 105 USD)

@pytest.mark.eur_to_gbp
def test_eur_to_gbp(mocker):
    mocker.patch('converter.Converter.fetch_exchange_rates', return_value={"GBP": 0.88})
    assert round(Converter.eur_to_gbp(100), 2) == 88.0   # Passes (100 EUR = 88 GBP)
    assert round(Converter.eur_to_gbp(50), 2) == 44.0   # Corrected (Expected 44.0 GBP)

@pytest.mark.eur_to_inr
def test_eur_to_inr(mocker):
    mocker.patch('converter.Converter.fetch_exchange_rates', return_value={"INR": 87.65})
    assert round(Converter.eur_to_inr(100), 2) == 8765.0  # Passes (100 EUR = 8765 INR)
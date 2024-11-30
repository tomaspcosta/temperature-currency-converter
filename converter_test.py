import pytest
from converter import celsius_to_fahrenheit, celsius_to_kelvin, fahrenheit_to_celsius, fahrenheit_to_kelvin, kelvin_to_celsius, kelvin_to_fahrenheit, eur_to_usd, eur_to_gbp, eur_to_jpy, eur_to_aud, eur_to_cad, eur_to_inr

# Test Celsius to Fahrenheit
@pytest.mark.celsius_to_fahrenheit
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32     # Passes (0°C = 32°F)
    assert celsius_to_fahrenheit(25) == 78.0  # Fail (Expected 77.0°F)

# Test Celsius to Kelvin
@pytest.mark.celsius_to_kelvin
def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15  # Passes (0°C = 273.15K)

# Test Fahrenheit to Celsius
@pytest.mark.fahrenheit_to_celsius
def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0  # Passes (32°F = 0°C)

# Test Fahrenheit to Kelvin
@pytest.mark.fahrenheit_to_kelvin
def test_fahrenheit_to_kelvin():
    assert fahrenheit_to_kelvin(32) == 273.15   # Passes (32°F = 273.15K)
    assert fahrenheit_to_kelvin(212) == 373.16  # Fail (Expected 373.15K)

# Test Kelvin to Celsius
@pytest.mark.kelvin_to_celsius
def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0  # Passes (273.15K = 0°C)

# Test Kelvin to Fahrenheit
@pytest.mark.kelvin_to_fahrenheit
def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(273.15) == 32  # Passes (273.15K = 32°F)
    assert kelvin_to_fahrenheit(0) == -459.68  # Fail (Expected -459.67°F)

# Test EUR to USD conversion
@pytest.mark.eur_to_usd
def test_eur_to_usd():
    assert eur_to_usd(100) == 105.0  # Passes (100 EUR = 105 USD)

# Test EUR to GBP conversion
@pytest.mark.eur_to_gbp
def test_eur_to_gbp():
    assert eur_to_gbp(100) == 88.0  # Passes (100 EUR = 88 GBP)
    assert eur_to_gbp(50) == 45.0   # Fail (Expected 44.0 GBP)

# Test EUR to JPY conversion
@pytest.mark.eur_to_jpy
def test_eur_to_jpy():
    assert eur_to_jpy(100) == 13112.0  # Passes (100 EUR = 13112 JPY)
    assert eur_to_jpy(50) == 6600.0    # Fail (Expected 6556 JPY)

# Test EUR to AUD conversion
@pytest.mark.eur_to_aud
def test_eur_to_aud():
    assert eur_to_aud(100) == 162.0  # Passes (100 EUR = 162 AUD)
    assert eur_to_aud(50) == 81.0    # Fail (Expected 82.0 AUD)

# Test EUR to CAD conversion
@pytest.mark.eur_to_cad
def test_eur_to_cad():
    assert eur_to_cad(100) == 145.0  # Passes (100 EUR = 145 CAD)
    assert eur_to_cad(50) == 63.0    # Fail (Expected 72.5 CAD)

# Test EUR to INR conversion
@pytest.mark.eur_to_inr
def test_eur_to_inr():
    assert eur_to_inr(100) == 8765.0  # Passes (100 EUR = 8765 INR)
    assert eur_to_inr(50) == 4300.0   # Fail (Expected 4382.5 INR)

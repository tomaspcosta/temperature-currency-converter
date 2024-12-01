# Temperature and Currency Conversion Application

## **Overview**
This is a Python-based application that provides temperature and currency conversion functionalities through a console menu. The application allows for converting temperatures between Celsius, Fahrenheit, and Kelvin, as well as converting currencies from EUR to several major currencies.

---

## **Features**

### **1. Temperature Conversions**

| **Conversion**            | **Description**               |
|---------------------------|-------------------------------|
| Celsius to Fahrenheit      | Convert Celsius to Fahrenheit  |
| Celsius to Kelvin          | Convert Celsius to Kelvin      |
| Fahrenheit to Celsius      | Convert Fahrenheit to Celsius  |
| Fahrenheit to Kelvin       | Convert Fahrenheit to Kelvin   |
| Kelvin to Celsius          | Convert Kelvin to Celsius      |
| Kelvin to Fahrenheit       | Convert Kelvin to Fahrenheit   |

### **2. Currency Conversions**

| **Conversion**            | **Description**               |
|---------------------------|-------------------------------|
| EUR to USD                | Convert EUR to USD            |
| EUR to GBP                | Convert EUR to GBP            |
| EUR to JPY                | Convert EUR to JPY            |
| EUR to AUD                | Convert EUR to AUD            |
| EUR to CAD                | Convert EUR to CAD            |
| EUR to INR                | Convert EUR to INR            |

---

## **OWASP ASVS Requirement**

This project implements **OWASP ASVS Requirement 5.1.4**:
- **"Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length, and pattern."**

### **Input Validation**
1. **Temperature Inputs**:
   - Ensures the input is a **numeric value** (rejecting special characters or strings).
   - Validates that the temperature is not below **absolute zero** (-273.15°C).
   
2. **Currency Inputs**:
   - Ensures the input is a **numeric value**.
   - Validates that the currency amount is **positive** and within a reasonable range.

---

## **API Integration**

The application uses the **ExchangeRate-API** to get the latest currency conversion rates. This API provides real-time exchange rate data, which ensures that currency conversions are based on the most current exchange rates. The API supports various currencies, with conversion rates being updated regularly.

- The API provides real-time exchange rates for multiple currencies against EUR, including USD, GBP, JPY, AUD, CAD, INR, and many more.

---

## **Requirements**

- Python 3.x
- `requests` library (for fetching live data from the ExchangeRate-API)
- `colorama` library (for text coloring in the console)

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt

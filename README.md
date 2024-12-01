# Temperature and Currency Conversion Application

## **Overview**
This is a Python-based application that provides temperature and currency conversion functionalities. The application includes a console menu for user interaction, enabling the user to convert temperatures between Celsius, Fahrenheit, and Kelvin, as well as currencies between EUR and several other major currencies.

---

## **Features**

### **1. Temperature Conversions**
- Convert Celsius to Fahrenheit
- Convert Celsius to Kelvin
- Convert Fahrenheit to Celsius
- Convert Fahrenheit to Kelvin
- Convert Kelvin to Celsius
- Convert Kelvin to Fahrenheit

### **2. Currency Conversions**
- Convert EUR to USD
- Convert EUR to GBP
- Convert EUR to JPY
- Convert EUR to AUD
- Convert EUR to CAD
- Convert EUR to INR

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

## **Currency Exchange API Integration**

This application fetches real-time currency conversion rates from the **ExchangeRate API**. The current exchange rates are automatically retrieved through the API and used for currency conversions. This ensures that the exchange rates are always up-to-date and correct.

### **API Details**
- **API provider**: [ExchangeRate API](https://www.exchangerate-api.com/)
- The API provides real-time conversion rates for multiple currencies, including EUR to USD, EUR to GBP, and others.

---

## **Dependencies**

### Required Python Packages

To run this project, you need the following Python packages:
- **requests**: For fetching live data from the ExchangeRate API.
- **pytest**: For running tests.
- **pytest-mock**: For mocking the API responses during testing.

### Installing Dependencies

You can install the required dependencies using `pip`:

```bash
pip install requests pytest pytest-mock

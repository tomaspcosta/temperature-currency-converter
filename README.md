# Temperature and Currency Conversion Application

## **Overview**
This is a Python-based application that provides temperature and currency conversion functionalities via a user-friendly console menu. It also incorporates **input validation** to meet **OWASP ASVS Requirement 1.1.4**, ensuring the application adheres to secure coding practices.

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
This project implements **OWASP ASVS Requirement 1.1.4**:
- **"Verify that all inputs are validated for type, length, format, and range."**

### **Input Validation**
1. **Temperature Inputs**:
   - Ensures the input is a **numeric value**.
   - Validates that the temperature is not below **absolute zero** (-273.15°C).
2. **Currency Inputs**:
   - Ensures the input is a **numeric value**.
   - Validates that the currency amount is **positive**.

These measures enhance security and ensure the app processes only valid inputs.

---

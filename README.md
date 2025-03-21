#   Temperature and Currency Conversion Console Application

##   Table of Contents

1.  [Project Description](#project-description)
2.  [Technologies Used](#technologies-used)
3.  [Features](#features)
4.  [OWASP ASVS Requirement](#owasp-asvs-requirement)
5.  [API Integration](#api-integration)
6.  [Requirements](#requirements)

##   1. Project Description

This is a Python-based console application that provides temperature and currency conversion functionalities through a console menu. The application allows for converting temperatures between Celsius, Fahrenheit, and Kelvin, as well as converting currencies from EUR to several major currencies.

This project offers a user-friendly way to perform common temperature and currency conversions directly from the command line. It is designed to be simple, efficient, and secure, with a focus on data validation and accurate results.

##   2. Technologies Used

* Python 3.x

##   3. Features

###   Temperature Conversions

* Convert Celsius to Fahrenheit
* Convert Celsius to Kelvin
* Convert Fahrenheit to Celsius
* Convert Fahrenheit to Kelvin
* Convert Kelvin to Celsius
* Convert Kelvin to Fahrenheit

###   Currency Conversions

* Convert EUR to USD
* Convert EUR to GBP
* Convert EUR to JPY
* Convert EUR to AUD
* Convert EUR to CAD
* Convert EUR to INR

##   4. OWASP ASVS Requirement

This project implements **OWASP ASVS Requirement 5.1.4**:

* "Verify that structured data is strongly typed and validated against a defined schema including allowed characters, length, and pattern."

###   Input Validation

1.  **Temperature Inputs**:
    * Ensures the input is a **numeric value** (rejecting special characters or strings).
    * Validates that the temperature is not below **absolute zero** (-273.15°C) and not above **1000°C**, ensuring realistic and valid temperature values.
2.  **Currency Inputs**:
    * Ensures the input is a **numeric value**.
    * Validates that the currency amount is **positive** and within a reasonable range, preventing extreme or incorrect input values.

These input validation measures ensure that data entered by users is both accurate and safe, complying with the OWASP ASVS guidelines for data security and integrity.

##   5. API Integration

The application uses the **ExchangeRate-API** to get the latest currency conversion rates. This API provides real-time exchange rate data, which ensures that currency conversions are based on the most current exchange rates. The API supports various currencies, with conversion rates being updated regularly.

* The API provides real-time exchange rates for multiple currencies against EUR, including USD, GBP, JPY, AUD, CAD, INR, and many more.

##   6. Requirements

* Python 3.x
* `requests` library (for fetching live data from the ExchangeRate-API)
* `colorama` library (for text coloring in the console)

To install the required dependencies, use the following command:

```bash
pip install -r requirements.txt

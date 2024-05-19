# URL Extractor

This Python script extracts URLs from a list of device information and associates them with their respective device types. It uses regular expressions to identify and extract the URLs from the provided data.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)

## Overview
**Purpose**

The primary goal of this script is to parse a list of device information and extract URLs embedded within specific tags. This is useful in scenarios where device data includes URLs that need to be extracted and used programmatically, such as for further data processing or API requests.

**Design Choices**

1- Regular Expressions (re module):

- We use Python's built-in **re** module to handle the pattern matching required for extracting URLs. Regular expressions are a powerful tool for string manipulation and pattern recognition, making them ideal for this task.
- The specific pattern **r'<url>(https?://[a-z0-9_.]+)</url>'** is designed to match URLs within **<url>** tags. This pattern accounts for common URL structures and ensures we capture valid URLs that start with **http** or **https**.

2- Function Definition:

- The function **extract_urls(data)** is created to encapsulate the logic for URL extraction. This function iterates over the list of tuples, applies the regular expression to find URLs, and stores the results in a dictionary.
- Encapsulating this logic in a function promotes code reuse and modularity, making it easier to test and maintain.

3- Data Structure:

The input data is expected to be a list of tuples, where each tuple contains a device type and a stats access link. This structure is chosen for its simplicity and ease of iteration.
The output is a dictionary mapping device types to their respective URLs. This format is chosen for its efficient look-up capabilities and clear association between device types and URLs.

**Benefits**

- Efficiency: Using regular expressions allows for efficient and concise pattern matching, which is faster than manually parsing strings.
- Scalability: The function can handle any number of device entries, making it scalable for large datasets.
- Reusability: Encapsulating the logic in a function makes it easy to reuse in different parts of a larger application or in different projects.

## Installation
To run this script, you need to have Python installed on your machine. This script does not require any external libraries beyond Python's standard library.

## Usage
1- Prepare your data as a list of tuples, where each tuple contains:
- Device type (string)
- Stats access link in a string that includes the URL wrapped in **"<URL>"** tags.

2- Call the **"extract_urls"** function with your data.

3- The function will return a dictionary mapping each device type to its URL.

## When you run the steps correctly, the result you should see;

![1](https://github.com/enesoncu/URL-Extractor/assets/142101802/026e722e-3e3d-4e35-a96c-0ef5d19318ac)

# SMS Sender

**SMS Sender** is a Python-based tool designed **exclusively for educational purposes** to demonstrate how to interact with APIs for sending SMS messages. It incorporates user agent rotation to simulate real-world HTTP request scenarios and features a professional console-based user interface powered by the `rich` library, including progress bars, result tables, and input validation.

⚠️ **Disclaimer**: This tool is intended **solely for educational use** to learn about API interactions, HTTP requests, and user agent rotation. Do not use it for illegal activities, such as spamming or unauthorized SMS sending. Always comply with applicable laws, regulations, and API terms of service.

## Educational Purpose
The SMS Sender tool is designed to serve as an educational resource for students, developers, and enthusiasts learning about:
- **API Interactions**: Understand how to send HTTP GET and POST requests to various APIs using Python's `requests` library.
- **User Agent Rotation**: Learn techniques to rotate user agents to mimic different devices and browsers, a common practice in web scraping and API testing.
- **HTTP Request Handling**: Explore headers, cookies, JSON payloads, and query parameters in HTTP requests.
- **Error Handling**: Study robust error handling for network issues, timeouts, and invalid inputs.
- **Console UI Design**: Use the `rich` library to create visually appealing console interfaces with progress bars, tables, and formatted output.
- **Ethical Considerations**: Understand the importance of ethical programming by adhering to legal and responsible use of APIs.

This tool provides a practical example of these concepts in a controlled environment. Users are encouraged to experiment with the code in a lawful manner, such as testing with APIs they have permission to use or in a sandbox environment.

## Features
- **User-Friendly Interface**: Colorful console output with a welcome panel, input prompts, and a progress bar.
- **API Integration**: Sends SMS via multiple APIs with user agent rotation to avoid detection.
- **Progress Tracking**: Visual progress bar to monitor SMS sending.
- **Result Summary**: Table displaying the success or failure of each API call.
- **Error Handling**: Validates inputs and handles network errors gracefully.
- **Modular Design**: Well-organized code for easy maintenance and extension.

## Prerequisites
- **Python 3.6+**: Ensure Python is installed on your system.
- **pip**: Python package manager for installing dependencies.
- **Internet Connection**: Required to interact with APIs.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mrTr1cky/sms-boomber.git
   cd sms-sender
   python3 boomber.py

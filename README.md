SMS Sender
SMS Sender is a Python-based tool designed exclusively for educational purposes to demonstrate how to interact with APIs for sending SMS messages. It incorporates user agent rotation to simulate real-world HTTP request scenarios and features a professional console-based user interface powered by the rich library, including progress bars, result tables, and input validation.
⚠️ Disclaimer: This tool is intended solely for educational use to learn about API interactions, HTTP requests, and user agent rotation. Do not use it for illegal activities, such as spamming or unauthorized SMS sending. Always comply with applicable laws, regulations, and API terms of service.
Educational Purpose
The SMS Sender tool is designed to serve as an educational resource for students, developers, and enthusiasts learning about:

API Interactions: Understand how to send HTTP GET and POST requests to various APIs using Python's requests library.
User Agent Rotation: Learn techniques to rotate user agents to mimic different devices and browsers, a common practice in web scraping and API testing.
HTTP Request Handling: Explore headers, cookies, JSON payloads, and query parameters in HTTP requests.
Error Handling: Study robust error handling for network issues, timeouts, and invalid inputs.
Console UI Design: Use the rich library to create visually appealing console interfaces with progress bars, tables, and formatted output.
Ethical Considerations: Understand the importance of ethical programming by adhering to legal and responsible use of APIs.

This tool provides a practical example of these concepts in a controlled environment. Users are encouraged to experiment with the code in a lawful manner, such as testing with APIs they have permission to use or in a sandbox environment.
Features

User-Friendly Interface: Colorful console output with a welcome panel, input prompts, and a progress bar.
API Integration: Sends SMS via multiple APIs with user agent rotation to avoid detection.
Progress Tracking: Visual progress bar to monitor SMS sending.
Result Summary: Table displaying the success or failure of each API call.
Error Handling: Validates inputs and handles network errors gracefully.
Modular Design: Well-organized code for easy maintenance and extension.

Prerequisites

Python 3.6+: Ensure Python is installed on your system.
pip: Python package manager for installing dependencies.
Internet Connection: Required to interact with APIs.

Installation

Clone the Repository:
git clone https://github.com/your-username/sms-sender.git
cd sms-sender


Install Dependencies:Install the required Python libraries using pip:
pip install rich requests



Usage

Run the Script:Execute the script using Python:
python sms_sender.py


Follow Prompts:

Phone Number: Enter a 10-digit phone number (without the country code 880). For educational purposes, use a test number or one you have permission to send to.
SMS Limit: Specify the number of SMS to send (1–100). Start with a low number to avoid overwhelming APIs.Example:

Enter phone number (without 880): 1234567890
How many SMS to send?: 5


Monitor Progress:

A progress bar will display the status of SMS sending.
Success or failure messages will be logged for each API call.
A summary table will show the results at the end.


Example Output:
╭───────────────────── SMS Sender ─────────────────────╮
│ Welcome to SMS Sender                               │
│ Developed by GrayByte                               │
│ Note: This tool is for educational purposes only.   │
│ Do not use for illegal activities.                  │
╰─────────────────────────────────────────────────────╯

Enter phone number (without 880): 1234567890
How many SMS to send?: 5

API responses may be slow. SMS delivery could be delayed. Please be patient.

[1] Sent SMS via https://www.bioscopelive.com
[2] Sent SMS via https://redx.com.bd
...

┌────────────────────────── SMS Sending Results ───────────────────────────┐
│ API                            │ Status                                 │
├────────────────────────────────┼────────────────────────────────────────┤
│ https://www.bioscopelive.com   │ Success                                │
│ https://redx.com.bd            │ Success                                │
│ https://bikroy.com             │ Failed                                 │
└────────────────────────────────┴────────────────────────────────────────┘
Total SMS sent: 2



Configuration

User Agents: The script rotates through a predefined list of user agents to simulate different devices and browsers. Modify the USER_AGENTS list in sms_sender.py to experiment with additional user agents.
APIs: The script uses multiple APIs for sending SMS. API configurations are stored in the api_configs list in the send_sms function. For educational purposes, you can add or remove APIs or replace them with test APIs you have permission to use.
Timeout: Each API request has a 10-second timeout to prevent hanging. Adjust the timeout parameter in the send_request function to study the impact of different timeout values.
Delay: A 1-second delay is added between API calls to prevent overwhelming servers. Modify the time.sleep(1) value in the send_sms function to experiment with request pacing.

Troubleshooting

Invalid Phone Number: Ensure the phone number is 10 digits and contains only numbers. Use a test number or one you have permission to send to.
Invalid Limit: The SMS limit must be a number between 1 and 100 to prevent abuse.
API Errors: If an API fails, check your internet connection or verify the API endpoint is still active. Some APIs may have rate limits, require authentication, or be deprecated.
Dependency Issues: Ensure rich and requests are installed. Run pip install rich requests to resolve.
Script Interrupted: Press Ctrl+C to safely exit the script.

Notes

API Reliability: APIs may change, become rate-limited, or require authentication. For educational purposes, test with a small SMS limit and consider using mock APIs or sandbox environments.
Duplicate API: The osudpotro.com API appears twice in the configuration. You may remove one to study the impact on performance or redundancy.
Ethical Use: Always obtain explicit consent from the recipient before sending SMS, even in a testing environment. Unauthorized use may violate API terms or laws.

Legal Disclaimer
This tool is provided exclusively for educational purposes to teach concepts related to API interactions, HTTP requests, and console UI design. Unauthorized use, such as sending unsolicited SMS, may violate laws, regulations, or the terms of service of the APIs used. The developers are not responsible for any misuse or damage caused by this tool. Always obtain consent from the recipient and use APIs you are authorized to access.
Contributing
Contributions are welcome, especially those that enhance the educational value of the tool! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

Please ensure your contributions align with the educational purpose of the tool and include clear documentation.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For questions, feedback, or educational inquiries, open an issue on the GitHub repository or contact the maintainer at [your-email@example.com].

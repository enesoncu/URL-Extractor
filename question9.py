import re

def extract_urls(data):
    device_urls = {}

    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'<url>(https?://[a-z0-9_.]+)</url>', re.IGNORECASE)

    for device_type, stats_access_link in data:
        matches = url_pattern.findall(stats_access_link)
        if matches:
            device_urls[device_type] = matches[0]

    return device_urls

def main():
    # Sample data
    data = [
        ("AXO145", "<url>https://xcd32112.smart_meter.com</url>"),
        ("TRU151", "<url>http://tXh67.dia_meter.com</url>"),
        ("ZOD231", "<url>http://yT5495.smart_meter.com</url>"),
        ("YRT326", "<url>https://ret323_TRu.crown.com</url>"),
        ("LWR245", "<url>https://luwr3243.celcius.com</url>")
    ]

    device_urls = extract_urls(data)

    if device_urls:
        for device_type, url in device_urls.items():
            print(f"Device Type: {device_type} - URL: {url}")
    else:
        print("No URLs found for any device.")

if __name__ == "__main__":
    main()

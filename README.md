# Izy - Facebook Post Share Automation Tool

A Python-based tool for automating Facebook post sharing using Termux.

## Prerequisites

Before installing this tool, make sure you have Termux installed on your Android device. You can download it from the [F-Droid store](https://f-droid.org/en/packages/com.termux/).

## Installation Steps

1. First, update Termux packages:
```bash
pkg update && pkg upgrade
```

2. Install required packages:
```bash
pkg install python git
```

3. Install pip for Python package management:
```bash
pkg install python-pip
```

4. Clone the repository:
```bash
git clone https://github.com/yurievisu/izy.git
```

5. Navigate to the project directory:
```bash
cd izy
```

6. Install required Python packages:
```bash
pip install rich aiohttp asyncio
```

## Usage

1. Run the script:
```bash
python izy-ENC.py
```

2. When prompted, enter the following information:
   - Your Facebook cookie (must be string or cookiedough format)
   - The Facebook post link (use Facebook Lite copied link)
   - Number of shares you want to perform

## Important Notes

### Account Safety
- ⚠️ ALWAYS USE A DUMMY/ALT ACCOUNT
- DO NOT use your main Facebook account to prevent account lock or disable
- Using this tool with important accounts may lead to account restrictions

### Supported Post Types
Only regular Facebook posts are supported. The following are NOT supported:
- Video posts
- Cover photo posts
- Profile picture posts
- Facebook main app links

### Link Format
- Always use Facebook Lite (fblite) links
- Copy the link directly from Facebook Lite for best results

## Features

- Asynchronous operation for better performance
- Progress tracking with rich console interface
- Support for multiple share operations
- Automatic token generation
- Error handling for invalid cookies

## Troubleshooting

If you encounter any issues:

1. Make sure your Facebook cookie is in the correct format (string or cookiedough)
2. Check if the post link is from Facebook Lite
3. Ensure you have a stable internet connection
4. Try reinstalling the required packages
5. Make sure your dummy account is not restricted

## License

This project is open source and available under the MIT License.

## Credits

Created by yurievisu

# Mobile App Automation - BrowserStack (Android & iOS)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Appium](https://img.shields.io/badge/Appium-3.0%2B-green.svg)](https://appium.io/)
[![BrowserStack](https://img.shields.io/badge/Platform-BrowserStack-orange.svg)](https://www.browserstack.com/)
[![Android](https://img.shields.io/badge/Android-Supported-green.svg)](https://developer.android.com/)
[![iOS](https://img.shields.io/badge/iOS-Supported-blue.svg)](https://developer.apple.com/ios/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Professional cross-platform mobile automation framework using **Appium-Python-Client** and **BrowserStack** cloud platform for scalable, reliable Android & iOS app testing.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Test Architecture](#test-architecture)
- [BrowserStack Integration](#browserstack-integration)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## 🎯 Overview

This framework provides a production-ready automation solution for **Android & iOS** mobile applications using:
- **Python 3.10+** - Modern, maintainable scripting
- **Appium-Python-Client 3.0+** - Industry-standard mobile automation
- **Selenium WebDriver** - Robust element interaction
- **BrowserStack Cloud** - Scalable device infrastructure
- **UiAutomator2** - Native Android automation engine
- **XCUITest** - Native iOS automation engine

---

## ✨ Features

- ✅ **Cross-Platform Support** - Test on both Android & iOS
- ✅ **BrowserStack Cloud Integration** - Test on 3000+ real devices
- ✅ **UiAutomator2 & XCUITest** - Fast, reliable native automation
- ✅ **Smart Element Location** - Multiple fallback locator strategies
- ✅ **Explicit Waits** - Robust synchronization handling
- ✅ **Comprehensive Error Handling** - Screenshots + detailed logging
- ✅ **Session Status Reporting** - Pass/fail status to BrowserStack
- ✅ **Professional Logging** - Clean, structured test output
- ✅ **Virtual Environment** - Isolated dependency management
- ✅ **Easy Platform Switching** - Simple configuration toggle

---

## 📦 Prerequisites

### Required Software
- **Python 3.10+** → [Download Python](https://www.python.org/downloads/)
- **pip** (included with Python)
- **Git** (optional, for version control)

### BrowserStack Account
- Active BrowserStack account → [Sign up here](https://www.browserstack.com/)
- Username and Access Key from [Account Settings](https://www.browserstack.com/accounts/settings)
- Uploaded app to BrowserStack → [Upload Apps](https://app-automate.browserstack.com/dashboard/v2/apps)
  - **Android**: Upload `.apk` file
  - **iOS**: Upload `.ipa` file

---

## 🚀 Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd clock-automation
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
pip list
# Should show: Appium-Python-Client, selenium
```

---

## ⚙️ Configuration

### Platform Selection

The framework supports **both Android and iOS**. Switch platforms by changing the `platform` value in `TEST_CONFIG`:

```python
TEST_CONFIG = {
    'platform': 'Android',  # Change to 'iOS' for iOS testing
    # ... other configs
}
```

### BrowserStack Credentials

Update credentials in `test/clock_alarm_test.py`:

```python
"bstack:options": {
    "userName": "YOUR_USERNAME",      # Replace with your username
    "accessKey": "YOUR_ACCESS_KEY",   # Replace with your access key
    # ... other options
}
```

### Android Configuration

Configure Android settings in `TEST_CONFIG`:

```python
'android': {
    'device': 'Samsung Galaxy S22',              # Target Android device
    'os_version': '12.0',                        # Android OS version
    'app_id': 'bs://YOUR_ANDROID_APP_ID',        # Uploaded .apk ID
}
```

**Available Android Devices:** Google Pixel, Samsung Galaxy, OnePlus, etc.

### iOS Configuration

Configure iOS settings in `TEST_CONFIG`:

```python
'ios': {
    'device': 'iPhone 14',                       # Target iOS device
    'os_version': '16',                          # iOS version
    'app_id': 'bs://YOUR_IOS_APP_ID',           # Uploaded .ipa ID
    'bundle_id': 'com.example.app'               # iOS bundle identifier
}
```

**Available iOS Devices:** iPhone 14/15, iPhone SE, iPad Pro, etc.

### Complete Configuration Example

```python
TEST_CONFIG = {
    'test_name': 'Mobile App Test',
    'platform': 'Android',  # Switch to 'iOS' for iOS testing
    
    # Android Configuration
    'android': {
        'device': 'Samsung Galaxy S22',
        'os_version': '12.0',
        'app_id': 'bs://your_android_app_id',
    },
    
    # iOS Configuration
    'ios': {
        'device': 'iPhone 14',
        'os_version': '16',
        'app_id': 'bs://your_ios_app_id',
        'bundle_id': 'com.example.app'
    },
    
    # Common Settings
    'project_name': 'Mobile App Automation',
    'build_name': 'Cross-Platform Execution'
}
```

---

## 🎮 Usage

### Run Cross-Platform Test Script

```bash
# Windows (with virtual environment)
.venv\Scripts\python.exe test\mobile_automation_test.py

# macOS/Linux (with virtual environment)
.venv/bin/python test/mobile_automation_test.py
```

This will automatically test **both Android and iOS** platforms sequentially.

### Quick Configuration

Edit `test/mobile_automation_test.py`:
```python
CONFIG = {
    'test_android': True,   # Enable/disable Android testing
    'test_ios': True,       # Enable/disable iOS testing
    'username': 'your_username',
    'access_key': 'your_access_key'
}
```

### Switch Between Platforms

**For Android Testing:**
1. Set `'platform': 'Android'` in `TEST_CONFIG`
2. Configure `android` section with device and app details
3. Run the test script

**For iOS Testing:**
1. Set `'platform': 'iOS'` in `TEST_CONFIG`
2. Configure `ios` section with device, app, and bundle ID
3. Run the test script

### Expected Output (Cross-Platform)

```
============================================================
  MOBILE APP AUTOMATION - CROSS-PLATFORM TEST
============================================================

Testing platforms: Android, iOS

============================================================
  TESTING ANDROID
============================================================
[1/5] Connecting to BrowserStack...
✅ Connected
[2/5] Verifying app launch...
✅ Package: com.google.android.permissioncontroller
[3/5] Detecting UI elements...
✅ Found 2 elements
[4/5] Capturing screenshot...
✅ Screenshot saved
[5/5] Updating session status...
✅ Status updated

✅ ANDROID TEST PASSED (21.3s)

Waiting 5s before next test...

============================================================
  TESTING IOS
============================================================
[1/5] Connecting to BrowserStack...
✅ Connected
[2/5] Verifying app launch...
✅ iOS app launched
[3/5] Detecting UI elements...
✅ Found 5 elements
[4/5] Capturing screenshot...
✅ Screenshot saved
[5/5] Updating session status...
✅ Status updated

✅ IOS TEST PASSED (24.1s)

============================================================
  TEST SUMMARY
============================================================

✅ ANDROID
   Status: PASSED
   Duration: 21.3s

✅ IOS
   Status: PASSED
   Duration: 24.1s

------------------------------------------------------------
Platforms: 2 | Passed: 2 | Failed: 0
Total Time: 53.5s
------------------------------------------------------------

✅ ALL TESTS PASSED!
```

### Platform-Specific Notes

**Android:**
- Uses **UiAutomator2** driver for automation
- Requires `.apk` file uploaded to BrowserStack
- Elements identified by: `android.widget.*` class names
- Common locators: resource-id, text, content-desc

**iOS:**
- Uses **XCUITest** driver for automation
- Requires `.ipa` file uploaded to BrowserStack
- Requires bundle identifier in configuration
- Elements identified by: `XCUIElementType*` class names
- Common locators: accessibility-id, name, label

---

## 📁 Project Structure

```
clock-automation/
│
├── test/
│   └── mobile_automation_test.py    # ⭐ Main test script (~200 lines)
│
├── .venv/                           # Virtual environment (not in git)
│
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore rules
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── INTERVIEW_GUIDE.md              # 📘 Interview walkthrough guide
└── TEST_EXECUTION_REPORT.md         # Latest test execution results
```

---

## 🏗️ Test Architecture

### Core Components

#### 1. **Configuration Layer**
```python
TEST_CONFIG = {
    'test_name': 'Mobile App Test',
    'platform': 'Android',  # or 'iOS'
    
    'android': {
        'device': 'Samsung Galaxy S22',
        'os_version': '12.0',
        'app_id': 'bs://android_app_id',
    },
    
    'ios': {
        'device': 'iPhone 14',
        'os_version': '16',
        'app_id': 'bs://ios_app_id',
        'bundle_id': 'com.example.app'
    },
    
    'project_name': 'Mobile App Automation',
    'build_name': 'Cross-Platform Execution'
}
```

#### 2. **Capability Management**
- `get_capabilities()` - Dynamically configures BrowserStack capabilities based on selected platform
- Returns `UiAutomator2Options` for Android or `XCUITestOptions` for iOS
- Automatically applies platform-specific settings
- Separates platform configs from BrowserStack options

#### 3. **Helper Functions**
- `wait_for_element()` - Explicit waits with timeout handling
- `wait_and_click()` - Safe click with element availability check
- `set_browserstack_status()` - Report test results to BrowserStack
- `print_execution_summary()` - Structured test reporting

#### 4. **Test Execution Flow**
1. Initialize WebDriver connection
2. Verify app launch and get package info
3. Interact with app UI elements
4. Capture screenshot evidence
5. Set BrowserStack session status
6. Cleanup and close session

#### 5. **Error Handling**
- Try-except-finally structure
- Screenshot capture on failure
- Graceful driver cleanup
- Detailed error logging

---

## 🌐 BrowserStack Integration

### Session Status Reporting

The framework automatically reports test status to BrowserStack:

```python
# On success
set_browserstack_status(driver, "passed", "Test executed successfully")

# On failure
set_browserstack_status(driver, "failed", "Error message")
```

### View Test Results

1. Visit [BrowserStack Dashboard](https://app-automate.browserstack.com/dashboard/v2)
2. Find your session under the configured project/build
3. View:
   - Screenshots
   - Video recordings
   - Network logs
   - Device logs
   - Session metadata

### Debug Features

Enable additional debugging in capabilities:

```python
"bstack:options": {
    "debug": True,          # Enable debug mode
    "networkLogs": True,    # Capture network traffic
    "video": True,          # Record session video
    "consoleLogs": "verbose"
}
```

---

## 🔧 Troubleshooting

### Issue: ModuleNotFoundError

**Error:** `ModuleNotFoundError: No module named 'appium'`

**Solution:**
```bash
# Activate virtual environment first
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Then install dependencies
pip install -r requirements.txt
```

### Issue: BrowserStack Connection Failed

**Error:** `Could not connect to BrowserStack`

**Solutions:**
1. Check internet connection
2. Verify credentials are correct
3. Ensure BrowserStack account is active
4. Check firewall/proxy settings

### Issue: App Not Found

**Error:** `[BROWSERSTACK_INVALID_APP_CAP]`

**Solution for Android:**
1. Upload your `.apk` to BrowserStack
2. Copy the app ID (starts with `bs://`)
3. Update `app_id` in `TEST_CONFIG['android']`

**Solution for iOS:**
1. Upload your `.ipa` to BrowserStack
2. Copy the app ID (starts with `bs://`)
3. Update `app_id` in `TEST_CONFIG['ios']`
4. Ensure `bundle_id` matches your app's bundle identifier

### Issue: iOS App Won't Launch

**Error:** `Application could not be started`

**Solutions:**
1. Verify `.ipa` is properly signed for testing
2. Check bundle identifier is correct
3. Ensure iOS version compatibility
4. Use BrowserStack's app inspector to validate upload

### Issue: Platform-Specific Element Not Found

**Error:** `TimeoutException: Element not found`

**Solution for Android:**
1. Use Android-specific locators: `android.widget.Button`, etc.
2. Check resource-id, content-desc, text attributes
3. Use BrowserStack Inspector to find correct locators

**Solution for iOS:**
1. Use iOS-specific locators: `XCUIElementTypeButton`, etc.
2. Check accessibility-id, name, label attributes
3. Use Xcode or BrowserStack Inspector for element identification

**Solution:**
1. Increase timeout values in `wait_for_element()`
2. Verify element locators using BrowserStack Inspector
3. Add more fallback locator strategies
4. Check if app screen has loaded completely

---

## 🎤 Interview Preparation

**Preparing for an interview?** Check out the [INTERVIEW_GUIDE.md](INTERVIEW_GUIDE.md) for:
- Complete code walkthrough
- Technical talking points
- Common interview questions & answers
- Demo script
- Extension points

---

## 📚 Best Practices

### 1. **Use Virtual Environments**
Always activate virtual environment before running tests to avoid dependency conflicts.

### 2. **Use Explicit Waits**
Prefer `WebDriverWait` over `time.sleep()` for more reliable synchronization.

### 3. **Multiple Locator Strategies**
Implement fallback locators for critical elements to handle UI variations.

### 4. **Error Handling**
Always use try-except-finally to ensure proper cleanup even on failures.

### 5. **Screenshot Evidence**
Capture screenshots on both success and failure for debugging.

### 6. **Meaningful Logs**
Use structured logging with clear step numbers and status indicators.

### 7. **Session Management**
Always close driver in finally block to avoid orphaned sessions.

### 8. **Configuration Management**
Keep test data separate from test logic using configuration dictionaries.

---

## 📊 Performance Metrics

- **Total Test Duration (Both Platforms):** ~54 seconds
- **Android Test:** ~21 seconds
- **iOS Test:** ~24 seconds
- **WebDriver Initialization:** 3-5 seconds per platform
- **App Launch Time:** 2-3 seconds
- **Element Interaction:** <1 second per action
- **Screenshot Capture:** <1 second

---

## 🔐 Security

- **Never commit credentials** to version control
- Use environment variables for sensitive data
- Keep `.env` files in `.gitignore`
- Rotate BrowserStack access keys regularly
- Use read-only credentials for CI/CD pipelines

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

- **BrowserStack Docs:** https://www.browserstack.com/docs/app-automate
- **Appium Documentation:** https://appium.io/docs/en/latest/
- **Python Appium Client:** https://github.com/appium/python-client

---

## 🎓 Additional Resources

- [Appium Python Client Documentation](https://appium.github.io/python-client-sphinx/)
- [BrowserStack App Automate Guide](https://www.browserstack.com/app-automate)
- [UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver)
- [Selenium WebDriver Docs](https://selenium-python.readthedocs.io/)

---

**Last Updated:** February 23, 2026  
**Framework Version:** 1.0.0  
**Maintained By:** Mobile Automation Team

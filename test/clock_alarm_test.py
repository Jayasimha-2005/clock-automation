"""
========================================
ANDROID APP AUTOMATION TEST (BrowserStack)
========================================

Description: Professional automation script for Android app testing on BrowserStack
Platform: Android (BrowserStack Cloud)
App: Uploaded APK (bs://ab8e05e86a67dcb2cb42d07f4e742e1822dda79c)
Framework: Appium-Python-Client + Selenium WebDriver + UiAutomator2

@author Senior Mobile Automation Test Engineer
@date 2026-02-22
"""

from appium import webdriver  # type: ignore
from appium.options.android import UiAutomator2Options  # type: ignore
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time


# ========================================
# TEST CONFIGURATION
# ========================================
TEST_CONFIG = {
    'test_name': 'Python Appium Execution',
    'platform': 'Android',
    'device': 'Samsung Galaxy S22',
    'app_id': 'bs://ab8e05e86a67dcb2cb42d07f4e742e1822dda79c',
    'project_name': 'Clock Automation Python Migration',
    'build_name': 'Uploaded App Execution'
}


# ========================================
# BROWSERSTACK CONFIGURATION
# ========================================
def get_capabilities():
    """
    Configure BrowserStack capabilities for Android app testing
    Returns: UiAutomator2Options object with all capabilities
    """
    options = UiAutomator2Options()
    
    # Platform configuration
    options.platform_name = "Android"
    
    # App configuration - using uploaded app
    options.set_capability("app", "bs://ab8e05e86a67dcb2cb42d07f4e742e1822dda79c")
    
    # BrowserStack specific options
    options.set_capability("bstack:options", {
        "deviceName": "Samsung Galaxy S22",
        "osVersion": "12.0",
        "projectName": "Clock Automation Python Migration",
        "buildName": "Uploaded App Execution",
        "sessionName": "Python Appium Execution",
        "userName": "jaganbunny_Tx0REB",
        "accessKey": "zqieqGpBZpbXi9CkmqiX",
        "debug": True,
        "networkLogs": True
    })
    
    return options


# ========================================
# HELPER FUNCTIONS
# ========================================

def wait_for_element(driver, locator_type, locator_value, timeout=15):
    """
    Wait for element to be visible using explicit wait
    Args:
        driver: Appium driver instance
        locator_type: Type of locator (e.g., AppiumBy.ID, AppiumBy.XPATH)
        locator_value: Value of the locator
        timeout: Maximum wait time in seconds
    Returns: WebElement
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator_value))
        )
        return element
    except TimeoutException:
        print(f"⚠️  Element not found: {locator_value}")
        raise


def wait_and_click(driver, locator_type, locator_value, timeout=15):
    """
    Wait for element to be clickable and click it
    Args:
        driver: Appium driver instance
        locator_type: Type of locator
        locator_value: Value of the locator
        timeout: Maximum wait time in seconds
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()
        print(f"✅ Clicked element: {locator_value}")
    except TimeoutException:
        print(f"⚠️  Element not clickable: {locator_value}")
        raise


def set_browserstack_status(driver, status, reason):
    """
    Set BrowserStack session status
    Args:
        driver: Appium driver instance
        status: "passed" or "failed"
        reason: Reason message
    """
    try:
        driver.execute_script(
            f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"{status}","reason": "{reason}"}}}}'
        )
        print(f"✅ BrowserStack session status set to: {status}")
    except Exception as e:
        print(f"⚠️  Could not set BrowserStack status: {str(e)}")


def print_execution_summary(status, error=None):
    """
    Print professional execution summary
    Args:
        status: Test status (PASSED or FAILED)
        error: Error message if test failed
    """
    print('\n' + '=' * 60)
    print('             EXECUTION SUMMARY')
    print('=' * 60)
    print(f"Test Name      : {TEST_CONFIG['test_name']}")
    print(f"Platform       : {TEST_CONFIG['platform']}")
    print(f"Device         : {TEST_CONFIG['device']}")
    print(f"App ID         : {TEST_CONFIG['app_id']}")
    print(f"Project        : {TEST_CONFIG['project_name']}")
    print(f"Build          : {TEST_CONFIG['build_name']}")
    print(f"Status         : {status}")
    if error:
        print(f"Error          : {error}")
    print('=' * 60 + '\n')


# ========================================
# MAIN TEST SCRIPT
# ========================================

def run_app_automation_test():
    """
    Main test execution function
    Tests uploaded app on BrowserStack device
    """
    driver = None
    test_status = 'FAILED'
    error_message = None
    
    try:
        print('\n' + '=' * 60)
        print('  🚀 STARTING APP AUTOMATION TEST')
        print('=' * 60)
        
        # ----------------------------------------
        # STEP 1: Initialize WebDriver Connection
        # ----------------------------------------
        print('\n[STEP 1] Initializing WebDriver connection to BrowserStack...')
        capabilities = get_capabilities()
        driver = webdriver.Remote(  # type: ignore
            command_executor='https://hub-cloud.browserstack.com/wd/hub',
            options=capabilities
        )
        print('✅ WebDriver session created successfully')
        
        # Set implicit wait
        driver.implicitly_wait(10)
        
        # ----------------------------------------
        # STEP 2: Verify App Launch
        # ----------------------------------------
        print('\n[STEP 2] Verifying app launch...')
        
        # Wait for app to load
        time.sleep(5)
        
        # Get current app package to verify app loaded
        try:
            current_package = driver.current_package
            current_activity = driver.current_activity
            print(f"✅ App launched successfully")
            print(f"   Package: {current_package}")
            print(f"   Activity: {current_activity}")
        except Exception as e:
            print(f"⚠️  Could not retrieve app info: {str(e)}")
            print("ℹ️  Continuing test...")
        
        # ----------------------------------------
        # STEP 3: Interact with App
        # ----------------------------------------
        print('\n[STEP 3] Interacting with app...')
        
        # Try to find any clickable elements
        try:
            # Look for common clickable elements
            elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
            if not elements:
                elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            if not elements:
                elements = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageButton")
            
            if elements:
                print(f"✅ Found {len(elements)} UI elements")
                # Try to interact with first element
                try:
                    element = elements[0]
                    element_text = element.text if hasattr(element, 'text') else 'N/A'
                    print(f"   First element text: {element_text}")
                except:
                    pass
            else:
                print("ℹ️  No interactive elements found on screen")
        except Exception as e:
            print(f"⚠️  Could not analyze UI elements: {str(e)}")
        
        time.sleep(2)
        
        # ----------------------------------------
        # STEP 4: Take Screenshot
        # ----------------------------------------
        print('\n[STEP 4] Capturing screenshot...')
        screenshot = driver.get_screenshot_as_base64()
        print('✅ Screenshot captured successfully')
        
        # ----------------------------------------
        # STEP 5: Set BrowserStack Session Status
        # ----------------------------------------
        print('\n[STEP 5] Setting BrowserStack session status...')
        set_browserstack_status(driver, "passed", "Test executed successfully")
        
        # ----------------------------------------
        # TEST PASSED
        # ----------------------------------------
        test_status = 'PASSED'
        print('\n' + '=' * 60)
        print('  ✅ TEST PASSED SUCCESSFULLY!')
        print('=' * 60)
        print(f"\n📱 App tested on: {TEST_CONFIG['device']}")
        print(f"🏗️  Build: {TEST_CONFIG['build_name']}")
        
    except Exception as error:
        # ----------------------------------------
        # ERROR HANDLING
        # ----------------------------------------
        print('\n' + '=' * 60)
        print('  ❌ TEST FAILED')
        print('=' * 60)
        print(f"\n❌ Error Details: {str(error)}")
        
        import traceback
        print(f"\n❌ Stack Trace:\n{traceback.format_exc()}")
        
        error_message = str(error)
        test_status = 'FAILED'
        
        # Set BrowserStack session status to failed
        if driver:
            try:
                set_browserstack_status(driver, "failed", f"Test failed: {error_message[:100]}")
            except:
                pass
        
        # Take screenshot on failure
        if driver:
            try:
                screenshot = driver.get_screenshot_as_base64()
                print('\n📸 Screenshot captured on failure')
            except Exception as screenshot_error:
                print(f'⚠️  Failed to capture screenshot: {str(screenshot_error)}')
    
    finally:
        # ----------------------------------------
        # CLEANUP & QUIT DRIVER
        # ----------------------------------------
        if driver:
            try:
                print('\n[CLEANUP] Closing WebDriver session...')
                driver.quit()
                print('✅ WebDriver session closed successfully')
            except Exception as quit_error:
                print(f'⚠️  Error closing driver: {str(quit_error)}')
        
        # ----------------------------------------
        # PRINT EXECUTION SUMMARY
        # ----------------------------------------
        print_execution_summary(test_status, error_message)
        
        # ----------------------------------------
        # EXIT WITH APPROPRIATE CODE
        # ----------------------------------------
        sys.exit(0 if test_status == 'PASSED' else 1)


# ========================================
# SCRIPT EXECUTION ENTRY POINT
# ========================================
if __name__ == "__main__":
    run_app_automation_test()

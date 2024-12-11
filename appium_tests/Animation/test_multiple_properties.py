import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.appium_config import logger
from time import sleep



class TestAnimationMultiplePropertiesPage:
    """Test suite for Animation/Multiple Properties page."""

    def test_open_animations_menu(self, appium_driver, wait):
        """Open the Animations menu."""
        logger.info("Starting test: Open Animations Menu")

        try:
            animations_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Animation' and @resource-id='android:id/text1']"))
            )
            assert animations_element.is_displayed(), "Animations menu item not displayed"
            logger.info("Animations menu item found and displayed")
            animations_element.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_open_animation_multiple_properties_menu(self, appium_driver, wait):
        """Open the Animation/Multiple Properties menu."""
        logger.info("Starting test: Open Animation/Multiple Properties Menu")

        try:
            animation_multiple_properties_menu = wait.until(
                EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Multiple Properties']"))
            )
            assert animation_multiple_properties_menu.is_displayed(), "Animation/Multiple Properties menu item not displayed"
            logger.info("Animation/Multiple Properties menu item found and displayed")
            animation_multiple_properties_menu.click()
            sleep(2)
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_verify_run_button_displayed(self, appium_driver, wait):
        """Verify the 'Run' button is displayed."""
        logger.info("Starting test: Verify Run Button Displayed")

        try:
            run_button = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert run_button.is_displayed(), "'Run' button not displayed"
            logger.info("'Run' button is displayed")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

    def test_click_run_button(self, appium_driver, wait):
        """Click the 'Run' button and verify its functionality."""
        logger.info("Starting test: Click Run Button")

        try:
            run_button = wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, "io.appium.android.apis:id/startButton"))
            )
            assert run_button.is_displayed(), "'Run' button not displayed"
            logger.info("'Run' button is displayed")
            run_button.click()
            logger.info("Clicked the 'Run' button")
            sleep(2)

            animation_view = wait.until(
                EC.visibility_of_element_located((AppiumBy.CLASS_NAME, "android.view.View"))
            )
            assert animation_view.is_displayed(), "Expected animation or view not displayed after clicking 'Run'"
            logger.info("Animation or view displayed after clicking 'Run' button")
        except Exception as e:
            logger.error(f"Test failed: {e}")
            raise

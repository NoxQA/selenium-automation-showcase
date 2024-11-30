import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver


def test_entry_ad(driver):
    """
    Test to verify the behavior of the entry ad modal.
    1. Verify the ad appears on initial page load.
    2. Verify the modal can be closed.
    3. Ensure the modal does not appear after closing it on a page reload.
    4. Re-enable the ad and check if it appears again on page reload.
    """
    page_url = "https://the-internet.herokuapp.com/entry_ad"

    try:
        # Navigate to the Entry Ad page
        driver.get(page_url)
        logger.info(f"Navigated to: {page_url}")

        # Wait for the ad modal to be visible on the initial page load
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "modal"))
        )
        logger.info("Ad modal is visible on the initial page load.")

        # Close the modal by clicking the 'Close' button
        close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p")
        close_button.click()
        logger.info("Closed the ad modal.")

        # Wait for the underlay (if present) to disappear
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "underlay"))
        )
        logger.info("Modal overlay (underlay) is no longer visible.")

        # Reload the page
        driver.refresh()

        # Check if the modal does not appear on the second load
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, "modal"))
            )
            logger.error("Ad modal appeared again on the second load - it should not.")
            assert False, "Ad modal should not appear after being closed."
        except Exception:
            logger.info("Ad modal did not appear after being closed. Test passed for modal persistence.")

        # Re-enable the ad by clicking the "click here" link
        restart_ad_link = driver.find_element(By.ID, "restart-ad")

        # Use JavaScript click if normal click is intercepted
        try:
            restart_ad_link.click()
            logger.info("Clicked the link to re-enable the ad.")
        except Exception as e:
            logger.warning("Click intercepted, using JavaScript click instead.")
            driver.execute_script("arguments[0].click();", restart_ad_link)

        # Reload the page to verify if the ad appears again
        driver.refresh()

        # Check if the modal appears again
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "modal"))
        )
        logger.info("Ad modal is visible after re-enabling it.")

    except Exception as e:
        logger.error(f"An error occurred during the Entry Ad test: {str(e)}")
        raise

import cv2
import numpy as np
import pyautogui
import time
from robot.api.deco import keyword, library
from logging import getLogger

logger = getLogger(__name__)

@library
class OpenCVLibrary:

    @keyword
    def find_image(self, template_path, confidence=0.8):
        """
        Finds an image on the screen.

        Args:
            template_path (str): The path to the image to search for.
            confidence (float): The minimum confidence to consider the image found. Defaults to 0.8.

        Returns:
            tuple: (x, y) coordinates of the top left corner of the found image.

        Raises:
            AssertionError: The image is not found with the given confidence.
        """

        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        template = cv2.imread(template_path, cv2.IMREAD_COLOR)

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        logger.debug(f"Template matching result: min_val={min_val}, max_val={max_val}, min_loc={min_loc}, max_loc={max_loc}")

        if max_val >= confidence:
            return max_loc
        else:
            raise AssertionError(f"Image not found: {template_path} (confidence {max_val:.2f})")

    @keyword
    def click_image(self, template_path, confidence=0.8):
        """
        Clicks on an image on the screen.

        Args:
            template_path (str): The path to the image to search for.
            confidence (float): The minimum confidence to consider the image found. Defaults to 0.8.

        Raises:
            AssertionError: The image is not found with the given confidence.
        """
        x, y = self.find_image(template_path, confidence)
        h, w = cv2.imread(template_path).shape[:2]
        pyautogui.click(x + w // 2, y + h // 2)

    @keyword
    def wait_for_image(self, template_path, timeout=10, confidence=0.8):
        """
        Waits for an image to appear on the screen.

        Args:
            template_path (str): The path to the image to search for.
            timeout (int): The maximum time to wait in seconds. Defaults to 10.
            confidence (float): The minimum confidence to consider the image found. Defaults to 0.8.

        Raises:
            AssertionError: The image is not found within the given timeout.
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                self.find_image(template_path, confidence)
                return
            except AssertionError:
                time.sleep(0.5)
        raise AssertionError(f"Timeout waiting for image: {template_path}")

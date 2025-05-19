from pywinauto import Application, Desktop
import time
import os
from robot.api.deco import keyword, library

@library
class OSLibrary:
    def __init__(self):
        self.app = None
        self.window = None

    @keyword
    def launch_app(self, path):
        """Launch an application using pywinauto."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Executable not found at {path}")
        self.app = Application(backend="uia").start(path)
        time.sleep(1)

    @keyword
    def wait_for_window(self, title, timeout=10):
        """Wait until the application window with the given title appears."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                self.window = Desktop(backend="uia").window(title_re=title)
                if self.window.exists(timeout=0.5):
                    self.window.set_focus()
                    return
            except Exception:
                pass
            time.sleep(0.5)
        raise Exception(f"Window with title matching '{title}' not found within {timeout} seconds")

    @keyword
    def click_button(self, name):
        """Click a button by name or automation ID."""
        if self.window:
            self.window.child_window(title=name).click()
        else:
            raise Exception("No window attached. Did you run 'wait_for_window'?")

    @keyword
    def get_text(self, automation_id):
        """Get text from an element by automation ID."""
        if self.window:
            elem = self.window.child_window(auto_id=automation_id)
            return elem.window_text()
        else:
            raise Exception("No window attached. Did you run 'wait_for_window'?")

    @keyword
    def close_app(self):
        """Close the application window."""
        if self.window:
            self.window.close()
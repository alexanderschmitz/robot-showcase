# Calculator Robot Framework Automation

This project demonstrates UI test automation for the Windows Calculator using [Robot Framework](https://robotframework.org/), `pywinauto`, and custom Python libraries.

## 📦 Project Structure

```
CALCULATOR-ROBOTFRAMEWORK/
│
├── cv_library/            # Optional: OpenCV-based library
│   └── OpenCVLibrary.py
│
├── os_library/            # Contains OS-based UI automation library using pywinauto
│   └── OSLibrary.py
│
├── results/               # Folder to store screenshots or output
│
├── test_calculator.robot  # Main test case
└── pyproject.toml         
```

## ✅ What It Does

The `test_calculator.robot` script:

1. Launches the Windows Calculator
2. Waits for the window to appear
3. Clicks buttons to perform the operation `2 + 3`
4. Verifies the result is `5`
5. Takes a screenshot of the result
6. Closes the Calculator

## 🛠️ Requirements

Install dependencies using:

```
poetry install
```

## ▶️ Running the Test

```
robot test_calculator.robot
```

This will execute the test and save the screenshot to the `results/` folder.

## 🧩 Custom Libraries

Where the magic happens.
Maybe this can be replaced by the AutoIT or FlaUI Libraries.

- **OSLibrary.py**: Handles app launch, window waiting, button clicking, and text reading via `pywinauto`.
- **OpenCVLibrary.py**: OpenCV-based image matching.

---

## 📸 Example Output

- `result.png`: Screenshot of the calculator after running the test.
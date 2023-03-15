# SpyderHound

## Usage

Start the app with `python run.py` or as a module: `python -m app`.

## Setup

* The base GUI only depends on PyQt6: `pip install pyqt6`
* To produce a standalone .exe file, also install pyinstaller (`pip install pyinstaller`) and run `tools\make_exe.bat`.
* To interactively edit the GUI, you can use Qt designer: `designer.exe app\ui\app.ui`. All changes made to ui files have to be converted with the provided `tools\uicomp.bat` script. To obtain the
  designer, there are multiple options:
    * Install [Qt](https://doc.qt.io/)
    * If you are using [conda](https://docs.conda.io/en/latest/) conda install qt` and run `designer.exe app\ui\app.ui`

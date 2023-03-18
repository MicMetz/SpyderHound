# SpyderHound

## Usage

Start the app with `python run.py` or as a module: `python -m app`.

## Setup

A. The GUI is built with tkinter, and customtkinter:

```commandline
pip install customtkinter && pip install tkinter
```

<hr>
<br>

B. To produce a standalone .exe file, also install pyinstaller:

```commandline
pip install pyinstaller
```

Then run the `build batch` script to produce the .exe file.

```commandline
tools\make_exe.bat
```

<hr>
<br>

* To interactively edit the GUI, you can use Qt designer: `designer.exe app\ui\app.ui`. All changes made to ui files have to be converted with the provided `tools\uicomp.bat` script. To obtain the
  designer, there are multiple options:
    * Install [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
    * If you are using [conda](https://docs.conda.io/en/latest/) `conda install -c conda-forge tk`

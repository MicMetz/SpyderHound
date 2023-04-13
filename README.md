# SpyderHound

## Usage

### Run
<hr>

Start the app with `python run.py` or as a module: `python -m app`.

### Setup
<hr>

1. The GUI is built with tkinter, and customtkinter: `python pip install customtkinter && pip install tkinter`

2. To produce a standalone .exe file, also install pyinstaller, `pip install pyinstaller`; then run the build batch script, `tools/make_exe.bat` to produce the .exe file.


<hr>
<br>

* To interactively edit the GUI, you can use Qt designer: `designer.exe app/ui/app.ui`. All changes made to ui files have to be converted with the provided `tools/uicomp.bat` script. To obtain the
  designer, there are multiple options:
    * Install [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
    * If you are using [conda](https://docs.conda.io/en/latest/) `conda install -c conda-forge tk`



## Development
<hr>

### Project Structure

The project is structured as follows:

```
.
├── core (Core Application Logic)
│   ├── Controller.py
│   ├── Target.py
│   ├── Domain.py
│   ├── Database.py
├── data (Web Scraping Results)
│   ├── [Target Name]
│   │   ├── [Domain Name]
│   │   │   ├── [Date]
│   │   │   │   ├── [Time]
│   │   │   │   │   ├── [Data]
│   │   │   │   │   │   ├── [Data Type]
├── documentation (Documentation)
│   ├── images (Images)
├── resources (Resources)
├── ui (User Interface Tkinter Design)
│   ├── OutputTerminal.py
│   ├── InputTerminal.py
│   ├── SidePanel.py
│   ├── MessageTerminal.py
├── tools (Not Yet Implemented)
├── App.py (Main Application Entry Point)

```




### GUI

The GUI is built with tkinter, and customtkinter.

A. The first draft of the GUI can be found in the [documentation](./documentation) folder. It is a first draft, and will be updated as the project progresses.
![A first-take outline of how the GUI should look.](./documentation/images/Interface_First_Draft.PNG "First Draft")

<br>

B. The second draft of the GUI can be found in the [documentation](./documentation) folder.You can see that the GUI has been updated to include how the application will be designed around the user conducting multiple scrapes simultaneously.
![A more developed outline of how the GUI should look.](./documentation/images/Interface_Second_Draft.PNG "Second Draft")

<br>

C. 
    ![Light Mode](./documentation/images/Interface_Second_Draft_Light.PNG "Light Mode") 
    ![Splash Screen](./documentation/images/Splash_First_Draft.PNG "Splash Screen") 

<br>

Final GUI:
![Final GUI](./documentation/images/Final_Draft_Splash.PNG "Final Splash Screen")
![Final GUI](./documentation/images/Final_Draft_Layout.PNG "Final GUI Layout")
![Final GUI](./documentation/images/Scrape_Results_Example.PNG "Final GUI Layout")




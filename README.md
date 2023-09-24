# binanceVolatilityBot
## 1. Create a Virtual Environment.
   
To create a virtual environment in Python, you can use the <code>venv</code> module, which is included in Python 3.3 and later. Here's how to create a virtual environment:
- Open your command prompt or terminal.
- Navigate to the directory where you want to create the virtual environment.
  You can use the `cd` command to change directories.
  For example:
  ```bash
  cd /path/to/your/directory
  ```
 - Once you are in the desired directory, run the following command to create a virtual environment.
   You can replace <code>myenv</code> with the name you want to give your virtual environment:
   ```bash
   python3 -m venv myenv
   ```
   This command will create a directory named <code>myenv</code> (or the name you specified) in your current directory.
   Inside this directory, the virtual environment will be set up.

- To activate the virtual environment, you'll need to use the appropriate activation command based on your operating system:
  - On Windows:
  ```bash
  myenv\Scripts\activate
  ```
  - On macOS and Linux:
  ```bash
  source myenv/bin/activate
  ```
  After activation, your command prompt or terminal should indicate that you are now working within the virtual environment.

- You can now install Python packages and run Python scripts within the virtual environment, and they will be isolated from the system Python installation.

- To deactivate the virtual environment and return to the system Python, simply run the following command:
  ```bash
  deactivate
  ```
- Remember to activate the virtual environment whenever you work on a project that requires it.
## 2. Install Dependencies
- Install the <code>python-binance</code> library, which is a Python wrapper for the Binance API. You can use the following pip command:
  
  ```bash
  pip install python-binance
  ```
- Use the <code>python-decouple</code> library to manage your configuration settings, including API keys, in a <code>.env</code> file without exposing them in your code. 
  This library allows you to keep sensitive information separate from your source code, which is a good practice for security.
  Here are the steps to use python-decouple:
  - Install the <code>python-decouple</code> library if you haven't already. You can do this using <code>pip</code>:    
  ```bash
  pip install python-decouple
  ```
  - Create a <code>.env</code> file in your project's root directory (if you haven't already) and store your <code>API keys</code> or other configuration settings there. 
  For example:
  ```bash
  API_KEY = "3WSepunyDW5y8KWSsuKL0QJXQFtCDd1afchkNMICBwzCRV86r0Ai5uMeGEkNKM8R"
  API_SECRET = "sXyZV3pKoz3JTiJaGLYOtP38ZEDEyUewlbKatoXs7P70tndnBvUKd73omGAsCOlO"
  ```
  - If you are using VS Code with your Python script, and try to import the <code>Config</code> class from <code>decouple</code> trying to load the values from your .env 
  file, while using a python Virtual Environment, you will probably encounter this specific problem:

  `Import "decouple" could not be resolved Pylance report Missing Imports VSCode`  

  To address this issue, You may want to check which environment your VS Code is using. To select a specific environment:
  - Use the `Python: Select Interpreter` command from the Command Palette (Ctrl+Shift+P).
  - `+Enter Interpreter path`
  - Navigate inside the folder (directory) of `myenv/bin`.
  - Select `python3.xx` and you are good to go.

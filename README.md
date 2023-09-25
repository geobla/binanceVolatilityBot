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
![BinanceVolatilityBot](https://github.com/geobla/binanceVolatilityBot/assets/99928380/f8fb6175-755b-4955-a2ad-588e3a3d10ed)

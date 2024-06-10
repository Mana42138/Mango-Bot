"""
    Initiating process of Mango BOT
    
    This is the main start file.
"""

import subprocess

# Specify the path to your .bat file
bat_file_path = r"C:\Users\madsb\Source\Repos\Mango-Bot\start.bat"

# Run the .bat file
subprocess.run([bat_file_path], shell=True)
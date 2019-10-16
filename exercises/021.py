"""
Make a script that opens and runs an mp3 file.
"""

import os
import subprocess

os.chdir(os.getcwd())

subprocess.call(['afplay','021.mp3'])
subprocess.call(['afplay','022.mp3'])
print('End!')

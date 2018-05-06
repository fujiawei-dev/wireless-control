'''Command line wireless control tool.'''

import traceback

from cerium import AndroidDriver
from cerium.service import Service
from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory


service = Service()
service.disconnect_all()

driver = AndroidDriver()
driver.auto_connect()

commands = dir(driver)
DriverCompleter = WordCompleter(commands + ['driver'])

while True:
    command = prompt('>>> ',
                     history=FileHistory('.history'),
                     auto_suggest=AutoSuggestFromHistory(),
                     completer=DriverCompleter)
    if command[7:].split('(')[0] not in commands:
        print('Invalid parameters or command.')
    else:
        try:
            eval(command)
        except Exception:
            traceback.print_exc()

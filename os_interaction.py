import os
import platform
import json
import sys


def os_information():

    information_list = {
        "Type os": os.name,
        "Processor type": platform.processor(),
        "System bit": sys.platform
    }

    print(information_list)
    with open('os_report.json', 'w') as info:
        json.dump(information_list,info)

os_information()
# Android Wireless Control
![Platform](https://img.shields.io/badge/Platform-Windows-4BC51D.svg)(https://pypi.org/project/wireless-control/)
[![PyPI version](https://img.shields.io/pypi/v/wireless-control.svg)](https://pypi.org/project/wireless-control/)
[![Wheel](https://img.shields.io/pypi/wheel/wireless-control.svg)](https://pypi.org/project/wireless-control/)
[![Python version](https://img.shields.io/pypi/pyversions/wireless-control.svg)](https://pypi.org/project/wireless-control/)
[![license](https://img.shields.io/github/license/fjwCode/wireless-control.svg)] (https://github.com/fjwCode/wireless-control/LICENSE)

> Wireless-control based on wireless-control is a command line wireless control tool for Android automation enthusiasts. 

Wireless-control's source code is made available under the [BSD license](https://github.com/fjwCode/wireless-control/LICENSE).

## Supported Python Versions
* Python 3.6+

## Supported Platforms
* Windows 10 (Other platforms have not been tested and are not intended to be supported for the time being officially)

## Installation
If you have [pip](https://pip.pypa.io/) on your system, you can simply install or upgrade wireless-control:

    pip install -U wireless-control

Alternately, you can download the source distribution from [PyPI](https://badge.fury.io/py/wireless-control), unarchive it, and run:

    python setup.py install

Or by [github.com](https://github.com/fjwCode/wireless-control):

    git clone git@github.com:fjwCode/wireless-control.git
    cd wireless-control
    python setup.py install

> Note: You may want to consider using [virtualenv](http://www.virtualenv.org/) to create isolated Python environments.


## Usage

First, make sure that:

* Your Android phone has USB debugging turned on in developer options.
* Your computer and phone are connected to the same WiFi.
* Only **one phone** connects your computer via USB cable.

OK, Let us begin now!

    C:\WINDOWS\system32>python -m wireless_control.py
    Now you can unplug the USB cable, and control your device via WLAN.
    >>> driver.unlock(1997)   # unlock your device by password
    >>> driver.view_packgets_list(keyword='tencent')
    ['com.tencent.mm', 'com.tencent.android.qqdownloader', 'com.tencent.tim']
    >>> driver.make_a_call(18268237856)   # call me
    >>> driver.end_the_all()   # end the call


## Author

Wireless-control is written and maintained by [White Turing](https://github.com/fjwCode) (fujiawei@stu.hznu.edu.cn).
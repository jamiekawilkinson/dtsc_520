#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:25:52 2022

@author: mrsjneal
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
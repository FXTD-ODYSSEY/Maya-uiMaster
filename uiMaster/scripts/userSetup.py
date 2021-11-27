# -*- coding: utf-8 -*-
"""

"""

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-11-27 14:50:46"

# Import built-in modules
from functools import partial
import os

# Import third-party modules
from maya import cmds


name = "uiMaster"


def load_plugin(plugin_path):
    cmds.loadPlugin(plugin_path)
    cmds.uiMaster()


if not cmds.about(q=1, batch=1):
    module_path = cmds.getModulePath(mn=name)
    plugin_path = os.path.join(module_path, "plug-ins", name + ".py")
    if os.path.isfile(plugin_path):
        if not cmds.pluginInfo(plugin_path, q=1, loaded=1):
            cmds.evalDeferred(partial(load_plugin, plugin_path), lp=1)

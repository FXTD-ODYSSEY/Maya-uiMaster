# Maya-uiMaster

Autodesk Maya uiMaster Tool

Source from [link](https://clamdragon3d.com/blog/2017/1/8/uimaster-for-maya)

---

I add PySide2 & Py3 Support Here.

There is a `uiMaster/install.mel` script, drag this file into Maya.
Then you can launch the window with a mel command.

```Python
from maya import cmds
cmds.uiMaster()
```

![demo](/img/demo.png)

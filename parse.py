# -*- coding: utf-8 -*-
"""
change QtGui to QtWidgets
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-11-27 12:26:46"

import os
import re


DIR = os.path.dirname(os.path.abspath(__file__))
gui_list = [
    "QAbstractTextDocumentLayout",
    "QActionEvent",
    "QBitmap",
    "QBrush",
    "QClipboard",
    "QCloseEvent",
    "QColor",
    "QConicalGradient",
    "QContextMenuEvent",
    "QCursor",
    "QDesktopServices",
    "QDoubleValidator",
    "QDrag",
    "QDragEnterEvent",
    "QDragLeaveEvent",
    "QDragMoveEvent",
    "QDropEvent",
    "QFileOpenEvent",
    "QFocusEvent",
    "QFont",
    "QFontDatabase",
    "QFontInfo",
    "QFontMetrics",
    "QFontMetricsF",
    "QGradient",
    "QHelpEvent",
    "QHideEvent",
    "QHoverEvent",
    "QIcon",
    "QIconDragEvent",
    "QIconEngine",
    "QImage",
    "QImageIOHandler",
    "QImageReader",
    "QImageWriter",
    "QInputEvent",
    "QInputMethodEvent",
    "QIntValidator",
    "QKeyEvent",
    "QKeySequence",
    "QLinearGradient",
    "QMatrix",
    "QMatrix2x2",
    "QMatrix2x3",
    "QMatrix2x4",
    "QMatrix3x2",
    "QMatrix3x3",
    "QMatrix3x4",
    "QMatrix4x2",
    "QMatrix4x3",
    "QMatrix4x4",
    "QMouseEvent",
    "QMoveEvent",
    "QMovie",
    "QPaintDevice",
    "QPaintEngine",
    "QPaintEngineState",
    "QPaintEvent",
    "QPainter",
    "QPainterPath",
    "QPainterPathStroker",
    "QPalette",
    "QPen",
    "QPicture",
    "QPictureIO",
    "QPixmap",
    "QPixmapCache",
    "QPolygon",
    "QPolygonF",
    "QQuaternion",
    "QRadialGradient",
    "QRegExpValidator",
    "QRegion",
    "QResizeEvent",
    "QSessionManager",
    "QShortcutEvent",
    "QShowEvent",
    "QStandardItem",
    "QStandardItemModel",
    "QStatusTipEvent",
    "QSyntaxHighlighter",
    "QTabletEvent",
    "QTextBlock",
    "QTextBlockFormat",
    "QTextBlockGroup",
    "QTextBlockUserData",
    "QTextCharFormat",
    "QTextCursor",
    "QTextDocument",
    "QTextDocumentFragment",
    "QTextFormat",
    "QTextFragment",
    "QTextFrame",
    "QTextFrameFormat",
    "QTextImageFormat",
    "QTextInlineObject",
    "QTextItem",
    "QTextLayout",
    "QTextLength",
    "QTextLine",
    "QTextList",
    "QTextListFormat",
    "QTextObject",
    "QTextObjectInterface",
    "QTextOption",
    "QTextTable",
    "QTextTableCell",
    "QTextTableCellFormat",
    "QTextTableFormat",
    "QTouchEvent",
    "QTransform",
    "QValidator",
    "QVector2D",
    "QVector3D",
    "QVector4D",
    "QWhatsThisClickedEvent",
    "QWheelEvent",
    "QWindowStateChangeEvent",
    "__doc__",
    "__name__",
    "qAlpha",
    "qBlue",
    "qGray",
    "qGreen",
    "qIsGray",
    "qRed",
    "qRgb",
    "qRgba",
]


def main():
    target = os.path.join(DIR, "uiMaster.py")
    output = os.path.join(DIR, "uiMaster2.py")
    lines = []
    with open(target, "r") as f:
        for i, l in enumerate(f.readlines()):
            match = re.search(r"QtGui\.(\D+?)[^a-zA-Z]", l)
            if match:
                # print(dir(match))
                match = match.group(1)
                if match not in gui_list:
                    print(match)
                    l = l.replace("QtGui.","QtWidgets.")
            lines.append(l)   

    with open(output, "w") as f:
        f.write("".join(lines))


if __name__ == "__main__":
    main()

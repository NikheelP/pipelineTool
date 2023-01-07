import sys
#IMPORT MODULE ACCORDING TO REQUIREMENT
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

except:
    try:
        from PyQt4.QtGui import *
        from PyQt4.QtCore import *
    except:
        try:
            from PySide.QtGui import *
            from PySide.QtCore import *
        except:
            try:
                from PySide2.QtGui import *
                from PySide2.QtCore import *
                from PySide2.QtWidgets import *
            except:
                raise Exception('Python Version does not have PyQt5 or PyQt4 or Pyside or PySide2 \n' 
                                'please install any of this and run command again')



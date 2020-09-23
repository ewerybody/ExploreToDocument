import os
import krita
from PyQt5 import QtCore

EXTENSION_ID = 'pykrita_exploretodocument'
MENU_ENTRY = 'Explore To Document'
EXPLORER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


class Exploretodocument(krita.Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID, MENU_ENTRY, "tools/scripts")
        # parameter 1 = the name that Krita uses to identify the action
        # parameter 2 = the text to be added to the menu entry for this script
        # parameter 3 = location of menu entry
        action.triggered.connect(self.action_triggered)

    def action_triggered(self):
        doc =  krita.Krita.instance().activeDocument()
        if doc is None:
            raise FileNotFoundError('No document open!')

        this_file = doc.fileName()
        if not os.path.isfile(this_file):
            raise FileNotFoundError('doc has no fileName!')

        this_file = os.path.normpath(this_file)
        args = ['/select,', this_file]
        process = QtCore.QProcess()
        process.startDetached(EXPLORER_PATH, args)

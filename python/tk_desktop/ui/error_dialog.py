# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from sgtk.platform.qt import QtCore

for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls

from sgtk.platform.qt import QtGui

for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type):
        globals()[name] = cls


class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        if not ErrorDialog.objectName():
            ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.resize(572, 443)
        ErrorDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(ErrorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QLabel(ErrorDialog)
        self.icon.setObjectName("icon")

        self.horizontalLayout.addWidget(self.icon)

        self.title = QLabel(ErrorDialog)
        self.title.setObjectName("title")
        self.title.setStyleSheet("font-size: 20px;")
        self.title.setWordWrap(True)
        self.title.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse
        )

        self.horizontalLayout.addWidget(self.title)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.message = QTextEdit(ErrorDialog)
        self.message.setObjectName("message")
        self.message.setUndoRedoEnabled(False)
        self.message.setLineWrapMode(QTextEdit.NoWrap)
        self.message.setReadOnly(True)
        self.message.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByMouse
        )

        self.verticalLayout.addWidget(self.message)

        self.buttonBox = QDialogButtonBox(ErrorDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ErrorDialog)
        self.buttonBox.accepted.connect(ErrorDialog.accept)
        self.buttonBox.rejected.connect(ErrorDialog.reject)

        QMetaObject.connectSlotsByName(ErrorDialog)

    # setupUi

    def retranslateUi(self, ErrorDialog):
        ErrorDialog.setWindowTitle(
            QCoreApplication.translate("ErrorDialog", "Toolkit Error", None)
        )
        self.icon.setText(QCoreApplication.translate("ErrorDialog", "Error Icon", None))
        self.title.setText(QCoreApplication.translate("ErrorDialog", "Title", None))

    # retranslateUi

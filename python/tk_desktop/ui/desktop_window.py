# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktop_window.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_DesktopWindow(object):
    def setupUi(self, DesktopWindow):
        DesktopWindow.setObjectName("DesktopWindow")
        DesktopWindow.resize(427, 715)
        DesktopWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tk-desktop/default_systray_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DesktopWindow.setWindowIcon(icon)
        DesktopWindow.setDockNestingEnabled(False)
        DesktopWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.center = QtGui.QWidget(DesktopWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center.sizePolicy().hasHeightForWidth())
        self.center.setSizePolicy(sizePolicy)
        self.center.setMouseTracking(True)
        self.center.setObjectName("center")
        self.border_layout = QtGui.QVBoxLayout(self.center)
        self.border_layout.setSpacing(0)
        self.border_layout.setContentsMargins(0, 0, 0, 0)
        self.border_layout.setObjectName("border_layout")
        self.header = QtGui.QFrame(self.center)
        self.header.setFrameShape(QtGui.QFrame.NoFrame)
        self.header.setFrameShadow(QtGui.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.apps_button = QtGui.QPushButton(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apps_button.sizePolicy().hasHeightForWidth())
        self.apps_button.setSizePolicy(sizePolicy)
        self.apps_button.setMinimumSize(QtCore.QSize(0, 0))
        self.apps_button.setMouseTracking(True)
        self.apps_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.apps_button.setFlat(True)
        self.apps_button.setObjectName("apps_button")
        self.horizontalLayout_2.addWidget(self.apps_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.border_layout.addWidget(self.header)
        self.stack = QtGui.QStackedWidget(self.center)
        self.stack.setObjectName("stack")
        self.project_browser_page = QtGui.QWidget()
        self.project_browser_page.setObjectName("project_browser_page")
        self.verticalLayout = QtGui.QVBoxLayout(self.project_browser_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subheader = QtGui.QFrame(self.project_browser_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subheader.sizePolicy().hasHeightForWidth())
        self.subheader.setSizePolicy(sizePolicy)
        self.subheader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.subheader.setFrameShape(QtGui.QFrame.NoFrame)
        self.subheader.setFrameShadow(QtGui.QFrame.Plain)
        self.subheader.setLineWidth(1)
        self.subheader.setMidLineWidth(0)
        self.subheader.setObjectName("subheader")
        self.horizontalLayout = QtGui.QHBoxLayout(self.subheader)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setContentsMargins(20, 15, 20, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subheader_label = QtGui.QLabel(self.subheader)
        self.subheader_label.setMouseTracking(True)
        self.subheader_label.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.subheader_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.subheader_label.setObjectName("subheader_label")
        self.horizontalLayout.addWidget(self.subheader_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.search_frame = QtGui.QFrame(self.subheader)
        self.search_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.search_frame.setProperty("collapsed", False)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.search_frame)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_magnifier = QtGui.QLabel(self.search_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_magnifier.sizePolicy().hasHeightForWidth())
        self.search_magnifier.setSizePolicy(sizePolicy)
        self.search_magnifier.setMaximumSize(QtCore.QSize(17, 17))
        self.search_magnifier.setText("")
        self.search_magnifier.setPixmap(QtGui.QPixmap(":/tk-desktop/search_dark.png"))
        self.search_magnifier.setScaledContents(True)
        self.search_magnifier.setObjectName("search_magnifier")
        self.horizontalLayout_6.addWidget(self.search_magnifier)
        self.search_text = QtGui.QLineEdit(self.search_frame)
        self.search_text.setObjectName("search_text")
        self.horizontalLayout_6.addWidget(self.search_text)
        self.search_button = QtGui.QPushButton(self.search_frame)
        self.search_button.setMaximumSize(QtCore.QSize(17, 17))
        self.search_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.search_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tk-desktop/icon_inbox_clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QtCore.QSize(17, 17))
        self.search_button.setFlat(True)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_6.addWidget(self.search_button)
        self.horizontalLayout.addWidget(self.search_frame)
        self.verticalLayout.addWidget(self.subheader)
        self.projects = QtGui.QListView(self.project_browser_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects.sizePolicy().hasHeightForWidth())
        self.projects.setSizePolicy(sizePolicy)
        self.projects.setMouseTracking(True)
        self.projects.setFrameShape(QtGui.QFrame.NoFrame)
        self.projects.setFrameShadow(QtGui.QFrame.Plain)
        self.projects.setLineWidth(0)
        self.projects.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.projects.setAutoScroll(False)
        self.projects.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.projects.setProperty("showDropIndicator", False)
        self.projects.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.projects.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.projects.setMovement(QtGui.QListView.Static)
        self.projects.setFlow(QtGui.QListView.LeftToRight)
        self.projects.setProperty("isWrapping", True)
        self.projects.setResizeMode(QtGui.QListView.Adjust)
        self.projects.setLayoutMode(QtGui.QListView.SinglePass)
        self.projects.setSpacing(5)
        self.projects.setViewMode(QtGui.QListView.IconMode)
        self.projects.setUniformItemSizes(True)
        self.projects.setSelectionRectVisible(False)
        self.projects.setObjectName("projects")
        self.verticalLayout.addWidget(self.projects)
        self.stack.addWidget(self.project_browser_page)
        self.project_page = QtGui.QWidget()
        self.project_page.setObjectName("project_page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.project_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.project_subheader = QtGui.QFrame(self.project_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_subheader.sizePolicy().hasHeightForWidth())
        self.project_subheader.setSizePolicy(sizePolicy)
        self.project_subheader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.project_subheader.setFrameShape(QtGui.QFrame.NoFrame)
        self.project_subheader.setFrameShadow(QtGui.QFrame.Plain)
        self.project_subheader.setLineWidth(1)
        self.project_subheader.setMidLineWidth(0)
        self.project_subheader.setObjectName("project_subheader")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.project_subheader)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spacer_button_1 = QtGui.QPushButton(self.project_subheader)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_button_1.sizePolicy().hasHeightForWidth())
        self.spacer_button_1.setSizePolicy(sizePolicy)
        self.spacer_button_1.setMinimumSize(QtCore.QSize(10, 0))
        self.spacer_button_1.setMaximumSize(QtCore.QSize(10, 16777215))
        self.spacer_button_1.setBaseSize(QtCore.QSize(10, 0))
        self.spacer_button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spacer_button_1.setText("")
        self.spacer_button_1.setFlat(True)
        self.spacer_button_1.setObjectName("spacer_button_1")
        self.horizontalLayout_4.addWidget(self.spacer_button_1)
        self.project_arrow = QtGui.QPushButton(self.project_subheader)
        self.project_arrow.setMaximumSize(QtCore.QSize(30, 62))
        self.project_arrow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.project_arrow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tk-desktop/back_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_arrow.setIcon(icon2)
        self.project_arrow.setIconSize(QtCore.QSize(20, 20))
        self.project_arrow.setFlat(True)
        self.project_arrow.setObjectName("project_arrow")
        self.horizontalLayout_4.addWidget(self.project_arrow)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.project_icon = QtGui.QLabel(self.project_subheader)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_icon.sizePolicy().hasHeightForWidth())
        self.project_icon.setSizePolicy(sizePolicy)
        self.project_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.project_icon.setText("")
        self.project_icon.setPixmap(QtGui.QPixmap(":/tk-desktop/missing_thumbnail_project.png"))
        self.project_icon.setScaledContents(True)
        self.project_icon.setMargin(5)
        self.project_icon.setObjectName("project_icon")
        self.horizontalLayout_4.addWidget(self.project_icon)
        self.project_name = QtGui.QLabel(self.project_subheader)
        self.project_name.setMargin(5)
        self.project_name.setObjectName("project_name")
        self.horizontalLayout_4.addWidget(self.project_name)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.project_menu = QtGui.QToolButton(self.project_subheader)
        self.project_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tk-desktop/down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_menu.setIcon(icon3)
        self.project_menu.setIconSize(QtCore.QSize(20, 20))
        self.project_menu.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.project_menu.setObjectName("project_menu")
        self.horizontalLayout_4.addWidget(self.project_menu)
        self.spacer_button_4 = QtGui.QPushButton(self.project_subheader)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_button_4.sizePolicy().hasHeightForWidth())
        self.spacer_button_4.setSizePolicy(sizePolicy)
        self.spacer_button_4.setMinimumSize(QtCore.QSize(10, 0))
        self.spacer_button_4.setMaximumSize(QtCore.QSize(10, 16777215))
        self.spacer_button_4.setBaseSize(QtCore.QSize(10, 0))
        self.spacer_button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spacer_button_4.setText("")
        self.spacer_button_4.setFlat(True)
        self.spacer_button_4.setObjectName("spacer_button_4")
        self.horizontalLayout_4.addWidget(self.spacer_button_4)
        self.verticalLayout_2.addWidget(self.project_subheader)
        self.configuration_frame = QtGui.QFrame(self.project_page)
        self.configuration_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.configuration_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.configuration_frame.setObjectName("configuration_frame")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.configuration_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.configuration_name = QtGui.QLabel(self.configuration_frame)
        self.configuration_name.setAlignment(QtCore.Qt.AlignCenter)
        self.configuration_name.setObjectName("configuration_name")
        self.horizontalLayout_8.addWidget(self.configuration_name)
        self.configuration_label = QtGui.QLabel(self.configuration_frame)
        self.configuration_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.configuration_label.setObjectName("configuration_label")
        self.horizontalLayout_8.addWidget(self.configuration_label)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.configuration_frame)
        self.project_commands = GroupingListView(self.project_page)
        self.project_commands.setMouseTracking(True)
        self.project_commands.setFrameShape(QtGui.QFrame.NoFrame)
        self.project_commands.setFrameShadow(QtGui.QFrame.Plain)
        self.project_commands.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.project_commands.setAutoScroll(False)
        self.project_commands.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.project_commands.setProperty("showDropIndicator", False)
        self.project_commands.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.project_commands.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.project_commands.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.project_commands.setMovement(QtGui.QListView.Static)
        self.project_commands.setFlow(QtGui.QListView.LeftToRight)
        self.project_commands.setProperty("isWrapping", True)
        self.project_commands.setResizeMode(QtGui.QListView.Adjust)
        self.project_commands.setLayoutMode(QtGui.QListView.Batched)
        self.project_commands.setSpacing(0)
        self.project_commands.setViewMode(QtGui.QListView.IconMode)
        self.project_commands.setWordWrap(True)
        self.project_commands.setSelectionRectVisible(False)
        self.project_commands.setObjectName("project_commands")
        self.verticalLayout_2.addWidget(self.project_commands)
        self.stack.addWidget(self.project_page)
        self.border_layout.addWidget(self.stack)
        self.footer = QtGui.QFrame(self.center)
        self.footer.setMouseTracking(True)
        self.footer.setFrameShape(QtGui.QFrame.NoFrame)
        self.footer.setFrameShadow(QtGui.QFrame.Plain)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.shotgun_button = QtGui.QPushButton(self.footer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotgun_button.sizePolicy().hasHeightForWidth())
        self.shotgun_button.setSizePolicy(sizePolicy)
        self.shotgun_button.setMouseTracking(True)
        self.shotgun_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tk-desktop/shotgun_logo_light_medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shotgun_button.setIcon(icon4)
        self.shotgun_button.setIconSize(QtCore.QSize(122, 16))
        self.shotgun_button.setFlat(True)
        self.shotgun_button.setObjectName("shotgun_button")
        self.horizontalLayout_3.addWidget(self.shotgun_button)
        spacerItem5 = QtGui.QSpacerItem(173, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.user_button = QtGui.QPushButton(self.footer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_button.sizePolicy().hasHeightForWidth())
        self.user_button.setSizePolicy(sizePolicy)
        self.user_button.setMouseTracking(True)
        self.user_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.user_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tk-desktop/default_user_thumb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_button.setIcon(icon5)
        self.user_button.setIconSize(QtCore.QSize(30, 30))
        self.user_button.setFlat(True)
        self.user_button.setObjectName("user_button")
        self.horizontalLayout_3.addWidget(self.user_button)
        self.border_layout.addWidget(self.footer)
        DesktopWindow.setCentralWidget(self.center)
        self.actionQuit = QtGui.QAction(DesktopWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPin_to_Menu = QtGui.QAction(DesktopWindow)
        self.actionPin_to_Menu.setObjectName("actionPin_to_Menu")
        self.actionSign_Out = QtGui.QAction(DesktopWindow)
        self.actionSign_Out.setObjectName("actionSign_Out")
        self.actionKeep_on_Top = QtGui.QAction(DesktopWindow)
        self.actionKeep_on_Top.setCheckable(True)
        self.actionKeep_on_Top.setObjectName("actionKeep_on_Top")
        self.actionProject_Filesystem_Folder = QtGui.QAction(DesktopWindow)
        self.actionProject_Filesystem_Folder.setObjectName("actionProject_Filesystem_Folder")
        self.actionPreferences = QtGui.QAction(DesktopWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionShow_Console = QtGui.QAction(DesktopWindow)
        self.actionShow_Console.setObjectName("actionShow_Console")
        self.actionRefresh_Projects = QtGui.QAction(DesktopWindow)
        self.actionRefresh_Projects.setObjectName("actionRefresh_Projects")

        self.retranslateUi(DesktopWindow)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DesktopWindow)
        DesktopWindow.setTabOrder(self.projects, self.user_button)
        DesktopWindow.setTabOrder(self.user_button, self.search_button)
        DesktopWindow.setTabOrder(self.search_button, self.search_text)
        DesktopWindow.setTabOrder(self.search_text, self.project_commands)

    def retranslateUi(self, DesktopWindow):
        DesktopWindow.setWindowTitle(QtGui.QApplication.translate("DesktopWindow", "Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.apps_button.setText(QtGui.QApplication.translate("DesktopWindow", "Apps", None, QtGui.QApplication.UnicodeUTF8))
        self.subheader_label.setText(QtGui.QApplication.translate("DesktopWindow", "PROJECTS", None, QtGui.QApplication.UnicodeUTF8))
        self.search_frame.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Search Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_magnifier.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Search Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_text.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Search Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_text.setPlaceholderText(QtGui.QApplication.translate("DesktopWindow", "Search Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Clear search", None, QtGui.QApplication.UnicodeUTF8))
        self.project_arrow.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Back to Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name.setText(QtGui.QApplication.translate("DesktopWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.project_menu.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Project Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.configuration_name.setText(QtGui.QApplication.translate("DesktopWindow", "Configuration Name", None, QtGui.QApplication.UnicodeUTF8))
        self.configuration_label.setText(QtGui.QApplication.translate("DesktopWindow", "CONFIGURATION", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_button.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Open in Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.user_button.setToolTip(QtGui.QApplication.translate("DesktopWindow", "User menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("DesktopWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("DesktopWindow", "Meta+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPin_to_Menu.setText(QtGui.QApplication.translate("DesktopWindow", "Pin to Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSign_Out.setText(QtGui.QApplication.translate("DesktopWindow", "Sign Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKeep_on_Top.setText(QtGui.QApplication.translate("DesktopWindow", "Keep on Top", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProject_Filesystem_Folder.setText(QtGui.QApplication.translate("DesktopWindow", "Project Filesystem Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("DesktopWindow", "Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("DesktopWindow", "Ctrl+,", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Console.setText(QtGui.QApplication.translate("DesktopWindow", "Show Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Console.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Show the logging console.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh_Projects.setText(QtGui.QApplication.translate("DesktopWindow", "Refresh Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh_Projects.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Refreshes the project information.", None, QtGui.QApplication.UnicodeUTF8))

from ..grouping_list_view import GroupingListView
from . import resources_rc

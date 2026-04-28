# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KCC.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QWidget)
from . import KCC_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(566, 671)
        icon = QIcon()
        icon.addFile(u":/Icon/icons/comic2ebook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.croppingWidget = QWidget(self.centralWidget)
        self.croppingWidget.setObjectName(u"croppingWidget")
        self.croppingWidget.setVisible(False)
        self.gridLayout_5 = QGridLayout(self.croppingWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.croppingPowerSlider = QSlider(self.croppingWidget)
        self.croppingPowerSlider.setObjectName(u"croppingPowerSlider")
        self.croppingPowerSlider.setMaximum(300)
        self.croppingPowerSlider.setSingleStep(5)
        self.croppingPowerSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.croppingPowerSlider, 0, 1, 1, 1)

        self.preserveMarginBox = QSpinBox(self.croppingWidget)
        self.preserveMarginBox.setObjectName(u"preserveMarginBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preserveMarginBox.sizePolicy().hasHeightForWidth())
        self.preserveMarginBox.setSizePolicy(sizePolicy)
        self.preserveMarginBox.setMaximum(99)
        self.preserveMarginBox.setSingleStep(5)
        self.preserveMarginBox.setValue(0)

        self.gridLayout_5.addWidget(self.preserveMarginBox, 1, 1, 1, 1)

        self.preserveMarginLabel = QLabel(self.croppingWidget)
        self.preserveMarginLabel.setObjectName(u"preserveMarginLabel")

        self.gridLayout_5.addWidget(self.preserveMarginLabel, 1, 0, 1, 1)

        self.croppingPowerLabel = QLabel(self.croppingWidget)
        self.croppingPowerLabel.setObjectName(u"croppingPowerLabel")

        self.gridLayout_5.addWidget(self.croppingPowerLabel, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.croppingWidget, 9, 0, 1, 2)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.progressBar.setFont(font)
        self.progressBar.setVisible(False)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)

        self.jpegQualityWidget = QWidget(self.centralWidget)
        self.jpegQualityWidget.setObjectName(u"jpegQualityWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.jpegQualityWidget.sizePolicy().hasHeightForWidth())
        self.jpegQualityWidget.setSizePolicy(sizePolicy1)
        self.jpegQualityWidget.setVisible(False)
        self.horizontalLayout_12 = QHBoxLayout(self.jpegQualityWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.jpegQualityLabel = QLabel(self.jpegQualityWidget)
        self.jpegQualityLabel.setObjectName(u"jpegQualityLabel")

        self.horizontalLayout_12.addWidget(self.jpegQualityLabel)

        self.jpegQualitySpinBox = QSpinBox(self.jpegQualityWidget)
        self.jpegQualitySpinBox.setObjectName(u"jpegQualitySpinBox")
        self.jpegQualitySpinBox.setMaximum(95)
        self.jpegQualitySpinBox.setSingleStep(5)
        self.jpegQualitySpinBox.setValue(85)

        self.horizontalLayout_12.addWidget(self.jpegQualitySpinBox)


        self.gridLayout.addWidget(self.jpegQualityWidget, 10, 0, 1, 1)

        self.chunkSizeWidget = QWidget(self.centralWidget)
        self.chunkSizeWidget.setObjectName(u"chunkSizeWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chunkSizeWidget.sizePolicy().hasHeightForWidth())
        self.chunkSizeWidget.setSizePolicy(sizePolicy2)
        self.chunkSizeWidget.setVisible(False)
        self.horizontalLayout_4 = QHBoxLayout(self.chunkSizeWidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chunkSizeLabel = QLabel(self.chunkSizeWidget)
        self.chunkSizeLabel.setObjectName(u"chunkSizeLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chunkSizeLabel.sizePolicy().hasHeightForWidth())
        self.chunkSizeLabel.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.chunkSizeLabel)

        self.chunkSizeBox = QSpinBox(self.chunkSizeWidget)
        self.chunkSizeBox.setObjectName(u"chunkSizeBox")
        self.chunkSizeBox.setMinimum(50)
        self.chunkSizeBox.setMaximum(600)
        self.chunkSizeBox.setValue(400)

        self.horizontalLayout_4.addWidget(self.chunkSizeBox)

        self.chunkSizeWarnLabel = QLabel(self.chunkSizeWidget)
        self.chunkSizeWarnLabel.setObjectName(u"chunkSizeWarnLabel")
        sizePolicy3.setHeightForWidth(self.chunkSizeWarnLabel.sizePolicy().hasHeightForWidth())
        self.chunkSizeWarnLabel.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.chunkSizeWarnLabel)


        self.gridLayout.addWidget(self.chunkSizeWidget, 6, 0, 1, 1)

        self.jobList = QListWidget(self.centralWidget)
        self.jobList.setObjectName(u"jobList")
        self.jobList.setMinimumSize(QSize(0, 150))
        self.jobList.setStyleSheet(u"")
        self.jobList.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.jobList.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.jobList.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.gridLayout.addWidget(self.jobList, 2, 0, 1, 2)

        self.toolWidget = QWidget(self.centralWidget)
        self.toolWidget.setObjectName(u"toolWidget")
        self.gridLayout_6 = QGridLayout(self.toolWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.editorButton = QPushButton(self.toolWidget)
        self.editorButton.setObjectName(u"editorButton")
        self.editorButton.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/Other/icons/editor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editorButton.setIcon(icon1)

        self.gridLayout_6.addWidget(self.editorButton, 0, 0, 1, 1)

        self.kofiButton = QPushButton(self.toolWidget)
        self.kofiButton.setObjectName(u"kofiButton")
        self.kofiButton.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/Brand/icons/kofi_symbol.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.kofiButton.setIcon(icon2)
        self.kofiButton.setIconSize(QSize(19, 16))

        self.gridLayout_6.addWidget(self.kofiButton, 0, 1, 1, 1)

        self.wikiButton = QPushButton(self.toolWidget)
        self.wikiButton.setObjectName(u"wikiButton")
        self.wikiButton.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u":/Other/icons/wiki.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wikiButton.setIcon(icon3)

        self.gridLayout_6.addWidget(self.wikiButton, 0, 2, 1, 1)

        self.youtubeButton = QPushButton(self.toolWidget)
        self.youtubeButton.setObjectName(u"youtubeButton")
        self.youtubeButton.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.youtubeButton, 1, 0, 1, 1)

        self.humbleBundleButton = QPushButton(self.toolWidget)
        self.humbleBundleButton.setObjectName(u"humbleBundleButton")
        self.humbleBundleButton.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/Brand/icons/Humble_H-Red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.humbleBundleButton.setIcon(icon4)

        self.gridLayout_6.addWidget(self.humbleBundleButton, 1, 1, 1, 1)

        self.discordButton = QPushButton(self.toolWidget)
        self.discordButton.setObjectName(u"discordButton")
        self.discordButton.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.discordButton, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.toolWidget, 0, 0, 1, 2)

        self.optionWidget = QWidget(self.centralWidget)
        self.optionWidget.setObjectName(u"optionWidget")
        self.gridLayout_2 = QGridLayout(self.optionWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.noRotateBox = QCheckBox(self.optionWidget)
        self.noRotateBox.setObjectName(u"noRotateBox")

        self.gridLayout_2.addWidget(self.noRotateBox, 6, 1, 1, 1)

        self.maximizeStrips = QCheckBox(self.optionWidget)
        self.maximizeStrips.setObjectName(u"maximizeStrips")

        self.gridLayout_2.addWidget(self.maximizeStrips, 4, 1, 1, 1)

        self.rotateBox = QCheckBox(self.optionWidget)
        self.rotateBox.setObjectName(u"rotateBox")
        self.rotateBox.setTristate(True)

        self.gridLayout_2.addWidget(self.rotateBox, 1, 1, 1, 1)

        self.pngLegacyBox = QCheckBox(self.optionWidget)
        self.pngLegacyBox.setObjectName(u"pngLegacyBox")
        self.pngLegacyBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.pngLegacyBox, 11, 0, 1, 1)

        self.interPanelCropBox = QCheckBox(self.optionWidget)
        self.interPanelCropBox.setObjectName(u"interPanelCropBox")
        self.interPanelCropBox.setTristate(True)

        self.gridLayout_2.addWidget(self.interPanelCropBox, 6, 2, 1, 1)

        self.titleEdit = QLineEdit(self.optionWidget)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy2.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy2)
        self.titleEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.titleEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.titleEdit, 0, 0, 1, 1)

        self.authorEdit = QLineEdit(self.optionWidget)
        self.authorEdit.setObjectName(u"authorEdit")
        sizePolicy2.setHeightForWidth(self.authorEdit.sizePolicy().hasHeightForWidth())
        self.authorEdit.setSizePolicy(sizePolicy2)
        self.authorEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.authorEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.authorEdit, 0, 1, 1, 1)

        self.webtoonBox = QCheckBox(self.optionWidget)
        self.webtoonBox.setObjectName(u"webtoonBox")

        self.gridLayout_2.addWidget(self.webtoonBox, 2, 0, 1, 1)

        self.fileFusionBox = QCheckBox(self.optionWidget)
        self.fileFusionBox.setObjectName(u"fileFusionBox")

        self.gridLayout_2.addWidget(self.fileFusionBox, 6, 0, 1, 1)

        self.deleteBox = QCheckBox(self.optionWidget)
        self.deleteBox.setObjectName(u"deleteBox")

        self.gridLayout_2.addWidget(self.deleteBox, 5, 1, 1, 1)

        self.gammaBox = QCheckBox(self.optionWidget)
        self.gammaBox.setObjectName(u"gammaBox")

        self.gridLayout_2.addWidget(self.gammaBox, 2, 2, 1, 1)

        self.noQuantizeBox = QCheckBox(self.optionWidget)
        self.noQuantizeBox.setObjectName(u"noQuantizeBox")
        self.noQuantizeBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.noQuantizeBox, 10, 2, 1, 1)

        self.eraseRainbowBox = QCheckBox(self.optionWidget)
        self.eraseRainbowBox.setObjectName(u"eraseRainbowBox")

        self.gridLayout_2.addWidget(self.eraseRainbowBox, 7, 2, 1, 1)

        self.coverFillBox = QCheckBox(self.optionWidget)
        self.coverFillBox.setObjectName(u"coverFillBox")

        self.gridLayout_2.addWidget(self.coverFillBox, 9, 1, 1, 1)

        self.rotateRightBox = QCheckBox(self.optionWidget)
        self.rotateRightBox.setObjectName(u"rotateRightBox")

        self.gridLayout_2.addWidget(self.rotateRightBox, 10, 1, 1, 1)

        self.mangaBox = QCheckBox(self.optionWidget)
        self.mangaBox.setObjectName(u"mangaBox")

        self.gridLayout_2.addWidget(self.mangaBox, 1, 0, 1, 1)

        self.spreadShiftBox = QCheckBox(self.optionWidget)
        self.spreadShiftBox.setObjectName(u"spreadShiftBox")

        self.gridLayout_2.addWidget(self.spreadShiftBox, 5, 0, 1, 1)

        self.croppingBox = QCheckBox(self.optionWidget)
        self.croppingBox.setObjectName(u"croppingBox")
        self.croppingBox.setTristate(True)

        self.gridLayout_2.addWidget(self.croppingBox, 4, 2, 1, 1)

        self.jpegQualityBox = QCheckBox(self.optionWidget)
        self.jpegQualityBox.setObjectName(u"jpegQualityBox")

        self.gridLayout_2.addWidget(self.jpegQualityBox, 8, 0, 1, 1)

        self.outputSplit = QCheckBox(self.optionWidget)
        self.outputSplit.setObjectName(u"outputSplit")

        self.gridLayout_2.addWidget(self.outputSplit, 3, 1, 1, 1)

        self.metadataTitleBox = QCheckBox(self.optionWidget)
        self.metadataTitleBox.setObjectName(u"metadataTitleBox")
        self.metadataTitleBox.setTristate(True)

        self.gridLayout_2.addWidget(self.metadataTitleBox, 7, 0, 1, 1)

        self.noSmartCoverCropBox = QCheckBox(self.optionWidget)
        self.noSmartCoverCropBox.setObjectName(u"noSmartCoverCropBox")

        self.gridLayout_2.addWidget(self.noSmartCoverCropBox, 11, 1, 1, 1)

        self.rotateFirstBox = QCheckBox(self.optionWidget)
        self.rotateFirstBox.setObjectName(u"rotateFirstBox")

        self.gridLayout_2.addWidget(self.rotateFirstBox, 8, 1, 1, 1)

        self.mozJpegBox = QCheckBox(self.optionWidget)
        self.mozJpegBox.setObjectName(u"mozJpegBox")
        self.mozJpegBox.setTristate(True)

        self.gridLayout_2.addWidget(self.mozJpegBox, 4, 0, 1, 1)

        self.autoLevelBox = QCheckBox(self.optionWidget)
        self.autoLevelBox.setObjectName(u"autoLevelBox")

        self.gridLayout_2.addWidget(self.autoLevelBox, 8, 2, 1, 1)

        self.forcePngRgbBox = QCheckBox(self.optionWidget)
        self.forcePngRgbBox.setObjectName(u"forcePngRgbBox")
        self.forcePngRgbBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.forcePngRgbBox, 11, 2, 1, 1)

        self.upscaleBox = QCheckBox(self.optionWidget)
        self.upscaleBox.setObjectName(u"upscaleBox")
        self.upscaleBox.setTristate(True)

        self.gridLayout_2.addWidget(self.upscaleBox, 2, 1, 1, 1)

        self.borderBox = QCheckBox(self.optionWidget)
        self.borderBox.setObjectName(u"borderBox")
        self.borderBox.setTristate(True)

        self.gridLayout_2.addWidget(self.borderBox, 3, 0, 1, 1)

        self.qualityBox = QCheckBox(self.optionWidget)
        self.qualityBox.setObjectName(u"qualityBox")
        self.qualityBox.setTristate(True)

        self.gridLayout_2.addWidget(self.qualityBox, 1, 2, 1, 1)

        self.pdfExtractBox = QCheckBox(self.optionWidget)
        self.pdfExtractBox.setObjectName(u"pdfExtractBox")

        self.gridLayout_2.addWidget(self.pdfExtractBox, 9, 0, 1, 1)

        self.colorBox = QCheckBox(self.optionWidget)
        self.colorBox.setObjectName(u"colorBox")

        self.gridLayout_2.addWidget(self.colorBox, 3, 2, 1, 1)

        self.pdfWidthBox = QCheckBox(self.optionWidget)
        self.pdfWidthBox.setObjectName(u"pdfWidthBox")

        self.gridLayout_2.addWidget(self.pdfWidthBox, 10, 0, 1, 1)

        self.disableProcessingBox = QCheckBox(self.optionWidget)
        self.disableProcessingBox.setObjectName(u"disableProcessingBox")

        self.gridLayout_2.addWidget(self.disableProcessingBox, 5, 2, 1, 1)

        self.outputFolderWidget = QWidget(self.optionWidget)
        self.outputFolderWidget.setObjectName(u"outputFolderWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.outputFolderWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.defaultOutputFolderBox = QCheckBox(self.outputFolderWidget)
        self.defaultOutputFolderBox.setObjectName(u"defaultOutputFolderBox")
        sizePolicy.setHeightForWidth(self.defaultOutputFolderBox.sizePolicy().hasHeightForWidth())
        self.defaultOutputFolderBox.setSizePolicy(sizePolicy)
        self.defaultOutputFolderBox.setTristate(True)

        self.horizontalLayout_3.addWidget(self.defaultOutputFolderBox)

        self.defaultOutputFolderButton = QPushButton(self.outputFolderWidget)
        self.defaultOutputFolderButton.setObjectName(u"defaultOutputFolderButton")
        self.defaultOutputFolderButton.setMinimumSize(QSize(0, 30))
        icon5 = QIcon()
        icon5.addFile(u":/Other/icons/folder_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.defaultOutputFolderButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.defaultOutputFolderButton)


        self.gridLayout_2.addWidget(self.outputFolderWidget, 0, 2, 1, 1)

        self.chunkSizeCheckBox = QCheckBox(self.optionWidget)
        self.chunkSizeCheckBox.setObjectName(u"chunkSizeCheckBox")

        self.gridLayout_2.addWidget(self.chunkSizeCheckBox, 7, 1, 1, 1)

        self.autocontrastBox = QCheckBox(self.optionWidget)
        self.autocontrastBox.setObjectName(u"autocontrastBox")
        self.autocontrastBox.setTristate(True)

        self.gridLayout_2.addWidget(self.autocontrastBox, 9, 2, 1, 1)

        self.webpBox = QCheckBox(self.optionWidget)
        self.webpBox.setObjectName(u"webpBox")

        self.gridLayout_2.addWidget(self.webpBox, 12, 0, 1, 1)

        self.tempDirBox = QCheckBox(self.optionWidget)
        self.tempDirBox.setObjectName(u"tempDirBox")

        self.gridLayout_2.addWidget(self.tempDirBox, 12, 1, 1, 1)


        self.gridLayout.addWidget(self.optionWidget, 5, 0, 1, 2)

        self.buttonWidget = QWidget(self.centralWidget)
        self.buttonWidget.setObjectName(u"buttonWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy4)
        self.gridLayout_4 = QGridLayout(self.buttonWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.convertButton = QPushButton(self.buttonWidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setMinimumSize(QSize(0, 30))
        self.convertButton.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/Other/icons/convert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convertButton.setIcon(icon6)

        self.gridLayout_4.addWidget(self.convertButton, 1, 3, 1, 1)

        self.clearButton = QPushButton(self.buttonWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 30))
        icon7 = QIcon()
        icon7.addFile(u":/Other/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearButton.setIcon(icon7)

        self.gridLayout_4.addWidget(self.clearButton, 0, 3, 1, 1)

        self.deviceBox = QComboBox(self.buttonWidget)
        self.deviceBox.setObjectName(u"deviceBox")
        self.deviceBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.deviceBox, 1, 1, 1, 1)

        self.fileButton = QPushButton(self.buttonWidget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setMinimumSize(QSize(0, 30))
        icon8 = QIcon()
        icon8.addFile(u":/Other/icons/document_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileButton.setIcon(icon8)

        self.gridLayout_4.addWidget(self.fileButton, 0, 1, 1, 1)

        self.directoryButton = QPushButton(self.buttonWidget)
        self.directoryButton.setObjectName(u"directoryButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.directoryButton.sizePolicy().hasHeightForWidth())
        self.directoryButton.setSizePolicy(sizePolicy5)
        self.directoryButton.setIcon(icon5)

        self.gridLayout_4.addWidget(self.directoryButton, 0, 4, 1, 1)

        self.formatBox = QComboBox(self.buttonWidget)
        self.formatBox.setObjectName(u"formatBox")
        self.formatBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.formatBox, 1, 4, 1, 1)

        self.clearButton.raise_()
        self.deviceBox.raise_()
        self.convertButton.raise_()
        self.fileButton.raise_()
        self.directoryButton.raise_()
        self.formatBox.raise_()

        self.gridLayout.addWidget(self.buttonWidget, 3, 0, 1, 2)

        self.gammaWidget = QWidget(self.centralWidget)
        self.gammaWidget.setObjectName(u"gammaWidget")
        self.gammaWidget.setVisible(False)
        self.horizontalLayout_2 = QHBoxLayout(self.gammaWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gammaLabel = QLabel(self.gammaWidget)
        self.gammaLabel.setObjectName(u"gammaLabel")

        self.horizontalLayout_2.addWidget(self.gammaLabel)

        self.gammaSlider = QSlider(self.gammaWidget)
        self.gammaSlider.setObjectName(u"gammaSlider")
        self.gammaSlider.setMaximum(250)
        self.gammaSlider.setSingleStep(5)
        self.gammaSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.gammaSlider)


        self.gridLayout.addWidget(self.gammaWidget, 7, 0, 1, 2)

        self.customWidget = QWidget(self.centralWidget)
        self.customWidget.setObjectName(u"customWidget")
        self.customWidget.setVisible(False)
        self.gridLayout_3 = QGridLayout(self.customWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hLabel = QLabel(self.customWidget)
        self.hLabel.setObjectName(u"hLabel")
        sizePolicy1.setHeightForWidth(self.hLabel.sizePolicy().hasHeightForWidth())
        self.hLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.hLabel, 0, 2, 1, 1)

        self.widthBox = QSpinBox(self.customWidget)
        self.widthBox.setObjectName(u"widthBox")
        self.widthBox.setMaximum(6000)

        self.gridLayout_3.addWidget(self.widthBox, 0, 1, 1, 1)

        self.wLabel = QLabel(self.customWidget)
        self.wLabel.setObjectName(u"wLabel")
        sizePolicy1.setHeightForWidth(self.wLabel.sizePolicy().hasHeightForWidth())
        self.wLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.wLabel, 0, 0, 1, 1)

        self.heightBox = QSpinBox(self.customWidget)
        self.heightBox.setObjectName(u"heightBox")
        self.heightBox.setMaximum(8000)

        self.gridLayout_3.addWidget(self.heightBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.customWidget, 8, 0, 1, 2)

        mainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        mainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.jobList, self.fileButton)
        QWidget.setTabOrder(self.fileButton, self.clearButton)
        QWidget.setTabOrder(self.clearButton, self.deviceBox)
        QWidget.setTabOrder(self.deviceBox, self.widthBox)
        QWidget.setTabOrder(self.widthBox, self.heightBox)
        QWidget.setTabOrder(self.heightBox, self.convertButton)
        QWidget.setTabOrder(self.convertButton, self.mangaBox)
        QWidget.setTabOrder(self.mangaBox, self.rotateBox)
        QWidget.setTabOrder(self.rotateBox, self.qualityBox)
        QWidget.setTabOrder(self.qualityBox, self.webtoonBox)
        QWidget.setTabOrder(self.webtoonBox, self.upscaleBox)
        QWidget.setTabOrder(self.upscaleBox, self.gammaBox)
        QWidget.setTabOrder(self.gammaBox, self.gammaSlider)
        QWidget.setTabOrder(self.gammaSlider, self.borderBox)
        QWidget.setTabOrder(self.borderBox, self.outputSplit)
        QWidget.setTabOrder(self.outputSplit, self.colorBox)
        QWidget.setTabOrder(self.colorBox, self.mozJpegBox)
        QWidget.setTabOrder(self.mozJpegBox, self.maximizeStrips)
        QWidget.setTabOrder(self.maximizeStrips, self.croppingBox)
        QWidget.setTabOrder(self.croppingBox, self.croppingPowerSlider)
        QWidget.setTabOrder(self.croppingPowerSlider, self.preserveMarginBox)
        QWidget.setTabOrder(self.preserveMarginBox, self.spreadShiftBox)
        QWidget.setTabOrder(self.spreadShiftBox, self.deleteBox)
        QWidget.setTabOrder(self.deleteBox, self.disableProcessingBox)
        QWidget.setTabOrder(self.disableProcessingBox, self.fileFusionBox)
        QWidget.setTabOrder(self.fileFusionBox, self.noRotateBox)
        QWidget.setTabOrder(self.noRotateBox, self.interPanelCropBox)
        QWidget.setTabOrder(self.interPanelCropBox, self.metadataTitleBox)
        QWidget.setTabOrder(self.metadataTitleBox, self.coverFillBox)
        QWidget.setTabOrder(self.coverFillBox, self.chunkSizeCheckBox)
        QWidget.setTabOrder(self.chunkSizeCheckBox, self.chunkSizeBox)
        QWidget.setTabOrder(self.chunkSizeBox, self.eraseRainbowBox)
        QWidget.setTabOrder(self.eraseRainbowBox, self.rotateFirstBox)
        QWidget.setTabOrder(self.rotateFirstBox, self.autoLevelBox)
        QWidget.setTabOrder(self.autoLevelBox, self.autocontrastBox)
        QWidget.setTabOrder(self.autocontrastBox, self.editorButton)
        QWidget.setTabOrder(self.editorButton, self.kofiButton)
        QWidget.setTabOrder(self.kofiButton, self.wikiButton)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Kindle Comic Converter", None))
#if QT_CONFIG(tooltip)
        self.preserveMarginLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u8ba1\u7b97\u526a\u5207\u8fb9\u754c\u540e\uff0c\u5411\u540e\u4fdd\u7559\u6307\u5b9a\u767e\u5206\u6bd4\u7684\u8fb9\u8ddd\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preserveMarginLabel.setText(QCoreApplication.translate("mainWindow", u"\u4fdd\u7559\u8fb9\u8ddd%", None))
        self.croppingPowerLabel.setText(QCoreApplication.translate("mainWindow", u"\u526a\u5207\u5f3a\u5ea6:", None))
        self.jpegQualityLabel.setText(QCoreApplication.translate("mainWindow", u"JPEG\u8d28\u91cf:", None))
#if QT_CONFIG(tooltip)
        self.chunkSizeWidget.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u8b66\u544a\uff1a\u5206\u5757\u5927\u5c0f\u5927\u4e8e\u9ed8\u8ba4\u503c\u53ef\u80fd\u5bfc\u81f4<br/>\u6027\u80fd/\u7535\u6c60\u95ee\u9898\uff0c\u7279\u522b\u662f\u5728\u65e7\u8bbe\u5907\u4e0a\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chunkSizeLabel.setText(QCoreApplication.translate("mainWindow", u"\u5206\u5757\u5927\u5c0fMB:", None))
        self.chunkSizeWarnLabel.setText(QCoreApplication.translate("mainWindow", u"\u5927\u4e8e\u9ed8\u8ba4\u503c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u65e7\u7535\u5b50\u4e66\u8bbe\u5907\u51fa\u73b0\u6027\u80fd\u95ee\u9898\u3002", None))
#if QT_CONFIG(tooltip)
        self.jobList.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u53cc\u51fb\u6e90\u6587\u4ef6\u5728\u5143\u6570\u636e\u7f16\u8f91\u5668\u4e2d\u6253\u5f00\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.editorButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Shift+\u70b9\u51fb\u7f16\u8f91\u76ee\u5f55\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.editorButton.setText(QCoreApplication.translate("mainWindow", u"\u5143\u6570\u636e\u7f16\u8f91\u5668", None))
        self.kofiButton.setText(QCoreApplication.translate("mainWindow", u"\u5728Ko-fi\u4e0a\u652f\u6301\u6211\u4eec", None))
        self.wikiButton.setText(QCoreApplication.translate("mainWindow", u"\u7ef4\u57fa", None))
        self.youtubeButton.setText(QCoreApplication.translate("mainWindow", u"YouTube", None))
        self.humbleBundleButton.setText(QCoreApplication.translate("mainWindow", u"Humble Bundle\u63a8\u5e7f", None))
        self.discordButton.setText(QCoreApplication.translate("mainWindow", u"Discord", None))
#if QT_CONFIG(tooltip)
        self.noRotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5728\u8de8\u9875\u62c6\u5206\u9009\u9879\u4e2d\u4e0d\u65cb\u8f6c\u8de8\u9875\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.noRotateBox.setText(QCoreApplication.translate("mainWindow", u"\u4e0d\u65cb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.maximizeStrips.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - 1x4<br/></span>\u4fdd\u63011x4\u7684\u5206\u680f\u6761\u683c\u5f0f\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - 2x2<br/></span>\u5c061x4\u6761\u8f6c\u5316\u4e3a2x2\u4ee5\u6700\u5927\u5316\u5c4f\u5e55\u4f7f\u7528\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeStrips.setText(QCoreApplication.translate("mainWindow", u"1x4\u8f6c2x2\u6761", None))
#if QT_CONFIG(tooltip)
        self.rotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u62c6\u5206<br/></span>\u8de8\u9875\u5c06\u88ab\u5207\u5206\u4e3a\u4e24\u4e2a\u5355\u72ec\u7684\u9875\u9762\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u62c6\u5206\u548c\u65cb\u8f6c<br/></span>\u8de8\u9875\u5c06\u663e\u793a\u4e24\u6b21\u3002\u5148\u62c6\u5206\u518d\u65cb\u8f6c\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u65cb\u8f6c<br/></span>\u8de8\u9875\u5c06\u88ab\u65cb\u8f6c\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateBox.setText(QCoreApplication.translate("mainWindow", u"\u8de8\u9875\u62c6\u5206", None))
#if QT_CONFIG(tooltip)
        self.pngLegacyBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u4f7f\u7528\u517c\u5bb9\u6027\u66f4\u597d\u76848\u4f4dPNG\u800c\u4e0d\u662f4\u4f4d\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.pngLegacyBox.setText(QCoreApplication.translate("mainWindow", u"PNG\u4f20\u7edf\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.interPanelCropBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u7981\u7528<br/></span>\u7981\u7528</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u6c34\u5e73<br/></span>\u526a\u5207\u7a7a\u767d\u7684\u6c34\u5e73\u7ebf\u6761\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u5168\u90e8<br/></span>\u526a\u5207\u7a7a\u767d\u7684\u6c34\u5e73\u548c\u5782\u76f4\u7ebf\u6761\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.interPanelCropBox.setText(QCoreApplication.translate("mainWindow", u"\u5206\u5c4f\u95f4\u526a\u5207", None))
#if QT_CONFIG(tooltip)
        self.titleEdit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u9ed8\u8ba4\u6807\u9898</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u9ed8\u8ba4\u6807\u9898", None))
#if QT_CONFIG(tooltip)
        self.authorEdit.setToolTip(QCoreApplication.translate("mainWindow", u"\u9ed8\u8ba4\u4f5c\u8005\u662fKCC", None))
#endif // QT_CONFIG(tooltip)
        self.authorEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u9ed8\u8ba4\u4f5c\u8005", None))
#if QT_CONFIG(tooltip)
        self.webtoonBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u542f\u7528\u97e9\u56fd\u6761\u6f2b\u7279\u6b8a\u89e3\u6790\u6a21\u5f0f\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.webtoonBox.setText(QCoreApplication.translate("mainWindow", u"\u6761\u6f2b\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.fileFusionBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u5c06\u6240\u6709\u9009\u4e2d\u7684\u6587\u4ef6\u5408\u5e76\u4e3a\u4e00\u4e2a\u6587\u4ef6\u3002\uff08\u6709\u52a9\u4e8e\u5c06\u7ae0\u8282\u5408\u5e76\u4e3a\u5377\u3002\uff09</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileFusionBox.setText(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6\u5408\u5e76", None))
#if QT_CONFIG(tooltip)
        self.deleteBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u8f93\u5165\u6587\u4ef6\u6216\u76ee\u5f55\u3002\u4e0d\u53ef\u6062\u590d\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBox.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u8f93\u5165", None))
#if QT_CONFIG(tooltip)
        self.gammaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u8bbe\u7f6e\u81ea\u5b9a\u4e49\u4f3d\u9a6c\u6821\u6b63\u3002</p><p>1.0\u4e3a\u9ed8\u8ba4\uff08\u7981\u7528\uff09\u3002<br/>&lt; 1.0\u4f7f\u56fe\u50cf\u66f4\u4eae\u3002<br/>&gt; 1.0\u4f7f\u56fe\u50cf\u66f4\u6697\u3002</p><p>1.8\u662fKCC 9.1.0\u53ca\u66f4\u65e9\u7248\u672c\u7684\u9ed8\u8ba4\u503c\u3002</p><p>\u5f53\u6587\u672c\u662f\u9ed1\u8272\u4f46\u56fe\u7247\u662f\u7070\u8272\u65f6\uff0c\u4f7f\u7528\u6781\u7aef\u9ed1\u573a\u4f1a\u6709\u6240\u5e2e\u52a9\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gammaBox.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49\u4f3d\u9a6c", None))
#if QT_CONFIG(tooltip)
        self.noQuantizeBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u4e0d\u5c06PNG\u56fe\u50cf\u91cf\u5316\u4e3a16\u8272\uff084\u4f4d\uff09\u3002\n"
"\n"
"\u8fd9\u4f1a\u4f7f\u6587\u4ef6\u5927\u5c0f\u7ffb\u500d\uff0c\u4f46\u4f1a\u4fdd\u7559\u5168\u90e8256\u8272\uff088\u4f4d\uff09\u3002\n"
"\n"
"\u7535\u5b50\u58a8\u6c34\u5c4f\u53ea\u670916\u7ea7\u7070\u5ea6\uff0c\u6240\u4ee5\u60a8\u53ef\u80fd\u4e0d\u9700\u8981\u8fd9\u4e2a\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.noQuantizeBox.setText(QCoreApplication.translate("mainWindow", u"\u4e0d\u91cf\u5316", None))
#if QT_CONFIG(tooltip)
        self.eraseRainbowBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u901a\u8fc7\u8870\u51cf\u5e72\u6270\u9891\u7387\u6765\u6d88\u9664\u5f69\u8272\u7535\u5b50\u58a8\u6c34\u5c4f\u5e55\u4e0a\u7684\u5f69\u8679\u6548\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.eraseRainbowBox.setText(QCoreApplication.translate("mainWindow", u"\u5f69\u8679\u6d88\u9664", None))
#if QT_CONFIG(tooltip)
        self.coverFillBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u901a\u8fc7\u5148\u5c45\u4e2d\u548c\u88c1\u526a\u5230\u5bbd\u9ad8\u6bd4\uff0c\u5c06\u5c01\u9762\u8c03\u6574\u5230\u786e\u5207\u7684\u8bbe\u5907\u5206\u8fa8\u7387\u3002\u6839\u636e\u6e90\u5bbd\u9ad8\u6bd4\u53ef\u80fd\u4f1a\u88c1\u526a\u9876\u90e8/\u5e95\u90e8\u6216\u5de6\u4fa7/\u53f3\u4fa7\u3002Kindle Scribe\u672a\u5b9e\u73b0\u6b64\u529f\u80fd\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.coverFillBox.setText(QCoreApplication.translate("mainWindow", u"\u5c01\u9762\u586b\u5145", None))
#if QT_CONFIG(tooltip)
        self.rotateRightBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u4ee5\u4e0e\u6b63\u5e38\u76f8\u53cd\u7684\u65b9\u5411\u65cb\u8f6c\u4e24\u9875\u8de8\u9875\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.rotateRightBox.setText(QCoreApplication.translate("mainWindow", u"\u5411\u53f3\u65cb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.mangaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u542f\u7528\u4ece\u53f3\u5230\u5de6\u9605\u8bfb\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mangaBox.setText(QCoreApplication.translate("mainWindow", u"\u4ece\u53f3\u5230\u5de6\uff08\u6f2b\u753b\uff09", None))
#if QT_CONFIG(tooltip)
        self.spreadShiftBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5728\u6a2a\u5c4f\u4e2d\u5c06\u7b2c\u4e00\u9875\u79fb\u5230\u53e6\u4e00\u4fa7\uff0c\u4ee5\u5b9e\u73b0\u4e24\u9875\u8de8\u9875\u5bf9\u9f50", None))
#endif // QT_CONFIG(tooltip)
        self.spreadShiftBox.setText(QCoreApplication.translate("mainWindow", u"\u8de8\u9875\u79fb\u4f4d", None))
#if QT_CONFIG(tooltip)
        self.croppingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u7981\u7528</span></p><p>\u7981\u7528</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u8fb9\u8ddd<br/></span>\u8fb9\u8ddd</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u8fb9\u8ddd+\u9875\u7801<br/></span>\u8fb9\u8ddd+\u9875\u7801</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.croppingBox.setText(QCoreApplication.translate("mainWindow", u"\u526a\u5207\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.jpegQualityBox.setToolTip(QCoreApplication.translate("mainWindow", u"JPEG\u8d28\u91cf\uff0c\u8303\u56f4\u4ece0\uff08\u6700\u5dee\uff09\u523095\uff08\u6700\u4f73\uff09\u3002\n"
"\n"
"\u9ed8\u8ba4\u5927\u591a\u6570\u8bbe\u5907\u4e3a85\uff0c\u4f46Kindle Scribe\u548cColorsoft\u8bbe\u5907\u4e3a90\u3002\n"
"\n"
"\u66f4\u9ad8\u7684\u503c\u66f4\u5927\u4e14\u8d28\u91cf\u66f4\u9ad8\uff0c\u5e76\u53ef\u80fd\u89e3\u51b3\u7a7a\u767d\u9875\u95ee\u9898\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.jpegQualityBox.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49JPEG\u8d28\u91cf", None))
#if QT_CONFIG(tooltip)
        self.outputSplit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u81ea\u52a8\u6a21\u5f0f<br/></span>\u8f93\u51fa\u5c06\u81ea\u52a8\u5206\u5272\u3002</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u5206\u5377\u6a21\u5f0f<br/></span>\u6bcf\u4e2a\u5b50\u76ee\u5f55\u5c06\u88ab\u89c6\u4e3a\u5355\u72ec\u7684\u5377\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.outputSplit.setText(QCoreApplication.translate("mainWindow", u"\u8f93\u51fa\u5206\u5272", None))
#if QT_CONFIG(tooltip)
        self.metadataTitleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u4e0d\u4f7f\u7528\u5143\u6570\u636e\u6807\u9898<br/></span>\u7f16\u5199\u9ed8\u8ba4\u6807\u9898\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u5c06\u5143\u6570\u636e\u6807\u9898\u6dfb\u52a0\u5230\u9ed8\u8ba4\u683c\u5f0f<br/></span>\u7528\u6765\u81eaComicInfo.xml\u6216\u5176\u4ed6\u5d4c\u5165\u5143\u6570\u636e\u7684\u6807\u9898\u7f16\u5199\u9ed8\u8ba4\u6807\u9898\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u4ec5\u4f7f\u7528\u5143\u6570\u636e\u6807\u9898<br/></span>\u4ec5\u4f7f\u7528\u6765\u81eaComicInfo.xml\u6216\u5176\u4ed6\u5d4c\u5165\u5143\u6570\u636e\u7684\u6807\u9898\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.metadataTitleBox.setText(QCoreApplication.translate("mainWindow", u"\u5143\u6570\u636e\u6807\u9898", None))
#if QT_CONFIG(tooltip)
        self.noSmartCoverCropBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u7981\u7528\u5c1d\u8bd5\u4ece\u5bbd\u5e45\u56fe\u50cf\u4e2d\u88c1\u526a\u4e3b\u5c01\u9762\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.noSmartCoverCropBox.setText(QCoreApplication.translate("mainWindow", u"\u7981\u7528\u667a\u80fd\u5c01\u9762\u88c1\u526a", None))
#if QT_CONFIG(tooltip)
        self.rotateFirstBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u5f53\u8de8\u9875\u62c6\u5206\u9009\u9879\u88ab\u90e8\u5206\u52fe\u9009\u65f6\uff0c</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u6700\u540e\u65cb\u8f6c<br/></span>\u5c06\u65cb\u8f6c\u540e\u7684\u4e24\u9875\u8de8\u9875\u653e\u5728\u62c6\u5206\u9875\u9762\u4e4b\u540e\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u5148\u65cb\u8f6c<br/></span>\u5c06\u65cb\u8f6c\u540e\u7684\u4e24\u9875\u8de8\u9875\u653e\u5728\u62c6\u5206\u9875\u9762\u4e4b\u524d\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateFirstBox.setText(QCoreApplication.translate("mainWindow", u"\u5148\u65cb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.mozJpegBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - JPEG<br/></span>\u4f7f\u7528JPEG\u6587\u4ef6</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u5f3a\u5236PNG<br/></span>\u4e3a\u9ed1\u767d\u56fe\u50cf\u521b\u5efaPNG\u6587\u4ef6\u800c\u4e0d\u662fJPEG</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - mozJpeg<br/></span>\u6587\u4ef6\u66f4\u5c0f10-20%\uff0c\u56fe\u50cf\u8d28\u91cf\u76f8\u540c\uff0c\u4f46\u5904\u7406\u65f6\u95f4\u7ffb\u500d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mozJpegBox.setText(QCoreApplication.translate("mainWindow", u"JPEG/PNG/mozJpeg", None))
#if QT_CONFIG(tooltip)
        self.autoLevelBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u9ed8\u8ba4\u60c5\u51b5\u4e0b\uff0cKCC\u5c06\u6700\u6697\u50cf\u7d20\u503c\u6620\u5c04\u4e3a\u7eaf\u9ed1\uff08\u9ed1\u573a\uff09\u3002</p><p>\u6781\u7aef\u9ed1\u573a\u5c06\u9ed1\u573a\u8bbe\u7f6e\u4e3a\u6700\u5e38\u89c1\u7684\u6697\u50cf\u7d20\u503c\u3002</p><p>\u5f53\u6587\u672c\u662f\u9ed1\u8272\u4f46\u56fe\u7247\u662f\u7070\u8272\u65f6\u5f88\u6709\u7528\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autoLevelBox.setText(QCoreApplication.translate("mainWindow", u"\u6781\u7aef\u9ed1\u573a", None))
#if QT_CONFIG(tooltip)
        self.forcePngRgbBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5f3a\u5236\u5168\u5f69\u8272\u56fe\u50cf\u4ee5\u65e0\u635fPNG\u683c\u5f0f\u4fdd\u5b58\uff0c\u5927\u5e45\u589e\u52a0\u6587\u4ef6\u5927\u5c0f\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.forcePngRgbBox.setText(QCoreApplication.translate("mainWindow", u"\u5f3a\u5236PNG RGB", None))
#if QT_CONFIG(tooltip)
        self.upscaleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u65e0<br/></span>\u5c0f\u4e8e\u8bbe\u5907\u5206\u8fa8\u7387\u7684\u56fe\u50cf\u5c06\u4e0d\u4f1a\u8c03\u6574\u5927\u5c0f\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u62c9\u4f38<br/></span>\u5c0f\u4e8e\u8bbe\u5907\u5206\u8fa8\u7387\u7684\u56fe\u50cf\u5c06\u88ab\u8c03\u6574\u5927\u5c0f\u3002\u5bbd\u9ad8\u6bd4\u5c06\u4e0d\u4f1a\u4fdd\u7559\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u653e\u5927<br/></span>\u5c0f\u4e8e\u8bbe\u5907\u5206\u8fa8\u7387\u7684\u56fe\u50cf\u5c06\u88ab\u8c03\u6574\u5927\u5c0f\u3002\u5bbd\u9ad8\u6bd4\u5c06\u88ab\u4fdd\u7559\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.upscaleBox.setText(QCoreApplication.translate("mainWindow", u"\u62c9\u4f38/\u653e\u5927", None))
#if QT_CONFIG(tooltip)
        self.borderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u81ea\u52a8\u68c0\u6d4b<br/></span>\u8fb9\u8ddd\u586b\u5145\u989c\u8272\u5c06\u81ea\u52a8\u68c0\u6d4b\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u767d\u8272<br/></span>\u8fb9\u8ddd\u5c06\u4e0d\u4f1a\u88ab\u89e6\u78b0\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u9ed1\u8272<br/></span>\u8fb9\u8ddd\u5c06\u7528\u9ed1\u8272\u586b\u5145\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.borderBox.setText(QCoreApplication.translate("mainWindow", u"\u767d/\u9ed1\u8fb9\u8ddd", None))
#if QT_CONFIG(tooltip)
        self.qualityBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - 4\u4e2a\u5206\u5c4f<br/></span>\u5206\u522b\u653e\u5927\u6bcf\u4e2a\u89d2\u843d\u3002</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - 2\u4e2a\u5206\u5c4f<br/></span>\u4ec5\u653e\u5927\u9875\u9762\u9876\u90e8\u548c\u5e95\u90e8\u3002</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - 4\u4e2a\u9ad8\u8d28\u91cf\u5206\u5c4f<br/></span>\u5206\u522b\u653e\u5927\u6bcf\u4e2a\u89d2\u843d\u3002\u5c1d\u8bd5\u63d0\u9ad8\u653e\u5927\u8d28\u91cf\u3002\u67e5\u770b\u7ef4\u57fa\u4e86\u89e3\u66f4\u591a\u8be6\u60c5\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.qualityBox.setText(QCoreApplication.translate("mainWindow", u"\u5206\u5c4f\u89c6\u56fe 4/2/\u9ad8\u8d28\u91cf", None))
#if QT_CONFIG(tooltip)
        self.pdfExtractBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u4f7f\u7528KCC 8\u53ca\u66f4\u65e9\u7248\u672c\u4e2d\u7684PDF\u56fe\u50cf\u63d0\u53d6\u65b9\u6cd5\u3002\n"
"\n"
"\u5bf9\u4e8e\u975e\u5e38\u5947\u602a\u7684PDF\u5f88\u6709\u7528\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.pdfExtractBox.setText(QCoreApplication.translate("mainWindow", u"PDF\u4f20\u7edf\u63d0\u53d6", None))
#if QT_CONFIG(tooltip)
        self.colorBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u7981\u7528\u8f6c\u6362\u4e3a\u7070\u5ea6\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.colorBox.setText(QCoreApplication.translate("mainWindow", u"\u5f69\u8272\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.pdfWidthBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5c06\u77e2\u91cfPDF\u6e32\u67d3\u5230\u8bbe\u5907\u5bbd\u5ea6\u800c\u4e0d\u662f\u9ad8\u5ea6\u3002\n"
"\n"
"\u5982\u679c\u60a8\u8ba1\u5212\u88c1\u526a\u9876\u90e8\u548c\u5e95\u90e8\u7684\u4e00\u70b9\u4ee5\u586b\u5145\u5c4f\u5e55\uff0c\u8fd9\u4f1a\u5f88\u6709\u7528\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.pdfWidthBox.setText(QCoreApplication.translate("mainWindow", u"PDF\u5bbd\u5ea6\u6e32\u67d3", None))
#if QT_CONFIG(tooltip)
        self.disableProcessingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u4e0d\u5904\u7406\u4efb\u4f55\u56fe\u50cf\uff0c\u5ffd\u7565\u914d\u7f6e\u6587\u4ef6\u548c\u5904\u7406\u9009\u9879\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.disableProcessingBox.setText(QCoreApplication.translate("mainWindow", u"\u7981\u7528\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.defaultOutputFolderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u6e90\u6587\u4ef6\u65c1\u8fb9<br/></span>\u5c06\u8f93\u51fa\u6587\u4ef6\u653e\u5728\u6e90\u6587\u4ef6\u65c1\u8fb9</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u6e90\u6587\u4ef6\u65c1\u8fb9\u7684\u6587\u4ef6\u5939<br/></span>\u5c06\u8f93\u51fa\u6587\u4ef6\u653e\u5728\u6e90\u6587\u4ef6\u65c1\u8fb9\u7684\u6587\u4ef6\u5939\u4e2d</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u81ea\u5b9a\u4e49<br/></span>\u5c06\u8f93\u51fa\u6587\u4ef6\u653e\u5728\u53f3\u4fa7\u6309\u94ae\u6307\u5b9a\u7684\u81ea\u5b9a\u4e49\u76ee\u5f55\u4e2d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultOutputFolderBox.setText(QCoreApplication.translate("mainWindow", u"\u8f93\u51fa\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.defaultOutputFolderButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u4f7f\u7528\u6b64\u6309\u94ae\u9009\u62e9\u9ed8\u8ba4\u8f93\u51fa\u76ee\u5f55\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultOutputFolderButton.setText("")
#if QT_CONFIG(tooltip)
        self.chunkSizeCheckBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">\u672a\u52fe\u9009<br/></span>\u6761\u6f2b\u7684\u6700\u5927\u8f93\u51fa\u6587\u4ef6\u5927\u5c0f\u4e3a100MB\uff0c\u5176\u4ed6\u60c5\u51b5\u5728\u62c6\u5206\u53d1\u751f\u524d\u4e3a400MB\u3002</p><p><span style=\" font-weight:700; text-decoration: underline;\">\u5df2\u52fe\u9009</span><br/><p><span style=\"font-weight:600; text-decoration: underline;\"></span>\u5728\"\u5206\u5757\u5927\u5c0fMB\"\u4e2d\u6307\u5b9a\u8f93\u51fa\u6587\u4ef6\u5927\u5c0f\uff0c\u7136\u540e\u53d1\u751f\u62c6\u5206\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chunkSizeCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u5206\u5757\u5927\u5c0f", None))
#if QT_CONFIG(tooltip)
        self.autocontrastBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u4ec5\u9ed1\u767d<br/></span>\u4ec5\u5bf9\u9ed1\u767d\u9875\u9762\u81ea\u52a8\u5bf9\u6bd4\u5ea6\u3002\u5bf9\u4e8e\u6ca1\u6709\u63a5\u8fd1\u9ed1\u767d\u7684\u9875\u9762\u5c06\u88ab\u5ffd\u7565\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u90e8\u5206\u52fe\u9009 - \u7981\u7528<br/></span>\u7981\u7528\u81ea\u52a8\u5bf9\u6bd4\u5ea6</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u9ed1\u767d\u548c\u5f69\u8272<br/></span>\u9ed1\u767d\u548c\u5f69\u8272\u56fe\u50cf\u5c06\u81ea\u52a8\u5bf9\u6bd4\u5ea6\u3002\u5bf9\u4e8e\u6ca1\u6709\u63a5\u8fd1\u9ed1\u767d\u7684\u9875\u9762\u5c06\u88ab\u5ffd\u7565\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autocontrastBox.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u52a8\u5bf9\u6bd4\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.webpBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u7528\u6709\u635fWebP\u66ff\u6362JPEG\uff0c\u7528\u65e0\u635fWebP\u66ff\u6362PNG\u3002\u8fd9\u5305\u62ecJPEG\u8d28\u91cf\u3002\n"
"\n"
"\u5bf9\u4e8eKindle EPUB/MOBI\u548c\u6240\u6709PDF\u683c\u5f0f\u5c06\u88ab\u5ffd\u7565\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.webpBox.setText(QCoreApplication.translate("mainWindow", u"WebP\uff08\u5b9e\u9a8c\u6027\uff09", None))
#if QT_CONFIG(tooltip)
        self.tempDirBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u52fe\u9009 - \u4e3b\u9a71\u52a8\u5668<br/></span>\u5728\u4e3b\u64cd\u4f5c\u7cfb\u7edf\u9a71\u52a8\u5668\u4e0a\u4f7f\u7528\u4e13\u7528\u4e34\u65f6\u76ee\u5f55\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u5df2\u52fe\u9009 - \u6e90\u6587\u4ef6\u9a71\u52a8\u5668<br/></span>\u5728\u6e90\u6587\u4ef6\u9a71\u52a8\u5668\u4e0a\u521b\u5efa\u4e34\u65f6\u6587\u4ef6\u76ee\u5f55\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tempDirBox.setText(QCoreApplication.translate("mainWindow", u"\u4e34\u65f6\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.convertButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Shift+\u70b9\u51fb\u9009\u62e9\u6b64\u5217\u8868\u7684\u8f93\u51fa\u76ee\u5f55\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.convertButton.setText(QCoreApplication.translate("mainWindow", u"\u8f6c\u6362", None))
        self.clearButton.setText(QCoreApplication.translate("mainWindow", u"\u6e05\u7a7a\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.deviceBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u76ee\u6807\u8bbe\u5907\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fileButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u5c06CBR\u3001CBZ\u3001CB7\u6216PDF\u6587\u4ef6\u6dfb\u52a0\u5230\u961f\u5217\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileButton.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u8f93\u5165\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.directoryButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u5c06\u5305\u542bJPG\u3001PNG\u6216GIF\u6587\u4ef6\u7684\u76ee\u5f55\u6dfb\u52a0\u5230\u961f\u5217\u3002<br/><span style=\" font-weight:600;\">\u5185\u90e8\u7684CBR\u3001CBZ\u548cCB7\u6587\u4ef6\u4e0d\u4f1a\u88ab\u5904\u7406\uff01</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.directoryButton.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u8f93\u5165\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.formatBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u8f93\u51fa\u683c\u5f0f\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gammaLabel.setText(QCoreApplication.translate("mainWindow", u"\u4f3d\u9a6c\u503c\uff1a\u81ea\u52a8", None))
#if QT_CONFIG(tooltip)
        self.hLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u76ee\u6807\u8bbe\u5907\u7684\u5206\u8fa8\u7387\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hLabel.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49\u9ad8\u5ea6:", None))
#if QT_CONFIG(tooltip)
        self.widthBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u76ee\u6807\u8bbe\u5907\u7684\u5206\u8fa8\u7387\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u76ee\u6807\u8bbe\u5907\u7684\u5206\u8fa8\u7387\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wLabel.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49\u5bbd\u5ea6:", None))
#if QT_CONFIG(tooltip)
        self.heightBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u76ee\u6807\u8bbe\u5907\u7684\u5206\u8fa8\u7387\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


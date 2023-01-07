from spark.widget.import_module import *



class COMMON_PROPERTY:
    def __init__(self):
        self.size_policy_list = [QSizePolicy.Fixed, QSizePolicy.Minimum, QSizePolicy.Maximum, QSizePolicy.Preferred, QSizePolicy.MinimumExpanding, QSizePolicy.Expanding, QSizePolicy.Ignored]
        self.antialize = [QFont.PreferDefault, QFont.NoAntialias, QFont.PreferAntialias]
        self.cursor = [Qt.ArrowCursor, Qt.UpArrow, Qt.CrossCursor, Qt.WaitCursor, Qt.IBeamCursor, Qt.SizeVerCursor, Qt.SizeHorCursor, Qt.SizeBDiagCursor, Qt.SizeAllCursor]
        self.focus = [Qt.NoFocus, Qt.TabFocus, Qt.ClickFocus, Qt.StrongFocus, Qt.WheelFocus]
        self.contexMenuPolicy = [Qt.NoContextMenu, Qt.DefaultContextMenu, Qt.ActionsContextMenu, Qt.CustomContextMenu, Qt.PreventContextMenu]
        self.layoutDirection = [Qt.LeftToRight, Qt.RightToLeft, Qt.LayoutDirectionAuto]
        self.inputMethodHint = [Qt.ImhHiddenText, Qt.ImhSensitiveData, Qt.ImhNoAutoUppercase, Qt.ImhPreferNumbers, Qt.ImhSensitiveData,
                                Qt.ImhNoAutoUppercase, Qt.ImhPreferNumbers, Qt.ImhPreferUppercase, Qt.ImhPreferLowercase, Qt.ImhNoPredictiveText,
                                Qt.ImhDate, Qt.ImhTime, Qt.ImhPreferLatin, Qt.ImhMultiLine,
                                Qt.ImhDigitsOnly, Qt.ImhFormattedNumbersOnly, Qt.ImhUppercaseOnly, Qt.ImhLowercaseOnly, Qt.ImhDialableCharactersOnly, Qt.ImhEmailCharactersOnly,
                                Qt.ImhUrlCharactersOnly, Qt.ImhLatinOnly, Qt.ImhExclusiveInputMask]

        self.layoutSizeConstraint = [QLayout.SetDefaultConstraint, QLayout.SetNoConstraint, QLayout.SetMinimumSize, QLayout.SetFixedSize,
                                     QLayout.SetMaximumSize, QLayout.SetMinAndMaxSize]

        self.sizetype = [QSizePolicy.Fixed, QSizePolicy.Minimum, QSizePolicy.Maximum, QSizePolicy.Preferred, QSizePolicy.MinimumExpanding,
                         QSizePolicy.Expanding, QSizePolicy.Ignored]



    def common_property(self, object, setObjectName='', enable=True, setGeometry_x= 0, setGeometry_y= 0, setGeometry_width= 100, setGeometry_height= 100,
                        setSizePolicy_horizontal=3, setSizePolicy_vertical=3, setSizePolicy_horizontal_stretch=0, setSizePolicy_vertical_stretch=0,
                        setMinimumSize_width=0, setMinimumSize_height=0, setMaximumSize_width=16777215, setMaximumSize_height=16777215,
                        setSizeIncrement_width=0, setSizeIncrement_height=0, setBaseSize_width=0, setBaseSize_height=0,
                        setFamily='', setPointSize=8, setBold=False, setItalic=False,
                        setUnderline=False, setStrikeOut=False, setKerning=True, setAntialias=0,
                        setCursor=0, setMouseTracking=False, setTabletTracking=False, setFocusPolicy=2,
                        setContextMenuPolicy=3, setAcceptDrops=False, setToolTip='', setToolTipDuration=-3, setStatusTip='',
                        setWhatsThis='', setAccessibleName='', setAccessibleDescription='', setLayoutDirection=0,
                        setAutoFillBackground=True, setStyleSheet='', setWindowFilePath='',
                        ImhHiddenText=False, ImhSensitiveData= False, ImhNoAutoUppercase= False,
                        ImhPreferNumbers= False, ImhPreferUppercase= False, ImhPreferLowercase= False,
                        ImhNoPredictiveText= False, ImhDate= False, ImhTime= False,
                        ImhPreferLatin= False, ImhMultiLine= False,
                        ImhDigitsOnly= False, ImhFormattedNumbersOnly= False,
                        ImhUppercaseOnly= False, ImhLowercaseOnly= False, ImhDialableCharactersOnly= False,
                        ImhEmailCharactersOnly= False, ImhUrlCharactersOnly= False, ImhLatinOnly= False,
                        ImhExclusiveInputMask= False):



        object.setObjectName(setObjectName)

        object.setGeometry(QRect(setGeometry_x, setGeometry_y, setGeometry_width, setGeometry_height))

        sizePolicy = QSizePolicy(self.size_policy_list[setSizePolicy_horizontal-1], self.size_policy_list[setSizePolicy_vertical - 1])
        sizePolicy.setHorizontalStretch(setSizePolicy_horizontal_stretch)
        sizePolicy.setVerticalStretch(setSizePolicy_vertical_stretch)
        sizePolicy.setHeightForWidth(object.sizePolicy().hasHeightForWidth())
        object.setSizePolicy(sizePolicy)

        object.setMinimumSize(QSize(setMinimumSize_width, setMinimumSize_height))

        object.setMaximumSize(QSize(setMaximumSize_width, setMaximumSize_height))

        object.setSizeIncrement(QSize(setSizeIncrement_width, setSizeIncrement_height))

        object.setBaseSize(QSize(setBaseSize_width, setBaseSize_height))

        object.setFont(self.setFont(setFamily=setFamily,
                                    setPointSize=setPointSize,
                                    setBold=setBold,
                                    setItalic=setItalic,
                                    setUnderline=setUnderline,
                                    setStrikeOut=setStrikeOut,
                                    setKerning=setKerning,
                                    setAntialias=setAntialias))

        object.setCursor(QCursor(setCursor))

        object.setMouseTracking(setMouseTracking)

        object.setTabletTracking(setTabletTracking)

        object.setTabletTracking(setTabletTracking)

        object.setFocusPolicy(self.focus[setFocusPolicy])

        object.setContextMenuPolicy(self.contexMenuPolicy[setContextMenuPolicy])

        object.setAcceptDrops(setAcceptDrops)

        object.setToolTip(setToolTip)

        object.setToolTipDuration(setToolTipDuration)

        object.setStatusTip(setStatusTip)

        object.setWhatsThis(setWhatsThis)

        object.setAccessibleName(setAccessibleName)

        object.setAccessibleDescription(setAccessibleDescription)

        object.setLayoutDirection(self.layoutDirection[setLayoutDirection])

        object.setAutoFillBackground(setAutoFillBackground)

        object.setStyleSheet(setStyleSheet)

        object.setLocale(QLocale(QLocale.English, QLocale.India))

        object.setWindowFilePath(setWindowFilePath)

        method_hint = []
        a = 0
        for each in [ImhHiddenText, ImhSensitiveData, ImhNoAutoUppercase,
                        ImhPreferNumbers, ImhPreferUppercase, ImhPreferLowercase,
                        ImhNoPredictiveText, ImhDate, ImhTime,
                        ImhPreferLatin, ImhMultiLine,
                        ImhDigitsOnly, ImhFormattedNumbersOnly,
                        ImhUppercaseOnly, ImhLowercaseOnly, ImhDialableCharactersOnly,
                        ImhEmailCharactersOnly, ImhUrlCharactersOnly, ImhLatinOnly,
                        ImhExclusiveInputMask]:
            if each == True:
                method_hint.append(self.inputMethodHint[a] )

            a+=1
        if method_hint:
            object.setInputMethodHints(method_hint)


        return object



    def setFont(self, setFamily='', setPointSize=8, setBold=False, setItalic=False,
                setUnderline=False, setStrikeOut=False, setKerning=True, setAntialias=0):

        font = QFont()
        font.setFamily(setFamily)
        font.setPointSizeF(float(setPointSize))
        font.setBold(setBold)
        font.setItalic(setItalic)
        font.setUnderline(setUnderline)
        font.setStrikeOut(setStrikeOut)
        font.setKerning(setKerning)
        font.setStyleStrategy(self.antialize[setAntialias])

        return font

    def common_layout_property(self, layout_name, objectName='', leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0,
                               setSpacing=0, setSizeConstraint=0):
        '''

        '''



        layout_name.setObjectName(objectName)

        layout_name.setContentsMargins(leftMargin, topMargin, rightMargin, bottomMargin)

        if isinstance(layout_name, QVBoxLayout) or isinstance(layout_name, QHBoxLayout):
            layout_name.setSpacing(setSpacing)

            layout_name.setSizeConstraint(self.layoutSizeConstraint[setSizeConstraint])

        return layout_name

    def add_spaceItem(self, vertical=False, horizontal=False):

        '''

        '''

        if vertical:
            spaceItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            return spaceItem

        if horizontal:
            spaceItem = QSpacerItem(20, 40,  QSizePolicy.Minimum, QSizePolicy.Expanding)
            return spaceItem

    def abstractButton(self, button, setText='Sample', setIcon='', icon_width=0, icon_height=0, setCheckable=False, setChecked=False, setAutoRepeat=False,
                       setAutoExclusive=False, setAutoRepeatDelay=300, setAutoRepeatInterval=100):

        '''

        '''

        button.setText(setText)

        icon = QIcon()
        icon.addPixmap(QPixmap(setIcon), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)

        button.setIconSize(QSize(icon_width, icon_height))

        button.setCheckable(setCheckable)

        button.setChecked(setChecked)

        button.setAutoRepeat(setAutoRepeat)

        button.setAutoExclusive(setAutoExclusive)

        button.setAutoRepeatDelay(setAutoRepeatDelay)

        button.setAutoRepeatInterval(setAutoRepeatInterval)


        return button















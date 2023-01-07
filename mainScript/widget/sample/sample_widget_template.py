from spark.widget.import_module import *

from spark.widget.sample import styleSheet
from spark.widget.sample.sample_qt_widget_template import common_property
#from importlib import reload
for each in [styleSheet, common_property]:
    reload(each)


from spark.widget.sample.styleSheet import STYLESHEET
from spark.widget.sample.sample_qt_widget_template.common_property import COMMON_PROPERTY

class SAMPLE_WIDGET_TEMPLATE():
    def __init__(self):
        self.styleSheet_class = STYLESHEET()
        self.common_property_class = COMMON_PROPERTY()
        self.max_size = 16777215
        self.vertical = 'vertical'
        self.horizonatal = 'horizonatal'
        self.validator = QDoubleValidator()

        self.lineedit_type_float = 'float'
        self.lineedit_type_string = 'string'

    def widget_def(self, parent_self= '', set_object_name='', min_size=[0, 0], max_size=[16777215, 16777215], set_styleSheet=''''''):
        '''
        SPECIFY THE WIDGET WITH SOME DEFAULT SETTING
        @param parent_self: PARENT OBJECT
        @param set_object_name: SET OBJECT NAME FOR THE WIDGET
        @param min_size: SET THE MIN SIZE
        @param max_size: SET THE MAX SIZE
        @return:
        '''
        #CREATE A WIDGET
        if parent_self == '':
            widget = QWidget()
        else:
            widget = QWidget(parent_self)


        #WIDGET SET OBJECT NAME
        widget.setObjectName(set_object_name)


        #SET MAX AND MIN SIZE
        if max_size[0] > 16777215:
            max_size[0] = 16777215
        if max_size[1] > 16777215:
            max_size[1] = 16777215


        widget.setMinimumSize(QSize(min_size[0], min_size[1]))

        widget.setMaximumSize(QSize(max_size[0], max_size[1]))

        widget.setStyleSheet(set_styleSheet)

        return widget

    def dock_widget_def(self, parent_self, set_object_name, window_title='', set_styleSheet=''''''):
        '''
        DOCK WIDGET
        @param parent_self: PARENT OBJECT
        @param set_object_name: SET OBJECT NAME
        @param window_title:
        @return:
        '''
        #CREATE DOCK WIDGET
        dock_widget = QDockWidget(parent_self)

        #DOCK WIDGET SET OBJECT NAME
        dock_widget.setObjectName(set_object_name)

        #DOCK WIDGET SET TITLE WINDOW
        dock_widget.setWindowTitle(window_title)

        dock_widget.setStyleSheet(set_styleSheet)

        #RETURN
        return dock_widget

    def splitter_def(self, parent_self, set_orientation='vertical', set_object_name='', set_handle_width=2, set_styleSheet='''''', min_size=[0, 0], max_size=[16777215, 16777215]):
        '''
        THIS IS THE SPLITTER DEF

        @param parent_self: THIS IS THE PARENT SELF
        @param set_orientation: THIS IS THE SET ORIENTATION ['vertical', horizonatal]
        @param set_object_name: THIS IS THE SET OBJECT
        @return: SPLITTER
        '''

        splitter = QSplitter(parent_self)

        lower_set_orientation = set_orientation.lower()
        if lower_set_orientation == 'vertical':
            splitter.setOrientation(Qt.Vertical)
        elif lower_set_orientation == 'horizonatal':
            splitter.setOrientation(Qt.Horizontal)
        else: RuntimeError('Please Do Specify {vertical} or {horizonatal}')

        self.set_object_name(obj_name=splitter, set_object_name=set_object_name, else_name='splitter')

        splitter.setStyleSheet(set_styleSheet)

        splitter.setHandleWidth(set_handle_width)

        splitter.setMinimumSize(QSize(min_size[0], min_size[1]))

        splitter.setMaximumSize(QSize(max_size[0], max_size[1]))



        return splitter

    def vertical_layout(self, parent_self, set_contents_margins=[0, 0, 0, 0], set_spacing=0, set_object_name=''):
        '''
        CREATE A VERTICAL LAYOUT
        @param parent_self: PARENT OBJECT
        @param set_contents_margins: SET CONTENTS MARGINS
        @param set_spacing: SET SPACING
        @return:
        '''

        vertical_layout = QVBoxLayout(parent_self)

        vertical_layout = self.common_property_class.common_layout_property(vertical_layout,
                                                                            objectName=set_object_name,
                                                                            leftMargin=set_contents_margins[0],
                                                                            topMargin=set_contents_margins[1],
                                                                            rightMargin=set_contents_margins[2],
                                                                            bottomMargin=set_contents_margins[3],
                                                                            setSpacing=set_spacing,
                                                                            setSizeConstraint=0)


        self.set_object_name(obj_name=vertical_layout, set_object_name=set_object_name, else_name='vertical_layouyt')

        return vertical_layout

    def horizontal_layout(self, parent_self, set_contents_margins=[0, 0, 0, 0], set_spacing=0, set_object_name=''):
        '''
        CREATE A VERTICAL LAYOUT
        @param parent_self: PARENT OBJECT
        @param set_contents_margins: SET CONTENTS MARGINS
        @param set_spacing: SET SPACING
        @return:
        '''

        horizontal_layout = QHBoxLayout(parent_self)

        if len(set_contents_margins) == 4:
            horizontal_layout = self.common_property_class.common_layout_property(horizontal_layout,
                                                                                  objectName=set_object_name,
                                                                                  leftMargin=set_contents_margins[0],
                                                                                  topMargin=set_contents_margins[1],
                                                                                  rightMargin=set_contents_margins[2],
                                                                                  bottomMargin=set_contents_margins[3],
                                                                                  setSpacing=set_spacing,
                                                                                  setSizeConstraint=0)

        self.set_object_name(obj_name=horizontal_layout, set_object_name=set_object_name, else_name='horizontal_layouyt')

        return horizontal_layout

    def grid_layout(self, parent_self='', set_contents_margins=[0, 0, 0, 0], set_horizontal_space=0,
                    set_vertical_space=0, set_object_name='', set_spacing=0):
        '''
        CREATE GRID LAYOUT
        @param parent_self: PARENT OBJECT
        @param set_contents_margins: SET CONTENT MARGINE
        @param set_horizontal_space: SET HORIZONTAL SPACE
        @param set_vertical_space: SET VERTICAL SPACE
        @param set_object_name: SET OBJECT NAME
        @return:
        '''
        if parent_self != '':
            grid_layout = QGridLayout(parent_self)
        else:
            grid_layout = QGridLayout()

        if len(set_contents_margins) == 4:
            grid_layout = self.common_property_class.common_layout_property(grid_layout,
                                                                            objectName=set_object_name,
                                                                            leftMargin=set_contents_margins[0],
                                                                            topMargin=set_contents_margins[1],
                                                                            rightMargin=set_contents_margins[2],
                                                                            bottomMargin=set_contents_margins[3],
                                                                            setSpacing=set_spacing,
                                                                            setSizeConstraint=0)



        grid_layout.setHorizontalSpacing(set_horizontal_space)

        grid_layout.setVerticalSpacing(set_vertical_space)

        self.set_object_name(obj_name=grid_layout, set_object_name=set_object_name, else_name='grid_layout')

        grid_layout.setSpacing(set_spacing)

        return grid_layout

    def label(self, set_alighment='left', set_object_name='', set_text='', set_tool_tip='', set_status='', set_styleSheet='''''', min_size=[0, 0], max_size=[16777215, 16777215]):
        '''
        CREATE LABEL
        @param set_alighment: SET ALIGHMENT EX>> LEFT, RIGHT, CENTER
        @param set_object_name: SET OBJECT NAME
        @param set_tool_tip: SET TOOL TIP
        @param set_status: SET STATUS
        @return:
        '''

        label = QLabel()

        label.setText(set_text)

        alighment = set_alighment.lower()
        if alighment == 'left':
            label.setAlignment(Qt.AlignLeft)
        elif alighment == 'right':
            label.setAlignment(Qt.AlignRight)
        elif alighment == 'center':
            label.setAlignment(Qt.AlignCenter)
        elif alighment == 'justify':
            label.setAlignment(Qt.AlignJustify)
        else:
            Exception('Please Do Specify proper alighment for the label')

        self.set_object_name(obj_name=label, set_object_name=set_object_name, else_name='label')

        label.setToolTip(set_tool_tip)

        label.setStyleSheet(set_styleSheet)

        label.setStatusTip(set_status)

        label.setMinimumSize(QSize(min_size[0], min_size[1]))

        label.setMaximumSize(QSize(max_size[0], max_size[1]))


        return label



    def pushButton(self, parent_self='', min_size=[0, 0], max_size=[16777215, 16777215], set_text='', set_object_name='', set_tool_tip='', set_status='', set_icon='', set_icon_size=[0, 0],
                   set_styleSheet='''''', setCheckable=False, setChecked=False, setAutoRepeat=False,
                   setAutoExclusive=False, setAutoRepeatDelay=300, setAutoRepeatInterval=100,
                   connect=''):
        '''
        SET PUSH BUTTON
        @param min_size: SET THE MIN SIZE
        @param max_size: SET THE MAZ SIZE
        @param set_text: SET TEXT
        @param set_object_name: SET OBJECT NAME
        @param set_tool_tip: SET TOOL TIP
        @param set_status: SET STATUS
        @return:
        '''
        #CREATE PUSH BUTTON
        if parent_self == '':
            pushButton = QPushButton()
        else:
            pushButton = QPushButton(parent_self)

        #SET MINIMUM SIZE
        pushButton.setMinimumSize(QSize(min_size[0], min_size[1]))

        #SET MAXIMUM SIZE
        pushButton.setMaximumSize(QSize(max_size[0], max_size[1]))


        pushButton = self.common_property_class.abstractButton(pushButton, setText=set_text, setIcon=set_icon, icon_width=set_icon_size[0],
                                                               icon_height=set_icon_size[1],
                                                               setCheckable=setCheckable, setChecked=setChecked, setAutoRepeat=setAutoRepeat,
                                                               setAutoExclusive=setAutoExclusive, setAutoRepeatDelay=setAutoRepeatDelay,
                                                               setAutoRepeatInterval=setAutoRepeatInterval)

        #SET OBJECT NAME
        self.set_object_name(obj_name=pushButton, set_object_name=set_object_name, else_name='pushButton')

        #SET TOOLTIP
        pushButton.setToolTip(set_tool_tip)

        #SET STATUS
        pushButton.setStatusTip(set_status)

        pushButton.setStyleSheet(set_styleSheet)

        if connect != '':
            pushButton.clicked.connect(connect)

        return pushButton

    def line_edit(self, parent_self='', set_object_name='', set_text='', set_styleSheet='''''', set_PlaceholderText='', type=''):
        '''
        SET LINEEDIT
        @param parent_self: SPECIFY THE PARENT OBJECT
        @param set_object_name: SPECIFY THE SET OBJECT NAME
        @param set_text: SET TEXT
        @return:
        '''

        if parent_self != '':
            line_edit = QLineEdit(parent_self)
        else:
            line_edit = QLineEdit()

        self.set_object_name(line_edit, set_object_name, 'line_edit')

        line_edit.setText(set_text)

        line_edit.setPlaceholderText(set_PlaceholderText)

        line_edit.setStyleSheet(set_styleSheet)

        if type == '':
            if type == self.lineedit_type_float:
                validator = QDoubleValidator()
                line_edit.setValidator(validator)

        return line_edit

    def checkbox(self, set_text='', set_object_name='', set_tool_tip='', set_status='', set_checked=False, stateChanged='', set_styleSheet=''''''):
        checkbox = QCheckBox()

        checkbox.setText(set_text)

        checkbox.setObjectName(set_object_name)

        checkbox.setToolTip(set_tool_tip)

        checkbox.setStatusTip(set_status)

        checkbox.setChecked(set_checked)

        if stateChanged != '':
            checkbox.stateChanged.connect(stateChanged)

        checkbox.setStyleSheet(set_styleSheet)

        return checkbox

    def line(self):
        #line = QLine(0, 0, option.rect.width(), 0)
        #line = QLine(0, 0, option.rect.width(), 0)
        pass


    def set_object_name(self, obj_name, set_object_name, else_name):
        '''
        SET THE OBJECT NAME
        @param obj_name: OBJECT NAME
        @param set_object_name: SET OBJECT NAME
        @return:
        '''
        if set_object_name == '':
            obj_name.setObjectName(else_name)
        else:
            obj_name.setObjectName(set_object_name)

    def tab_widget(self, parent_self, set_layout_direction='left', set_object_name='', set_styleSheet=''''''):
        '''
        SET TAB WIDGET
        @param parent_self: PARENT WIDGET
        @param set_layout_direction: SET LAYOUT DIRECTION
        @param set_object_name: SET OBJECT NAME
        @return: TABWIDGET
        '''
        tabWidet = QTabWidget(parent_self)

        lower_set_layout_direction = set_layout_direction.lower()
        if lower_set_layout_direction == 'left':
            tabWidet.setLayoutDirection(Qt.LeftToRight)
        elif lower_set_layout_direction == 'right':
            tabWidet.setLayoutDirection(Qt.RightToLeft)
        else:
            RuntimeError('Please do Specify Left or Right')

        tabWidet.setStyleSheet(set_styleSheet)

        self.set_object_name(tabWidet, set_object_name=set_object_name, else_name='tabWidget')

        return tabWidet

    def scrollArea(self, parent_self, set_obj_name='', set_widget_resizable=True, set_styleSheet=''''''):
        '''
        CREATE SCROLL AREA
        @param parent_self: SPECIFY THE PARENT SELF
        @param set_obj_name: SPECIFY THE SET OBJECT NAME
        @param set_geometry: SPECIFY THE SET GEOMETRY
        @return:
        '''

        scrollArea = QScrollArea(parent_self)

        self.set_object_name(scrollArea, set_object_name=set_obj_name, else_name='scrollArea')

        scrollArea.setWidgetResizable(set_widget_resizable)

        scrollArea.setStyleSheet(set_styleSheet)

        return scrollArea

    def color_styleSheet(self, obj_name, color=[]):
        '''
        specify the string value for styleSheet
        @param obj_name : specify the object name in string
        @type obj_name: str

        @param red : specify list of the Color value it should be 3 Color Ex=[1, 2, 3]
        @type red: list

        '''
        if len(color) != 3:
            return None
        return '%s: rgb(%s, %s, %s);\n' %(obj_name, color[0], color[1], color[2]) #f'{obj_name}: rgb({color[0]}, {color[1]}, {color[2]});\n'

    def list_widget(self):

        listWidget = QListWidget()

        return listWidget

    def treeWidget(self, parent_self='', setHeaderHidden=False):
        '''

        :return:
        '''

        if parent_self != '':
            treeWidget = QTreeWidget(parent_self)
        else:
            treeWidget = QTreeWidget()

        treeWidget.setHeaderHidden(setHeaderHidden)

        treeWidget.setSelectionMode(treeWidget.ExtendedSelection)

        return treeWidget

    def styleSheet_def(self, obj_name, color=[], background_color=[],
                       border_pix=0, border_type='Solid',
                       padding=0, padding_top=0, padding_bottom=0,
                       selection_background_color=[],
                       selection_color=[], spacing=0,
                       width=0, height=0, margin_top = 0,
                       margin_bottom=0, image='',
                       margin_left=0, margin_right=0,
                       background=[], opacity=0,
                       outline=None, font_weight='',
                       border_radius=0, subcontrol_origin='',
                       subcntrol_position=[], left=0,
                       padding_left=0, padding_right=0,
                       margin=0,
                       alternate_background_color=[], border_color=[],
                       min_width=0, max_width=0,
                       border_left=[],
                       border_top_color=[],
                       border_right_color=[], border_bottom_color=[],
                       border_left_color=[], gridline_color=[],
                       font_size=0,
                       border = [5, 'solid', [0, 255, 127]]):



        '''
        Specify the StyhleSheet

        @param obj_name : specify the object name in string
        @type obj_name: str

        @param color : specify the color in list
        @type color: list or str

        @param background_color : specify the baclkground color in list
        @type background_color: list or str

        @param alternate_background_color : specify the alternate background color
        @type alternate_background_color: list or str

        @param border_color : specify the border color in list
        @type border_color: list or str

        @param border_top_color : specify the border top color in list
        @type border_top_color: list or str

        @param border_right_color : specify the border right color in list
        @type border_right_color: list or str

        @param border_bottom_color : specify the border bottom color in list
        @type border_bottom_color: list or str

        @param border_left_color : specify the boirder left color in list
        @type border_left_color: list or str

        @param gridline_color : specify the gridline color in list
        @type gridline_color: list or str

        @param selection_background_color : specify the selection background color in list
        @type selection_background_color: list or str

        @param selection_color : specify the selection color in list
        @type selection_color: list or str

        @param font_size : specify font size
        @type font_size: int or float

        @param font_weight : specify the font weight
        @type font_weight: str
        '''


        if obj_name[0] != '#':
            obj_name = '#' + obj_name

        # SPECIFY THE START OF THE COLOR
        string_val = ''.join([obj_name, '{\n'])
        space = '    '
        # ADD COLOR IF  SPECIFIED
        if color:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_color(color)])

        # ADD BACKGROUND COLOR IF  SPECIFIED
        if background_color:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_background_color(background_color)])

        #ADD BORDER
        if border_pix != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_border(pix=border_pix, type=border_type, color=border_color)])

        if padding != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_padding(padding_val=padding)])

        if padding_top != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_padding_top(value=padding_top)])

        if padding_bottom != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_padding_bottom(value=padding_bottom)])

        if padding_left != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_padding_left(value=padding_left)])

        if padding_right != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_padding_right(value=padding_right)])

        if selection_background_color:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_selection_background_color(color=selection_background_color)])

        if selection_color:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_selection_color(color=selection_color)])

        if spacing != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_spacing(spacing)])

        if width != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_width(value=width)])

        if height !=0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_height(value=height)])

        if margin != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_margin(value=margin)])

        if margin_top != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_margine_top(value=margin_top)])

        if margin_bottom != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_margine_bottom(value=margin_bottom)])

        if image != '':
            string_val = ''.join([string_val, space, self.styleSheet_class.set_image(value=image)])

        if margin_left != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_margin_left(value=margin_left)])

        if margin_right != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_margin_right(value=margin_right)])

        if background != []:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_background(value=background)])

        if opacity != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_opacity(value=opacity)])

        if outline != None:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_outline(value=outline)])

        if font_weight != '':
            string_val = ''.join([string_val, space, self.styleSheet_class.set_font_weight(value=font_weight)])

        if border_radius != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_border_radius(value=border_radius)])

        if subcontrol_origin != '':
            string_val = ''.join([string_val, space, self.styleSheet_class.set_subcontrol_origin(value=subcontrol_origin)])

        if subcntrol_position != []:
            if len(subcntrol_position) == 2:
                if type(subcntrol_position[0]) is str and type(subcntrol_position[1]) is str:
                    string_val = ''.join([string_val, space, self.styleSheet_class.set_subcontrol_poistion(pos_one=subcntrol_position[0], pos_two=subcntrol_position[1])])

        if left != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_left(value=left)])


        if alternate_background_color != []:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_alternate_background_color(color=alternate_background_color)])

        if min_width != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_min_width(value=min_width)])

        if max_width != 0:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_max_width(value=max_width)])

        if border_left != []:
            string_val = ''.join([string_val, space, self.styleSheet_class.set_border_left(pix=border_left[0], type=border_left[1], color=border_left[2])])


        '''
        # ADD ALTERNATE BACKGROUND COLOR IF  SPECIFIED
        if alternate_background_color != [] and len(alternate_background_color) == 3:
            string_val = ''.join([string_val, space, self.color_styleSheet(obj_name='alternate-background-color',
                                                                           color=alternate_background_color)])
        elif type(alternate_background_color) == str:
            string_val = ''.join([string_val, space, 'alternate-background-color: ', alternate_background_color, ';\n'])

        # ADD BORDER COLOR IF  SPECIFIED
        if border_color != [] and len(border_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='border-color', color=border_color)])
        elif type(border_color) == str:
            string_val = ''.join([string_val, space, 'border-color: ', border_color, ';\n'])

        # ADD BORDER TOP COLOR IF  SPECIFIED
        if border_top_color != [] and len(border_top_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='border-top-color', color=border_top_color)])
        elif type(border_top_color) == str:
            string_val = ''.join([string_val, space, 'border-top-color: ', border_top_color, ';\n'])

        # ADD BORDER RIGHT COLOR IF  SPECIFIED
        if border_right_color != [] and len(border_right_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='border-right-color', color=border_right_color)])
        elif type(border_right_color) == str:
            string_val = ''.join([string_val, space, 'border-right-color: ', border_right_color, ';\n'])

        # ADD BORDER BOTTOM COLOR IF  SPECIFIED
        if border_bottom_color != [] and len(border_bottom_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='border-bottom-color', color=border_bottom_color)])
        elif type(border_bottom_color) == str:
            string_val = ''.join([string_val, space, 'border-bottom-color: ', border_bottom_color, ';\n'])

        # ADD BORDER LEFT COLOR IF  SPECIFIED
        if border_left_color != [] and len(border_left_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='border-left-color', color=border_left_color)])
        elif type(border_left_color) == str:
            string_val = ''.join([string_val, space, 'border-left-color: ', border_left_color, ';\n'])

        # ADD GRIDLINE  COLOR IF  SPECIFIED
        if gridline_color != [] and len(gridline_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='gridline-color', color=gridline_color)])
        elif type(gridline_color) == str:
            string_val = ''.join([string_val, space, 'gridline-color: ', gridline_color, ';\n'])

        # ADD SELECTION BACKGRIUND COLOR IF  SPECIFIED
        if selection_background_color != [] and len(selection_background_color) == 3:
            string_val = ''.join([string_val, space, self.color_styleSheet(obj_name='selection-background-color',
                                                                           color=selection_background_color)])
        elif type(selection_background_color) == str:
            string_val = ''.join([string_val, space, 'selection-background-color: ', selection_background_color, ';\n'])

        # ADD SELCTION COLOR IF  SPECIFIED
        if selection_color != [] and len(selection_color) == 3:
            string_val = ''.join(
                [string_val, space, self.color_styleSheet(obj_name='selection-color', color=selection_color)])
        elif type(selection_color) == str:
            string_val = ''.join([string_val, space, 'selection-color: ', selection_color, ';\n'])

        # ADD BORDER RADIUS
        if border_radius != 0.0:
            string_val = ''.join([string_val, space, 'border-radius:', str(border_radius), 'px;\n'])
        elif type(border_radius) == str:
            string_val = ''.join([string_val, space, 'border-radius: ', border_radius])

        # FONT SIZE
        if font_size != 0:
            string_val = ''.join([string_val, space, 'font-size:', str(font_size), 'pt;\n'])

        # FONT WEIGHT
        if font_weight != '':
            string_val = ''.join([string_val, space, 'font-weight:', str(font_weight), ';\n'])

        string_val = ''.join([string_val, space, 'border:', str(font_weight), ';\n'])
        #border:5px solid rgb(0, 255, 127);
        '''
        string_val = string_val + '}'
        return string_val

    def action(self, parent_self, name='', setStatusTip='', setToolTip=''):
        '''
        CREATE ACTION AND RETURN
        @param parent_self: PARENT OBJECT
        @param name: NAME OF THE ACTION
        @return:
        '''
        #ACTION NAME
        action_name = QAction(name, parent_self)

        #SET STATUS TIP
        action_name.setStatusTip(setStatusTip)

        #SET TOOL TIP
        action_name.setToolTip(setToolTip)

        return action_name

    def gridLayout_widget(self, type_object='', noOfColum=1,noOfObject=0, max_size_list=[], min_size_list=[], set_object_list=[], set_tool_tip_list=[],
                          set_status_list=[], set_icon_list=[], set_icon_size_list=[], set_styleSheet_list=[], set_text_list=[]):
        '''
        @param type_object: specify the type in the gridLayout list for Ex: 'checkbox' or 'pushbutton' or  'label'
        @param noOfColum: specify the no of the coloum in the gridLayout
        @param max_size_list: specify the max size list
        @param min_size_list: specify the min_size_list
        @param set_object_list: specify the set_object_list
        @param set_tool_tip_list: specify the set_tool_tip_list
        @param set_status_list: specify the set_status_list
        @param set_icon_size_list: specify the set_icon_size_list
        @param set_styleSheet_list: specify the set_styleSheet_list
        @param set_text_list: specify the set_text_list
        '''
        #QUERY THE OBJECT
        if type(type_object) != str:
            RuntimeError('Please Specify the String in type object')

        length_list = 999999999
        for each in [max_size_list, min_size_list, set_object_list, set_tool_tip_list, set_status_list, set_icon_list, set_icon_size_list,
                     set_styleSheet_list, set_text_list]:
                    if length_list == 999999999:
                        length_list = len(each)
                    else:
                        if len(each) != length_list:
                            RuntimeError('Total Length is Not mathcin with the : ', each)

        new_type = type.lower()

        grid_layout = self.grid_layout()

        if new_type == 'checkbox':
            checkbox_list = []
            a = 0
            new_value = 0
            vertical_val = 0
            while a < noOfObject:
                checkbox = self.checkbox(set_text=set_text_list[a], set_object_name=set_object_list[a], set_tool_tip=set_tool_tip_list[a],
                                         set_status=set_status_list[a])
                grid_layout.addWidget(checkbox, vertical_val, new_value, 1, 1)
                checkbox_list.append(checkbox)
                new_value+=1
                if new_value > noOfColum:
                    new_value = 0
                    vertical_val +=1
                a+=1


        elif new_type == 'pushbutton':
            print('this is the button')

        elif new_type == 'label':
            print('this is the label')

    def removeObject(self, layout_name):
        if layout_name is not None:
            while layout_name.count():
                item = layout_name.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.removeObject(item.layout())

    def button_default_return(self, value=True, text_name='', toolTip='', connect=''):
        '''

        '''

        button_text = text_name

        button_object = button_text.replace(' ', '_')

        button_toolTip = toolTip

        return [value, button_text, button_object, button_toolTip, connect]

    def comboBox(self, parent_self='', addItems=[], setEditable=False, currentIndexChanged=''):
        '''

        '''

        comboBox = QComboBox()

        comboBox.setEditable(setEditable)

        comboBox.addItems(addItems)

        if currentIndexChanged != '':
            comboBox.currentIndexChanged.connect(currentIndexChanged)

        return comboBox

    def spaceItem(self):
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        return spacerItem

    def plainTextEdit(self):
        '''

        :return:
        '''

        plainTextEdit = QPlainTextEdit()


        return plainTextEdit

    def setObjectName(self, text=''):
        '''
        set the object name from the object
        :param text: specify the object
        :return:
        '''

        text = text.replace(' ', '_')

        obj_name = text + '_Object'

        return obj_name

    def progressBar(self, self_val=''):
        '''

        :return:
        '''

        progress_bar = QProgressBar()

        return progress_bar



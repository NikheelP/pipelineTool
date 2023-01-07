from spark.widget.import_module import *

from spark.widget.sample import sample_widget_template
from spark.widget.sample import sample_color_variable
#from importlib import reload
for each in [sample_widget_template, sample_color_variable]:
    reload(each)

from spark.widget.sample.sample_widget_template import SAMPLE_WIDGET_TEMPLATE
from spark.widget.sample.sample_color_variable import COLOR_VARIABLE
import os, getpass

current_dir = os.path.dirname(os.path.realpath(__file__))
user_name = getpass.getuser()


class SAMPLE_WIDGET(QMainWindow):

    def __init__(self, title='Sample Title', width=800, height=600, user_widget=False):
        super().__init__()

        self.user_center_widget_expand = False
        self.title = title
        self.user_widget_val = user_widget

        #GET RESIZE
        self.resize(width, height)

        self._mousePressed = False
        self.styleSheet = ''' '''

        self.color_variable_class = COLOR_VARIABLE()
        self.sample_widget_template = SAMPLE_WIDGET_TEMPLATE()

        # SET THE CENTRAL WIDGET
        sample_central_widget_object = 'sample_central_widget'
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=sample_central_widget_object,
                                                                 background_color=self.color_variable_class.yellow_color.get_value())
        self.color_variable_class.background_color.set_value = [10, 10, 10]
        self.sample_central_widget = self.sample_widget_template.widget_def(parent_self=self,
                                                                            set_object_name=sample_central_widget_object,
                                                                            set_styleSheet=style_sheet)

        self.widget_def()
        self.setCentralWidget(self.sample_central_widget)

        #SHOW WINDOW
        self.show()

    def widget_def(self):
        # SET THE VERTICAL LAYOUT
        self.sample_vertical_layout = self.sample_widget_template.vertical_layout(parent_self=self.sample_central_widget)

        #TITLE WIDGET
        tilte_widet_object = 'title_widgt'
        title_widget_stylesheet = self.sample_widget_template.styleSheet_def(obj_name=tilte_widet_object,
                                                                             background_color=self.color_variable_class.new_background_color.get_value())
        self.title_widgt = self.sample_widget_template.widget_def(parent_self=self.sample_central_widget,
                                                                  min_size=[0, 57], max_size=[16777215, 60],
                                                                  set_object_name=tilte_widet_object,
                                                                  set_styleSheet=title_widget_stylesheet)
        self.sample_vertical_layout.addWidget(self.title_widgt)

        #TITLE WIDGET
        self.title_widget_def()


        #MAIN CENTER WIDGET
        main_center_widget = 'main_center_widget'
        main_center_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=main_center_widget,
                                                                            background_color=self.color_variable_class.new_background_color.get_value())
        self.main_center_widget = self.sample_widget_template.widget_def(parent_self=self.sample_central_widget,
                                                                         set_object_name=main_center_widget,
                                                                         set_styleSheet=main_center_styleSheet)
        self.main_center_widget_def()
        self.sample_vertical_layout.addWidget(self.main_center_widget)


        # SET FRAMELESS
        self.set_window_frameless()

        # MAKE A DOCK WIDGET

        #STATUS
        self.set_status()

    def title_widget_def(self):
        def moveWindow(event):
            # RESTORE BEFORE MOVE

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                if self.isMaximized():
                    self.showNormal()
                self.move(self.pos() + event.globalPos() - self._mousePos)
                self._mousePos = event.globalPos()
                event.accept()

        def maximize_pushButton_def(event):
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()


        self.title_gridLayout = self.sample_widget_template.grid_layout(parent_self=self.title_widgt,
                                                                        set_horizontal_space=5,
                                                                        set_vertical_space=0,
                                                                        set_object_name='title_gridLayout',
                                                                        set_contents_margins=[0, 0, 4, 0],
                                                                        set_spacing=4)

        #OPTION BUTTON
        if self.user_widget_val:
            option_pushButton_object = 'option_pushButton'
            option_pushButton_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=option_pushButton_object,
                                                                                      border_radius=30,
                                                                                      background_color=self.color_variable_class.yellow_color.get_value())
            self.option_pushButton = self.sample_widget_template.pushButton(min_size=[60, 60],
                                                                            max_size=[60, 60],
                                                                            set_icon_size=[40, 40],
                                                                            set_object_name=option_pushButton_object,
                                                                            set_styleSheet=option_pushButton_styleSheet)
            self.option_pushButton.clicked.connect(self.option_pushButton_def)
            self.title_gridLayout.addWidget(self.option_pushButton, 0, 0, 2, 1)

        #TITLE LABEL
        title_label_object = 'Sample_Title'

        title_label_set_text = '<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">%s</span></p></body></html>' %(self.title)
        title_label_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=title_label_object,
                                                                            color=self.color_variable_class.green_color.get_value())
        self.title_label = self.sample_widget_template.label(min_size=[0, 52],
                                                             max_size=[16777215, 52],
                                                             set_object_name=title_label_object,
                                                             set_text=title_label_set_text,
                                                             set_alighment='center',
                                                             set_styleSheet=title_label_styleSheet,
                                                             set_tool_tip=self.title,
                                                             set_status=self.title)
        self.title_label.mouseMoveEvent = moveWindow
        self.title_label.mouseDoubleClickEvent = maximize_pushButton_def
        self.title_gridLayout.addWidget(self.title_label, 0, 1, 1, 1)

        # USER NAME LABEL
        user_name_label_object = 'user_name_label'
        user_name_label_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=user_name_label_object,
                                                                                color=self.color_variable_class.white_color.get_value(),
                                                                                background_color=self.color_variable_class.background_another_color.get_value())
        self.user_name_label = self.sample_widget_template.label(set_alighment='right',
                                                                 set_object_name=user_name_label_object,
                                                                 set_styleSheet=user_name_label_styleSheet,
                                                                 set_text=' | ' + user_name.upper())
        self.title_gridLayout.addWidget(self.user_name_label, 1, 1, 1, 4)



        # MINIMIZE BUTTON
        border_radius = 10
        minimize_button_object = 'minimize_button'
        minimize_button_setStyleSheet = self.sample_widget_template.styleSheet_def(obj_name=minimize_button_object,
                                                                                   background_color=self.color_variable_class.minimize_color.get_value(),
                                                                                   border_radius=border_radius)
        minimize_button_setStyleSheet = minimize_button_setStyleSheet + self.sample_widget_template.styleSheet_def(obj_name=minimize_button_object + ':hover',
                                                                                         background_color=self.color_variable_class.minimize_hover_color.get_value())
        self.minimize_button = self.sample_widget_template.pushButton(min_size=[20, 20],
                                                                      max_size=[20, 20],
                                                                      set_object_name=minimize_button_object,
                                                                      set_styleSheet=minimize_button_setStyleSheet,
                                                                      set_status='Minimize',
                                                                      set_tool_tip='Minimize')
        self.minimize_button.clicked.connect(self.showMinimized)
        self.title_gridLayout.addWidget(self.minimize_button, 0, 2, 1, 1)

        # MAXIMIZE BUTTON
        maximize_button_object = 'maximize_button'
        maximize_button_setStyleSheet = self.sample_widget_template.styleSheet_def(obj_name=maximize_button_object,
                                                                                   background_color=self.color_variable_class.maximize_color.get_value(),
                                                                                   border_radius=border_radius)
        maximize_button_setStyleSheet = maximize_button_setStyleSheet + self.sample_widget_template.styleSheet_def(obj_name=maximize_button_object + ':hover',
                                                                                                                   background_color=self.color_variable_class.maximize_hover_color.get_value())
        self.maximize_button = self.sample_widget_template.pushButton(min_size=[20, 20],
                                                                      max_size=[20, 20],
                                                                      set_object_name=maximize_button_object,
                                                                      set_styleSheet=maximize_button_setStyleSheet,
                                                                      set_status='Maximize',
                                                                      set_tool_tip='Maximize')
        self.maximize_button.clicked.connect(self.maximize_pushButton_def)
        self.title_gridLayout.addWidget(self.maximize_button, 0, 3, 1, 1)

        # CLOSET BUTTON
        close_button_object = 'close_button'
        close_button_setStyleSheet = self.sample_widget_template.styleSheet_def(obj_name=close_button_object,
                                                                                background_color=self.color_variable_class.close_color.get_value(),
                                                                                border_radius=border_radius)
        close_button_setStyleSheet = close_button_setStyleSheet + self.sample_widget_template.styleSheet_def(obj_name=close_button_object + ':hover',
                                                                                                             background_color=self.color_variable_class.close_hover_color.get_value())
        self.close_button = self.sample_widget_template.pushButton(min_size=[20, 20],
                                                                   max_size=[20, 20],
                                                                   set_object_name=close_button_object,
                                                                   set_styleSheet=close_button_setStyleSheet,
                                                                   set_status='Close',
                                                                   set_tool_tip='Close')
        self.close_button.clicked.connect(self.close)
        self.title_gridLayout.addWidget(self.close_button, 0, 4, 1, 1)

    def option_pushButton_def(self):
        '''
        SET THE USER WIDGET IS EXPAND AND COLLAPS
        @return:
        '''
        if self.user_center_widget_expand:
            self.collaps_def()
        else:
            self.user_center_widget.setMinimumSize(QSize(128, 0))
            self.expand_def()

    def expand_def(self):
        self.user_center_widget.setMinimumSize(QSize(128, 0))
        self.user_center_widget_expand = True

        ##############################
        self.user_help_button.setText(self.user_help_button_name.upper())
        self.user_button.setText(user_name.upper())

    def collaps_def(self):
        self.user_center_widget.setMinimumSize(QSize(64, 0))
        self.user_center_widget_expand = False

        ###################
        self.user_help_button.setText('')
        self.user_button.setText('')

    def main_center_widget_def(self):
        self.main_central_horizontal_layour = self.sample_widget_template.horizontal_layout(parent_self=self.main_center_widget,
                                                                                            set_object_name='main_central_horizontal_layour')

        if self.user_widget_val:
            #USER WIDGET
            user_center_widget_object = 'user_center_widget'
            user_center_widger_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=user_center_widget_object,
                                                                                       background_color=self.color_variable_class.yellow_color.get_value(),
                                                                                       border_radius=10)
            self.user_center_widget = self.sample_widget_template.widget_def(parent_self=self.main_center_widget,
                                                                             min_size=[64, 0],
                                                                             max_size=[0, 16777215],
                                                                             set_object_name=user_center_widget_object,
                                                                             set_styleSheet=user_center_widger_styleSheet)


            self.user_center_widget_def()
            self.main_central_horizontal_layour.addWidget(self.user_center_widget)


        main_widget_object = 'main_widget'
        main_widget_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=main_widget_object,
                                                                            background_color=self.color_variable_class.background_another_color.get_value())
        self.main_widget = self.sample_widget_template.widget_def(parent_self=self.main_center_widget,
                                                                  set_object_name=main_widget_object,
                                                                  set_styleSheet=main_widget_styleSheet)
        self.main_central_horizontal_layour.addWidget(self.main_widget)

    def get_main_widget(self):
        return self.main_widget

    def user_center_widget_def(self):
        self.user_main_widget_verticalLayout = self.sample_widget_template.vertical_layout(self.user_center_widget,
                                                                                           set_object_name='user_main_widget_verticalLayout')
        #TOOL WIDGET

        user_tool_widget_object = 'user_tool_widget'
        user_tool_widget_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=user_tool_widget_object,
                                                                                 background_color=self.color_variable_class.new_background_color.get_value())
        self.user_tool_widget = self.sample_widget_template.widget_def(parent_self=self.user_center_widget,
                                                                       set_object_name=user_tool_widget_object,
                                                                       set_styleSheet=user_tool_widget_styleSheet)
        self.user_tool_layout_def()
        self.user_main_widget_verticalLayout.addWidget(self.user_tool_widget)

        #USER WIDGET
        user_widget_object = 'user_widget'
        user_widget_setStyleSheet = self.sample_widget_template.styleSheet_def(obj_name=user_widget_object,
                                                                               background=self.color_variable_class.new_background_color.get_value())
        self.user_widget = self.sample_widget_template.widget_def(parent_self=self.user_center_widget,
                                                                  set_object_name='user_widget',
                                                                  set_styleSheet=user_widget_setStyleSheet)
        self.user_button_widget()
        self.user_main_widget_verticalLayout.addWidget(self.user_widget)

    def user_tool_layout_def(self):
        self.user_tool_vertical_layout = self.sample_widget_template.vertical_layout(parent_self=self.user_tool_widget)

    def get_user_tool_layout(self):
        return self.user_tool_vertical_layout

    def user_button_widget(self):
        self.user_vertical_layout = self.sample_widget_template.vertical_layout(parent_self=self.user_widget)

        #HELP BUTTON
        self.user_help_button_name = 'Help'
        size = 50

        user_help_icon = current_dir + '\icon\help.png'
        user_help_object = 'user_help_button'
        self.user_help_button = self.sample_widget_template.pushButton(set_object_name=user_help_object,
                                                                       set_tool_tip='HELP', set_status='HELP',
                                                                       set_text='', set_icon=user_help_icon,
                                                                       set_icon_size=[size, size])
        self.user_help_button.clicked.connect(self.user_help_button_def)
        self.user_vertical_layout.addWidget(self.user_help_button)

        #USER BUTTON
        user_button_object = 'user_button_object'
        user_button_icon = current_dir + '\\icon\\user.webp'
        self.user_button = self.sample_widget_template.pushButton(set_object_name=user_button_object,
                                                                  set_tool_tip=user_name.upper(), set_status=user_name.upper(),
                                                                  set_text='', set_icon=user_button_icon,
                                                                  set_icon_size=[size, size])
        self.user_button.clicked.connect(self.user_button_def)
        self.user_vertical_layout.addWidget(self.user_button)

    def user_help_button_def(self):
        print('user_help will run')

    def user_button_def(self):
        print('this is user button')



    def set_styleSheet(self):
        self.setStyleSheet(self.styleSheet)

    def set_append(self, new_val):
        self.styleSheet = self.styleSheet + '\n' + new_val
        return self.styleSheet



    def dock_widget_def(self):
        ###################################################>>>>LAYOUT WIDGET<<<<###################################################
        #USER DOCK WIDGET
        user_dock_widget = 'user_dock_widget'
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=user_dock_widget,
                                                                 background_color=self.color_variable_class.background_color.get_value(),
                                                                 color=self.color_variable_class.minimize_color.get_value())
        self.user_dock_widget = self.sample_widget_template.dock_widget_def(parent_self=self, set_object_name=user_dock_widget,
                                                                            window_title='User Window',
                                                                            set_styleSheet=style_sheet)

        user_dock_widget_contents_object = 'user_dock_widget_contents'
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=user_dock_widget_contents_object,
                                                                 background_color=self.color_variable_class.background_color.get_value())
        self.user_dock_widget_contents = self.sample_widget_template.widget_def(parent_self=self.user_dock_widget, set_object_name='user_dock_widget_contents',
                                                                                set_styleSheet=style_sheet)

        #USER VERTICAL LAYOUT
        self.user_verticalLayout = self.sample_widget_template.vertical_layout(parent_self=self.user_dock_widget_contents, set_object_name='user_verticalLayout')

        self.user_splitter = self.sample_widget_template.splitter_def(parent_self=self.user_dock_widget_contents, set_orientation='vertical', set_object_name='user_splitter')

        self.user_tool_widget = self.sample_widget_template.widget_def(parent_self=self.user_splitter, set_object_name='user_tool_widget')

        self.user_tool_vertical_layout = self.sample_widget_template.vertical_layout(parent_self=self.user_tool_widget, set_object_name='user_tool_vertical_layout')

        user_help_widget_object = 'user_help_widget'
        self.sample_widget_template.styleSheet_def(obj_name=user_help_widget_object,
                                                   background_color=self.color_variable_class.background_color.get_value())
        self.user_help_widget = self.sample_widget_template.widget_def(parent_self=self.user_splitter, set_object_name=user_help_widget_object,
                                                                       set_styleSheet=style_sheet)

        self.user_help_vertical_layout = self.sample_widget_template.vertical_layout(parent_self=self.user_help_widget, set_spacing=0, set_object_name='user_help_vertical_layout')

        user_grid_layout_object = 'user_grid_layout'
        self.user_grid_layout = self.sample_widget_template.grid_layout(parent_self=self.user_help_widget, set_spacing=5, set_object_name=user_grid_layout_object,
                                                                        )
        self.user_help_vertical_layout.addLayout(self.user_grid_layout)
        ##############################################################################################################################################################


        user_help_icon = current_dir + '\icon\help.png'
        user_help_object = 'user_help_button'
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=user_help_object,
                                                                 background_color=[154, 154, 154],
                                                                 border_radius=30)
        style_sheet = style_sheet + self.sample_widget_template.styleSheet_def(obj_name=user_help_object + ':hover',
                                                                               background_color=[80, 80, 80])
        self.user_help_button = self.sample_widget_template.pushButton(min_size=[60, 60], max_size=[60, 60], set_object_name=user_help_object,
                                                                       set_tool_tip='HELP', set_status='HELP',
                                                                       set_text='', set_icon=user_help_icon,
                                                                       set_styleSheet=style_sheet, set_icon_size=[50, 50])
        self.user_help_button.clicked.connect(self.user_help_button_def)
        self.user_grid_layout.addWidget(self.user_help_button, 1, 0, 1, 1)

        #USER BUTTON


        user_button_object = 'user_button'
        user_button_icon = current_dir + '\\icon\\user.webp'
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=user_button_object,
                                                                 background_color=[154, 154, 154],
                                                                 border_radius=30)
        style_sheet = style_sheet + self.sample_widget_template.styleSheet_def(obj_name=user_button_object + ':hover',
                                                                               background_color=[80, 80, 80])

        self.user_button = self.sample_widget_template.pushButton(min_size=[60, 60], max_size=[60, 60], set_object_name=user_button_object,
                                                                  set_tool_tip=user_name.upper(), set_status=user_name.upper(),
                                                                  set_text='', set_icon=user_button_icon,
                                                                  set_icon_size=[50, 50], set_styleSheet=style_sheet)
        self.user_button.clicked.connect(self.user_button_def)
        self.user_grid_layout.addWidget(self.user_button, 2, 0, 1, 1)

        self.user_verticalLayout.addWidget(self.user_splitter)
        self.user_dock_widget.setWidget(self.user_dock_widget_contents)
        self.addDockWidget(Qt.DockWidgetArea(1), self.user_dock_widget)

    def get_user_tool_layout(self):
        return self.user_tool_vertical_layout

    def get_main_layout(self):
        return self.main_vertical_layout

    def scale_vertical_sapce(self):
        self.main_spacerItem.changeSize(0, 0)

    def set_window_frameless(self):
        # CREATE WINDOW FRAMELESS
        self.setWindowFlag(Qt.FramelessWindowHint)

    def set_status(self):
        staus_bar_obj_name = 'statusbar'
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(staus_bar_obj_name)
        self.setStatusBar(self.statusbar)
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=staus_bar_obj_name,
                                                                 background_color=self.color_variable_class.new_background_color.get_value(),
                                                                 color=self.color_variable_class.color.get_value())
        self.statusbar.setStyleSheet(style_sheet)

    def maximize_pushButton_def(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self._mousePos = event.globalPos()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SAMPLE_WIDGET()
    sys.exit(app.exec_())

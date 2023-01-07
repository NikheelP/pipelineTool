

from

'''

from widget.sample import sample_widget_template
from widget.sample import sample_color_variable
from widget.sample import style_sheet_template


for each in [sample_widget_template, sample_color_variable, style_sheet_template]:
    reload(each)



from spark.widget.sample.sample_widget_template import SAMPLE_WIDGET_TEMPLATE
from spark.widget.sample.sample_color_variable import COLOR_VARIABLE
from spark.widget.sample.style_sheet_template import STYLE_SHEET_TEMPLATE

class SAMPLE_WIDGET(QMainWindow):
    def __init__(self, title='Sample Title', width=800, height=600, user_widget=False, parent=None):
        super(SAMPLE_WIDGET, self).__init__(parent)

        self.setWindowTitle(title)

        self.user_center_widget_expand = False
        self.title = title
        self.user_widget_val = user_widget

        # GET RESIZE
        self.resize(width, height)

        self._mousePressed = False
        self.styleSheet = ''' '''

        self.color_variable_class = COLOR_VARIABLE()
        self.sample_widget_template = SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_template = STYLE_SHEET_TEMPLATE()

        # SET THE CENTRAL WIDGET
        sample_central_widget_object = 'sample_central_widget'
        self.sample_central_widget = self.sample_widget_template.widget_def(parent_self=self,
                                                                            set_object_name=sample_central_widget_object)
        # self.widget_def()
        self.setCentralWidget(self.sample_central_widget)

        # SHOW WINDOW
        self.show()


    def main_center_widget_def(self):
        sample_central_widget_object = 'sample_central_widget'
        style_sheet = self.sample_widget_template.styleSheet_def(obj_name=sample_central_widget_object,
                                                                 background_color=self.color_variable_class.yellow_color.get_value())
        self.color_variable_class.background_color.set_value = [10, 10, 10]
        self.sample_central_widget = self.sample_widget_template.widget_def(parent_self=self,
                                                                            set_object_name=sample_central_widget_object,
                                                                            set_styleSheet=style_sheet)


        self.main_central_horizontal_layout = self.sample_widget_template.horizontal_layout(parent_self=self.sample_central_widget,
                                                                                            set_object_name='main_central_horizontal_layout')
        \'''
        main_widget_object = 'main_widget'
        main_widget_styleSheet = self.sample_widget_template.styleSheet_def(obj_name=main_widget_object,
                                                                            background_color=self.color_variable_class.background_another_color.get_value())
        self.main_widget = self.sample_widget_template.widget_def(parent_self=sample_central_widget_object,
                                                                  set_object_name=main_widget_object,
                                                                  set_styleSheet=main_widget_styleSheet)
        \'''
        self.main_central_horizontal_layout.addWidget(self.main_widget)

    def get_main_widget(self):
        return self.sample_central_widget


'''
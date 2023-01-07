from spark.widget.import_module import *
from spark.widget.sample.sample_widget import SAMPLE_WIDGET_TEMPLATE
from spark.widget.sample.sample_color_variable import COLOR_VARIABLE


class STYLE_SHEET_TEMPLATE():
    def __init__(self):
        self.sample_widget_template = SAMPLE_WIDGET_TEMPLATE()
        self.color_variable_class = COLOR_VARIABLE()


    def pushbutton_1_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_1_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_1_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_1_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_1_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_1_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_1_background_hover_color.get_value())
        return styleSheet

    def pushbutton_2_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_2_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_2_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_2_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_2_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_2_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_2_background_hover_color.get_value())
        return styleSheet

    def pushbutton_3_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_3_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_3_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_3_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_3_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_3_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_3_background_hover_color.get_value())
        return styleSheet

    def pushbutton_4_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_4_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_4_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_4_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_4_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_4_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_4_background_hover_color.get_value())
        return styleSheet

    def pushbutton_5_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_5_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_5_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_5_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_5_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_5_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_5_background_hover_color.get_value())
        return styleSheet

    def pushbutton_6_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_6_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_6_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_6_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_6_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_6_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_6_background_hover_color.get_value())
        return styleSheet

    def pushbutton_7_sample(self, obj_name):
        styleSheet = self.pushbutton_basic_sample(obj_name=obj_name,
                                                  background_color=self.color_variable_class.pushbutton_basic_7_background_color.get_value(),
                                                  color=self.color_variable_class.pushbutton_basic_7_color.get_value(),
                                                  font_size= self.color_variable_class.pushbutton_basic_7_font_size.get_value(),
                                                  font_weight=self.color_variable_class.pushbutton_basic_7_font_weight.get_value(),
                                                  border_radius=self.color_variable_class.pushbutton_basic_7_font_radius.get_value(),
                                                  background_hover_color=self.color_variable_class.pushbutton_basic_7_background_hover_color.get_value())
        return styleSheet

    def pushbutton_outline_sample(self, obj_name,
                                  background='',
                                  border = [5, 'solid', [0, 255, 127]],
                                  color = [255, 255, 255],
                                  font_size=10,
                                  border_radius=10,
                                  font_weight='bold',
                                  border_hover = [5, 'solid', [0, 181, 87]],
                                  color_hover =[255, 255, 255]):
        '''
        SPECIFY THE OBJECT AND AUTOMATIC CREATE A STYLESHEET FOR YOU
        @param obj_name: SPECIFY THE OBJECT NAME
        @param background: SPECIFY THE BACKGROUND COLOR
        @param border: SPECIFY THE BORDER WEIGHT, TYPE = 'solid', SPECIFY COLOR
        @param color: SPECIFY COLOR
        @param font_size: SPECIFY FONT SIZE
        @param border_radius: SPECIFY BORDER RADIUS
        @param font_weight: SPECIFY FONT WEIGHT
        @param border_hover: SPECIFY BORDER HOVER
        @param color_hover: SPECIFY COLOR HOVER
        @return:
        '''
        styleSheet = ''''''
        # SET OBJ AND OBJ HOVER NAME
        obj_hover_name = obj_name + ':hover'

        # OBJECT SET

        styleSheet = styleSheet + self.sample_widget_template.styleSheet_def(obj_name=obj_name,
                                                                             background=background,
                                                                             border=[5, 'solid', [0, 255, 127]])
        # HOVER OBJECT
        styleSheet = styleSheet + self.sample_widget_template.styleSheet_def(obj_name=obj_hover_name,
                                                                             background_color=background_hover_color)

        return styleSheet

    def pushbutton_basic_sample(self, obj_name,
                                background_color = [117, 138, 255],
                                color = [255, 255, 255],
                                font_size = 10,
                                border_radius = 10,
                                font_weight='bold',
                                background_hover_color = [0, 145, 80]):
        '''
        THIS IS A SAMPLE STYLESHEET 1
        @param obj_name: SPRCIFY THE OBJECT NAME
        @return:
        '''
        styleSheet = ''''''
        #SET OBJ AND OBJ HOVER NAME
        obj_hover_name = obj_name + ':hover'

        #OBJECT SET

        styleSheet = styleSheet + self.sample_widget_template.styleSheet_def(obj_name=obj_name, background_color=background_color,
                                                                             color=color, font_size=font_size, font_weight=font_weight,
                                                                             border_radius=border_radius)
        #HOVER OBJECT
        styleSheet = styleSheet + self.sample_widget_template.styleSheet_def(obj_name=obj_hover_name, background_color=background_hover_color)

        return styleSheet










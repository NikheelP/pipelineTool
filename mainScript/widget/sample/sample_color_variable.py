
class COLOR_VARIABLE_CHILD():
    def __init__(self, value):
        self._color_value = value

    @property
    def set_value(self):
        '''
        return the color value
        '''
        return self._color_value

    def get_value(self):
        '''
        return the color value
        '''
        return self._color_value

    @set_value.setter
    def set_value(self, value):
        '''
        setting up the new value
        @param value: list value
        @type value: list

        '''
        if not isinstance(value, list):
            raise Exception('value is not a list please Define the List')

        self._color_value = value
        return self._color_value

class COLOR_VARIABLE():
    '''
    this is the color variable which will be include all the related to color in the widget
    can be get and set new value to change the widget color
    '''
    def __init__(self):



        # 18color
        self.red_color = COLOR_VARIABLE_CHILD(value=[254, 0, 2])
        self.blue_color = COLOR_VARIABLE_CHILD(value=[1, 0, 254])
        self.green_color = COLOR_VARIABLE_CHILD(value=[1, 154, 1])
        self.orange_color = COLOR_VARIABLE_CHILD(value=[255, 154, 0])
        self.yellow_color = COLOR_VARIABLE_CHILD(value=[255, 255, 1])
        self.pink_color = COLOR_VARIABLE_CHILD(value=[255, 205, 208])
        self.purple_color = COLOR_VARIABLE_CHILD(value=[152, 0, 134])
        self.violet_color = COLOR_VARIABLE_CHILD(value=[255, 131, 243])
        self.turquoise_color = COLOR_VARIABLE_CHILD(value=[0, 225, 209])
        self.gold_color = COLOR_VARIABLE_CHILD(value=[255, 216, 1])
        self.lime_color = COLOR_VARIABLE_CHILD(value=[1, 255, 1])
        self.aqua_color = COLOR_VARIABLE_CHILD(value=[99, 255, 255])
        self.navy_color = COLOR_VARIABLE_CHILD(value=[2, 0, 133])
        self.coral_color = COLOR_VARIABLE_CHILD(value=[255, 128, 77])
        self.teal_color = COLOR_VARIABLE_CHILD(value=[1, 129, 132])
        self.brown_color = COLOR_VARIABLE_CHILD(value=[193, 37, 40])
        self.white_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.black_color = COLOR_VARIABLE_CHILD(value=[80, 80, 80])

        basic_font_radius_size = 10
        basic_font_weight = 'bold'


        #make a object color
        self.nurbsCurve_color = self.orange_color
        self.dynamicConstraint_color = self.green_color
        self.transform_color = self.blue_color
        self.mesh_color = self.yellow_color
        self.ncloth_color = self.pink_color
        self.locator_color = self.pink_color
        self.camera_color = self.violet_color
        self.nucleus_color = self.red_color
        self.clusterHandle_color = self.lime_color
        self.light_color = self.brown_color

        #CFX COLOR
        self.nCloth_color = self.lime_color
        self.nRigit_color = self.orange_color
        self.nConstraint_color = self.yellow_color
        self.nHair_color = self.red_color
        self.folical_color = self.gold_color

        # PUSHBUTTON BASIC 1 COLOR
        self.pushbutton_basic_1_background_color = COLOR_VARIABLE_CHILD(value=[117, 138, 255])
        self.pushbutton_basic_1_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_1_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_1_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_1_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_1_background_hover_color = COLOR_VARIABLE_CHILD(value=[0, 145, 80])

        # PUSHBUTTON BASIC 2 COLOR
        self.pushbutton_basic_2_background_color = COLOR_VARIABLE_CHILD(value=[254, 82, 147])
        self.pushbutton_basic_2_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_2_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_2_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_2_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_2_background_hover_color = COLOR_VARIABLE_CHILD(value=[189, 61, 110])

        # PUSHBUTTON BASIC 3 COLOR
        self.pushbutton_basic_3_background_color = COLOR_VARIABLE_CHILD(value=[250, 37, 71])
        self.pushbutton_basic_3_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_3_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_3_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_3_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_3_background_hover_color = COLOR_VARIABLE_CHILD(value=[198, 28, 57])

        # PUSHBUTTON BASIC 4 COLOR
        self.pushbutton_basic_4_background_color = COLOR_VARIABLE_CHILD(value=[255, 132, 61])
        self.pushbutton_basic_4_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_4_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_4_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_4_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_4_background_hover_color = COLOR_VARIABLE_CHILD(value=[202, 102, 48])

        # PUSHBUTTON BASIC 5 COLOR
        self.pushbutton_basic_5_background_color = COLOR_VARIABLE_CHILD(value=[104, 99, 160])
        self.pushbutton_basic_5_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_5_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_5_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_5_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_5_background_hover_color = COLOR_VARIABLE_CHILD(value=[136, 131, 211])

        # PUSHBUTTON BASIC 6 COLOR
        self.pushbutton_basic_6_background_color = COLOR_VARIABLE_CHILD(value=[0, 143, 254])
        self.pushbutton_basic_6_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_6_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_6_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_6_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_6_background_hover_color = COLOR_VARIABLE_CHILD(value=[0, 105, 186])

        # PUSHBUTTON BASIC 7 COLOR
        self.pushbutton_basic_7_background_color = COLOR_VARIABLE_CHILD(value=[188, 188, 188])
        self.pushbutton_basic_7_color = COLOR_VARIABLE_CHILD(value=[255, 255, 255])
        self.pushbutton_basic_7_font_size = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_7_font_weight = COLOR_VARIABLE_CHILD(value=basic_font_weight)
        self.pushbutton_basic_7_font_radius = COLOR_VARIABLE_CHILD(value=basic_font_radius_size)
        self.pushbutton_basic_7_background_hover_color = COLOR_VARIABLE_CHILD(value=[220, 220, 220])


        self.background_color = COLOR_VARIABLE_CHILD(value=[0, 255, 132])
        self.new_background_color = COLOR_VARIABLE_CHILD(value=[0, 39, 46])
        self.background_another_color = COLOR_VARIABLE_CHILD(value=[43, 82, 112])
        self.color = COLOR_VARIABLE_CHILD(value=[0, 255, 0])

        # TITLE LABEL
        self.title_label = COLOR_VARIABLE_CHILD(value=[0, 255, 0])

        # MINIMIZE COLOR
        self.minimize_color = COLOR_VARIABLE_CHILD(value=[0, 255, 0])
        self.minimize_hover_color = COLOR_VARIABLE_CHILD(value=[20, 145, 1])

        # MAXIMIZE COLOR
        self.maximize_color = COLOR_VARIABLE_CHILD(value=[255, 255, 0])
        self.maximize_hover_color = COLOR_VARIABLE_CHILD(value=[166, 166, 0])

        # CLOSE COLOR
        self.close_color = COLOR_VARIABLE_CHILD(value=[255, 0, 0])
        self.close_hover_color = COLOR_VARIABLE_CHILD(value=[171, 0, 0])

        # DOCK WIDGET COLOR
        self.dockwidget_color = COLOR_VARIABLE_CHILD(value=[0, 255, 0])
        self.dockwidget_hover_color = COLOR_VARIABLE_CHILD(value=[255, 85, 0])
        self.splitter_background_color = COLOR_VARIABLE_CHILD(value=[255, 85, 0])

        # USER TOOL COLOR
        self.user_tool_color = COLOR_VARIABLE_CHILD(value=[74, 74, 74])
        self.user_help_color = COLOR_VARIABLE_CHILD(value=[74, 74, 74])



    def color_list(self):
        color_list = [[255, 0, 0], (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (192,192,192),
                      (128,128,128), (128,0,0), (128,128,0), (0,128,0), (128,0,128), (0,128,128), (0,0,128),
                      (128,0,0), (139,0,0), (165,42,42), (178,34,34), (220,20,60), (255,0,0), (255,99,71), (255,127,80),
                      (205,92,92), (240,128,128), (233,150,122), (250,128,114), (255,160,122), (255,69,0), (255,140,0),
                      (255,165,0), (255,215,0)]

        return color_list

    def bright_color(self):

        return [self.red_color, self.blue_color, self.green_color, self.orange_color,
                self.yellow_color, self.pink_color, self.purple_color, self.violet_color,
                self.turquoise_color, self.gold_color, self.lime_color, self.aqua_color, self.navy_color,
                self.coral_color, self.teal_color, self.brown_color, self.white_color, self.black_color]









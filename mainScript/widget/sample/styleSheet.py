
import re


class STYLESHEET():
    '''
        THIS IS A STYLE SHEET TEMPLATES FOR THE SAMPLE WIDGET TEMPLATE STYLESHEET
        HERE YOU CAN CREATE AS MANY AS STYLESHEET AND APPLY TO SAMPLE WIDGET TEMPLATE
    '''
    def __init__(self):
        self.background_color_str = 'background-color'
        self.background = 'background'
        self.color_str = 'color'
        self.border = 'border'
        self.padding = 'padding'
        self.padding_top = 'padding-top'
        self.padding_bottom = 'padding-bottom'
        self.padding_left = 'padding-left'
        self.padding_right = 'padding-right'
        self.selection_background_color = 'selection-background-color'
        self.selection_color = 'selection-color'
        self.spacing = 'spacing'
        self.width = 'width'
        self.height = 'height'
        self.margine_top = 'margin-top'
        self.margine_bottom = 'margin-bottom'
        self.image = 'image'
        self.margin = 'margin'
        self.margine_left = 'margin-left'
        self.margine_right = 'margin-right'
        self.opacity = 'opacity'
        self.outline = 'outline'
        self.font_weight = 'font-weight'
        self.border_radius = 'border-radius'
        self.subcontrol_origin = 'subcontrol-origin'
        self.subcontrol_position = 'subcontrol-position'
        self.left = 'left'
        self.alternate_background_color = 'alternate-background-color'
        self.max_width = 'min-width'
        self.min_width = 'min-width'
        self.border_left = 'border-left'

    def color_sample(self, string_val, color):
        '''
        CREATE A COLOR SAMPLE
        @param string_val: GET STRING VALUE DATA
        @param color: GET COLOR VALUE
        @return:
        '''
        if type(color) == str:
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
            if match:
                string_val = ' '.join([string_val, color, ';\n'])
            else:
                RuntimeError('Please HEX Job is not Valid')
        if type(color) == list:
            str_list = str(color)
            if len(color) == 3:
                string_val = '%s rgb(%s, %s, %s);\n' %(string_val, color[0], color[1], color[2])      #f'{string_val} rgb({color[0]}, {color[1]}, {color[2]});\n'
            elif len(color) == 4:
                string_val = '%s rgb(%s, %s, %s, %s);\n' %(string_val, color[0], color[1], color[2], color[3])  #f'{string_val} rgb({color[0]}, {color[1]}, {color[2]}, {color[3]});\n'
        else:
            RuntimeError('Please Do Specify the string or list for the color')

        return string_val

    def set_background_color(self, color):
        '''
        CREATE A STYLESHEET FOR THE BACKGROUND COLOR
        @param color: SPECIFY THE LIST OF THE COLOR [0, 0, 0, 0] OR str
        @return: str
        '''
        string_val = self.color_sample(self.background_color_str + ':', color=color)
        return string_val

    def set_color(self, color):
        '''
        CREATE A STYLESHEET FOR THE COLOR
        @param color: SPECIFY THE LIST OF THE COLOR [0, 0, 0, 0] OR str
        @return: str
        '''
        string_val = self.color_sample(self.color_str + ' : ', color=color)
        return string_val

    def set_border(self, pix, type, color):
        '''
        CREATE A STYLESHEET FOR THE SETBORDER
        @param pix: SPECIFY THE PIXAL
        @param type: SPECIFY THE TYPE
        @param color: SPECIFY THE COLOR
        @return:
        '''
        string_val  = '%s: %spx %s' % (self.border, pix, type)    #f'{self.border}: {pix}px {type} '

        string_val = self.color_sample(string_val, color=color)
        return string_val

    def set_padding(self, padding_val):
        '''
        CREATE A STYLESHEET FOR THE PADDING
        @param padding_val: SPECIFY THE PADDING
        @return:
        '''
        string_val = '%s: %spx;\n' %(self.padding, padding_val)   #f'{self.padding}: {padding_val}px;\n'
        return string_val

    def set_padding_top(self, value):
        '''
        CREATE A PADDING TOP
        @param value: SPECOIFY THE PADDING TOP
        @return:
        '''
        string_val = '%s:%spx\n' %(self.padding_top, value) #f'{self.padding_top}: {value}px;\n'
        return string_val

    def set_padding_bottom(self, value):
        '''
        CREATE A PADDING TOP
        @param value: SPECOIFY THE PADDING TOP
        @return:
        '''
        string_val = '%s:%spx\n' %(self.padding_bottom, value) #f'{self.padding_bottom}: {value}px;\n'
        return string_val

    def set_padding_left(self, value):
        '''
        CREATE PADDING LEFT
        @param value: SPECIFY THE VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.padding_left, value) #f'{self.padding_left}: {value}px;\n'
        return string_val

    def set_padding_right(self, value):
        '''
        CREATE PADDING RIGHT
        @param value: SPECIFY THE VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.padding_right, value) #f'{self.padding_right}: {value}px;\n'
        return string_val

    def set_selection_background_color(self, color):
        '''
        CREATE A STYLESHEET FOR THE SELECTION BACKGROUND COLOR
        @param color: SELECTION BACKGROUND COLOR
        @return:
        '''
        string_val = self.color_sample(self.selection_background_color + ':', color=color)
        return string_val

    def set_selection_color(self, color):
        '''
        CREATE A STYLESHEET FOR THE
        @param color: SELECTION SELECTION COLOR
        @return:
        '''

        string_val = self.color_sample(self.selection_color + ':', color=color)
        return string_val

    def set_spacing(self, value):
        '''
        CREATE A SPACING
        @param value: SPACING VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.spacing, value) #f'{self.spacing}: {value}px;\n'
        return string_val

    def set_width(self, value):
        '''
        SET WIDTH
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.width, value) #f'{self.width}: {value}px;\n'
        return  string_val

    def set_height(self, value):
        '''
        SET HEIGHT
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.height, value) #f'{self.height}: {value}px;\n'
        return  string_val

    def set_margine_top(self, value):
        '''
        SET MARGINE TOP
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.margine_top, value) #f'{self.margine_top}: {value}px;\n'
        return string_val

    def set_margine_bottom(self, value):
        '''
        SET MARGINE BOTTOM
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.margine_bottom, value) #f'{self.margine_bottom}: {value}px;\n'
        return string_val

    def set_image(self, value):
        '''
        SET IMAGE
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:url("%s");\n' %(self.image, value) #f'{self.image}: url("{value}");\n'
        return string_val

    def set_margin_left(self, value):
        '''
        SET MARGIN LEFT
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.margine_left, value) #f'{self.margine_left}: {value}px;\n'
        return string_val

    def set_margin_right(self, value):
        '''
        SET MARGIN RIGHT
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.margine_right, value) #f'{self.margine_right}: {value}px;\n'
        return string_val

    def set_background(self, value):
        '''
        SET BACKGROUND
        @param value: SET VALUE
        @return:
        '''

        string_val = self.color_sample(self.background + ' : ', color=value)
        return string_val

    def set_opacity(self, value):
        '''
        SET OPECITY
        @param value: SET VALUE
        @return:
        '''

        string_val = '%s:%s\n' %(self.opacity, value) #f'{self.opacity}: {value};\n'
        return string_val

    def set_outline(self, value):
        '''
        SET OUTLINE
        @param value: SET VALUE
        @return:string_val
        '''
        string_val = '%s:%s\n' %(self.outline, value) #f'{self.outline}: {value};\n'
        return string_val

    def set_font_weight(self, value):
        '''
        SET FONT WEIGHT
        @param value:
        @return:string_val
        '''
        string_val = '%s:%s\n' %(self.font_weight, value) #f'{self.font_weight}: {value};\n'
        return string_val

    def set_border_radius(self, value):
        '''
        SET FONT BORDER RADIUS
        @param value: SET VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.border_radius, value) #f'{self.border_radius}: {value}px;\n'
        return string_val

    def set_subcontrol_origin(self, value):
        '''
        SET SUBCONTROL ORIGIN
        @param value:
        @return:
        '''
        string_val = '%s:%s\n' %(self.subcontrol_origin, value) #f'{self.subcontrol_origin}: {value};\n'
        return string_val

    def set_subcontrol_poistion(self, pos_one, pos_two):
        '''
        SET SUBCONTROL POSITION
        @param pos_one: SET THE POSITION ONE
        @param pos_two: SET THE POSITION TWO
        @return:
        '''
        string_val = '%s: %s %s;\n' %(self.subcontrol_position, pos_one, pos_two) #f'{self.subcontrol_position}: {pos_one} {pos_two};\n'
        return string_val

    def set_left(self, value):
        '''
        SET LEFT POSITION
        @param value: SET POTION VALUE
        @return:
        '''
        string_val = '%s:%s\n' %(self.left, value) #f'{self.left}: {value};\n'
        return string_val

    def set_margin(self, value):
        '''
        SET MARGIN VALUE
        @param value: SET MARGIN VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.margin, value) #f'{self.margin}: {value}px;\n'
        return string_val

    def set_alternate_background_color(self, color):
        '''
        SET ALTERNATE BACKGROUND COLOR
        @param value: SET ALTERNALT NBACKGROUND COLOR
        @return:
        '''
        string_val = self.color_sample(self.alternate_background_color + ':', color=color)
        return string_val

    def set_max_width(self, value):
        '''
        SET MAX WIDTH
        @param value: SET MAX VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.max_width, value) #f'{self.max_width}: {value}px;\n'
        return string_val

    def set_min_width(self, value):
        '''
        SET MAX WIDTH
        @param value: SET MAX VALUE
        @return:
        '''
        string_val = '%s:%spx\n' %(self.min_width, value) #f'{self.min_width}: {value}px;\n'
        return string_val

    def set_border_left(self, pix, type, color):
        '''
        SET BORDER LEFT
        @param pix: SET THE PIX VALUE IT SHOULD BE INT
        @param type: SET THE TYPE IT SHOULD BE STRING
        @param color: SET THE COLOR IT COULD BE STRING OR LIST OF THE COLOR
        @return:
        '''
        if pix != int or  type != str or  color != str or  color != list:
            RuntimeError('something is missing in the list please specicyfy the proper')


        string_val = '%s: %spx %s' %(self.border_left, pix, type) #f'{self.border_left}: {pix}px {type} '

        string_val = self.color_sample(string_val, color=color)
        return string_val
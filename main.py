from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        pass

    def on_x_release(self):
        pass

    def on_triangle_press(self):
        pass

    def on_triangle_release(self):
        pass

    def on_circle_press(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    def on_L1_press(self):
        pass

    def on_L1_release(self):
        pass

    def on_L2_press(self, value):
        pass

    def on_L2_release(self):
        pass

    def on_R1_press(self):
        pass

    def on_R1_release(self):
        pass

    def on_R2_press(self, value):
        pass

    def on_R2_release(self):
        pass

    def on_up_arrow_press(self):
        pass

    def on_up_down_arrow_release(self):
        pass

    def on_down_arrow_press(self):
        pass

    def on_left_arrow_press(self):
        pass

    def on_left_right_arrow_release(self):
        pass

    def on_right_arrow_press(self):
        pass

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        #print("on_L3_down: {}".format(value))
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_y_at_rest(self):
        pass

    def on_L3_x_at_rest(self):
        pass

    def on_L3_press(self):
        pass

    def on_L3_release(self):
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_y_at_rest(self):
        pass

    def on_R3_x_at_rest(self):
        pass

    def on_R3_press(self):
        pass

    def on_R3_release(self):
        pass

    def on_options_press(self):
        pass

    def on_options_release(self):
        pass

    def on_share_press(self):
        pass

    def on_share_release(self):
        pass

    def on_playstation_button_press(self):
        pass

    def on_playstation_button_release(self):
        pass


interfaces = []
interface_in_use = ""
for i in range (0, 100):
    try:
        open(f"/dev/input/js{i}")
        interfaces.append(f"/dev/input/js{i}")


    except FileNotFoundError:
        pass

print("Available Interfaces :\n")
for index, interface in enumerate(interfaces):
    print(f"{index} : {interface}")

interface_choice = input("\n\nInterface >>")
interface_in_use = interfaces[interface_choice]

print(interface_in_use)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
print(controller.interface)
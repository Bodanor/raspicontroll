import sys
import logging
import datetime
import contextlib

from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.logger_controller = logging.getLogger(controller.interface)
    def on_x_press(self):
        self.logger_controller.info("BUTTON_X_PRESSED")

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


#Logging settings
log_now = datetime.datetime.now()
log_now = log_now.strftime("%y_%m_%d-%H_%M_%S")
logging.basicConfig(level=logging.DEBUG, filename=f'log-{log_now}', format='[%(asctime)s] [%(name)s] %(message)s')

# Interface variables

interfaces = []
interface_in_use = ""
interface_found = False
scanning = True

#Scanning for interfaces

while scanning == True:
    for i in range (0, 100):
        try:
            open(f"/dev/input/js{i}")
            interfaces.append(f"/dev/input/js{i}")
            interface_found = True


        except Exception as e:
            pass

    if not interface_found:
        scan_choice = input("No interfaces found. Would you like to scan again ? (y/n)")
        logging.info("No interface found")
        if (scan_choice == "y" or scan_choice == "Y" or scan_choice == "YES" or scan_choice == "yes"):
            scanning = True
            logging.info("Scanning again")
        else:
            logging.info("Exiting program")
            sys.exit(0)

    else:
        scanning = False

#Printing the interfaces and choose one

print("Available Interfaces :\n")

for index, interface in enumerate(interfaces):
    print(f"{index} : {interface}")
    logging.info(f"Found interface : {interface}")

interface_in_use = input("\n\nInterface to use >> ")
interface_in_use = interfaces[int(interface_in_use)]

logging.info(f"Interface choosed : {interface_in_use}")
# Listening for input from the interface
try:
    controller = MyController(interface=interface_in_use, connecting_using_ds4drv=False)
    controller.listen()

except Exception as e:
    logging.error("Exception occured with the interface", exc_info=True)
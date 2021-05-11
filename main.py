import sys
import logging
import datetime
import contextlib

from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.logger_controller = logging.getLogger(self.interface)
    def on_x_press(self):
        self.logger_controller.info("BUTTON_X_PRESSED")

    def on_x_release(self):
        self.logger_controller.info("BUTTON_X_RELEASED")

    def on_triangle_press(self):
        self.logger_controller.info("BUTTON_TRIANGLE_PRESSED")

    def on_triangle_release(self):
        self.logger_controller.info("BUTTON_TRIANGLE_RELEASED")

    def on_circle_press(self):
        self.logger_controller.info("BUTTON_CIRCLE_PRESSED")

    def on_circle_release(self):
        self.logger_controller.info("BUTTON_CIRCLE_RELEASED")

    def on_square_press(self):
        self.logger_controller.info("BUTTON_SQUARE_PRESSED")

    def on_square_release(self):
        self.logger_controller.info("BUTTON_SQUARE_RELEASED")

    def on_L1_press(self):
        self.logger_controller.info("BUTTON_L1_PRESSED")

    def on_L1_release(self):
        self.logger_controller.info("BUTTON_L1_RELEASED")

    def on_L2_press(self, value):
        self.logger_controller.info("BUTTON_L2_PRESSED")

    def on_L2_release(self):
        self.logger_controller.info("BUTTON_L2_RELEASED")

    def on_R1_press(self):
        self.logger_controller.info("BUTTON_R1_PRESSED")

    def on_R1_release(self):
        self.logger_controller.info("BUTTON_R1_RELEASED")

    def on_R2_press(self, value):
        self.logger_controller.info("BUTTON_R2_PRESSED")

    def on_R2_release(self):
        self.logger_controller.info("BUTTON_R2_RELEASED")

    def on_up_arrow_press(self):
        self.logger_controller.info("ARROW_UP_PRESSED")

    def on_up_down_arrow_release(self):
        self.logger_controller.info("ARROW_UP_DOWN_RELEASED")

    def on_down_arrow_press(self):
        self.logger_controller.info("ARROW_DOWN_PRESSED")

    def on_left_arrow_press(self):
        self.logger_controller.info("ARROW_LEFT_PRESSED")

    def on_left_right_arrow_release(self):
        self.logger_controller.info("ARROW_LEFT_RIGHT_RELEASED")

    def on_right_arrow_press(self):
        self.logger_controller.info("ARROW_RIGHT_PRESSED")

    def on_L3_up(self, value):
        self.logger_controller.info(f"JOY_L3_UP : {value}")

    def on_L3_down(self, value):
        self.logger_controller.info(f"JOY_L3_DOWN : {value}")
        pass

    def on_L3_left(self, value):
        self.logger_controller.info(f"JOY_L3_LEFT : {value}")

    def on_L3_right(self, value):
        self.logger_controller.info(f"JOY_L3_RIGHT : {value}")

    def on_L3_y_at_rest(self):
        self.logger_controller.info(f"JOY_L3_Y_AT_REST")

    def on_L3_x_at_rest(self):
        self.logger_controller.info(f"JOY_L3_X_AT_REST")

    def on_L3_press(self):
        self.logger_controller.info(f"JOY_L3_PRESSED")

    def on_L3_release(self):
        self.logger_controller.info(f"JOY_L3_RELEASED")

    def on_R3_up(self, value):
        self.logger_controller.info(f"JOY_R3_UP : {value}")

    def on_R3_down(self, value):
        self.logger_controller.info(f"JOY_R3_DOWN : {value}")

    def on_R3_left(self, value):
        self.logger_controller.info(f"JOY_R3_LEFT : {value}")

    def on_R3_right(self, value):
        self.logger_controller.info(f"JOY_R3_RIGHT : {value}")

    def on_R3_y_at_rest(self):
        self.logger_controller.info(f"JOY_R3_Y_AT_REST")

    def on_R3_x_at_rest(self):
        self.logger_controller.info(f"JOY_R3_X_AT_REST")

    def on_R3_press(self):
        self.logger_controller.info(f"JOY_R3_PRESSED")

    def on_R3_release(self):
        self.logger_controller.info(f"JOY_R3_RELEASED")

    def on_options_press(self):
        self.logger_controller.info(f"BUTTON_OPTIONS_PRESSED")

    def on_options_release(self):
        self.logger_controller.info(f"BUTTON_OPTIONS_RELEASED")

    def on_share_press(self):
        self.logger_controller.info(f"BUTTON_SHARE_PRESSED")

    def on_share_release(self):
        self.logger_controller.info(f"BUTTON_SHARE_RELEASED")

    def on_playstation_button_press(self):
        self.logger_controller.info(f"BUTTON_PS_PRESSED")

    def on_playstation_button_release(self):
        self.logger_controller.info(f"BUTTON_PS_RELEASED")

    def disconnect(self):
        self.logger_controller.warning("Interface Disconnected !")


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

valid_interface = False

while valid_interface == False:
    try:
        print("Available Interfaces :\n")

        for index, interface in enumerate(interfaces):
            print(f"{index} : {interface}")
            logging.info(f"Found interface : {interface}")

        interface_in_use = input("\n\nInterface to use >> ")
        if interface_in_use.strip().isdigit():
            interface_in_use = interfaces[int(interface_in_use)]
            valid_interface = True

        else:
            valid_interface = False

        logging.info(f"Interface choosed : {interface_in_use}")

    except Exception as e:
        logging.error("Exception occured at the interfacing choosing menu", exc_info=True)
        valid_interface = False

# Listening for input from the interface
try:
    controller = MyController(interface=interface_in_use, connecting_using_ds4drv=False)
    controller.listen(on_disconnect=controller.disconnect)

except Exception as e:
    logging.error("Exception occured with the interface", exc_info=True)
import usb_hid

# This is only one example of a gamepad descriptor, and may not suit your needs.
GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09, 0x04,  # Usage (Joystick)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x04,  #   Report ID (4)
    0x05, 0x09,  #   Usage Page (Button)
    0x19, 0x01,  #   Usage Minimum (Button 1)
    0x29, 0x21,  #   Usage Maximum (Button 33)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x01,  #   Logical Maximum (1)
    0x75, 0x01,  #   Report Size (1)
    0x95, 0x21,  #   Report Count (33)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x95, 0x01,  #   Report Count (1)
    0x75, 0x07,  #   Report Size (7)
    0x81, 0x01,  #   Input (Constant) for padding
    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x16, 0x00, 0x80,  #   Logical Minimum (-32768)
    0x26, 0xff, 0x7F,  #   Logical Maximum (32767)
    0x09, 0x30,  #   Usage (X)
    0x09, 0x31,  #   Usage (Y)
    0x09, 0x32,  #   Usage (Z)
    0x09, 0x35,  #   Usage (Rz)
    0x75, 0x10,  #   Report Size (16)
    0x95, 0x04,  #   Report Count (4)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,        # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x04,                # Joystick
    report_ids=(4,),           # Descriptor uses report ID 4.
    in_report_lengths=(13,),   # This gamepad sends 10 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     gamepad)
)
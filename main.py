from urllib import request
from time import sleep
import platform
from pynotifier import Notification
import os


class InternetNotifier:
    def __init__(self) -> None:
        self.state = None
        self.timeout = 10
        self.url = "https://www.google.com"
        self.icon = os.path.join(os.getcwd(), '')
        plat = platform.system().lower()
        # for windows notifier requires .ico format
        self.icon += "icon.ico" if plat == "windows" else "icon.png"

        self.check_internet()

    def check_internet(self) -> None:
        while True:
            try:
                request.urlopen(self.url, timeout=10)
                state = True
            except Exception as e:
                state = False

            self.change_state(state)
            sleep(self.timeout)

    def change_state(self, state: bool) -> None:
        if self.state == None:
            # Setting the initial state and returning as we only want to notify when the internet state is changed
            # This is probably because this will be the first execution of program
            self.state = state
            return

        if self.state == state:
            # We don't want to do anything if the states are same
            return

        self.state = state
        self.send_notification()

    def send_notification(self) -> None:
        title = ""
        description = ""

        if self.state:
            title = "Internet is Back"
            description = "Hurray!! internet is back"
        else:
            title = "No Internet"
            description = "Seems like we have no internet"

        Notification(
            title=title,
            description=description,
            icon_path=self.icon,
            duration=10,
            urgency='normal'
        ).send()


Notification(
    title="Checking",
    description="Looks Like its working",
    # icon_path=self.icon,
    duration=5,
    urgency='normal'
).send()


InternetNotifier()

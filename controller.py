import model
from conf import Log
import conf.Configuration as Conf


if __name__ == '__main__':
    Conf.Configuration.Init("setup.cfg")

    # Build GUI
    model.buildGUI()
    Log.LogEvent("Grab Wave Command Invoked", Log.Debug)

import conf.Log

import model

if __name__ == '__main__':
    # Build GUI
    model.buildGUI()
    Log.LogEvent("Grab Wave Command Invoked", Log.Debug)

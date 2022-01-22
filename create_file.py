# Import package json to can write the data at a json file.
import json


class SaveResult:
    """Save the computed data (Inputs + Results)
    into a Json file"""

    def __init__(self, v0, alpha, h_max, x_max):
        """Define values to the dictionary to write files."""
        self.v0 = v0
        self.alpha = alpha
        self.h_max = h_max
        self.x_max = x_max

    def write_file(self, computer_women_file):
        """Define Key:Value pairs where key is the name to
        represent each value. Value is the initial velocity (v0),
        launch angle (alpha), maximum height of the projectile (h_max),
        maximum traveled distance (x_max)"""

        dictionary_computer = {
            "InitialVelocity": self.v0,
            "LaunchAngle": self.alpha,
            "h_max": self.h_max,
            "x_max": self.x_max,
        }

        # Write the dictionary in a json file.
        with open(computer_women_file, "w") as cw:
            json.dump(dictionary_computer, cw)

        return True

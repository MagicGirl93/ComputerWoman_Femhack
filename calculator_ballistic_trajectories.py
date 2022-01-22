# Import module maths to access to the mathematical
import math


class BallisticTrajectories:
    """Calculate quickly the information
    ballistic trajectories."""

    def __init__(self, v0, alpha, g=9.8):
        """Ask Initial Velocity, named as v0,
        and Launch Angle, named as alpha."""
        self.v0 = v0
        self.alpha = alpha
        self.g = g

    def cal_h_max(self):
        """Compute the maximum height of the projectile,
        named as h_max."""
        h_max = (self.v0 * self.v0) / (2 * self.g)
        return h_max

    def cal_x_max(self):
        """Compute the maximum traveled distance,
        named as x_max."""
        x_max = 2 * self.v0 * math.sin(self.alpha * math.pi / 180) / self.g
        return x_max



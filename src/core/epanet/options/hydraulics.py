from enum import Enum

from core.inputfile import Section

from core.epanet.time_patterns.patterns import Pattern


class FlowUnits(Enum):
    """Flow Units"""
    CFS = 1
    GPM = 2
    MGD = 3
    IMGD = 4
    AFD = 5
    LPS = 6
    LPM = 7
    MLD = 8
    CMH = 9
    CMD = 10


class HeadLoss(Enum):
    """Head Loss"""
    H_W = 1
    D_W = 2
    C_M = 3


class Hydraulics(Enum):
    """Hydraulics"""
    USE = 1
    SAVE = 2


class Unbalanced(Enum):
    """What to do if hydraulic solution cannot be reached"""
    STOP = 1
    CONTINUE = 2


class HydraulicsOptions(Section):
    """EPANET Hydraulics Options"""

    SECTION_NAME = "[OPTIONS]"

    # @staticmethod
    # def default():
    #     return EPANETHydraulicOptions(EPANETOptions.SECTION_NAME, None, None, -1)

    def __init__(self, name, value, default_value, index):
        Section.__init__(self, name, value, None, index)
        # TODO: parse "value" argument to extract values for each field, after setting default values below
        # TODO: document valid values in docstrings below and/or implement each as an Enum or class

        self.flow_units = FlowUnits.CFS
        """FlowUnits: units in use for flow values"""

        self.head_loss = HeadLoss.H_W
        """HeadLoss: formula to use for computing head loss"""

        self.specific_gravity = 1.0
        """Ratio of the density of the fluid being modeled to that of water at 4 deg. C"""

        self.relative_viscosity = 1.0
        """Kinematic viscosity of the fluid being modeled relative to that of water at 20 deg. C"""

        self.maximum_trials = 40
        """Maximum number of trials used to solve network hydraulics at each hydraulic time step of a simulation"""

        self.accuracy = 0.001
        """Prescribes the convergence criterion that determines when a hydraulic solution has been reached"""

        self.unbalanced = Unbalanced.STOP
        """Determines what happens if a hydraulic solution cannot be reached within the prescribed number of TRIALS"""

        self.unbalanced_continue = 1
        """If continuing after n trials, continue this many more trials with links held fixed"""

        self.default_pattern = Pattern
        """Default demand pattern to be applied to all junctions where no demand pattern was specified"""

        self.demand_multiplier = 1.0
        """Used to adjust the values of baseline demands for all junctions and all demand categories"""

        self.emitter_exponent = 0.5
        """Specifies the power to which the pressure is raised when computing the flow issuing from an emitter"""

        self.check_frequency = 0.0
        """Undocumented"""

        self.max_check = 0.0
        """Undocumented"""

        self.damp_limit = 0.0
        """Undocumented"""

        self.hydraulics = Hydraulics.SAVE
        """Either SAVE the current hydraulics solution to a file or USE a previously saved hydraulics solution"""

        self.hydraulics_file = ""
        """Hydraulics file to either use or save"""
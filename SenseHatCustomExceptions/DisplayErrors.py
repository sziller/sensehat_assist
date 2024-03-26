"""Exceptions to be rasied when using SenseHat in Sziller's projects"""


class MissingDisplay(Exception):
    """=== Exception name: MissingDisplay ==============================================================================
    Exception should be used when Sense hat stle display or Emulator not found to import.
    ============================================================================================== by Sziller ==="""
    def __init__(self, message="Display not found: you either need sense_hat or sense_emu.\n"
                               "for further help see package README.adoc"):
        self.message = message
        super().__init__(self.message)

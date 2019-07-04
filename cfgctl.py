class cfgctl(object):
    """docstring for CfgCtl."""

    def __init__(self, arg):
        super(cfgctl, self).__init__()
        self.arg = arg

    # @staticmethod
    def BuildDefault():
        """docstring for BuildDefault."""
        example = """
        {
            \"DEBUG_MODE\" : 1
            \"SHELL\" : \"{SHELL}\",
            \"APPDIR\" : \"{APPDIR}\",
            \"LAWDIR\" : \"{LAWDIR}\",
            \"LOG_FILE\" = \"{LOG_FILE}\",
            \"INS_FILE\" : \"{INS_FILE}\",
            \"CLANG\" : \"{CLANG}\",
            \"SCSD\" : { {SCSD} },
            \"CTC\" : { {CTC} }
        }""".format(SHELL="", APPDIR="", LAWDIR="", LOG_FILE="", INS_FILE="",
                    CLANG="SCHLUM2", SDSC="", CTC="")
        print(example)

    # BuildDefault = staticmethod(BuildDefault)

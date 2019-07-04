class Identify(object):
    """docstring for Identify."""

    SC = {
        "AB": "absrc",
        "AC": "acsrc",
        "AD": "adsrc",
        "AM": "amsrc",
        "AP": "apsrc",
        "AR": "arsrc",
        "BL": "blsrc",
        "BN": "bnsrc",
        "BR": "brsrc",
        "CB": "cbsrc",
        "CS": "cssrc",
        "CX": "cxsrc",
        "DT": "dtsrc",
        "EB": "ebsrc",
        "ED": "edsrc",
        "EE": "eesrc",
        "ET": "etsrc",
        "FR": "frsrc",
        "GL": "glsrc",
        "GM": "gmsrc",
        "HR": "hrsrc",
        "IA": "iasrc",
        "IC": "icsrc",
        "IF": "ifsrc",
        "IS": "issrc",
        "LA": "lasrc",
        "LM": "lmsrc",
        "MA": "masrc",
        "MC": "mcsrc",
        "ML": "mlsrc",
        "OE": "oesrc",
        "PA": "pasrc",
        "PB": "pbsrc",
        "PH": "phsrc",
        "PO": "posrc",
        "PR": "prsrc",
        "PW": "pwsrc",
        "RQ": "rqsrc",
        "SA": "sasrc",
        "SI": "sisrc",
        "SL": "slsrc",
        "TA": "tasrc",
        "TE": "tesrc",
        "TM": "tmsrc",
        "TP": "tpsrc",
        "TX": "txsrc",
        "UG": "ugsrc",
        "UN": "unsrc",
        "WF": "wfsrc",
        "WH": "whsrc",
        "WO": "wosrc",
        "XC": "xcsrc",
        "XP": "xpsrc",
        "XQ": "xqsrc",
        "XR": "xrsrc",
        "ZL": "zlsrc",
        "ZP": "zpsrc",
        "ZR": "zrsrc",
        "ZT": "ztsrc",
        "BASE": "src"
    }      # TODO: migrate to config.json

    LAWDIR = ""    # TODO: migrate to config.json
    PL = ""        # TODO: self aquire

    def __init__(self, lawdir, product_line):
        super(Identify, self).__init__()

        self.LAWDIR = lawdir
        self.PL = product_line

    def SCsrc(self, system_code):
        return self.LAWDIR + '/' + self.PL + '/' + self.SC[system_code] + '/'

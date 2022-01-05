from random import choice



class Cor():
    def __init__(self):
        self.p = "\033[;30m"
        self.vr = "\033[;31m"
        self.vd = "\033[;32m"
        self.ar = "\033[;33m"
        self.az = "\033[;34m"
        self.m = "\033[;35m"
        self.c = "\033[;36m"
        self.cc = "\033[;37m"
        self.ce = "\033[;90m"
        self.vrc = "\033[;91m"
        self.vdc = "\033[;92m"
        self.arc = "\033[;93m"
        self.azc = "\033[;94m"
        self.mc = "\033[;95m"
        self.cic = "\033[;96m"
        self.b = "\033[;97m"
        self.fp = "\033[;40m"
        self.fvr = "\033[;41m"
        self.fvd = "\033[;42m"
        self.far = "\033[;43m"
        self.faz = "\033[;44m"
        self.fm = "\033[;45m"
        self.fc = "\033[;46m"
        self.fcc = "\033[;47m"
        self.fce = "\033[;100m"
        self.fvrc = "\033[;101m"
        self.fvdc = "\033[;102m"
        self.farc = "\033[;103m"
        self.fazc = "\033[;104m"
        self.fmc = "\033[;105m"
        self.fcic = "\033[;106m"
        self.fb = "\033[;107m"
        self.n = "\033[1m"
        self.s = "\033[4m"
        self.i = "\033[7m"
        self.a = "\033[m"
    
    def colorir(self, string: str = "") -> str:
        stringColorida: str = ""
        cores = [self.vr, self.vd, self.ar, self.az, self.m, self.c, self.vrc, self.vdc, self.arc, self.azc, self.mc, self.cc]

       
        for i in range(0, len(string)):
            stringColorida = stringColorida + choice(cores) + string[i]


        return stringColorida

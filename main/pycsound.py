
from main.exceptions import CsoundFileCompilationError, FileExtensionError, SaveError, CsoundError
from typing import TextIO
import subprocess
import os
import platform
import sys
from main.perf_graph import PlotPerformance

class main:

    def __init__(self) -> None:
        self.__options = None
        self.__header = {"sr": 44100, "ksmps": 1, "nchnls": 2, "0dbfs": 1}
        self.__orc = None
        self.__sco = None
        self.__score_statements = {"i": {}}
        self.__instruments_params = {"i": {}}

    @property
    def options(self):
        return self.__options
    
    @options.setter
    def options(self, opt: str) -> None:
        self.__options = opt.split(" ")
    
    @property
    def orc(self):
        return self.__orc
    
    @orc.setter
    def orc(self, orchestra: str) -> None:
        self.__orc = orchestra
    
    @property
    def sco(self):
        return self.__sco
    
    @sco.setter
    def sco(self, score: str) -> None:
        self.__sco = score
    
    @property
    def header(self):
        return self.__header
    
    @header.setter
    def header(self, header: dict) -> None:
        self.__header = header
    
    def add_score_statement(self, statement: str, params: list) -> None:

        """
        Generate score statements, see Csound manual at http://www.csounds.com/manual/html/ScoreStatements.html

        :param -> statement: statement type
        :param -> params: list of params to pass
        """

        assert statement in ["i", "f", "t"], "[INFO] statement not yet implemented!"
        
        string_params = " ".join(list(map(str, params)))

        if statement == "i":

            # dict for instruments params
            if params[0] in self.__instruments_params["i"]:
                self.__instruments_params["i"][params[0]].append(params[1:])
            else:
                self.__instruments_params["i"][params[0]] = [params[1:]]
            
            stat = "i " + string_params
            key = "i" + str(params[0])
            if key in self.__score_statements["i"]:
                self.__score_statements["i"][key] += stat + "\n"
            else:
                self.__score_statements["i"][key] = stat + "\n"
        else:
            stat = statement + " " + string_params
            if statement in self.__score_statements:
                self.__score_statements[statement] += stat + "\n"
            else:
                self.__score_statements[statement] = stat + "\n"

    def compile(self) -> str:

        """
        Compile orchestra and score file
        """

        try:
            if self.__orc is None:
                raise CsoundFileCompilationError
        except CsoundFileCompilationError:
            print("[ERROR] Compilation error: no orchestra or score file!")
            sys.exit()

        head = ""
        for key in self.__header:
            head += key + " " + "=" + " " + str(self.__header[key]) + "\n"
        self.__orc = "\n" + head + self.__orc

        if self.__sco is None:
            score = ""
            if "f" in self.__score_statements:
                score += self.__score_statements["f"]
            if "t" in self.__score_statements:
                score += self.__score_statements["t"]
            
            instrument_list = ""
            for instrument in self.__score_statements["i"]:
                instrument_list += self.__score_statements["i"][instrument]
            if not instrument_list:
                print("[INFO] You have not activated any instrument from the score!")
            self.__sco = score + instrument_list
        
    def run(self, *argv):

        """
        Run Csound

        It is possible to launch csound by compiling 
        by default orc and sco, or indicate in the 
        arguments the path of the individual files orc, sco or csd.
        """

        cmd = "where" if platform.system() == "Windows" else "which"

        try:
            subprocess.call([cmd, "csound"])
        except CsoundError:
            print("[ERROR] Csound not installed!\n")
            sys.exit()

        files = {"orc": None, "sco": None, "csd": None}

        for arg in argv:

            try:
                open_file = open(arg, "r")
            except FileNotFoundError:
                print(f"[ERROR] File {arg} not found!")
                sys.exit()
            
            f = arg.split(".")
            last = f[-1]
            
            try:
                if last not in ["orc", "sco", "csd"]:
                    raise FileExtensionError
            except FileExtensionError:
                print("[ERROR] File extension not allowed!")
                sys.exit()

            files[f[-1]] = arg
        
        if files["csd"] is None:
            compiled_orc = ""
            rem_orc = True
            compiled_sco = ""
            rem_sco = True

            if files["orc"]:
                compiled_orc = files["orc"]
                rem_orc = False
            else:
                with open("temp.orc", "w") as orchestra:
                    orchestra.write(self.__orc)
                compiled_orc = "temp.orc"

            if files["sco"]:
                compiled_sco = files["sco"]
                rem_sco = False
            else:
                with open("temp.sco", "w") as score:
                    score.write(self.__sco)
                compiled_sco = "temp.sco"

        proc = ["csound"]
        for com in self.__options:
            proc.append(com)
        
        if files["csd"] is None:
            proc.append(compiled_orc)
            proc.append(compiled_sco)
        else:
            proc.append(files["csd"])

        subprocess.call(proc)

        if rem_orc:
            os.remove("temp.orc")
        if rem_sco:
            os.remove("temp.sco")
    
    def save_csound_file(self, mode: str, name: str = "", path: str = "") -> TextIO:

        """
        Save orc or sco file generated

        :param -> mode: specifies whether to save orc or sco
        :param -> name: name of file
        :param -> path: path to save the file
        """

        try:
            if mode not in ["orc", "sco", "csd"]:
                raise SaveError
        except SaveError:
            print("[ERROR] The specified type of file to save must be orc, sco or csd!")
            sys.exit()
        
        self.compile()

        name = name if name else "generated_file"

        path = path + "/" if path else ""

        p = path + name + "." + mode
        with open(p, "w") as f:
            if mode == "orc":
                file_to_save = self.__orc
            elif mode == "sco":
                file_to_save = self.__sco
            else:
                file_to_save = "<CsoundSynthesizer>\n<CsOptions>\n"
                file_to_save += " ".join(self.__options) + "\n"
                file_to_save += "</CsOptions>\n<CsInstruments>\n"
                file_to_save += self.__orc
                file_to_save += "</CsInstruments>\n<CsScore>\n"
                file_to_save += self.__sco
                file_to_save += "</CsScore>\n</CsoundSynthesizer>"
            f.write(file_to_save)
    
    def plot_performance(self):
        p = PlotPerformance(database=self.__instruments_params["i"])
        p.time_instr()
        








    


        
    


    
    



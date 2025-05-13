# Generated from ChartParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,56,316,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,0,1,0,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,
        2,1,2,1,2,4,2,58,8,2,11,2,12,2,59,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,4,3,72,8,3,11,3,12,3,73,1,3,1,3,3,3,78,8,3,1,4,1,4,4,4,
        82,8,4,11,4,12,4,83,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,213,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,221,8,6,
        1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,230,8,9,10,9,12,9,233,9,9,1,10,1,
        10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,3,14,246,8,14,1,
        14,3,14,249,8,14,1,14,5,14,252,8,14,10,14,12,14,255,9,14,1,14,1,
        14,1,14,3,14,260,8,14,1,14,5,14,263,8,14,10,14,12,14,266,9,14,1,
        14,3,14,269,8,14,1,15,3,15,272,8,15,1,15,1,15,3,15,276,8,15,1,15,
        1,15,3,15,280,8,15,1,15,1,15,3,15,284,8,15,1,16,3,16,287,8,16,1,
        16,1,16,3,16,291,8,16,1,16,1,16,3,16,295,8,16,1,16,1,16,3,16,299,
        8,16,5,16,301,8,16,10,16,12,16,304,9,16,1,17,1,17,1,17,1,17,3,17,
        310,8,17,1,18,1,18,1,19,1,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,0,4,1,0,15,17,1,0,32,33,1,0,38,41,
        1,0,42,47,341,0,41,1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,63,1,0,0,
        0,8,79,1,0,0,0,10,212,1,0,0,0,12,220,1,0,0,0,14,222,1,0,0,0,16,224,
        1,0,0,0,18,226,1,0,0,0,20,234,1,0,0,0,22,238,1,0,0,0,24,240,1,0,
        0,0,26,242,1,0,0,0,28,245,1,0,0,0,30,271,1,0,0,0,32,286,1,0,0,0,
        34,305,1,0,0,0,36,311,1,0,0,0,38,313,1,0,0,0,40,42,3,2,1,0,41,40,
        1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,
        45,46,5,0,0,1,46,1,1,0,0,0,47,50,3,4,2,0,48,50,3,6,3,0,49,47,1,0,
        0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,52,5,54,0,0,52,53,5,50,0,0,53,
        54,3,28,14,0,54,55,5,51,0,0,55,57,5,52,0,0,56,58,3,2,1,0,57,56,1,
        0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,
        62,5,53,0,0,62,5,1,0,0,0,63,64,5,1,0,0,64,65,3,12,6,0,65,66,5,2,
        0,0,66,67,3,14,7,0,67,68,5,3,0,0,68,77,3,10,5,0,69,71,5,52,0,0,70,
        72,3,2,1,0,71,70,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,
        0,74,75,1,0,0,0,75,76,5,53,0,0,76,78,1,0,0,0,77,69,1,0,0,0,77,78,
        1,0,0,0,78,7,1,0,0,0,79,81,5,52,0,0,80,82,3,2,1,0,81,80,1,0,0,0,
        82,83,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,
        53,0,0,86,9,1,0,0,0,87,88,5,4,0,0,88,89,3,16,8,0,89,90,5,36,0,0,
        90,91,3,24,12,0,91,213,1,0,0,0,92,93,5,5,0,0,93,94,3,16,8,0,94,95,
        5,36,0,0,95,96,3,24,12,0,96,213,1,0,0,0,97,98,5,6,0,0,98,99,3,16,
        8,0,99,100,5,36,0,0,100,101,3,24,12,0,101,213,1,0,0,0,102,103,5,
        7,0,0,103,104,3,16,8,0,104,105,5,36,0,0,105,106,3,24,12,0,106,213,
        1,0,0,0,107,108,5,4,0,0,108,109,3,16,8,0,109,110,5,8,0,0,110,111,
        3,22,11,0,111,112,5,36,0,0,112,113,3,24,12,0,113,213,1,0,0,0,114,
        115,5,4,0,0,115,116,3,16,8,0,116,117,5,9,0,0,117,118,3,22,11,0,118,
        119,5,36,0,0,119,120,3,24,12,0,120,213,1,0,0,0,121,122,5,5,0,0,122,
        123,5,18,0,0,123,124,3,22,11,0,124,125,5,36,0,0,125,126,3,24,12,
        0,126,213,1,0,0,0,127,128,5,10,0,0,128,129,3,16,8,0,129,130,5,11,
        0,0,130,131,3,22,11,0,131,132,5,36,0,0,132,133,3,24,12,0,133,213,
        1,0,0,0,134,135,5,10,0,0,135,136,3,16,8,0,136,137,5,12,0,0,137,138,
        3,22,11,0,138,139,5,36,0,0,139,140,3,24,12,0,140,213,1,0,0,0,141,
        142,5,13,0,0,142,143,3,18,9,0,143,144,5,32,0,0,144,145,3,18,9,0,
        145,213,1,0,0,0,146,147,5,14,0,0,147,148,3,26,13,0,148,149,3,18,
        9,0,149,150,5,2,0,0,150,151,3,20,10,0,151,213,1,0,0,0,152,153,5,
        19,0,0,153,154,3,16,8,0,154,155,5,31,0,0,155,156,3,24,12,0,156,213,
        1,0,0,0,157,158,5,20,0,0,158,159,3,16,8,0,159,160,5,31,0,0,160,161,
        3,24,12,0,161,213,1,0,0,0,162,163,5,21,0,0,163,164,3,16,8,0,164,
        165,5,31,0,0,165,166,3,24,12,0,166,213,1,0,0,0,167,168,5,22,0,0,
        168,169,3,16,8,0,169,170,5,31,0,0,170,171,3,20,10,0,171,213,1,0,
        0,0,172,173,5,23,0,0,173,174,3,16,8,0,174,175,5,31,0,0,175,176,3,
        20,10,0,176,213,1,0,0,0,177,178,5,24,0,0,178,179,3,20,10,0,179,180,
        5,30,0,0,180,213,1,0,0,0,181,182,5,25,0,0,182,183,3,18,9,0,183,184,
        5,36,0,0,184,185,3,24,12,0,185,186,5,2,0,0,186,187,3,20,10,0,187,
        213,1,0,0,0,188,189,5,26,0,0,189,190,3,18,9,0,190,191,5,36,0,0,191,
        192,3,24,12,0,192,213,1,0,0,0,193,194,5,27,0,0,194,195,3,16,8,0,
        195,196,5,32,0,0,196,197,3,16,8,0,197,213,1,0,0,0,198,199,5,28,0,
        0,199,200,3,16,8,0,200,201,5,32,0,0,201,202,3,16,8,0,202,213,1,0,
        0,0,203,204,5,29,0,0,204,205,3,16,8,0,205,206,5,48,0,0,206,207,3,
        16,8,0,207,208,5,48,0,0,208,209,3,16,8,0,209,210,5,36,0,0,210,211,
        3,24,12,0,211,213,1,0,0,0,212,87,1,0,0,0,212,92,1,0,0,0,212,97,1,
        0,0,0,212,102,1,0,0,0,212,107,1,0,0,0,212,114,1,0,0,0,212,121,1,
        0,0,0,212,127,1,0,0,0,212,134,1,0,0,0,212,141,1,0,0,0,212,146,1,
        0,0,0,212,152,1,0,0,0,212,157,1,0,0,0,212,162,1,0,0,0,212,167,1,
        0,0,0,212,172,1,0,0,0,212,177,1,0,0,0,212,181,1,0,0,0,212,188,1,
        0,0,0,212,193,1,0,0,0,212,198,1,0,0,0,212,203,1,0,0,0,213,11,1,0,
        0,0,214,221,3,16,8,0,215,221,3,18,9,0,216,217,3,16,8,0,217,218,5,
        34,0,0,218,219,3,16,8,0,219,221,1,0,0,0,220,214,1,0,0,0,220,215,
        1,0,0,0,220,216,1,0,0,0,221,13,1,0,0,0,222,223,5,55,0,0,223,15,1,
        0,0,0,224,225,5,55,0,0,225,17,1,0,0,0,226,231,5,55,0,0,227,228,5,
        48,0,0,228,230,5,55,0,0,229,227,1,0,0,0,230,233,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,19,1,0,0,0,233,231,1,0,0,0,234,235,5,
        55,0,0,235,236,5,35,0,0,236,237,5,55,0,0,237,21,1,0,0,0,238,239,
        5,55,0,0,239,23,1,0,0,0,240,241,5,55,0,0,241,25,1,0,0,0,242,243,
        7,0,0,0,243,27,1,0,0,0,244,246,5,37,0,0,245,244,1,0,0,0,245,246,
        1,0,0,0,246,248,1,0,0,0,247,249,5,50,0,0,248,247,1,0,0,0,248,249,
        1,0,0,0,249,253,1,0,0,0,250,252,5,37,0,0,251,250,1,0,0,0,252,255,
        1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,253,
        1,0,0,0,256,264,3,30,15,0,257,259,7,1,0,0,258,260,5,37,0,0,259,258,
        1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,263,3,30,15,0,262,257,
        1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,268,
        1,0,0,0,266,264,1,0,0,0,267,269,5,37,0,0,268,267,1,0,0,0,268,269,
        1,0,0,0,269,29,1,0,0,0,270,272,5,50,0,0,271,270,1,0,0,0,271,272,
        1,0,0,0,272,273,1,0,0,0,273,275,3,32,16,0,274,276,5,51,0,0,275,274,
        1,0,0,0,275,276,1,0,0,0,276,277,1,0,0,0,277,279,3,38,19,0,278,280,
        5,50,0,0,279,278,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,283,
        3,32,16,0,282,284,5,51,0,0,283,282,1,0,0,0,283,284,1,0,0,0,284,31,
        1,0,0,0,285,287,5,50,0,0,286,285,1,0,0,0,286,287,1,0,0,0,287,288,
        1,0,0,0,288,290,3,34,17,0,289,291,5,51,0,0,290,289,1,0,0,0,290,291,
        1,0,0,0,291,302,1,0,0,0,292,294,3,36,18,0,293,295,5,50,0,0,294,293,
        1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,298,3,34,17,0,297,299,
        5,51,0,0,298,297,1,0,0,0,298,299,1,0,0,0,299,301,1,0,0,0,300,292,
        1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,33,1,
        0,0,0,304,302,1,0,0,0,305,309,5,55,0,0,306,307,3,36,18,0,307,308,
        5,55,0,0,308,310,1,0,0,0,309,306,1,0,0,0,309,310,1,0,0,0,310,35,
        1,0,0,0,311,312,7,2,0,0,312,37,1,0,0,0,313,314,7,3,0,0,314,39,1,
        0,0,0,25,43,49,59,73,77,83,212,220,231,245,248,253,259,264,268,271,
        275,279,283,286,290,294,298,302,309
    ]

class ChartParser ( Parser ):

    grammarFileName = "ChartParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'with'", "'from'", "'chart:'", "'compare'", 
                     "'differences'", "'contrast'", "'versus'", "'split by'", 
                     "'grouped by'", "'show'", "'stacked by'", "'subgroups'", 
                     "'show correlation between'", "'log'", "'progression of'", 
                     "'trend of'", "'growth of'", "'within'", "'show proportion of'", 
                     "'show share of'", "'show percentage of'", "'show frequency of'", 
                     "'show distribution of'", "'show frequency in'", "'accumulation of'", 
                     "'stacked trend of'", "'scatter plot of'", "'pattern of'", 
                     "'bubble of'", "'buckets'", "'by'", "'and'", "'or'", 
                     "'at'", "'to'", "'for'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", 
                     "','", "':'", "'('", "')'", "'{'", "'}'", "'while'" ]

    symbolicNames = [ "<INVALID>", "WITH", "FROM", "CHART", "COMPARE", "DIFFERENCES", 
                      "CONTRAST", "VERSUS", "SPLIT_BY", "GROUPED_BY", "SHOW", 
                      "STACKED_BY", "SUBGROUPS", "CORRELATION", "LOG", "PROGRESSION_OF", 
                      "TREND_OF", "GROWTH_OF", "WITHIN", "SHOW_PROPORTION", 
                      "SHOW_SHARE", "SHOW_PERCENTAGE", "SHOW_FREQUENCY", 
                      "SHOW_DISTRIBUTION", "SHOW_FREQUENCY_BUCKETS", "ACCUMULATION", 
                      "STACKED_TREND", "SCATTER_PLOT", "PATTERN", "BUBBLE", 
                      "BUCKETS", "BY", "AND", "OR", "AT", "TO", "FOR", "NOT", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LT", "LTE", 
                      "GT", "GTE", "EQ", "NEQ", "COMMA", "COLON", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "WHILE", "IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loop = 2
    RULE_command = 3
    RULE_block = 4
    RULE_chartFunction = 5
    RULE_data = 6
    RULE_table = 7
    RULE_var = 8
    RULE_continuousVar = 9
    RULE_range = 10
    RULE_subgroup = 11
    RULE_cases = 12
    RULE_trendKeyword = 13
    RULE_condition = 14
    RULE_logicalOperation = 15
    RULE_operationBody = 16
    RULE_operation = 17
    RULE_operationSign = 18
    RULE_logicalOperationSign = 19

    ruleNames =  [ "program", "statement", "loop", "command", "block", "chartFunction", 
                   "data", "table", "var", "continuousVar", "range", "subgroup", 
                   "cases", "trendKeyword", "condition", "logicalOperation", 
                   "operationBody", "operation", "operationSign", "logicalOperationSign" ]

    EOF = Token.EOF
    WITH=1
    FROM=2
    CHART=3
    COMPARE=4
    DIFFERENCES=5
    CONTRAST=6
    VERSUS=7
    SPLIT_BY=8
    GROUPED_BY=9
    SHOW=10
    STACKED_BY=11
    SUBGROUPS=12
    CORRELATION=13
    LOG=14
    PROGRESSION_OF=15
    TREND_OF=16
    GROWTH_OF=17
    WITHIN=18
    SHOW_PROPORTION=19
    SHOW_SHARE=20
    SHOW_PERCENTAGE=21
    SHOW_FREQUENCY=22
    SHOW_DISTRIBUTION=23
    SHOW_FREQUENCY_BUCKETS=24
    ACCUMULATION=25
    STACKED_TREND=26
    SCATTER_PLOT=27
    PATTERN=28
    BUBBLE=29
    BUCKETS=30
    BY=31
    AND=32
    OR=33
    AT=34
    TO=35
    FOR=36
    NOT=37
    PLUS=38
    MINUS=39
    MULTIPLY=40
    DIVIDE=41
    LT=42
    LTE=43
    GT=44
    GTE=45
    EQ=46
    NEQ=47
    COMMA=48
    COLON=49
    LPAREN=50
    RPAREN=51
    LBRACE=52
    RBRACE=53
    WHILE=54
    IDENTIFIER=55
    WS=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ChartParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChartParser.StatementContext,i)


        def getRuleIndex(self):
            return ChartParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ChartParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.statement()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==54):
                    break

            self.state = 45
            self.match(ChartParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop(self):
            return self.getTypedRuleContext(ChartParser.LoopContext,0)


        def command(self):
            return self.getTypedRuleContext(ChartParser.CommandContext,0)


        def getRuleIndex(self):
            return ChartParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ChartParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.loop()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ChartParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ChartParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(ChartParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(ChartParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ChartParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChartParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChartParser.StatementContext,i)


        def getRuleIndex(self):
            return ChartParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)




    def loop(self):

        localctx = ChartParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ChartParser.WHILE)
            self.state = 52
            self.match(ChartParser.LPAREN)
            self.state = 53
            self.condition()
            self.state = 54
            self.match(ChartParser.RPAREN)
            self.state = 55
            self.match(ChartParser.LBRACE)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.statement()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==54):
                    break

            self.state = 61
            self.match(ChartParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(ChartParser.WITH, 0)

        def data(self):
            return self.getTypedRuleContext(ChartParser.DataContext,0)


        def FROM(self):
            return self.getToken(ChartParser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(ChartParser.TableContext,0)


        def CHART(self):
            return self.getToken(ChartParser.CHART, 0)

        def chartFunction(self):
            return self.getTypedRuleContext(ChartParser.ChartFunctionContext,0)


        def LBRACE(self):
            return self.getToken(ChartParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChartParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChartParser.StatementContext,i)


        def getRuleIndex(self):
            return ChartParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ChartParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ChartParser.WITH)
            self.state = 64
            self.data()
            self.state = 65
            self.match(ChartParser.FROM)
            self.state = 66
            self.table()
            self.state = 67
            self.match(ChartParser.CHART)
            self.state = 68
            self.chartFunction()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 69
                self.match(ChartParser.LBRACE)
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 70
                    self.statement()
                    self.state = 73 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1 or _la==54):
                        break

                self.state = 75
                self.match(ChartParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ChartParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ChartParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.StatementContext)
            else:
                return self.getTypedRuleContext(ChartParser.StatementContext,i)


        def getRuleIndex(self):
            return ChartParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ChartParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ChartParser.LBRACE)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.statement()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==54):
                    break

            self.state = 85
            self.match(ChartParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChartFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARE(self):
            return self.getToken(ChartParser.COMPARE, 0)

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.VarContext)
            else:
                return self.getTypedRuleContext(ChartParser.VarContext,i)


        def FOR(self):
            return self.getToken(ChartParser.FOR, 0)

        def cases(self):
            return self.getTypedRuleContext(ChartParser.CasesContext,0)


        def DIFFERENCES(self):
            return self.getToken(ChartParser.DIFFERENCES, 0)

        def CONTRAST(self):
            return self.getToken(ChartParser.CONTRAST, 0)

        def VERSUS(self):
            return self.getToken(ChartParser.VERSUS, 0)

        def SPLIT_BY(self):
            return self.getToken(ChartParser.SPLIT_BY, 0)

        def subgroup(self):
            return self.getTypedRuleContext(ChartParser.SubgroupContext,0)


        def GROUPED_BY(self):
            return self.getToken(ChartParser.GROUPED_BY, 0)

        def WITHIN(self):
            return self.getToken(ChartParser.WITHIN, 0)

        def SHOW(self):
            return self.getToken(ChartParser.SHOW, 0)

        def STACKED_BY(self):
            return self.getToken(ChartParser.STACKED_BY, 0)

        def SUBGROUPS(self):
            return self.getToken(ChartParser.SUBGROUPS, 0)

        def CORRELATION(self):
            return self.getToken(ChartParser.CORRELATION, 0)

        def continuousVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.ContinuousVarContext)
            else:
                return self.getTypedRuleContext(ChartParser.ContinuousVarContext,i)


        def AND(self):
            return self.getToken(ChartParser.AND, 0)

        def LOG(self):
            return self.getToken(ChartParser.LOG, 0)

        def trendKeyword(self):
            return self.getTypedRuleContext(ChartParser.TrendKeywordContext,0)


        def FROM(self):
            return self.getToken(ChartParser.FROM, 0)

        def range_(self):
            return self.getTypedRuleContext(ChartParser.RangeContext,0)


        def SHOW_PROPORTION(self):
            return self.getToken(ChartParser.SHOW_PROPORTION, 0)

        def BY(self):
            return self.getToken(ChartParser.BY, 0)

        def SHOW_SHARE(self):
            return self.getToken(ChartParser.SHOW_SHARE, 0)

        def SHOW_PERCENTAGE(self):
            return self.getToken(ChartParser.SHOW_PERCENTAGE, 0)

        def SHOW_FREQUENCY(self):
            return self.getToken(ChartParser.SHOW_FREQUENCY, 0)

        def SHOW_DISTRIBUTION(self):
            return self.getToken(ChartParser.SHOW_DISTRIBUTION, 0)

        def SHOW_FREQUENCY_BUCKETS(self):
            return self.getToken(ChartParser.SHOW_FREQUENCY_BUCKETS, 0)

        def BUCKETS(self):
            return self.getToken(ChartParser.BUCKETS, 0)

        def ACCUMULATION(self):
            return self.getToken(ChartParser.ACCUMULATION, 0)

        def STACKED_TREND(self):
            return self.getToken(ChartParser.STACKED_TREND, 0)

        def SCATTER_PLOT(self):
            return self.getToken(ChartParser.SCATTER_PLOT, 0)

        def PATTERN(self):
            return self.getToken(ChartParser.PATTERN, 0)

        def BUBBLE(self):
            return self.getToken(ChartParser.BUBBLE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.COMMA)
            else:
                return self.getToken(ChartParser.COMMA, i)

        def getRuleIndex(self):
            return ChartParser.RULE_chartFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChartFunction" ):
                listener.enterChartFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChartFunction" ):
                listener.exitChartFunction(self)




    def chartFunction(self):

        localctx = ChartParser.ChartFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_chartFunction)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(ChartParser.COMPARE)
                self.state = 88
                self.var()
                self.state = 89
                self.match(ChartParser.FOR)
                self.state = 90
                self.cases()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(ChartParser.DIFFERENCES)
                self.state = 93
                self.var()
                self.state = 94
                self.match(ChartParser.FOR)
                self.state = 95
                self.cases()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(ChartParser.CONTRAST)
                self.state = 98
                self.var()
                self.state = 99
                self.match(ChartParser.FOR)
                self.state = 100
                self.cases()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.match(ChartParser.VERSUS)
                self.state = 103
                self.var()
                self.state = 104
                self.match(ChartParser.FOR)
                self.state = 105
                self.cases()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.match(ChartParser.COMPARE)
                self.state = 108
                self.var()
                self.state = 109
                self.match(ChartParser.SPLIT_BY)
                self.state = 110
                self.subgroup()
                self.state = 111
                self.match(ChartParser.FOR)
                self.state = 112
                self.cases()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 114
                self.match(ChartParser.COMPARE)
                self.state = 115
                self.var()
                self.state = 116
                self.match(ChartParser.GROUPED_BY)
                self.state = 117
                self.subgroup()
                self.state = 118
                self.match(ChartParser.FOR)
                self.state = 119
                self.cases()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 121
                self.match(ChartParser.DIFFERENCES)
                self.state = 122
                self.match(ChartParser.WITHIN)
                self.state = 123
                self.subgroup()
                self.state = 124
                self.match(ChartParser.FOR)
                self.state = 125
                self.cases()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 127
                self.match(ChartParser.SHOW)
                self.state = 128
                self.var()
                self.state = 129
                self.match(ChartParser.STACKED_BY)
                self.state = 130
                self.subgroup()
                self.state = 131
                self.match(ChartParser.FOR)
                self.state = 132
                self.cases()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.match(ChartParser.SHOW)
                self.state = 135
                self.var()
                self.state = 136
                self.match(ChartParser.SUBGROUPS)
                self.state = 137
                self.subgroup()
                self.state = 138
                self.match(ChartParser.FOR)
                self.state = 139
                self.cases()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 141
                self.match(ChartParser.CORRELATION)
                self.state = 142
                self.continuousVar()
                self.state = 143
                self.match(ChartParser.AND)
                self.state = 144
                self.continuousVar()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 146
                self.match(ChartParser.LOG)
                self.state = 147
                self.trendKeyword()
                self.state = 148
                self.continuousVar()
                self.state = 149
                self.match(ChartParser.FROM)
                self.state = 150
                self.range_()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 152
                self.match(ChartParser.SHOW_PROPORTION)
                self.state = 153
                self.var()
                self.state = 154
                self.match(ChartParser.BY)
                self.state = 155
                self.cases()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 157
                self.match(ChartParser.SHOW_SHARE)
                self.state = 158
                self.var()
                self.state = 159
                self.match(ChartParser.BY)
                self.state = 160
                self.cases()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 162
                self.match(ChartParser.SHOW_PERCENTAGE)
                self.state = 163
                self.var()
                self.state = 164
                self.match(ChartParser.BY)
                self.state = 165
                self.cases()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 167
                self.match(ChartParser.SHOW_FREQUENCY)
                self.state = 168
                self.var()
                self.state = 169
                self.match(ChartParser.BY)
                self.state = 170
                self.range_()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 172
                self.match(ChartParser.SHOW_DISTRIBUTION)
                self.state = 173
                self.var()
                self.state = 174
                self.match(ChartParser.BY)
                self.state = 175
                self.range_()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 177
                self.match(ChartParser.SHOW_FREQUENCY_BUCKETS)
                self.state = 178
                self.range_()
                self.state = 179
                self.match(ChartParser.BUCKETS)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 181
                self.match(ChartParser.ACCUMULATION)
                self.state = 182
                self.continuousVar()
                self.state = 183
                self.match(ChartParser.FOR)
                self.state = 184
                self.cases()
                self.state = 185
                self.match(ChartParser.FROM)
                self.state = 186
                self.range_()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 188
                self.match(ChartParser.STACKED_TREND)
                self.state = 189
                self.continuousVar()
                self.state = 190
                self.match(ChartParser.FOR)
                self.state = 191
                self.cases()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 193
                self.match(ChartParser.SCATTER_PLOT)
                self.state = 194
                self.var()
                self.state = 195
                self.match(ChartParser.AND)
                self.state = 196
                self.var()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 198
                self.match(ChartParser.PATTERN)
                self.state = 199
                self.var()
                self.state = 200
                self.match(ChartParser.AND)
                self.state = 201
                self.var()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 203
                self.match(ChartParser.BUBBLE)
                self.state = 204
                self.var()
                self.state = 205
                self.match(ChartParser.COMMA)
                self.state = 206
                self.var()
                self.state = 207
                self.match(ChartParser.COMMA)
                self.state = 208
                self.var()
                self.state = 209
                self.match(ChartParser.FOR)
                self.state = 210
                self.cases()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.VarContext)
            else:
                return self.getTypedRuleContext(ChartParser.VarContext,i)


        def continuousVar(self):
            return self.getTypedRuleContext(ChartParser.ContinuousVarContext,0)


        def AT(self):
            return self.getToken(ChartParser.AT, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = ChartParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_data)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.continuousVar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.var()
                self.state = 217
                self.match(ChartParser.AT)
                self.state = 218
                self.var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ChartParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = ChartParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ChartParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ChartParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = ChartParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ChartParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuousVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.IDENTIFIER)
            else:
                return self.getToken(ChartParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.COMMA)
            else:
                return self.getToken(ChartParser.COMMA, i)

        def getRuleIndex(self):
            return ChartParser.RULE_continuousVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinuousVar" ):
                listener.enterContinuousVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinuousVar" ):
                listener.exitContinuousVar(self)




    def continuousVar(self):

        localctx = ChartParser.ContinuousVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_continuousVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ChartParser.IDENTIFIER)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 227
                self.match(ChartParser.COMMA)
                self.state = 228
                self.match(ChartParser.IDENTIFIER)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.IDENTIFIER)
            else:
                return self.getToken(ChartParser.IDENTIFIER, i)

        def TO(self):
            return self.getToken(ChartParser.TO, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)




    def range_(self):

        localctx = ChartParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(ChartParser.IDENTIFIER)
            self.state = 235
            self.match(ChartParser.TO)
            self.state = 236
            self.match(ChartParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubgroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ChartParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_subgroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubgroup" ):
                listener.enterSubgroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubgroup" ):
                listener.exitSubgroup(self)




    def subgroup(self):

        localctx = ChartParser.SubgroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_subgroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ChartParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ChartParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_cases

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCases" ):
                listener.enterCases(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCases" ):
                listener.exitCases(self)




    def cases(self):

        localctx = ChartParser.CasesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_cases)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(ChartParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrendKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRESSION_OF(self):
            return self.getToken(ChartParser.PROGRESSION_OF, 0)

        def TREND_OF(self):
            return self.getToken(ChartParser.TREND_OF, 0)

        def GROWTH_OF(self):
            return self.getToken(ChartParser.GROWTH_OF, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_trendKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrendKeyword" ):
                listener.enterTrendKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrendKeyword" ):
                listener.exitTrendKeyword(self)




    def trendKeyword(self):

        localctx = ChartParser.TrendKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_trendKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOperation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.LogicalOperationContext)
            else:
                return self.getTypedRuleContext(ChartParser.LogicalOperationContext,i)


        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.NOT)
            else:
                return self.getToken(ChartParser.NOT, i)

        def LPAREN(self):
            return self.getToken(ChartParser.LPAREN, 0)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.AND)
            else:
                return self.getToken(ChartParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.OR)
            else:
                return self.getToken(ChartParser.OR, i)

        def getRuleIndex(self):
            return ChartParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ChartParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 244
                self.match(ChartParser.NOT)


            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 247
                self.match(ChartParser.LPAREN)


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 250
                self.match(ChartParser.NOT)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self.logicalOperation()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 258
                    self.match(ChartParser.NOT)


                self.state = 261
                self.logicalOperation()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 267
                self.match(ChartParser.NOT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operationBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.OperationBodyContext)
            else:
                return self.getTypedRuleContext(ChartParser.OperationBodyContext,i)


        def logicalOperationSign(self):
            return self.getTypedRuleContext(ChartParser.LogicalOperationSignContext,0)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.LPAREN)
            else:
                return self.getToken(ChartParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.RPAREN)
            else:
                return self.getToken(ChartParser.RPAREN, i)

        def getRuleIndex(self):
            return ChartParser.RULE_logicalOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperation" ):
                listener.enterLogicalOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperation" ):
                listener.exitLogicalOperation(self)




    def logicalOperation(self):

        localctx = ChartParser.LogicalOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logicalOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 270
                self.match(ChartParser.LPAREN)


            self.state = 273
            self.operationBody()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 274
                self.match(ChartParser.RPAREN)


            self.state = 277
            self.logicalOperationSign()
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 278
                self.match(ChartParser.LPAREN)


            self.state = 281
            self.operationBody()
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 282
                self.match(ChartParser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.OperationContext)
            else:
                return self.getTypedRuleContext(ChartParser.OperationContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.LPAREN)
            else:
                return self.getToken(ChartParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.RPAREN)
            else:
                return self.getToken(ChartParser.RPAREN, i)

        def operationSign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ChartParser.OperationSignContext)
            else:
                return self.getTypedRuleContext(ChartParser.OperationSignContext,i)


        def getRuleIndex(self):
            return ChartParser.RULE_operationBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationBody" ):
                listener.enterOperationBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationBody" ):
                listener.exitOperationBody(self)




    def operationBody(self):

        localctx = ChartParser.OperationBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_operationBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 285
                self.match(ChartParser.LPAREN)


            self.state = 288
            self.operation()
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 289
                self.match(ChartParser.RPAREN)


            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4123168604160) != 0):
                self.state = 292
                self.operationSign()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 293
                    self.match(ChartParser.LPAREN)


                self.state = 296
                self.operation()
                self.state = 298
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 297
                    self.match(ChartParser.RPAREN)


                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ChartParser.IDENTIFIER)
            else:
                return self.getToken(ChartParser.IDENTIFIER, i)

        def operationSign(self):
            return self.getTypedRuleContext(ChartParser.OperationSignContext,0)


        def getRuleIndex(self):
            return ChartParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = ChartParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(ChartParser.IDENTIFIER)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 306
                self.operationSign()
                self.state = 307
                self.match(ChartParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ChartParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ChartParser.MINUS, 0)

        def MULTIPLY(self):
            return self.getToken(ChartParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ChartParser.DIVIDE, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_operationSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationSign" ):
                listener.enterOperationSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationSign" ):
                listener.exitOperationSign(self)




    def operationSign(self):

        localctx = ChartParser.OperationSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operationSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4123168604160) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperationSignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ChartParser.LT, 0)

        def LTE(self):
            return self.getToken(ChartParser.LTE, 0)

        def GT(self):
            return self.getToken(ChartParser.GT, 0)

        def GTE(self):
            return self.getToken(ChartParser.GTE, 0)

        def EQ(self):
            return self.getToken(ChartParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ChartParser.NEQ, 0)

        def getRuleIndex(self):
            return ChartParser.RULE_logicalOperationSign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperationSign" ):
                listener.enterLogicalOperationSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperationSign" ):
                listener.exitLogicalOperationSign(self)




    def logicalOperationSign(self):

        localctx = ChartParser.LogicalOperationSignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logicalOperationSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 277076930199552) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






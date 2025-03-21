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
        4,1,54,276,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,167,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,175,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,5,5,184,
        8,5,10,5,12,5,187,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        8,1,8,1,9,1,9,1,10,1,10,1,11,3,11,206,8,11,1,11,3,11,209,8,11,1,
        11,5,11,212,8,11,10,11,12,11,215,9,11,1,11,1,11,1,11,3,11,220,8,
        11,1,11,5,11,223,8,11,10,11,12,11,226,9,11,1,11,3,11,229,8,11,1,
        12,3,12,232,8,12,1,12,1,12,3,12,236,8,12,1,12,1,12,3,12,240,8,12,
        1,12,1,12,3,12,244,8,12,1,13,3,13,247,8,13,1,13,1,13,3,13,251,8,
        13,1,13,1,13,3,13,255,8,13,1,13,1,13,3,13,259,8,13,5,13,261,8,13,
        10,13,12,13,264,9,13,1,14,1,14,1,14,1,14,3,14,270,8,14,1,15,1,15,
        1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,0,4,1,0,15,17,1,0,32,33,1,0,43,46,1,0,47,52,298,0,34,1,0,0,0,
        2,166,1,0,0,0,4,174,1,0,0,0,6,176,1,0,0,0,8,178,1,0,0,0,10,180,1,
        0,0,0,12,188,1,0,0,0,14,194,1,0,0,0,16,198,1,0,0,0,18,200,1,0,0,
        0,20,202,1,0,0,0,22,205,1,0,0,0,24,231,1,0,0,0,26,246,1,0,0,0,28,
        265,1,0,0,0,30,271,1,0,0,0,32,273,1,0,0,0,34,35,5,1,0,0,35,36,3,
        4,2,0,36,37,5,2,0,0,37,38,3,6,3,0,38,39,5,3,0,0,39,40,3,2,1,0,40,
        1,1,0,0,0,41,42,5,4,0,0,42,43,3,8,4,0,43,44,5,36,0,0,44,45,3,18,
        9,0,45,167,1,0,0,0,46,47,5,5,0,0,47,48,3,8,4,0,48,49,5,36,0,0,49,
        50,3,18,9,0,50,167,1,0,0,0,51,52,5,6,0,0,52,53,3,8,4,0,53,54,5,36,
        0,0,54,55,3,18,9,0,55,167,1,0,0,0,56,57,5,7,0,0,57,58,3,8,4,0,58,
        59,5,36,0,0,59,60,3,18,9,0,60,167,1,0,0,0,61,62,5,4,0,0,62,63,3,
        8,4,0,63,64,5,8,0,0,64,65,3,16,8,0,65,66,5,36,0,0,66,67,3,18,9,0,
        67,167,1,0,0,0,68,69,5,4,0,0,69,70,3,8,4,0,70,71,5,9,0,0,71,72,3,
        16,8,0,72,73,5,36,0,0,73,74,3,18,9,0,74,167,1,0,0,0,75,76,5,5,0,
        0,76,77,5,18,0,0,77,78,3,16,8,0,78,79,5,36,0,0,79,80,3,18,9,0,80,
        167,1,0,0,0,81,82,5,10,0,0,82,83,3,8,4,0,83,84,5,11,0,0,84,85,3,
        16,8,0,85,86,5,36,0,0,86,87,3,18,9,0,87,167,1,0,0,0,88,89,5,10,0,
        0,89,90,3,8,4,0,90,91,5,12,0,0,91,92,3,16,8,0,92,93,5,36,0,0,93,
        94,3,18,9,0,94,167,1,0,0,0,95,96,5,13,0,0,96,97,3,10,5,0,97,98,5,
        32,0,0,98,99,3,10,5,0,99,167,1,0,0,0,100,101,5,14,0,0,101,102,3,
        20,10,0,102,103,3,10,5,0,103,104,5,2,0,0,104,105,3,14,7,0,105,167,
        1,0,0,0,106,107,5,19,0,0,107,108,3,8,4,0,108,109,5,31,0,0,109,110,
        3,18,9,0,110,167,1,0,0,0,111,112,5,20,0,0,112,113,3,8,4,0,113,114,
        5,31,0,0,114,115,3,18,9,0,115,167,1,0,0,0,116,117,5,21,0,0,117,118,
        3,8,4,0,118,119,5,31,0,0,119,120,3,18,9,0,120,167,1,0,0,0,121,122,
        5,22,0,0,122,123,3,8,4,0,123,124,5,31,0,0,124,125,3,14,7,0,125,167,
        1,0,0,0,126,127,5,23,0,0,127,128,3,8,4,0,128,129,5,31,0,0,129,130,
        3,14,7,0,130,167,1,0,0,0,131,132,5,24,0,0,132,133,3,14,7,0,133,134,
        5,30,0,0,134,167,1,0,0,0,135,136,5,25,0,0,136,137,3,10,5,0,137,138,
        5,36,0,0,138,139,3,18,9,0,139,140,5,2,0,0,140,141,3,14,7,0,141,167,
        1,0,0,0,142,143,5,26,0,0,143,144,3,10,5,0,144,145,5,36,0,0,145,146,
        3,18,9,0,146,167,1,0,0,0,147,148,5,27,0,0,148,149,3,8,4,0,149,150,
        5,32,0,0,150,151,3,8,4,0,151,167,1,0,0,0,152,153,5,28,0,0,153,154,
        3,8,4,0,154,155,5,32,0,0,155,156,3,8,4,0,156,167,1,0,0,0,157,158,
        5,29,0,0,158,159,3,8,4,0,159,160,5,37,0,0,160,161,3,8,4,0,161,162,
        5,37,0,0,162,163,3,8,4,0,163,164,5,36,0,0,164,165,3,18,9,0,165,167,
        1,0,0,0,166,41,1,0,0,0,166,46,1,0,0,0,166,51,1,0,0,0,166,56,1,0,
        0,0,166,61,1,0,0,0,166,68,1,0,0,0,166,75,1,0,0,0,166,81,1,0,0,0,
        166,88,1,0,0,0,166,95,1,0,0,0,166,100,1,0,0,0,166,106,1,0,0,0,166,
        111,1,0,0,0,166,116,1,0,0,0,166,121,1,0,0,0,166,126,1,0,0,0,166,
        131,1,0,0,0,166,135,1,0,0,0,166,142,1,0,0,0,166,147,1,0,0,0,166,
        152,1,0,0,0,166,157,1,0,0,0,167,3,1,0,0,0,168,175,3,8,4,0,169,175,
        3,10,5,0,170,171,3,8,4,0,171,172,5,34,0,0,172,173,3,8,4,0,173,175,
        1,0,0,0,174,168,1,0,0,0,174,169,1,0,0,0,174,170,1,0,0,0,175,5,1,
        0,0,0,176,177,5,53,0,0,177,7,1,0,0,0,178,179,5,53,0,0,179,9,1,0,
        0,0,180,185,5,53,0,0,181,182,5,37,0,0,182,184,5,53,0,0,183,181,1,
        0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,11,1,0,
        0,0,187,185,1,0,0,0,188,189,5,41,0,0,189,190,5,39,0,0,190,191,3,
        22,11,0,191,192,5,40,0,0,192,193,5,38,0,0,193,13,1,0,0,0,194,195,
        5,53,0,0,195,196,5,35,0,0,196,197,5,53,0,0,197,15,1,0,0,0,198,199,
        5,53,0,0,199,17,1,0,0,0,200,201,5,53,0,0,201,19,1,0,0,0,202,203,
        7,0,0,0,203,21,1,0,0,0,204,206,5,42,0,0,205,204,1,0,0,0,205,206,
        1,0,0,0,206,208,1,0,0,0,207,209,5,39,0,0,208,207,1,0,0,0,208,209,
        1,0,0,0,209,213,1,0,0,0,210,212,5,42,0,0,211,210,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,213,
        1,0,0,0,216,224,3,24,12,0,217,219,7,1,0,0,218,220,5,42,0,0,219,218,
        1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,223,3,24,12,0,222,217,
        1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,228,
        1,0,0,0,226,224,1,0,0,0,227,229,5,42,0,0,228,227,1,0,0,0,228,229,
        1,0,0,0,229,23,1,0,0,0,230,232,5,39,0,0,231,230,1,0,0,0,231,232,
        1,0,0,0,232,233,1,0,0,0,233,235,3,26,13,0,234,236,5,40,0,0,235,234,
        1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,0,237,239,3,32,16,0,238,240,
        5,39,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,243,
        3,26,13,0,242,244,5,40,0,0,243,242,1,0,0,0,243,244,1,0,0,0,244,25,
        1,0,0,0,245,247,5,39,0,0,246,245,1,0,0,0,246,247,1,0,0,0,247,248,
        1,0,0,0,248,250,3,28,14,0,249,251,5,40,0,0,250,249,1,0,0,0,250,251,
        1,0,0,0,251,262,1,0,0,0,252,254,3,30,15,0,253,255,5,39,0,0,254,253,
        1,0,0,0,254,255,1,0,0,0,255,256,1,0,0,0,256,258,3,28,14,0,257,259,
        5,40,0,0,258,257,1,0,0,0,258,259,1,0,0,0,259,261,1,0,0,0,260,252,
        1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,27,1,
        0,0,0,264,262,1,0,0,0,265,269,5,53,0,0,266,267,3,30,15,0,267,268,
        5,53,0,0,268,270,1,0,0,0,269,266,1,0,0,0,269,270,1,0,0,0,270,29,
        1,0,0,0,271,272,7,2,0,0,272,31,1,0,0,0,273,274,7,3,0,0,274,33,1,
        0,0,0,19,166,174,185,205,208,213,219,224,228,231,235,239,243,246,
        250,254,258,262,269
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
                     "'at'", "'to'", "'for'", "','", "':'", "'('", "')'", 
                     "'while'", "'!'", "'+'", "'-'", "'*'", "'/'", "'<'", 
                     "'<='", "'>'", "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "WITH", "FROM", "CHART", "COMPARE", "DIFFERENCES", 
                      "CONTRAST", "VERSUS", "SPLIT_BY", "GROUPED_BY", "SHOW", 
                      "STACKED_BY", "SUBGROUPS", "CORRELATION", "LOG", "PROGRESSION_OF", 
                      "TREND_OF", "GROWTH_OF", "WITHIN", "SHOW_PROPORTION", 
                      "SHOW_SHARE", "SHOW_PERCENTAGE", "SHOW_FREQUENCY", 
                      "SHOW_DISTRIBUTION", "SHOW_FREQUENCY_BUCKETS", "ACCUMULATION", 
                      "STACKED_TREND", "SCATTER_PLOT", "PATTERN", "BUBBLE", 
                      "BUCKETS", "BY", "AND", "OR", "AT", "TO", "FOR", "COMMA", 
                      "COLON", "LPAREN", "RPAREN", "WHILE", "NOT", "PLUS", 
                      "MINUS", "MULTIPLY", "DIVIDE", "LT", "LTE", "GT", 
                      "GTE", "EQ", "NEQ", "IDENTIFIER", "WS" ]

    RULE_command = 0
    RULE_chartFunction = 1
    RULE_data = 2
    RULE_table = 3
    RULE_var = 4
    RULE_continuousVar = 5
    RULE_loop = 6
    RULE_range = 7
    RULE_subgroup = 8
    RULE_cases = 9
    RULE_trendKeyword = 10
    RULE_condition = 11
    RULE_logicalOperation = 12
    RULE_operationBody = 13
    RULE_operation = 14
    RULE_operationSign = 15
    RULE_logicalOperationSign = 16

    ruleNames =  [ "command", "chartFunction", "data", "table", "var", "continuousVar", 
                   "loop", "range", "subgroup", "cases", "trendKeyword", 
                   "condition", "logicalOperation", "operationBody", "operation", 
                   "operationSign", "logicalOperationSign" ]

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
    COMMA=37
    COLON=38
    LPAREN=39
    RPAREN=40
    WHILE=41
    NOT=42
    PLUS=43
    MINUS=44
    MULTIPLY=45
    DIVIDE=46
    LT=47
    LTE=48
    GT=49
    GTE=50
    EQ=51
    NEQ=52
    IDENTIFIER=53
    WS=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ChartParser.WITH)
            self.state = 35
            self.data()
            self.state = 36
            self.match(ChartParser.FROM)
            self.state = 37
            self.table()
            self.state = 38
            self.match(ChartParser.CHART)
            self.state = 39
            self.chartFunction()
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
        self.enterRule(localctx, 2, self.RULE_chartFunction)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ChartParser.COMPARE)
                self.state = 42
                self.var()
                self.state = 43
                self.match(ChartParser.FOR)
                self.state = 44
                self.cases()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(ChartParser.DIFFERENCES)
                self.state = 47
                self.var()
                self.state = 48
                self.match(ChartParser.FOR)
                self.state = 49
                self.cases()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(ChartParser.CONTRAST)
                self.state = 52
                self.var()
                self.state = 53
                self.match(ChartParser.FOR)
                self.state = 54
                self.cases()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(ChartParser.VERSUS)
                self.state = 57
                self.var()
                self.state = 58
                self.match(ChartParser.FOR)
                self.state = 59
                self.cases()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 61
                self.match(ChartParser.COMPARE)
                self.state = 62
                self.var()
                self.state = 63
                self.match(ChartParser.SPLIT_BY)
                self.state = 64
                self.subgroup()
                self.state = 65
                self.match(ChartParser.FOR)
                self.state = 66
                self.cases()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.match(ChartParser.COMPARE)
                self.state = 69
                self.var()
                self.state = 70
                self.match(ChartParser.GROUPED_BY)
                self.state = 71
                self.subgroup()
                self.state = 72
                self.match(ChartParser.FOR)
                self.state = 73
                self.cases()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.match(ChartParser.DIFFERENCES)
                self.state = 76
                self.match(ChartParser.WITHIN)
                self.state = 77
                self.subgroup()
                self.state = 78
                self.match(ChartParser.FOR)
                self.state = 79
                self.cases()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.match(ChartParser.SHOW)
                self.state = 82
                self.var()
                self.state = 83
                self.match(ChartParser.STACKED_BY)
                self.state = 84
                self.subgroup()
                self.state = 85
                self.match(ChartParser.FOR)
                self.state = 86
                self.cases()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 88
                self.match(ChartParser.SHOW)
                self.state = 89
                self.var()
                self.state = 90
                self.match(ChartParser.SUBGROUPS)
                self.state = 91
                self.subgroup()
                self.state = 92
                self.match(ChartParser.FOR)
                self.state = 93
                self.cases()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 95
                self.match(ChartParser.CORRELATION)
                self.state = 96
                self.continuousVar()
                self.state = 97
                self.match(ChartParser.AND)
                self.state = 98
                self.continuousVar()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 100
                self.match(ChartParser.LOG)
                self.state = 101
                self.trendKeyword()
                self.state = 102
                self.continuousVar()
                self.state = 103
                self.match(ChartParser.FROM)
                self.state = 104
                self.range_()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 106
                self.match(ChartParser.SHOW_PROPORTION)
                self.state = 107
                self.var()
                self.state = 108
                self.match(ChartParser.BY)
                self.state = 109
                self.cases()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 111
                self.match(ChartParser.SHOW_SHARE)
                self.state = 112
                self.var()
                self.state = 113
                self.match(ChartParser.BY)
                self.state = 114
                self.cases()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 116
                self.match(ChartParser.SHOW_PERCENTAGE)
                self.state = 117
                self.var()
                self.state = 118
                self.match(ChartParser.BY)
                self.state = 119
                self.cases()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 121
                self.match(ChartParser.SHOW_FREQUENCY)
                self.state = 122
                self.var()
                self.state = 123
                self.match(ChartParser.BY)
                self.state = 124
                self.range_()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 126
                self.match(ChartParser.SHOW_DISTRIBUTION)
                self.state = 127
                self.var()
                self.state = 128
                self.match(ChartParser.BY)
                self.state = 129
                self.range_()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 131
                self.match(ChartParser.SHOW_FREQUENCY_BUCKETS)
                self.state = 132
                self.range_()
                self.state = 133
                self.match(ChartParser.BUCKETS)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 135
                self.match(ChartParser.ACCUMULATION)
                self.state = 136
                self.continuousVar()
                self.state = 137
                self.match(ChartParser.FOR)
                self.state = 138
                self.cases()
                self.state = 139
                self.match(ChartParser.FROM)
                self.state = 140
                self.range_()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 142
                self.match(ChartParser.STACKED_TREND)
                self.state = 143
                self.continuousVar()
                self.state = 144
                self.match(ChartParser.FOR)
                self.state = 145
                self.cases()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 147
                self.match(ChartParser.SCATTER_PLOT)
                self.state = 148
                self.var()
                self.state = 149
                self.match(ChartParser.AND)
                self.state = 150
                self.var()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 152
                self.match(ChartParser.PATTERN)
                self.state = 153
                self.var()
                self.state = 154
                self.match(ChartParser.AND)
                self.state = 155
                self.var()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 157
                self.match(ChartParser.BUBBLE)
                self.state = 158
                self.var()
                self.state = 159
                self.match(ChartParser.COMMA)
                self.state = 160
                self.var()
                self.state = 161
                self.match(ChartParser.COMMA)
                self.state = 162
                self.var()
                self.state = 163
                self.match(ChartParser.FOR)
                self.state = 164
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
        self.enterRule(localctx, 4, self.RULE_data)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.continuousVar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.var()
                self.state = 171
                self.match(ChartParser.AT)
                self.state = 172
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
        self.enterRule(localctx, 6, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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
        self.enterRule(localctx, 10, self.RULE_continuousVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ChartParser.IDENTIFIER)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 181
                self.match(ChartParser.COMMA)
                self.state = 182
                self.match(ChartParser.IDENTIFIER)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def COLON(self):
            return self.getToken(ChartParser.COLON, 0)

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
        self.enterRule(localctx, 12, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ChartParser.WHILE)
            self.state = 189
            self.match(ChartParser.LPAREN)
            self.state = 190
            self.condition()
            self.state = 191
            self.match(ChartParser.RPAREN)
            self.state = 192
            self.match(ChartParser.COLON)
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
        self.enterRule(localctx, 14, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ChartParser.IDENTIFIER)
            self.state = 195
            self.match(ChartParser.TO)
            self.state = 196
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
        self.enterRule(localctx, 16, self.RULE_subgroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 18, self.RULE_cases)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
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
        self.enterRule(localctx, 20, self.RULE_trendKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
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
        self.enterRule(localctx, 22, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(ChartParser.NOT)


            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 207
                self.match(ChartParser.LPAREN)


            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 210
                self.match(ChartParser.NOT)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.logicalOperation()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 218
                    self.match(ChartParser.NOT)


                self.state = 221
                self.logicalOperation()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 227
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
        self.enterRule(localctx, 24, self.RULE_logicalOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 230
                self.match(ChartParser.LPAREN)


            self.state = 233
            self.operationBody()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 234
                self.match(ChartParser.RPAREN)


            self.state = 237
            self.logicalOperationSign()
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(ChartParser.LPAREN)


            self.state = 241
            self.operationBody()
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 242
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
        self.enterRule(localctx, 26, self.RULE_operationBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 245
                self.match(ChartParser.LPAREN)


            self.state = 248
            self.operation()
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 249
                self.match(ChartParser.RPAREN)


            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131941395333120) != 0):
                self.state = 252
                self.operationSign()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 253
                    self.match(ChartParser.LPAREN)


                self.state = 256
                self.operation()
                self.state = 258
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 257
                    self.match(ChartParser.RPAREN)


                self.state = 264
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
        self.enterRule(localctx, 28, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ChartParser.IDENTIFIER)
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 266
                self.operationSign()
                self.state = 267
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
        self.enterRule(localctx, 30, self.RULE_operationSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 131941395333120) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_logicalOperationSign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8866461766385664) != 0)):
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






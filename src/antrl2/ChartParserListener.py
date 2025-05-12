# Generated from ChartParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChartParser import ChartParser
else:
    from ChartParser import ChartParser

# This class defines a complete listener for a parse tree produced by ChartParser.
class ChartParserListener(ParseTreeListener):

    # Enter a parse tree produced by ChartParser#program.
    def enterProgram(self, ctx:ChartParser.ProgramContext):
        pass

    # Exit a parse tree produced by ChartParser#program.
    def exitProgram(self, ctx:ChartParser.ProgramContext):
        pass


    # Enter a parse tree produced by ChartParser#statement.
    def enterStatement(self, ctx:ChartParser.StatementContext):
        pass

    # Exit a parse tree produced by ChartParser#statement.
    def exitStatement(self, ctx:ChartParser.StatementContext):
        pass


    # Enter a parse tree produced by ChartParser#loop.
    def enterLoop(self, ctx:ChartParser.LoopContext):
        pass

    # Exit a parse tree produced by ChartParser#loop.
    def exitLoop(self, ctx:ChartParser.LoopContext):
        pass


    # Enter a parse tree produced by ChartParser#command.
    def enterCommand(self, ctx:ChartParser.CommandContext):
        pass

    # Exit a parse tree produced by ChartParser#command.
    def exitCommand(self, ctx:ChartParser.CommandContext):
        pass


    # Enter a parse tree produced by ChartParser#block.
    def enterBlock(self, ctx:ChartParser.BlockContext):
        pass

    # Exit a parse tree produced by ChartParser#block.
    def exitBlock(self, ctx:ChartParser.BlockContext):
        pass


    # Enter a parse tree produced by ChartParser#chartFunction.
    def enterChartFunction(self, ctx:ChartParser.ChartFunctionContext):
        pass

    # Exit a parse tree produced by ChartParser#chartFunction.
    def exitChartFunction(self, ctx:ChartParser.ChartFunctionContext):
        pass


    # Enter a parse tree produced by ChartParser#data.
    def enterData(self, ctx:ChartParser.DataContext):
        pass

    # Exit a parse tree produced by ChartParser#data.
    def exitData(self, ctx:ChartParser.DataContext):
        pass


    # Enter a parse tree produced by ChartParser#table.
    def enterTable(self, ctx:ChartParser.TableContext):
        pass

    # Exit a parse tree produced by ChartParser#table.
    def exitTable(self, ctx:ChartParser.TableContext):
        pass


    # Enter a parse tree produced by ChartParser#var.
    def enterVar(self, ctx:ChartParser.VarContext):
        pass

    # Exit a parse tree produced by ChartParser#var.
    def exitVar(self, ctx:ChartParser.VarContext):
        pass


    # Enter a parse tree produced by ChartParser#continuousVar.
    def enterContinuousVar(self, ctx:ChartParser.ContinuousVarContext):
        pass

    # Exit a parse tree produced by ChartParser#continuousVar.
    def exitContinuousVar(self, ctx:ChartParser.ContinuousVarContext):
        pass


    # Enter a parse tree produced by ChartParser#range.
    def enterRange(self, ctx:ChartParser.RangeContext):
        pass

    # Exit a parse tree produced by ChartParser#range.
    def exitRange(self, ctx:ChartParser.RangeContext):
        pass


    # Enter a parse tree produced by ChartParser#subgroup.
    def enterSubgroup(self, ctx:ChartParser.SubgroupContext):
        pass

    # Exit a parse tree produced by ChartParser#subgroup.
    def exitSubgroup(self, ctx:ChartParser.SubgroupContext):
        pass


    # Enter a parse tree produced by ChartParser#cases.
    def enterCases(self, ctx:ChartParser.CasesContext):
        pass

    # Exit a parse tree produced by ChartParser#cases.
    def exitCases(self, ctx:ChartParser.CasesContext):
        pass


    # Enter a parse tree produced by ChartParser#trendKeyword.
    def enterTrendKeyword(self, ctx:ChartParser.TrendKeywordContext):
        pass

    # Exit a parse tree produced by ChartParser#trendKeyword.
    def exitTrendKeyword(self, ctx:ChartParser.TrendKeywordContext):
        pass


    # Enter a parse tree produced by ChartParser#condition.
    def enterCondition(self, ctx:ChartParser.ConditionContext):
        pass

    # Exit a parse tree produced by ChartParser#condition.
    def exitCondition(self, ctx:ChartParser.ConditionContext):
        pass


    # Enter a parse tree produced by ChartParser#logicalOperation.
    def enterLogicalOperation(self, ctx:ChartParser.LogicalOperationContext):
        pass

    # Exit a parse tree produced by ChartParser#logicalOperation.
    def exitLogicalOperation(self, ctx:ChartParser.LogicalOperationContext):
        pass


    # Enter a parse tree produced by ChartParser#operationBody.
    def enterOperationBody(self, ctx:ChartParser.OperationBodyContext):
        pass

    # Exit a parse tree produced by ChartParser#operationBody.
    def exitOperationBody(self, ctx:ChartParser.OperationBodyContext):
        pass


    # Enter a parse tree produced by ChartParser#operation.
    def enterOperation(self, ctx:ChartParser.OperationContext):
        pass

    # Exit a parse tree produced by ChartParser#operation.
    def exitOperation(self, ctx:ChartParser.OperationContext):
        pass


    # Enter a parse tree produced by ChartParser#operationSign.
    def enterOperationSign(self, ctx:ChartParser.OperationSignContext):
        pass

    # Exit a parse tree produced by ChartParser#operationSign.
    def exitOperationSign(self, ctx:ChartParser.OperationSignContext):
        pass


    # Enter a parse tree produced by ChartParser#logicalOperationSign.
    def enterLogicalOperationSign(self, ctx:ChartParser.LogicalOperationSignContext):
        pass

    # Exit a parse tree produced by ChartParser#logicalOperationSign.
    def exitLogicalOperationSign(self, ctx:ChartParser.LogicalOperationSignContext):
        pass



del ChartParser
# Generated from ChartDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ChartDSLParser import ChartDSLParser
else:
    from ChartDSLParser import ChartDSLParser

# This class defines a complete listener for a parse tree produced by ChartDSLParser.
class ChartDSLListener(ParseTreeListener):

    # Enter a parse tree produced by ChartDSLParser#command.
    def enterCommand(self, ctx:ChartDSLParser.CommandContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#command.
    def exitCommand(self, ctx:ChartDSLParser.CommandContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#chartFunction.
    def enterChartFunction(self, ctx:ChartDSLParser.ChartFunctionContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#chartFunction.
    def exitChartFunction(self, ctx:ChartDSLParser.ChartFunctionContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#table.
    def enterTable(self, ctx:ChartDSLParser.TableContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#table.
    def exitTable(self, ctx:ChartDSLParser.TableContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#var.
    def enterVar(self, ctx:ChartDSLParser.VarContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#var.
    def exitVar(self, ctx:ChartDSLParser.VarContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#data.
    def enterData(self, ctx:ChartDSLParser.DataContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#data.
    def exitData(self, ctx:ChartDSLParser.DataContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#subgroup.
    def enterSubgroup(self, ctx:ChartDSLParser.SubgroupContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#subgroup.
    def exitSubgroup(self, ctx:ChartDSLParser.SubgroupContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#cases.
    def enterCases(self, ctx:ChartDSLParser.CasesContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#cases.
    def exitCases(self, ctx:ChartDSLParser.CasesContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#continuousVar.
    def enterContinuousVar(self, ctx:ChartDSLParser.ContinuousVarContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#continuousVar.
    def exitContinuousVar(self, ctx:ChartDSLParser.ContinuousVarContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#range.
    def enterRange(self, ctx:ChartDSLParser.RangeContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#range.
    def exitRange(self, ctx:ChartDSLParser.RangeContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#trendKeyword.
    def enterTrendKeyword(self, ctx:ChartDSLParser.TrendKeywordContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#trendKeyword.
    def exitTrendKeyword(self, ctx:ChartDSLParser.TrendKeywordContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#loop.
    def enterLoop(self, ctx:ChartDSLParser.LoopContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#loop.
    def exitLoop(self, ctx:ChartDSLParser.LoopContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:ChartDSLParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:ChartDSLParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#condition.
    def enterCondition(self, ctx:ChartDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#condition.
    def exitCondition(self, ctx:ChartDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#logicalOperation.
    def enterLogicalOperation(self, ctx:ChartDSLParser.LogicalOperationContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#logicalOperation.
    def exitLogicalOperation(self, ctx:ChartDSLParser.LogicalOperationContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#operationBody.
    def enterOperationBody(self, ctx:ChartDSLParser.OperationBodyContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#operationBody.
    def exitOperationBody(self, ctx:ChartDSLParser.OperationBodyContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#operation.
    def enterOperation(self, ctx:ChartDSLParser.OperationContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#operation.
    def exitOperation(self, ctx:ChartDSLParser.OperationContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#operationSign.
    def enterOperationSign(self, ctx:ChartDSLParser.OperationSignContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#operationSign.
    def exitOperationSign(self, ctx:ChartDSLParser.OperationSignContext):
        pass


    # Enter a parse tree produced by ChartDSLParser#logicalOperationSign.
    def enterLogicalOperationSign(self, ctx:ChartDSLParser.LogicalOperationSignContext):
        pass

    # Exit a parse tree produced by ChartDSLParser#logicalOperationSign.
    def exitLogicalOperationSign(self, ctx:ChartDSLParser.LogicalOperationSignContext):
        pass



del ChartDSLParser
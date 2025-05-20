// Generated from ChartParser.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ChartParser}.
 */
public interface ChartParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ChartParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ChartParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ChartParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ChartParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ChartParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(ChartParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(ChartParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ChartParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ChartParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(ChartParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(ChartParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#chartFunction}.
	 * @param ctx the parse tree
	 */
	void enterChartFunction(ChartParser.ChartFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#chartFunction}.
	 * @param ctx the parse tree
	 */
	void exitChartFunction(ChartParser.ChartFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#data}.
	 * @param ctx the parse tree
	 */
	void enterData(ChartParser.DataContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#data}.
	 * @param ctx the parse tree
	 */
	void exitData(ChartParser.DataContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#table}.
	 * @param ctx the parse tree
	 */
	void enterTable(ChartParser.TableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#table}.
	 * @param ctx the parse tree
	 */
	void exitTable(ChartParser.TableContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(ChartParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(ChartParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#continuousVar}.
	 * @param ctx the parse tree
	 */
	void enterContinuousVar(ChartParser.ContinuousVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#continuousVar}.
	 * @param ctx the parse tree
	 */
	void exitContinuousVar(ChartParser.ContinuousVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#range}.
	 * @param ctx the parse tree
	 */
	void enterRange(ChartParser.RangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#range}.
	 * @param ctx the parse tree
	 */
	void exitRange(ChartParser.RangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#subgroup}.
	 * @param ctx the parse tree
	 */
	void enterSubgroup(ChartParser.SubgroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#subgroup}.
	 * @param ctx the parse tree
	 */
	void exitSubgroup(ChartParser.SubgroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#cases}.
	 * @param ctx the parse tree
	 */
	void enterCases(ChartParser.CasesContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#cases}.
	 * @param ctx the parse tree
	 */
	void exitCases(ChartParser.CasesContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#trendKeyword}.
	 * @param ctx the parse tree
	 */
	void enterTrendKeyword(ChartParser.TrendKeywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#trendKeyword}.
	 * @param ctx the parse tree
	 */
	void exitTrendKeyword(ChartParser.TrendKeywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(ChartParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(ChartParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#logicalOperation}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOperation(ChartParser.LogicalOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#logicalOperation}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOperation(ChartParser.LogicalOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#operationBody}.
	 * @param ctx the parse tree
	 */
	void enterOperationBody(ChartParser.OperationBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#operationBody}.
	 * @param ctx the parse tree
	 */
	void exitOperationBody(ChartParser.OperationBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterOperation(ChartParser.OperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitOperation(ChartParser.OperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#operationSign}.
	 * @param ctx the parse tree
	 */
	void enterOperationSign(ChartParser.OperationSignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#operationSign}.
	 * @param ctx the parse tree
	 */
	void exitOperationSign(ChartParser.OperationSignContext ctx);
	/**
	 * Enter a parse tree produced by {@link ChartParser#logicalOperationSign}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOperationSign(ChartParser.LogicalOperationSignContext ctx);
	/**
	 * Exit a parse tree produced by {@link ChartParser#logicalOperationSign}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOperationSign(ChartParser.LogicalOperationSignContext ctx);
}
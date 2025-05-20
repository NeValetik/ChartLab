// Generated from ChartParser.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ChartParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WITH=1, FROM=2, CHART=3, COMPARE=4, DIFFERENCES=5, CONTRAST=6, VERSUS=7, 
		SPLIT_BY=8, GROUPED_BY=9, SHOW=10, STACKED_BY=11, SUBGROUPS=12, CORRELATION=13, 
		LOG=14, PROGRESSION_OF=15, TREND_OF=16, GROWTH_OF=17, WITHIN=18, SHOW_PROPORTION=19, 
		SHOW_SHARE=20, SHOW_PERCENTAGE=21, SHOW_FREQUENCY=22, SHOW_DISTRIBUTION=23, 
		SHOW_FREQUENCY_BUCKETS=24, ACCUMULATION=25, STACKED_TREND=26, SCATTER_PLOT=27, 
		PATTERN=28, BUBBLE=29, BUCKETS=30, BY=31, AND=32, OR=33, AT=34, TO=35, 
		FOR=36, NOT=37, PLUS=38, MINUS=39, MULTIPLY=40, DIVIDE=41, LT=42, LTE=43, 
		GT=44, GTE=45, EQ=46, NEQ=47, COMMA=48, COLON=49, LPAREN=50, RPAREN=51, 
		LBRACE=52, RBRACE=53, WHILE=54, IDENTIFIER=55, WS=56;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_loop = 2, RULE_command = 3, 
		RULE_block = 4, RULE_chartFunction = 5, RULE_data = 6, RULE_table = 7, 
		RULE_var = 8, RULE_continuousVar = 9, RULE_range = 10, RULE_subgroup = 11, 
		RULE_cases = 12, RULE_trendKeyword = 13, RULE_condition = 14, RULE_logicalOperation = 15, 
		RULE_operationBody = 16, RULE_operation = 17, RULE_operationSign = 18, 
		RULE_logicalOperationSign = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "loop", "command", "block", "chartFunction", 
			"data", "table", "var", "continuousVar", "range", "subgroup", "cases", 
			"trendKeyword", "condition", "logicalOperation", "operationBody", "operation", 
			"operationSign", "logicalOperationSign"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'with'", "'from'", "'chart:'", "'compare'", "'differences'", "'contrast'", 
			"'versus'", "'split by'", "'grouped by'", "'show'", "'stacked by'", "'subgroups'", 
			"'show correlation between'", "'log'", "'progression of'", "'trend of'", 
			"'growth of'", "'within'", "'show proportion of'", "'show share of'", 
			"'show percentage of'", "'show frequency of'", "'show distribution of'", 
			"'show frequency in'", "'accumulation of'", "'stacked trend of'", "'scatter plot of'", 
			"'pattern of'", "'bubble of'", "'buckets'", "'by'", "'and'", "'or'", 
			"'at'", "'to'", "'for'", "'!'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", 
			"'>'", "'>='", "'=='", "'!='", "','", "':'", "'('", "')'", "'{'", "'}'", 
			"'while'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WITH", "FROM", "CHART", "COMPARE", "DIFFERENCES", "CONTRAST", 
			"VERSUS", "SPLIT_BY", "GROUPED_BY", "SHOW", "STACKED_BY", "SUBGROUPS", 
			"CORRELATION", "LOG", "PROGRESSION_OF", "TREND_OF", "GROWTH_OF", "WITHIN", 
			"SHOW_PROPORTION", "SHOW_SHARE", "SHOW_PERCENTAGE", "SHOW_FREQUENCY", 
			"SHOW_DISTRIBUTION", "SHOW_FREQUENCY_BUCKETS", "ACCUMULATION", "STACKED_TREND", 
			"SCATTER_PLOT", "PATTERN", "BUBBLE", "BUCKETS", "BY", "AND", "OR", "AT", 
			"TO", "FOR", "NOT", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LT", "LTE", 
			"GT", "GTE", "EQ", "NEQ", "COMMA", "COLON", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "WHILE", "IDENTIFIER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ChartParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ChartParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ChartParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(40);
				statement();
				}
				}
				setState(43); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WITH || _la==WHILE );
			setState(45);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public CommandContext command() {
			return getRuleContext(CommandContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(49);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WHILE:
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				loop();
				}
				break;
			case WITH:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				command();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(ChartParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(ChartParser.LPAREN, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ChartParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(ChartParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ChartParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitLoop(this);
		}
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_loop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(WHILE);
			setState(52);
			match(LPAREN);
			setState(53);
			condition();
			setState(54);
			match(RPAREN);
			setState(55);
			match(LBRACE);
			setState(57); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(56);
				statement();
				}
				}
				setState(59); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WITH || _la==WHILE );
			setState(61);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public TerminalNode WITH() { return getToken(ChartParser.WITH, 0); }
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public TerminalNode FROM() { return getToken(ChartParser.FROM, 0); }
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public TerminalNode CHART() { return getToken(ChartParser.CHART, 0); }
		public ChartFunctionContext chartFunction() {
			return getRuleContext(ChartFunctionContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(ChartParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ChartParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitCommand(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_command);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(WITH);
			setState(64);
			data();
			setState(65);
			match(FROM);
			setState(66);
			table();
			setState(67);
			match(CHART);
			setState(68);
			chartFunction();
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LBRACE) {
				{
				setState(69);
				match(LBRACE);
				setState(71); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(70);
					statement();
					}
					}
					setState(73); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==WITH || _la==WHILE );
				setState(75);
				match(RBRACE);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(ChartParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ChartParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(LBRACE);
			setState(81); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(80);
				statement();
				}
				}
				setState(83); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WITH || _la==WHILE );
			setState(85);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChartFunctionContext extends ParserRuleContext {
		public TerminalNode COMPARE() { return getToken(ChartParser.COMPARE, 0); }
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
		}
		public TerminalNode FOR() { return getToken(ChartParser.FOR, 0); }
		public CasesContext cases() {
			return getRuleContext(CasesContext.class,0);
		}
		public TerminalNode DIFFERENCES() { return getToken(ChartParser.DIFFERENCES, 0); }
		public TerminalNode CONTRAST() { return getToken(ChartParser.CONTRAST, 0); }
		public TerminalNode VERSUS() { return getToken(ChartParser.VERSUS, 0); }
		public TerminalNode SPLIT_BY() { return getToken(ChartParser.SPLIT_BY, 0); }
		public SubgroupContext subgroup() {
			return getRuleContext(SubgroupContext.class,0);
		}
		public TerminalNode GROUPED_BY() { return getToken(ChartParser.GROUPED_BY, 0); }
		public TerminalNode WITHIN() { return getToken(ChartParser.WITHIN, 0); }
		public TerminalNode SHOW() { return getToken(ChartParser.SHOW, 0); }
		public TerminalNode STACKED_BY() { return getToken(ChartParser.STACKED_BY, 0); }
		public TerminalNode SUBGROUPS() { return getToken(ChartParser.SUBGROUPS, 0); }
		public TerminalNode CORRELATION() { return getToken(ChartParser.CORRELATION, 0); }
		public List<ContinuousVarContext> continuousVar() {
			return getRuleContexts(ContinuousVarContext.class);
		}
		public ContinuousVarContext continuousVar(int i) {
			return getRuleContext(ContinuousVarContext.class,i);
		}
		public TerminalNode AND() { return getToken(ChartParser.AND, 0); }
		public TerminalNode LOG() { return getToken(ChartParser.LOG, 0); }
		public TrendKeywordContext trendKeyword() {
			return getRuleContext(TrendKeywordContext.class,0);
		}
		public TerminalNode FROM() { return getToken(ChartParser.FROM, 0); }
		public RangeContext range() {
			return getRuleContext(RangeContext.class,0);
		}
		public TerminalNode SHOW_PROPORTION() { return getToken(ChartParser.SHOW_PROPORTION, 0); }
		public TerminalNode BY() { return getToken(ChartParser.BY, 0); }
		public TerminalNode SHOW_SHARE() { return getToken(ChartParser.SHOW_SHARE, 0); }
		public TerminalNode SHOW_PERCENTAGE() { return getToken(ChartParser.SHOW_PERCENTAGE, 0); }
		public TerminalNode SHOW_FREQUENCY() { return getToken(ChartParser.SHOW_FREQUENCY, 0); }
		public TerminalNode SHOW_DISTRIBUTION() { return getToken(ChartParser.SHOW_DISTRIBUTION, 0); }
		public TerminalNode SHOW_FREQUENCY_BUCKETS() { return getToken(ChartParser.SHOW_FREQUENCY_BUCKETS, 0); }
		public TerminalNode BUCKETS() { return getToken(ChartParser.BUCKETS, 0); }
		public TerminalNode ACCUMULATION() { return getToken(ChartParser.ACCUMULATION, 0); }
		public TerminalNode STACKED_TREND() { return getToken(ChartParser.STACKED_TREND, 0); }
		public TerminalNode SCATTER_PLOT() { return getToken(ChartParser.SCATTER_PLOT, 0); }
		public TerminalNode PATTERN() { return getToken(ChartParser.PATTERN, 0); }
		public TerminalNode BUBBLE() { return getToken(ChartParser.BUBBLE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ChartParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ChartParser.COMMA, i);
		}
		public ChartFunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_chartFunction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterChartFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitChartFunction(this);
		}
	}

	public final ChartFunctionContext chartFunction() throws RecognitionException {
		ChartFunctionContext _localctx = new ChartFunctionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_chartFunction);
		try {
			setState(209);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				match(COMPARE);
				setState(88);
				var();
				setState(89);
				match(FOR);
				setState(90);
				cases();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				match(DIFFERENCES);
				setState(93);
				var();
				setState(94);
				match(FOR);
				setState(95);
				cases();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(97);
				match(CONTRAST);
				setState(98);
				var();
				setState(99);
				match(FOR);
				setState(100);
				cases();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(102);
				match(VERSUS);
				setState(103);
				var();
				setState(104);
				match(FOR);
				setState(105);
				cases();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(107);
				match(COMPARE);
				setState(108);
				var();
				setState(109);
				match(SPLIT_BY);
				setState(110);
				subgroup();
				setState(111);
				match(FOR);
				setState(112);
				cases();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(114);
				match(COMPARE);
				setState(115);
				var();
				setState(116);
				match(GROUPED_BY);
				setState(117);
				subgroup();
				setState(118);
				match(FOR);
				setState(119);
				cases();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(121);
				match(DIFFERENCES);
				setState(122);
				match(WITHIN);
				setState(123);
				subgroup();
				setState(124);
				match(FOR);
				setState(125);
				cases();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(127);
				match(SHOW);
				setState(128);
				var();
				setState(129);
				match(STACKED_BY);
				setState(130);
				subgroup();
				setState(131);
				match(FOR);
				setState(132);
				cases();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(134);
				match(SHOW);
				setState(135);
				var();
				setState(136);
				match(SUBGROUPS);
				setState(137);
				subgroup();
				setState(138);
				match(FOR);
				setState(139);
				cases();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(141);
				match(CORRELATION);
				setState(142);
				continuousVar();
				setState(143);
				match(AND);
				setState(144);
				continuousVar();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(146);
				match(LOG);
				setState(147);
				trendKeyword();
				setState(148);
				continuousVar();
				setState(149);
				match(FROM);
				setState(150);
				range();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(152);
				match(SHOW_PROPORTION);
				setState(153);
				var();
				setState(154);
				match(BY);
				setState(155);
				cases();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(157);
				match(SHOW_SHARE);
				setState(158);
				var();
				setState(159);
				match(BY);
				setState(160);
				cases();
				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(162);
				match(SHOW_PERCENTAGE);
				setState(163);
				var();
				setState(164);
				match(BY);
				setState(165);
				cases();
				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(167);
				match(SHOW_FREQUENCY);
				setState(168);
				var();
				}
				break;
			case 16:
				enterOuterAlt(_localctx, 16);
				{
				setState(169);
				match(SHOW_DISTRIBUTION);
				setState(170);
				var();
				setState(171);
				match(BY);
				setState(172);
				range();
				}
				break;
			case 17:
				enterOuterAlt(_localctx, 17);
				{
				setState(174);
				match(SHOW_FREQUENCY_BUCKETS);
				setState(175);
				range();
				setState(176);
				match(BUCKETS);
				}
				break;
			case 18:
				enterOuterAlt(_localctx, 18);
				{
				setState(178);
				match(ACCUMULATION);
				setState(179);
				continuousVar();
				setState(180);
				match(FOR);
				setState(181);
				cases();
				setState(182);
				match(FROM);
				setState(183);
				range();
				}
				break;
			case 19:
				enterOuterAlt(_localctx, 19);
				{
				setState(185);
				match(STACKED_TREND);
				setState(186);
				continuousVar();
				setState(187);
				match(FOR);
				setState(188);
				cases();
				}
				break;
			case 20:
				enterOuterAlt(_localctx, 20);
				{
				setState(190);
				match(SCATTER_PLOT);
				setState(191);
				var();
				setState(192);
				match(AND);
				setState(193);
				var();
				}
				break;
			case 21:
				enterOuterAlt(_localctx, 21);
				{
				setState(195);
				match(PATTERN);
				setState(196);
				var();
				setState(197);
				match(AND);
				setState(198);
				var();
				}
				break;
			case 22:
				enterOuterAlt(_localctx, 22);
				{
				setState(200);
				match(BUBBLE);
				setState(201);
				var();
				setState(202);
				match(COMMA);
				setState(203);
				var();
				setState(204);
				match(COMMA);
				setState(205);
				var();
				setState(206);
				match(FOR);
				setState(207);
				cases();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DataContext extends ParserRuleContext {
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
		}
		public ContinuousVarContext continuousVar() {
			return getRuleContext(ContinuousVarContext.class,0);
		}
		public TerminalNode AT() { return getToken(ChartParser.AT, 0); }
		public DataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterData(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitData(this);
		}
	}

	public final DataContext data() throws RecognitionException {
		DataContext _localctx = new DataContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_data);
		try {
			setState(217);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(211);
				var();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(212);
				continuousVar();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(213);
				var();
				setState(214);
				match(AT);
				setState(215);
				var();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ChartParser.IDENTIFIER, 0); }
		public TableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterTable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitTable(this);
		}
	}

	public final TableContext table() throws RecognitionException {
		TableContext _localctx = new TableContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_table);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ChartParser.IDENTIFIER, 0); }
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitVar(this);
		}
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContinuousVarContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(ChartParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ChartParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(ChartParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ChartParser.COMMA, i);
		}
		public ContinuousVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continuousVar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterContinuousVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitContinuousVar(this);
		}
	}

	public final ContinuousVarContext continuousVar() throws RecognitionException {
		ContinuousVarContext _localctx = new ContinuousVarContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_continuousVar);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			match(IDENTIFIER);
			setState(228);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(224);
				match(COMMA);
				setState(225);
				match(IDENTIFIER);
				}
				}
				setState(230);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RangeContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(ChartParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ChartParser.IDENTIFIER, i);
		}
		public TerminalNode TO() { return getToken(ChartParser.TO, 0); }
		public RangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterRange(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitRange(this);
		}
	}

	public final RangeContext range() throws RecognitionException {
		RangeContext _localctx = new RangeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(IDENTIFIER);
			setState(232);
			match(TO);
			setState(233);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SubgroupContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ChartParser.IDENTIFIER, 0); }
		public SubgroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subgroup; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterSubgroup(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitSubgroup(this);
		}
	}

	public final SubgroupContext subgroup() throws RecognitionException {
		SubgroupContext _localctx = new SubgroupContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_subgroup);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CasesContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(ChartParser.IDENTIFIER, 0); }
		public CasesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cases; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterCases(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitCases(this);
		}
	}

	public final CasesContext cases() throws RecognitionException {
		CasesContext _localctx = new CasesContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_cases);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TrendKeywordContext extends ParserRuleContext {
		public TerminalNode PROGRESSION_OF() { return getToken(ChartParser.PROGRESSION_OF, 0); }
		public TerminalNode TREND_OF() { return getToken(ChartParser.TREND_OF, 0); }
		public TerminalNode GROWTH_OF() { return getToken(ChartParser.GROWTH_OF, 0); }
		public TrendKeywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_trendKeyword; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterTrendKeyword(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitTrendKeyword(this);
		}
	}

	public final TrendKeywordContext trendKeyword() throws RecognitionException {
		TrendKeywordContext _localctx = new TrendKeywordContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_trendKeyword);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 229376L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<LogicalOperationContext> logicalOperation() {
			return getRuleContexts(LogicalOperationContext.class);
		}
		public LogicalOperationContext logicalOperation(int i) {
			return getRuleContext(LogicalOperationContext.class,i);
		}
		public List<TerminalNode> NOT() { return getTokens(ChartParser.NOT); }
		public TerminalNode NOT(int i) {
			return getToken(ChartParser.NOT, i);
		}
		public TerminalNode LPAREN() { return getToken(ChartParser.LPAREN, 0); }
		public List<TerminalNode> AND() { return getTokens(ChartParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(ChartParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(ChartParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(ChartParser.OR, i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(241);
				match(NOT);
				}
				break;
			}
			setState(245);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(244);
				match(LPAREN);
				}
				break;
			}
			setState(250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOT) {
				{
				{
				setState(247);
				match(NOT);
				}
				}
				setState(252);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(253);
			logicalOperation();
			setState(261);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(254);
				_la = _input.LA(1);
				if ( !(_la==AND || _la==OR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(256);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NOT) {
					{
					setState(255);
					match(NOT);
					}
				}

				setState(258);
				logicalOperation();
				}
				}
				setState(263);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(265);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(264);
				match(NOT);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOperationContext extends ParserRuleContext {
		public List<OperationBodyContext> operationBody() {
			return getRuleContexts(OperationBodyContext.class);
		}
		public OperationBodyContext operationBody(int i) {
			return getRuleContext(OperationBodyContext.class,i);
		}
		public LogicalOperationSignContext logicalOperationSign() {
			return getRuleContext(LogicalOperationSignContext.class,0);
		}
		public List<TerminalNode> LPAREN() { return getTokens(ChartParser.LPAREN); }
		public TerminalNode LPAREN(int i) {
			return getToken(ChartParser.LPAREN, i);
		}
		public List<TerminalNode> RPAREN() { return getTokens(ChartParser.RPAREN); }
		public TerminalNode RPAREN(int i) {
			return getToken(ChartParser.RPAREN, i);
		}
		public LogicalOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterLogicalOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitLogicalOperation(this);
		}
	}

	public final LogicalOperationContext logicalOperation() throws RecognitionException {
		LogicalOperationContext _localctx = new LogicalOperationContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_logicalOperation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(267);
				match(LPAREN);
				}
				break;
			}
			setState(270);
			operationBody();
			setState(272);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==RPAREN) {
				{
				setState(271);
				match(RPAREN);
				}
			}

			setState(274);
			logicalOperationSign();
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(275);
				match(LPAREN);
				}
				break;
			}
			setState(278);
			operationBody();
			setState(280);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(279);
				match(RPAREN);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationBodyContext extends ParserRuleContext {
		public List<OperationContext> operation() {
			return getRuleContexts(OperationContext.class);
		}
		public OperationContext operation(int i) {
			return getRuleContext(OperationContext.class,i);
		}
		public List<TerminalNode> LPAREN() { return getTokens(ChartParser.LPAREN); }
		public TerminalNode LPAREN(int i) {
			return getToken(ChartParser.LPAREN, i);
		}
		public List<TerminalNode> RPAREN() { return getTokens(ChartParser.RPAREN); }
		public TerminalNode RPAREN(int i) {
			return getToken(ChartParser.RPAREN, i);
		}
		public List<OperationSignContext> operationSign() {
			return getRuleContexts(OperationSignContext.class);
		}
		public OperationSignContext operationSign(int i) {
			return getRuleContext(OperationSignContext.class,i);
		}
		public OperationBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operationBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterOperationBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitOperationBody(this);
		}
	}

	public final OperationBodyContext operationBody() throws RecognitionException {
		OperationBodyContext _localctx = new OperationBodyContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_operationBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(282);
				match(LPAREN);
				}
			}

			setState(285);
			operation();
			setState(287);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(286);
				match(RPAREN);
				}
				break;
			}
			setState(299);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4123168604160L) != 0)) {
				{
				{
				setState(289);
				operationSign();
				setState(291);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LPAREN) {
					{
					setState(290);
					match(LPAREN);
					}
				}

				setState(293);
				operation();
				setState(295);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
				case 1:
					{
					setState(294);
					match(RPAREN);
					}
					break;
				}
				}
				}
				setState(301);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(ChartParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(ChartParser.IDENTIFIER, i);
		}
		public OperationSignContext operationSign() {
			return getRuleContext(OperationSignContext.class,0);
		}
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitOperation(this);
		}
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_operation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			match(IDENTIFIER);
			setState(306);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(303);
				operationSign();
				setState(304);
				match(IDENTIFIER);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationSignContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(ChartParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(ChartParser.MINUS, 0); }
		public TerminalNode MULTIPLY() { return getToken(ChartParser.MULTIPLY, 0); }
		public TerminalNode DIVIDE() { return getToken(ChartParser.DIVIDE, 0); }
		public OperationSignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operationSign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterOperationSign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitOperationSign(this);
		}
	}

	public final OperationSignContext operationSign() throws RecognitionException {
		OperationSignContext _localctx = new OperationSignContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_operationSign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4123168604160L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOperationSignContext extends ParserRuleContext {
		public TerminalNode LT() { return getToken(ChartParser.LT, 0); }
		public TerminalNode LTE() { return getToken(ChartParser.LTE, 0); }
		public TerminalNode GT() { return getToken(ChartParser.GT, 0); }
		public TerminalNode GTE() { return getToken(ChartParser.GTE, 0); }
		public TerminalNode EQ() { return getToken(ChartParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(ChartParser.NEQ, 0); }
		public LogicalOperationSignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOperationSign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).enterLogicalOperationSign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ChartParserListener ) ((ChartParserListener)listener).exitLogicalOperationSign(this);
		}
	}

	public final LogicalOperationSignContext logicalOperationSign() throws RecognitionException {
		LogicalOperationSignContext _localctx = new LogicalOperationSignContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_logicalOperationSign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 277076930199552L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u00018\u0139\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0004\u0000*\b\u0000\u000b\u0000"+
		"\f\u0000+\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001"+
		"2\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0004\u0002:\b\u0002\u000b\u0002\f\u0002;\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0004\u0003H\b\u0003\u000b\u0003\f\u0003"+
		"I\u0001\u0003\u0001\u0003\u0003\u0003N\b\u0003\u0001\u0004\u0001\u0004"+
		"\u0004\u0004R\b\u0004\u000b\u0004\f\u0004S\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u0005\u00d2\b\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u00da\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0005\t\u00e3"+
		"\b\t\n\t\f\t\u00e6\t\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0003\u000e\u00f3\b"+
		"\u000e\u0001\u000e\u0003\u000e\u00f6\b\u000e\u0001\u000e\u0005\u000e\u00f9"+
		"\b\u000e\n\u000e\f\u000e\u00fc\t\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0003\u000e\u0101\b\u000e\u0001\u000e\u0005\u000e\u0104\b\u000e\n\u000e"+
		"\f\u000e\u0107\t\u000e\u0001\u000e\u0003\u000e\u010a\b\u000e\u0001\u000f"+
		"\u0003\u000f\u010d\b\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0111\b"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0115\b\u000f\u0001\u000f\u0001"+
		"\u000f\u0003\u000f\u0119\b\u000f\u0001\u0010\u0003\u0010\u011c\b\u0010"+
		"\u0001\u0010\u0001\u0010\u0003\u0010\u0120\b\u0010\u0001\u0010\u0001\u0010"+
		"\u0003\u0010\u0124\b\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u0128\b"+
		"\u0010\u0005\u0010\u012a\b\u0010\n\u0010\f\u0010\u012d\t\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u0133\b\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0000\u0000\u0014\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$&\u0000\u0004\u0001\u0000\u000f\u0011\u0001\u0000 !\u0001\u0000"+
		"&)\u0001\u0000*/\u0152\u0000)\u0001\u0000\u0000\u0000\u00021\u0001\u0000"+
		"\u0000\u0000\u00043\u0001\u0000\u0000\u0000\u0006?\u0001\u0000\u0000\u0000"+
		"\bO\u0001\u0000\u0000\u0000\n\u00d1\u0001\u0000\u0000\u0000\f\u00d9\u0001"+
		"\u0000\u0000\u0000\u000e\u00db\u0001\u0000\u0000\u0000\u0010\u00dd\u0001"+
		"\u0000\u0000\u0000\u0012\u00df\u0001\u0000\u0000\u0000\u0014\u00e7\u0001"+
		"\u0000\u0000\u0000\u0016\u00eb\u0001\u0000\u0000\u0000\u0018\u00ed\u0001"+
		"\u0000\u0000\u0000\u001a\u00ef\u0001\u0000\u0000\u0000\u001c\u00f2\u0001"+
		"\u0000\u0000\u0000\u001e\u010c\u0001\u0000\u0000\u0000 \u011b\u0001\u0000"+
		"\u0000\u0000\"\u012e\u0001\u0000\u0000\u0000$\u0134\u0001\u0000\u0000"+
		"\u0000&\u0136\u0001\u0000\u0000\u0000(*\u0003\u0002\u0001\u0000)(\u0001"+
		"\u0000\u0000\u0000*+\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		"+,\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0005\u0000\u0000"+
		"\u0001.\u0001\u0001\u0000\u0000\u0000/2\u0003\u0004\u0002\u000002\u0003"+
		"\u0006\u0003\u00001/\u0001\u0000\u0000\u000010\u0001\u0000\u0000\u0000"+
		"2\u0003\u0001\u0000\u0000\u000034\u00056\u0000\u000045\u00052\u0000\u0000"+
		"56\u0003\u001c\u000e\u000067\u00053\u0000\u000079\u00054\u0000\u00008"+
		":\u0003\u0002\u0001\u000098\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000"+
		"\u0000;9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<=\u0001\u0000"+
		"\u0000\u0000=>\u00055\u0000\u0000>\u0005\u0001\u0000\u0000\u0000?@\u0005"+
		"\u0001\u0000\u0000@A\u0003\f\u0006\u0000AB\u0005\u0002\u0000\u0000BC\u0003"+
		"\u000e\u0007\u0000CD\u0005\u0003\u0000\u0000DM\u0003\n\u0005\u0000EG\u0005"+
		"4\u0000\u0000FH\u0003\u0002\u0001\u0000GF\u0001\u0000\u0000\u0000HI\u0001"+
		"\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"JK\u0001\u0000\u0000\u0000KL\u00055\u0000\u0000LN\u0001\u0000\u0000\u0000"+
		"ME\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\u0007\u0001\u0000"+
		"\u0000\u0000OQ\u00054\u0000\u0000PR\u0003\u0002\u0001\u0000QP\u0001\u0000"+
		"\u0000\u0000RS\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001"+
		"\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000UV\u00055\u0000\u0000V\t\u0001"+
		"\u0000\u0000\u0000WX\u0005\u0004\u0000\u0000XY\u0003\u0010\b\u0000YZ\u0005"+
		"$\u0000\u0000Z[\u0003\u0018\f\u0000[\u00d2\u0001\u0000\u0000\u0000\\]"+
		"\u0005\u0005\u0000\u0000]^\u0003\u0010\b\u0000^_\u0005$\u0000\u0000_`"+
		"\u0003\u0018\f\u0000`\u00d2\u0001\u0000\u0000\u0000ab\u0005\u0006\u0000"+
		"\u0000bc\u0003\u0010\b\u0000cd\u0005$\u0000\u0000de\u0003\u0018\f\u0000"+
		"e\u00d2\u0001\u0000\u0000\u0000fg\u0005\u0007\u0000\u0000gh\u0003\u0010"+
		"\b\u0000hi\u0005$\u0000\u0000ij\u0003\u0018\f\u0000j\u00d2\u0001\u0000"+
		"\u0000\u0000kl\u0005\u0004\u0000\u0000lm\u0003\u0010\b\u0000mn\u0005\b"+
		"\u0000\u0000no\u0003\u0016\u000b\u0000op\u0005$\u0000\u0000pq\u0003\u0018"+
		"\f\u0000q\u00d2\u0001\u0000\u0000\u0000rs\u0005\u0004\u0000\u0000st\u0003"+
		"\u0010\b\u0000tu\u0005\t\u0000\u0000uv\u0003\u0016\u000b\u0000vw\u0005"+
		"$\u0000\u0000wx\u0003\u0018\f\u0000x\u00d2\u0001\u0000\u0000\u0000yz\u0005"+
		"\u0005\u0000\u0000z{\u0005\u0012\u0000\u0000{|\u0003\u0016\u000b\u0000"+
		"|}\u0005$\u0000\u0000}~\u0003\u0018\f\u0000~\u00d2\u0001\u0000\u0000\u0000"+
		"\u007f\u0080\u0005\n\u0000\u0000\u0080\u0081\u0003\u0010\b\u0000\u0081"+
		"\u0082\u0005\u000b\u0000\u0000\u0082\u0083\u0003\u0016\u000b\u0000\u0083"+
		"\u0084\u0005$\u0000\u0000\u0084\u0085\u0003\u0018\f\u0000\u0085\u00d2"+
		"\u0001\u0000\u0000\u0000\u0086\u0087\u0005\n\u0000\u0000\u0087\u0088\u0003"+
		"\u0010\b\u0000\u0088\u0089\u0005\f\u0000\u0000\u0089\u008a\u0003\u0016"+
		"\u000b\u0000\u008a\u008b\u0005$\u0000\u0000\u008b\u008c\u0003\u0018\f"+
		"\u0000\u008c\u00d2\u0001\u0000\u0000\u0000\u008d\u008e\u0005\r\u0000\u0000"+
		"\u008e\u008f\u0003\u0012\t\u0000\u008f\u0090\u0005 \u0000\u0000\u0090"+
		"\u0091\u0003\u0012\t\u0000\u0091\u00d2\u0001\u0000\u0000\u0000\u0092\u0093"+
		"\u0005\u000e\u0000\u0000\u0093\u0094\u0003\u001a\r\u0000\u0094\u0095\u0003"+
		"\u0012\t\u0000\u0095\u0096\u0005\u0002\u0000\u0000\u0096\u0097\u0003\u0014"+
		"\n\u0000\u0097\u00d2\u0001\u0000\u0000\u0000\u0098\u0099\u0005\u0013\u0000"+
		"\u0000\u0099\u009a\u0003\u0010\b\u0000\u009a\u009b\u0005\u001f\u0000\u0000"+
		"\u009b\u009c\u0003\u0018\f\u0000\u009c\u00d2\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0005\u0014\u0000\u0000\u009e\u009f\u0003\u0010\b\u0000\u009f\u00a0"+
		"\u0005\u001f\u0000\u0000\u00a0\u00a1\u0003\u0018\f\u0000\u00a1\u00d2\u0001"+
		"\u0000\u0000\u0000\u00a2\u00a3\u0005\u0015\u0000\u0000\u00a3\u00a4\u0003"+
		"\u0010\b\u0000\u00a4\u00a5\u0005\u001f\u0000\u0000\u00a5\u00a6\u0003\u0018"+
		"\f\u0000\u00a6\u00d2\u0001\u0000\u0000\u0000\u00a7\u00a8\u0005\u0016\u0000"+
		"\u0000\u00a8\u00d2\u0003\u0010\b\u0000\u00a9\u00aa\u0005\u0017\u0000\u0000"+
		"\u00aa\u00ab\u0003\u0010\b\u0000\u00ab\u00ac\u0005\u001f\u0000\u0000\u00ac"+
		"\u00ad\u0003\u0014\n\u0000\u00ad\u00d2\u0001\u0000\u0000\u0000\u00ae\u00af"+
		"\u0005\u0018\u0000\u0000\u00af\u00b0\u0003\u0014\n\u0000\u00b0\u00b1\u0005"+
		"\u001e\u0000\u0000\u00b1\u00d2\u0001\u0000\u0000\u0000\u00b2\u00b3\u0005"+
		"\u0019\u0000\u0000\u00b3\u00b4\u0003\u0012\t\u0000\u00b4\u00b5\u0005$"+
		"\u0000\u0000\u00b5\u00b6\u0003\u0018\f\u0000\u00b6\u00b7\u0005\u0002\u0000"+
		"\u0000\u00b7\u00b8\u0003\u0014\n\u0000\u00b8\u00d2\u0001\u0000\u0000\u0000"+
		"\u00b9\u00ba\u0005\u001a\u0000\u0000\u00ba\u00bb\u0003\u0012\t\u0000\u00bb"+
		"\u00bc\u0005$\u0000\u0000\u00bc\u00bd\u0003\u0018\f\u0000\u00bd\u00d2"+
		"\u0001\u0000\u0000\u0000\u00be\u00bf\u0005\u001b\u0000\u0000\u00bf\u00c0"+
		"\u0003\u0010\b\u0000\u00c0\u00c1\u0005 \u0000\u0000\u00c1\u00c2\u0003"+
		"\u0010\b\u0000\u00c2\u00d2\u0001\u0000\u0000\u0000\u00c3\u00c4\u0005\u001c"+
		"\u0000\u0000\u00c4\u00c5\u0003\u0010\b\u0000\u00c5\u00c6\u0005 \u0000"+
		"\u0000\u00c6\u00c7\u0003\u0010\b\u0000\u00c7\u00d2\u0001\u0000\u0000\u0000"+
		"\u00c8\u00c9\u0005\u001d\u0000\u0000\u00c9\u00ca\u0003\u0010\b\u0000\u00ca"+
		"\u00cb\u00050\u0000\u0000\u00cb\u00cc\u0003\u0010\b\u0000\u00cc\u00cd"+
		"\u00050\u0000\u0000\u00cd\u00ce\u0003\u0010\b\u0000\u00ce\u00cf\u0005"+
		"$\u0000\u0000\u00cf\u00d0\u0003\u0018\f\u0000\u00d0\u00d2\u0001\u0000"+
		"\u0000\u0000\u00d1W\u0001\u0000\u0000\u0000\u00d1\\\u0001\u0000\u0000"+
		"\u0000\u00d1a\u0001\u0000\u0000\u0000\u00d1f\u0001\u0000\u0000\u0000\u00d1"+
		"k\u0001\u0000\u0000\u0000\u00d1r\u0001\u0000\u0000\u0000\u00d1y\u0001"+
		"\u0000\u0000\u0000\u00d1\u007f\u0001\u0000\u0000\u0000\u00d1\u0086\u0001"+
		"\u0000\u0000\u0000\u00d1\u008d\u0001\u0000\u0000\u0000\u00d1\u0092\u0001"+
		"\u0000\u0000\u0000\u00d1\u0098\u0001\u0000\u0000\u0000\u00d1\u009d\u0001"+
		"\u0000\u0000\u0000\u00d1\u00a2\u0001\u0000\u0000\u0000\u00d1\u00a7\u0001"+
		"\u0000\u0000\u0000\u00d1\u00a9\u0001\u0000\u0000\u0000\u00d1\u00ae\u0001"+
		"\u0000\u0000\u0000\u00d1\u00b2\u0001\u0000\u0000\u0000\u00d1\u00b9\u0001"+
		"\u0000\u0000\u0000\u00d1\u00be\u0001\u0000\u0000\u0000\u00d1\u00c3\u0001"+
		"\u0000\u0000\u0000\u00d1\u00c8\u0001\u0000\u0000\u0000\u00d2\u000b\u0001"+
		"\u0000\u0000\u0000\u00d3\u00da\u0003\u0010\b\u0000\u00d4\u00da\u0003\u0012"+
		"\t\u0000\u00d5\u00d6\u0003\u0010\b\u0000\u00d6\u00d7\u0005\"\u0000\u0000"+
		"\u00d7\u00d8\u0003\u0010\b\u0000\u00d8\u00da\u0001\u0000\u0000\u0000\u00d9"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d9\u00d4\u0001\u0000\u0000\u0000\u00d9"+
		"\u00d5\u0001\u0000\u0000\u0000\u00da\r\u0001\u0000\u0000\u0000\u00db\u00dc"+
		"\u00057\u0000\u0000\u00dc\u000f\u0001\u0000\u0000\u0000\u00dd\u00de\u0005"+
		"7\u0000\u0000\u00de\u0011\u0001\u0000\u0000\u0000\u00df\u00e4\u00057\u0000"+
		"\u0000\u00e0\u00e1\u00050\u0000\u0000\u00e1\u00e3\u00057\u0000\u0000\u00e2"+
		"\u00e0\u0001\u0000\u0000\u0000\u00e3\u00e6\u0001\u0000\u0000\u0000\u00e4"+
		"\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000\u0000\u00e5"+
		"\u0013\u0001\u0000\u0000\u0000\u00e6\u00e4\u0001\u0000\u0000\u0000\u00e7"+
		"\u00e8\u00057\u0000\u0000\u00e8\u00e9\u0005#\u0000\u0000\u00e9\u00ea\u0005"+
		"7\u0000\u0000\u00ea\u0015\u0001\u0000\u0000\u0000\u00eb\u00ec\u00057\u0000"+
		"\u0000\u00ec\u0017\u0001\u0000\u0000\u0000\u00ed\u00ee\u00057\u0000\u0000"+
		"\u00ee\u0019\u0001\u0000\u0000\u0000\u00ef\u00f0\u0007\u0000\u0000\u0000"+
		"\u00f0\u001b\u0001\u0000\u0000\u0000\u00f1\u00f3\u0005%\u0000\u0000\u00f2"+
		"\u00f1\u0001\u0000\u0000\u0000\u00f2\u00f3\u0001\u0000\u0000\u0000\u00f3"+
		"\u00f5\u0001\u0000\u0000\u0000\u00f4\u00f6\u00052\u0000\u0000\u00f5\u00f4"+
		"\u0001\u0000\u0000\u0000\u00f5\u00f6\u0001\u0000\u0000\u0000\u00f6\u00fa"+
		"\u0001\u0000\u0000\u0000\u00f7\u00f9\u0005%\u0000\u0000\u00f8\u00f7\u0001"+
		"\u0000\u0000\u0000\u00f9\u00fc\u0001\u0000\u0000\u0000\u00fa\u00f8\u0001"+
		"\u0000\u0000\u0000\u00fa\u00fb\u0001\u0000\u0000\u0000\u00fb\u00fd\u0001"+
		"\u0000\u0000\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000\u00fd\u0105\u0003"+
		"\u001e\u000f\u0000\u00fe\u0100\u0007\u0001\u0000\u0000\u00ff\u0101\u0005"+
		"%\u0000\u0000\u0100\u00ff\u0001\u0000\u0000\u0000\u0100\u0101\u0001\u0000"+
		"\u0000\u0000\u0101\u0102\u0001\u0000\u0000\u0000\u0102\u0104\u0003\u001e"+
		"\u000f\u0000\u0103\u00fe\u0001\u0000\u0000\u0000\u0104\u0107\u0001\u0000"+
		"\u0000\u0000\u0105\u0103\u0001\u0000\u0000\u0000\u0105\u0106\u0001\u0000"+
		"\u0000\u0000\u0106\u0109\u0001\u0000\u0000\u0000\u0107\u0105\u0001\u0000"+
		"\u0000\u0000\u0108\u010a\u0005%\u0000\u0000\u0109\u0108\u0001\u0000\u0000"+
		"\u0000\u0109\u010a\u0001\u0000\u0000\u0000\u010a\u001d\u0001\u0000\u0000"+
		"\u0000\u010b\u010d\u00052\u0000\u0000\u010c\u010b\u0001\u0000\u0000\u0000"+
		"\u010c\u010d\u0001\u0000\u0000\u0000\u010d\u010e\u0001\u0000\u0000\u0000"+
		"\u010e\u0110\u0003 \u0010\u0000\u010f\u0111\u00053\u0000\u0000\u0110\u010f"+
		"\u0001\u0000\u0000\u0000\u0110\u0111\u0001\u0000\u0000\u0000\u0111\u0112"+
		"\u0001\u0000\u0000\u0000\u0112\u0114\u0003&\u0013\u0000\u0113\u0115\u0005"+
		"2\u0000\u0000\u0114\u0113\u0001\u0000\u0000\u0000\u0114\u0115\u0001\u0000"+
		"\u0000\u0000\u0115\u0116\u0001\u0000\u0000\u0000\u0116\u0118\u0003 \u0010"+
		"\u0000\u0117\u0119\u00053\u0000\u0000\u0118\u0117\u0001\u0000\u0000\u0000"+
		"\u0118\u0119\u0001\u0000\u0000\u0000\u0119\u001f\u0001\u0000\u0000\u0000"+
		"\u011a\u011c\u00052\u0000\u0000\u011b\u011a\u0001\u0000\u0000\u0000\u011b"+
		"\u011c\u0001\u0000\u0000\u0000\u011c\u011d\u0001\u0000\u0000\u0000\u011d"+
		"\u011f\u0003\"\u0011\u0000\u011e\u0120\u00053\u0000\u0000\u011f\u011e"+
		"\u0001\u0000\u0000\u0000\u011f\u0120\u0001\u0000\u0000\u0000\u0120\u012b"+
		"\u0001\u0000\u0000\u0000\u0121\u0123\u0003$\u0012\u0000\u0122\u0124\u0005"+
		"2\u0000\u0000\u0123\u0122\u0001\u0000\u0000\u0000\u0123\u0124\u0001\u0000"+
		"\u0000\u0000\u0124\u0125\u0001\u0000\u0000\u0000\u0125\u0127\u0003\"\u0011"+
		"\u0000\u0126\u0128\u00053\u0000\u0000\u0127\u0126\u0001\u0000\u0000\u0000"+
		"\u0127\u0128\u0001\u0000\u0000\u0000\u0128\u012a\u0001\u0000\u0000\u0000"+
		"\u0129\u0121\u0001\u0000\u0000\u0000\u012a\u012d\u0001\u0000\u0000\u0000"+
		"\u012b\u0129\u0001\u0000\u0000\u0000\u012b\u012c\u0001\u0000\u0000\u0000"+
		"\u012c!\u0001\u0000\u0000\u0000\u012d\u012b\u0001\u0000\u0000\u0000\u012e"+
		"\u0132\u00057\u0000\u0000\u012f\u0130\u0003$\u0012\u0000\u0130\u0131\u0005"+
		"7\u0000\u0000\u0131\u0133\u0001\u0000\u0000\u0000\u0132\u012f\u0001\u0000"+
		"\u0000\u0000\u0132\u0133\u0001\u0000\u0000\u0000\u0133#\u0001\u0000\u0000"+
		"\u0000\u0134\u0135\u0007\u0002\u0000\u0000\u0135%\u0001\u0000\u0000\u0000"+
		"\u0136\u0137\u0007\u0003\u0000\u0000\u0137\'\u0001\u0000\u0000\u0000\u0019"+
		"+1;IMS\u00d1\u00d9\u00e4\u00f2\u00f5\u00fa\u0100\u0105\u0109\u010c\u0110"+
		"\u0114\u0118\u011b\u011f\u0123\u0127\u012b\u0132";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
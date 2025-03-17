from enum import Enum

class TokenType(Enum):
    # Keywords
    WITH_DATA_FROM = 1
    CHART = 2
    COMPARE = 3
    DIFFERENCES = 4
    CONTRAST = 5
    VERSUS = 6
    SPLIT_BY = 7
    GROUPED_BY = 8
    DIFFERENCES_WITHIN = 9
    SHOW = 10
    STACKED_BY = 11
    SUBGROUPS = 12
    CORRELATION_BETWEEN = 13
    AND = 14
    LOG = 15
    FROM = 16
    PROPORTION_OF = 17
    SHARE_OF = 18
    PERCENTAGE_OF = 19
    BY = 20
    FREQUENCY_OF = 21
    DISTRIBUTION_OF = 22
    FREQUENCY_IN = 23
    BUCKETS = 24
    ACCUMULATION_OF = 25
    STACKED_TREND_OF = 26
    SCATTER_PLOT_OF = 27
    PATTERN_OF = 28
    BUBBLE_OF = 29
    FOR = 30
    TO = 31
    WHILE = 32
    IF = 33

    # Symbols
    LEFT_PAREN = 34
    RIGHT_PAREN = 35
    COLON = 36
    EXCLAMATION = 37

    # Operators
    PLUS = 38
    MINUS = 39
    MULTIPLY = 40
    DIVIDE = 41
    LESS_THAN = 42
    LESS_EQUAL = 43
    GREATER_THAN = 44
    GREATER_EQUAL = 45
    EQUAL = 46
    NOT_EQUAL = 47

    # Identifiers (Dynamic Tokens)
    IDENTIFIER = 48
    TABLE = 49
    VAR = 50
    CONTINUOUS_VAR = 51
    CONTINUOUS_CASES = 52
    RANGE = 53
    SUBGROUP = 54
    CASES = 55
    TREND_KEYWORD = 56

    # Numbers
    DIGIT = 57

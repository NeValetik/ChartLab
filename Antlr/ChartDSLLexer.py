# Generated from ChartDSL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,58,583,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,31,
        1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,
        1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,40,1,40,1,40,1,41,
        1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,46,1,47,
        1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,50,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,52,
        1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,1,53,
        1,53,1,53,1,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,
        1,55,1,55,1,56,1,56,1,56,5,56,568,8,56,10,56,12,56,571,9,56,1,57,
        1,57,1,58,1,58,1,59,4,59,578,8,59,11,59,12,59,579,1,59,1,59,0,0,
        60,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,
        35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,
        46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,
        56,113,57,115,0,117,0,119,58,1,0,3,2,0,65,90,97,122,1,0,48,57,3,
        0,9,10,13,13,32,32,583,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,
        0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,
        0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,
        0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,
        0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,
        0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,
        0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,
        0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,
        0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,119,1,0,0,0,
        1,121,1,0,0,0,3,126,1,0,0,0,5,131,1,0,0,0,7,138,1,0,0,0,9,146,1,
        0,0,0,11,150,1,0,0,0,13,162,1,0,0,0,15,171,1,0,0,0,17,178,1,0,0,
        0,19,187,1,0,0,0,21,198,1,0,0,0,23,217,1,0,0,0,25,222,1,0,0,0,27,
        233,1,0,0,0,29,243,1,0,0,0,31,268,1,0,0,0,33,272,1,0,0,0,35,276,
        1,0,0,0,37,295,1,0,0,0,39,298,1,0,0,0,41,312,1,0,0,0,43,331,1,0,
        0,0,45,349,1,0,0,0,47,370,1,0,0,0,49,388,1,0,0,0,51,396,1,0,0,0,
        53,412,1,0,0,0,55,429,1,0,0,0,57,445,1,0,0,0,59,456,1,0,0,0,61,466,
        1,0,0,0,63,468,1,0,0,0,65,471,1,0,0,0,67,473,1,0,0,0,69,476,1,0,
        0,0,71,482,1,0,0,0,73,484,1,0,0,0,75,486,1,0,0,0,77,488,1,0,0,0,
        79,491,1,0,0,0,81,493,1,0,0,0,83,496,1,0,0,0,85,498,1,0,0,0,87,500,
        1,0,0,0,89,502,1,0,0,0,91,504,1,0,0,0,93,506,1,0,0,0,95,509,1,0,
        0,0,97,511,1,0,0,0,99,514,1,0,0,0,101,517,1,0,0,0,103,520,1,0,0,
        0,105,535,1,0,0,0,107,544,1,0,0,0,109,554,1,0,0,0,111,560,1,0,0,
        0,113,564,1,0,0,0,115,572,1,0,0,0,117,574,1,0,0,0,119,577,1,0,0,
        0,121,122,5,119,0,0,122,123,5,105,0,0,123,124,5,116,0,0,124,125,
        5,104,0,0,125,2,1,0,0,0,126,127,5,102,0,0,127,128,5,114,0,0,128,
        129,5,111,0,0,129,130,5,109,0,0,130,4,1,0,0,0,131,132,5,99,0,0,132,
        133,5,104,0,0,133,134,5,97,0,0,134,135,5,114,0,0,135,136,5,116,0,
        0,136,137,5,58,0,0,137,6,1,0,0,0,138,139,5,99,0,0,139,140,5,111,
        0,0,140,141,5,109,0,0,141,142,5,112,0,0,142,143,5,97,0,0,143,144,
        5,114,0,0,144,145,5,101,0,0,145,8,1,0,0,0,146,147,5,102,0,0,147,
        148,5,111,0,0,148,149,5,114,0,0,149,10,1,0,0,0,150,151,5,100,0,0,
        151,152,5,105,0,0,152,153,5,102,0,0,153,154,5,102,0,0,154,155,5,
        101,0,0,155,156,5,114,0,0,156,157,5,101,0,0,157,158,5,110,0,0,158,
        159,5,99,0,0,159,160,5,101,0,0,160,161,5,115,0,0,161,12,1,0,0,0,
        162,163,5,99,0,0,163,164,5,111,0,0,164,165,5,110,0,0,165,166,5,116,
        0,0,166,167,5,114,0,0,167,168,5,97,0,0,168,169,5,115,0,0,169,170,
        5,116,0,0,170,14,1,0,0,0,171,172,5,118,0,0,172,173,5,101,0,0,173,
        174,5,114,0,0,174,175,5,115,0,0,175,176,5,117,0,0,176,177,5,115,
        0,0,177,16,1,0,0,0,178,179,5,115,0,0,179,180,5,112,0,0,180,181,5,
        108,0,0,181,182,5,105,0,0,182,183,5,116,0,0,183,184,5,32,0,0,184,
        185,5,98,0,0,185,186,5,121,0,0,186,18,1,0,0,0,187,188,5,103,0,0,
        188,189,5,114,0,0,189,190,5,111,0,0,190,191,5,117,0,0,191,192,5,
        112,0,0,192,193,5,101,0,0,193,194,5,100,0,0,194,195,5,32,0,0,195,
        196,5,98,0,0,196,197,5,121,0,0,197,20,1,0,0,0,198,199,5,100,0,0,
        199,200,5,105,0,0,200,201,5,102,0,0,201,202,5,102,0,0,202,203,5,
        101,0,0,203,204,5,114,0,0,204,205,5,101,0,0,205,206,5,110,0,0,206,
        207,5,99,0,0,207,208,5,101,0,0,208,209,5,115,0,0,209,210,5,32,0,
        0,210,211,5,119,0,0,211,212,5,105,0,0,212,213,5,116,0,0,213,214,
        5,104,0,0,214,215,5,105,0,0,215,216,5,110,0,0,216,22,1,0,0,0,217,
        218,5,115,0,0,218,219,5,104,0,0,219,220,5,111,0,0,220,221,5,119,
        0,0,221,24,1,0,0,0,222,223,5,115,0,0,223,224,5,116,0,0,224,225,5,
        97,0,0,225,226,5,99,0,0,226,227,5,107,0,0,227,228,5,101,0,0,228,
        229,5,100,0,0,229,230,5,32,0,0,230,231,5,98,0,0,231,232,5,121,0,
        0,232,26,1,0,0,0,233,234,5,115,0,0,234,235,5,117,0,0,235,236,5,98,
        0,0,236,237,5,103,0,0,237,238,5,114,0,0,238,239,5,111,0,0,239,240,
        5,117,0,0,240,241,5,112,0,0,241,242,5,115,0,0,242,28,1,0,0,0,243,
        244,5,115,0,0,244,245,5,104,0,0,245,246,5,111,0,0,246,247,5,119,
        0,0,247,248,5,32,0,0,248,249,5,99,0,0,249,250,5,111,0,0,250,251,
        5,114,0,0,251,252,5,114,0,0,252,253,5,101,0,0,253,254,5,108,0,0,
        254,255,5,97,0,0,255,256,5,116,0,0,256,257,5,105,0,0,257,258,5,111,
        0,0,258,259,5,110,0,0,259,260,5,32,0,0,260,261,5,98,0,0,261,262,
        5,101,0,0,262,263,5,116,0,0,263,264,5,119,0,0,264,265,5,101,0,0,
        265,266,5,101,0,0,266,267,5,110,0,0,267,30,1,0,0,0,268,269,5,97,
        0,0,269,270,5,110,0,0,270,271,5,100,0,0,271,32,1,0,0,0,272,273,5,
        108,0,0,273,274,5,111,0,0,274,275,5,103,0,0,275,34,1,0,0,0,276,277,
        5,115,0,0,277,278,5,104,0,0,278,279,5,111,0,0,279,280,5,119,0,0,
        280,281,5,32,0,0,281,282,5,112,0,0,282,283,5,114,0,0,283,284,5,111,
        0,0,284,285,5,112,0,0,285,286,5,111,0,0,286,287,5,114,0,0,287,288,
        5,116,0,0,288,289,5,105,0,0,289,290,5,111,0,0,290,291,5,110,0,0,
        291,292,5,32,0,0,292,293,5,111,0,0,293,294,5,102,0,0,294,36,1,0,
        0,0,295,296,5,98,0,0,296,297,5,121,0,0,297,38,1,0,0,0,298,299,5,
        115,0,0,299,300,5,104,0,0,300,301,5,111,0,0,301,302,5,119,0,0,302,
        303,5,32,0,0,303,304,5,115,0,0,304,305,5,104,0,0,305,306,5,97,0,
        0,306,307,5,114,0,0,307,308,5,101,0,0,308,309,5,32,0,0,309,310,5,
        111,0,0,310,311,5,102,0,0,311,40,1,0,0,0,312,313,5,115,0,0,313,314,
        5,104,0,0,314,315,5,111,0,0,315,316,5,119,0,0,316,317,5,32,0,0,317,
        318,5,112,0,0,318,319,5,101,0,0,319,320,5,114,0,0,320,321,5,99,0,
        0,321,322,5,101,0,0,322,323,5,110,0,0,323,324,5,116,0,0,324,325,
        5,97,0,0,325,326,5,103,0,0,326,327,5,101,0,0,327,328,5,32,0,0,328,
        329,5,111,0,0,329,330,5,102,0,0,330,42,1,0,0,0,331,332,5,115,0,0,
        332,333,5,104,0,0,333,334,5,111,0,0,334,335,5,119,0,0,335,336,5,
        32,0,0,336,337,5,102,0,0,337,338,5,114,0,0,338,339,5,101,0,0,339,
        340,5,113,0,0,340,341,5,117,0,0,341,342,5,101,0,0,342,343,5,110,
        0,0,343,344,5,99,0,0,344,345,5,121,0,0,345,346,5,32,0,0,346,347,
        5,111,0,0,347,348,5,102,0,0,348,44,1,0,0,0,349,350,5,115,0,0,350,
        351,5,104,0,0,351,352,5,111,0,0,352,353,5,119,0,0,353,354,5,32,0,
        0,354,355,5,100,0,0,355,356,5,105,0,0,356,357,5,115,0,0,357,358,
        5,116,0,0,358,359,5,114,0,0,359,360,5,105,0,0,360,361,5,98,0,0,361,
        362,5,117,0,0,362,363,5,116,0,0,363,364,5,105,0,0,364,365,5,111,
        0,0,365,366,5,110,0,0,366,367,5,32,0,0,367,368,5,111,0,0,368,369,
        5,102,0,0,369,46,1,0,0,0,370,371,5,115,0,0,371,372,5,104,0,0,372,
        373,5,111,0,0,373,374,5,119,0,0,374,375,5,32,0,0,375,376,5,102,0,
        0,376,377,5,114,0,0,377,378,5,101,0,0,378,379,5,113,0,0,379,380,
        5,117,0,0,380,381,5,101,0,0,381,382,5,110,0,0,382,383,5,99,0,0,383,
        384,5,121,0,0,384,385,5,32,0,0,385,386,5,105,0,0,386,387,5,110,0,
        0,387,48,1,0,0,0,388,389,5,98,0,0,389,390,5,117,0,0,390,391,5,99,
        0,0,391,392,5,107,0,0,392,393,5,101,0,0,393,394,5,116,0,0,394,395,
        5,115,0,0,395,50,1,0,0,0,396,397,5,97,0,0,397,398,5,99,0,0,398,399,
        5,99,0,0,399,400,5,117,0,0,400,401,5,109,0,0,401,402,5,117,0,0,402,
        403,5,108,0,0,403,404,5,97,0,0,404,405,5,116,0,0,405,406,5,105,0,
        0,406,407,5,111,0,0,407,408,5,110,0,0,408,409,5,32,0,0,409,410,5,
        111,0,0,410,411,5,102,0,0,411,52,1,0,0,0,412,413,5,115,0,0,413,414,
        5,116,0,0,414,415,5,97,0,0,415,416,5,99,0,0,416,417,5,107,0,0,417,
        418,5,101,0,0,418,419,5,100,0,0,419,420,5,32,0,0,420,421,5,116,0,
        0,421,422,5,114,0,0,422,423,5,101,0,0,423,424,5,110,0,0,424,425,
        5,100,0,0,425,426,5,32,0,0,426,427,5,111,0,0,427,428,5,102,0,0,428,
        54,1,0,0,0,429,430,5,115,0,0,430,431,5,99,0,0,431,432,5,97,0,0,432,
        433,5,116,0,0,433,434,5,116,0,0,434,435,5,101,0,0,435,436,5,114,
        0,0,436,437,5,32,0,0,437,438,5,112,0,0,438,439,5,108,0,0,439,440,
        5,111,0,0,440,441,5,116,0,0,441,442,5,32,0,0,442,443,5,111,0,0,443,
        444,5,102,0,0,444,56,1,0,0,0,445,446,5,112,0,0,446,447,5,97,0,0,
        447,448,5,116,0,0,448,449,5,116,0,0,449,450,5,101,0,0,450,451,5,
        114,0,0,451,452,5,110,0,0,452,453,5,32,0,0,453,454,5,111,0,0,454,
        455,5,102,0,0,455,58,1,0,0,0,456,457,5,98,0,0,457,458,5,117,0,0,
        458,459,5,98,0,0,459,460,5,98,0,0,460,461,5,108,0,0,461,462,5,101,
        0,0,462,463,5,32,0,0,463,464,5,111,0,0,464,465,5,102,0,0,465,60,
        1,0,0,0,466,467,5,44,0,0,467,62,1,0,0,0,468,469,5,97,0,0,469,470,
        5,116,0,0,470,64,1,0,0,0,471,472,5,61,0,0,472,66,1,0,0,0,473,474,
        5,116,0,0,474,475,5,111,0,0,475,68,1,0,0,0,476,477,5,119,0,0,477,
        478,5,104,0,0,478,479,5,105,0,0,479,480,5,108,0,0,480,481,5,101,
        0,0,481,70,1,0,0,0,482,483,5,40,0,0,483,72,1,0,0,0,484,485,5,41,
        0,0,485,74,1,0,0,0,486,487,5,58,0,0,487,76,1,0,0,0,488,489,5,105,
        0,0,489,490,5,102,0,0,490,78,1,0,0,0,491,492,5,33,0,0,492,80,1,0,
        0,0,493,494,5,111,0,0,494,495,5,114,0,0,495,82,1,0,0,0,496,497,5,
        43,0,0,497,84,1,0,0,0,498,499,5,45,0,0,499,86,1,0,0,0,500,501,5,
        42,0,0,501,88,1,0,0,0,502,503,5,47,0,0,503,90,1,0,0,0,504,505,5,
        60,0,0,505,92,1,0,0,0,506,507,5,60,0,0,507,508,5,61,0,0,508,94,1,
        0,0,0,509,510,5,62,0,0,510,96,1,0,0,0,511,512,5,62,0,0,512,513,5,
        61,0,0,513,98,1,0,0,0,514,515,5,61,0,0,515,516,5,61,0,0,516,100,
        1,0,0,0,517,518,5,33,0,0,518,519,5,61,0,0,519,102,1,0,0,0,520,521,
        5,112,0,0,521,522,5,114,0,0,522,523,5,111,0,0,523,524,5,103,0,0,
        524,525,5,114,0,0,525,526,5,101,0,0,526,527,5,115,0,0,527,528,5,
        115,0,0,528,529,5,105,0,0,529,530,5,111,0,0,530,531,5,110,0,0,531,
        532,5,32,0,0,532,533,5,111,0,0,533,534,5,102,0,0,534,104,1,0,0,0,
        535,536,5,116,0,0,536,537,5,114,0,0,537,538,5,101,0,0,538,539,5,
        110,0,0,539,540,5,100,0,0,540,541,5,32,0,0,541,542,5,111,0,0,542,
        543,5,102,0,0,543,106,1,0,0,0,544,545,5,103,0,0,545,546,5,114,0,
        0,546,547,5,111,0,0,547,548,5,119,0,0,548,549,5,116,0,0,549,550,
        5,104,0,0,550,551,5,32,0,0,551,552,5,111,0,0,552,553,5,102,0,0,553,
        108,1,0,0,0,554,555,5,66,0,0,555,556,5,69,0,0,556,557,5,71,0,0,557,
        558,5,73,0,0,558,559,5,78,0,0,559,110,1,0,0,0,560,561,5,69,0,0,561,
        562,5,78,0,0,562,563,5,68,0,0,563,112,1,0,0,0,564,569,3,115,57,0,
        565,568,3,115,57,0,566,568,3,117,58,0,567,565,1,0,0,0,567,566,1,
        0,0,0,568,571,1,0,0,0,569,567,1,0,0,0,569,570,1,0,0,0,570,114,1,
        0,0,0,571,569,1,0,0,0,572,573,7,0,0,0,573,116,1,0,0,0,574,575,7,
        1,0,0,575,118,1,0,0,0,576,578,7,2,0,0,577,576,1,0,0,0,578,579,1,
        0,0,0,579,577,1,0,0,0,579,580,1,0,0,0,580,581,1,0,0,0,581,582,6,
        59,0,0,582,120,1,0,0,0,4,0,567,569,579,1,6,0,0
    ]

class ChartDSLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    START_PROGRAM = 55
    END_PROGRAM = 56
    IDENTIFIER = 57
    WS = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'with'", "'from'", "'chart:'", "'compare'", "'for'", "'differences'", 
            "'contrast'", "'versus'", "'split by'", "'grouped by'", "'differences within'", 
            "'show'", "'stacked by'", "'subgroups'", "'show correlation between'", 
            "'and'", "'log'", "'show proportion of'", "'by'", "'show share of'", 
            "'show percentage of'", "'show frequency of'", "'show distribution of'", 
            "'show frequency in'", "'buckets'", "'accumulation of'", "'stacked trend of'", 
            "'scatter plot of'", "'pattern of'", "'bubble of'", "','", "'at'", 
            "'='", "'to'", "'while'", "'('", "')'", "':'", "'if'", "'!'", 
            "'or'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", 
            "'=='", "'!='", "'progression of'", "'trend of'", "'growth of'", 
            "'BEGIN'", "'END'" ]

    symbolicNames = [ "<INVALID>",
            "START_PROGRAM", "END_PROGRAM", "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "START_PROGRAM", "END_PROGRAM", 
                  "IDENTIFIER", "LETTER", "DIGIT", "WS" ]

    grammarFileName = "ChartDSL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



from antlr4.tree.Tree import TerminalNode

def print_tokens(tokens):
    """ Print tokens in a formatted table """
    print("\n\033[1;34mTokens:\033[0m")
    print("=" * 40)
    print(f"{'Index':<6} {'Text':<15} {'Type':<10} {'Line:Col'}")
    print("=" * 40)
    for token in tokens:
        token_text = token.text.replace("\n", "\\n")  # Escape newlines
        print(f"{token.tokenIndex:<6} {token_text:<15} {token.type:<10} {token.line}:{token.column}")
    print("=" * 40)


def print_parse_tree(tree, parser, prefix="", is_last=True):
    """ Print parse tree in a structured tree-like format """
    branch = "└── " if is_last else "├── "
    next_prefix = prefix + ("    " if is_last else "│   ")

    if isinstance(tree, TerminalNode):
        print(f"{prefix}{branch}🟢 {tree.getText()}")
    else:
        print(f"{prefix}{branch}🔷 {parser.ruleNames[tree.getRuleIndex()]}")

        if tree.children:
            for i, child in enumerate(tree.children):
                print_parse_tree(child, parser, next_prefix, i == len(tree.children) - 1)

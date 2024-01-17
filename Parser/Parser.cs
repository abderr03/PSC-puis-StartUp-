namespace Parser {

  /*
  var func = new Dictionary<string, Delegate>(){
    {"LABEL", new Func<string, Tuple<int, int>>(Label)},
    {"POINT", new Func<Tuple<int, int>, Tuple<int, int>>(Point)},

    {"LEFT", new Action<int>(Left)},
    {"RIGHT", new Action<int>(Right)},
    {"UP", new Action<int>(Up)},
    {"DOWN", new Action<int>(Down)},

    //{"GOTO", new Func<>(Goto)},
    {"IDLE", new Action(Idle)}
  };
  */

  public enum TokenType: int {
		// Delimiers:
		DELIMITER = -10,

		// Literals:
		INTEGER = 0,
		STRING = 1,

		// Others:
		INSTRUCTION = 11
	}
  public class Token {

    public TokenType type;
    public string value;

    public Token(TokenType type, string value) {
      this.type = type;
      this.value = value;
    }
  }

  public class Node {
    public Token label;
    public List<Node> children;

    public Node(Token label, List<Node> children) {
      this.label = label;
      this.children = children;
    }

    public void AddChildren(Node child) {
      this.children.Add(child);
    }
  }

  public class Parser {
    public static bool IsDelimiter(char chr) {
    switch (chr) {
      case '(':
      case ')':
      case ',':
        return true;
      default:
        return false;
    }
  }
    public static List<Token> Tokenize(string sequence) {
      List<Token> tokens = new List<Token>();

      int i = 0;
      while (i < sequence.Length) {
        char current_character = sequence[i];

        List<char> current_token_name = new List<char>(0);
        while (!IsDelimiter(current_character)) {
          if (current_character != ' ') {
            current_token_name.Add(current_character);
          }

          i += 1;
          current_character = sequence[i];
        }

        if (current_token_name.Count == 0) {
          tokens.Add(new Token(TokenType.DELIMITER, current_character.ToString()));
          i += 1;

        } else {
          string token_name = String.Join("", current_token_name);
          
          if (char.IsDigit(current_token_name[0])) {
            tokens.Add(new Token(TokenType.INTEGER, token_name));
          } else if (current_token_name[0] == '"') {
            tokens.Add(new Token(TokenType.STRING, token_name));
          } else if (char.IsLetter(current_token_name[0])) {
            tokens.Add(new Token(TokenType.INSTRUCTION, token_name));
          } else {
            throw new ArgumentException("Error: invalid token name:" + token_name);
          }
        }
      }
      return tokens;
    }

    public Node Parse(List<Token> tokens) {
      int idx = 0;

      List<Node> build() {
        List<Node> nodes = new List<Node>();

        if (tokens[idx].value != ")") {
          nodes.Add(new Node(tokens[idx], new List<Node>(0)));
          idx += 1;
        }

        while ((idx < tokens.Count) && (tokens[idx].value != ")")) {
          switch (tokens[idx].value) {
            case "(":
              idx += 1;
              nodes.Last().children = build();
              break;
            case ",":
              nodes.Add(new Node(tokens[idx + 1], new List<Node>(0)));
              idx += 2;
              break;
            default:
              throw new ArgumentException("Misplaces delimiter:" + tokens[idx - 1].value);;
          }
        }
      
        idx += 1;
        return nodes;
      }
      return build()[0];
    }

    public Tuple<int, int> Label(string label) {
      switch (label) {
        case "A":
          return new Tuple<int, int>(0, 0);
        default:
          throw new Exception("Invalid label: " + label);
      }
    }

    public object Instruction(Node ast) {
      switch (ast.label.value) {
        case "LABEL":
          return Label((string) Execute(ast.children[0]));
        case "POINT":
          return new Tuple<int, int>((int) Execute(ast.children[0]), (int) Execute(ast.children[1]));
        case "LEFT":
          if (ast.children.Count == 0) {
            return null;
          }
          return null;
        case "RIGHT":
          if (ast.children.Count == 0) {
            return null;
          }
          return null;
        case "UP":
          if (ast.children.Count == 0) {
            return null;
          }
          return null;
        case "DOWN":
          if (ast.children.Count == 0) {
            return null;
          }
          return null;
        case "IDLE":
          return null;
        default:
          throw new Exception("Invalid instruction: " + ast.label.value);
      }
    }

    public object Execute(Node ast) {

      switch (ast.label.type) {
        case TokenType.INSTRUCTION:
          return Instruction(ast);
        case TokenType.INTEGER:
          return Int32.Parse(ast.label.value);
        case TokenType.STRING:
          return ast.label.value;
        default:
          throw new Exception("Error!");
      }
    }

    public static void Main(string[] args) {
      string str = """    GOTO ( POINT ("A", 7, 6 ) )""";
      foreach (Token tk in Tokenize(str)) {
        Console.WriteLine(tk.value);
      }
    }
  }
}
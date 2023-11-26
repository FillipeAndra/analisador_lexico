# declaração dos tokens
IDENTIFICADOR = 'IDENTIFICADOR'
NUMERO_REAL = 'NUMERO REAL'
NUMERO_INTEIRO = 'NUMERO INTEIRO'
OPERADOR_ATRIBUICAO = 'OPERADOR ATRIBUICAO'
OPERADOR_SOMA = 'OPERADOR SOMA'
OPERADOR_SUBTRACAO = 'OPERADOR SUBTRACAO'
OPERADOR_DIVISAO = 'OPERADOR DIVISAO'
OPERADOR_RESTO = 'OPERADOR RESTO'
OPERADOR_POTENCIACAO = 'OPERADOR POTENCIACAO'
OPERADOR_MULTIPLICACAO = 'OPERADOR MULTIPLICACAO'
OPERADOR_MAIOR = 'OPERADOR MAIOR QUE'
OPERADOR_MENOR = 'OPERADOR MENOR QUE'
OPERADOR_MAIOR_IGUAL = 'OPERADOR MAIOR IGUAL QUE'
OPERADOR_MENOR_IGUAL = 'OPERADOR MENOR IGUAL QUE'
OPERADOR_DIFERENTE = 'OPERADOR DIFERENTE'
OPERADOR_IGUAL = 'OPERADOR IGUAL'
SETLE = 'SETLE'
KILL = 'KILL'
FLASK = 'FLASK'
BESARY = 'BESARY'
QUEN = 'QUEN'
IGNI = 'IGNI'
AARD = 'AARD'
YRDEN = 'YRDEN'
AXII = 'AXII'
ALKEMY = 'ALKEMY'
POTI = 'POTI'
HOWI = 'HOWI'
POP = 'POP'
JOURNAL = 'JOURNAL'
AB = 'AB'
ON = 'ON'
RB = 'RB'
SIGN = 'SIGN'
GINS = 'GINS'
NAWED = 'NAWED'
NEKER = 'NEKER'
NEKWAR = 'NEKWAR'
INT = 'INT'
FLOAT = 'FLOAT'
BOOL = 'BOOL'
STRING = 'STRING'
ABRE_PARENTESES = 'ABRE PARENTESES'
FECHA_PARENTESES = 'FECHA PARENTESES'
ABRE_CHAVES = 'ABRE CHAVES'
FECHA_CHAVES = 'FECHA CHAVES'
ARROBA = 'ARROBA'
TRUE = 'TRUE'
FALSE = 'FALSE'
PONTO = 'PONTO'
PONTO_VIRGULA = 'PONTO E VIRGULA'

# função que detecta os tokens e os transforma em string


def token(input_string):
  tokens = []
  i = 0

  while i < len(input_string):
    char = input_string[i]
    # detectores de número
    
    if char.isdigit():
      j = i
      while j < len(input_string) and (input_string[j].isdigit() or input_string[j] == '.'):
        j += 1
      num_str = input_string[i:j]
      if '.' in num_str:
        if num_str.count('.') == 1 and (input_string[j+1].isdigit()):
          tokens.append((NUMERO_REAL, num_str))
        else:
          raise ValueError("Número invalido: " + num_str)
      else:
        tokens.append((NUMERO_INTEIRO, num_str))
      i = j - 1

    # operadores aritiméticos /lógicos
    elif char == '=':
      if input_string[i + 1] == '=':
        tokens.append((OPERADOR_IGUAL, char))
        i += 1

      else:
        tokens.append((OPERADOR_ATRIBUICAO, char))

    elif char == '+':
      tokens.append((OPERADOR_SOMA, char))

    elif char == '-':
      tokens.append((OPERADOR_SUBTRACAO, char))

    elif char == '/':
      tokens.append((OPERADOR_DIVISAO, char))

    elif char == '%':
      tokens.append((OPERADOR_RESTO, char))

    elif char == '*':
      if input_string[i + 1] == '*':
        tokens.append((OPERADOR_POTENCIACAO, char))
        i += 1

      else:
        tokens.append((OPERADOR_MULTIPLICACAO, char))

    elif char == '>':
      if input_string[i + 1] == '=':
        tokens.append((OPERADOR_MAIOR_IGUAL, char))
        i += 1

      else:
        tokens.append((OPERADOR_MAIOR, char))

    elif char == '<':
      if input_string[i + 1] == '=':
        tokens.append((OPERADOR_MENOR_IGUAL, char))
        i += 1

      else:
        tokens.append((OPERADOR_MENOR, char))

    elif char == '!' and input_string[i + 1] == '=':
      tokens.append((OPERADOR_DIFERENTE, char))
      i += 1

    elif char == '(':
      tokens.append((ABRE_PARENTESES, char))

    elif char == ')':
      tokens.append((FECHA_PARENTESES, char))

    elif char == '{':
      tokens.append((ABRE_CHAVES))

    elif char == '}':
      tokens.append((FECHA_CHAVES, char))

    elif char == '@':
      tokens.append((ARROBA, char))
      
    elif char == '.':
      tokens.append((PONTO, char))
      
    elif char == ';':
      tokens.append((PONTO_VIRGULA, char))
      
    #detores de palavas/ identificadores

    elif char.isalpha():
      k = i
      while k < len(input_string) and (input_string[k].isalpha() or input_string[k] == '_'):
        k += 1
      alpha_str = list(input_string[i:k].lower().strip())
      

      if alpha_str[0] == 'b':
        if alpha_str[1:] == ['e', 's', 'a', 'r', 'y']:
          tokens.append((BESARY, input_string[i:k]))

        elif alpha_str[1:] == ['o', 'o', 'l']:
          tokens.append((BOOL, input_string[i:k]))

        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))

      elif alpha_str[0:] == ['q', 'u', 'e', 'n']:
        tokens.append((QUEN, input_string[i:k]))

      elif alpha_str[0] == 'i':
        if alpha_str[1:] == ['g','n','i']:
          tokens.append((IGNI, input_string[i:k]))

        elif alpha_str[1:] == ['n','t']:
          tokens.append((INT, input_string[i:k]))
        
        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))

      elif alpha_str[0] == 'a':
        if alpha_str[1:] == ['a','r','d']:
          tokens.append((AARD, input_string[i:k]))
        
        elif alpha_str[1:] == ['a','b']:
          tokens.append((AB, input_string[i:k]))
          
        elif alpha_str[1:] == ['x','i','i']:
          tokens.append((AXII, input_string[i:k]))
          
        elif alpha_str[1:] == ['l','k','e','m','y']:
          tokens.append((ALKEMY, input_string[i:k]))
          
        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))
          
      elif alpha_str[0:] == ['y','r','d','e','n']:
        tokens.append((YRDEN, input_string[i:k]))

      elif alpha_str[0] == 'p':
        if alpha_str[1:] == ['o','t','i']:
          tokens.append((POTI, input_string[i:k]))
        
        elif alpha_str[1:] == ['o','p']:
          tokens.append((POP, input_string[i:k]))
          
        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))

      elif alpha_str[0:] == ['h','o','w','i']:
        tokens.append((HOWI, input_string[i:k]))

      elif alpha_str[0:] == ['j','o','u','r','n','a','l']:
        tokens.append((JOURNAL, input_string[i:k]))

      elif alpha_str[0:] == ['o','n']:
        tokens.append((ON, input_string[i:k]))

      elif alpha_str[0:] == ['r','b']:
        tokens.append((RB, input_string[i:k]))

      elif alpha_str[0] == 's':
        if alpha_str[1:] == ['i','g','n']:
          tokens.append((SIGN, input_string[i:k]))
        
        elif alpha_str[1:] == ['t','r','i','n','g']:
          tokens.append((STRING, input_string[i:k]))
          
        elif alpha_str[1:] == ['e', 't', 'l', 'e']:
          tokens.append((SETLE, input_string[i:k]))
          
        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))

      elif alpha_str[0:] == ['g','i','n','s']:
        tokens.append((GINS, input_string[i:k]))

      elif alpha_str[0] == 'n':
        if alpha_str[1:] == ['a','w','e','d']:
          tokens.append((NAWED, input_string[i:k]))
          
        elif alpha_str[1:] == ['e','k','e','r']:
          tokens.append((NEKER, input_string[i:k]))

        elif alpha_str[1:] == ['e','k','w','a','r']:
          tokens.append((NEKWAR, input_string[i:k]))
          
        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))

      elif alpha_str[0] == 'f':
        if alpha_str[1:] == ['l','o','a','t']:
          tokens.append((FLOAT, input_string[i:k]))

        elif alpha_str[1:] == ['a','l','s','e']:
          tokens.append((FALSE, input_string[i:k]))
          
        elif alpha_str[1:] == ['l','a','s','k']:
          tokens.append((FLASK, input_string[i:k]))
          
        else:
          tokens.append((IDENTIFICADOR, input_string[i:k]))
        
      elif alpha_str[0:] == ['t','r','u','e']:
        tokens.append((TRUE, input_string[i:k]))
        
      elif alpha_str[0:] == ['k', 'i', 'l', 'l']:
        tokens.append((KILL, input_string[i:k]))

      else:
        tokens.append((IDENTIFICADOR, input_string[i:k]))

      i = k-1
    i += 1
  return tokens


tokens = token('+ besary dsdsds igni int yrden  bool.kill flask/ .2();')
for token_type, token_value in tokens:
  print(f"{token_type}: {token_value}")

    
    

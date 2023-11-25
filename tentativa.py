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
SETLE = '.SETLE'
KILL = '.KILL'
FLASK = '.FLASK'
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

# função que detecta os tokens e os transforma em string


def token(input_string):
  tokens = []
  i = 0
  index = 0

  while i < len(input_string):
    char = input_string[i]
    def alfabeto(string):
      alfa = list(string.strip(""))
      if alfa[0] == 'b':
        if alfa[1:] == ['e', 's', 'a', 'r', 'y']:
          tokens.append((BESARY, string))

        elif alfa[1:] == ['o', 'o', 'l']:
          tokens.append((BOOL, string))

        else:
          tokens.append((IDENTIFICADOR, string))

      elif alfa[0:] == ['q', 'u', 'e', 'n']:
        tokens.append((QUEN, string))

      elif alfa[0] == 'i':
        if alfa[1:] == 'gni':
          tokens.append((IGNI, string))

        elif alfa[1:] == 'nt':
          tokens.append((INT, string))

      elif alfa[0] == 'aard':
        tokens.append((AARD, string))

      elif alfa == 'yrden':
        tokens.append((YRDEN, string))

      elif alfa == 'axii':
        tokens.append((AXII, string))

      elif alfa == 'alkemy':
        tokens.append((ALKEMY, string))

      elif alfa == 'poti':
        tokens.append((POTI, string))

      elif alfa == 'howi':
        tokens.append((HOWI, string))

      elif alfa == 'pop':
        tokens.append((POP, string))

      elif alfa == 'journal':
        tokens.append((JOURNAL, string))

      elif alfa == 'ab':
        tokens.append((AB, string))

      elif alfa == 'on':
        tokens.append((ON, string))

      elif alfa == 'rb':
        tokens.append((RB, string))

      elif alfa == 'sign':
        tokens.append((SIGN, string))

      elif alfa == 'gins':
        tokens.append((GINS, string))

      elif alfa == 'nawed':
        tokens.append((NAWED, string))

      elif alfa == 'neker':
        tokens.append((NEKER, string))

      elif alfa == 'nekwar':
        tokens.append((NEKWAR, string))

      elif alfa == 'float':
        tokens.append((FLOAT, string))

      elif alfa == 'string':
        tokens.append((STRING, string))

      elif alfa == 'true':
        tokens.append((TRUE, string))

      elif alfa == 'false':
        tokens.append((FALSE, string))

      else:
        tokens.append((IDENTIFICADOR, string))
    # detectores de número
    
    if char.isdigit():
      j = i
      while j < len(input_string) and (input_string[j].isdigit()
                                       or input_string[j] == '.'):
        j += 1
      num_str = input_string[i:j]
      if '.' in num_str:
        if num_str.count('.') == 1:
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
    #detores de palavas/ identificadores

    

    elif char.isalpha() or char == '.':
      k = i
      while k < len(input_string) and (input_string[k].isalpha()
                                       or input_string[k] == '_'
                                       or input_string[k] == '.'):
        k += 1
      alpha_str = list(input_string[i:k].lower().strip())

      if '.' in alpha_str:
        if alpha_str.count('.') == 1:
          if alpha_str[0] != '.':
            (alpha_str)
            index = alpha_str.index('.')
            palavra1 = ''.join(alpha_str[0:index])
            alfabeto(palavra1)
            k -= (index + 1)

          elif alpha_str[0] == '.':
            if alpha_str[0:] == ['.', 's', 'e', 't', 'l', 'e']:
              tokens.append((SETLE, input_string[i:k]))

            elif alpha_str[0:] == ['.', 'k', 'i', 'l', 'l']:
              tokens.append((KILL, input_string[i:k]))

            elif alpha_str[0:] == ['.', 'f', 'l', 'a', 's', 'k']:
              tokens.append((FLASK, input_string[i:k]))
        else:
          raise ValueError("Palavra reservada escrita errada: " +
                           input_string[i:k])

      else:
        palavra = ''.join(alpha_str)
        alfabeto(palavra)
      
      i = k -1
      
    i += 1
  return tokens


tokens = token('+ besary dsdsds    bool.kill1.flask/.2()')
for token_type, token_value in tokens:
  print(f"{token_type}: {token_value}")

    
    

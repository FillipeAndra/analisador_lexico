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

# função que detecta os tokens e os transforma em string

def token(input_string):
  tokens = []
  i = 0
  while i < len(input_string):
    char = input_string[i]

    # detectores de número 
    if char.isdigit():
      j = i
      while j <len(input_string) and (input_string[j].isdigit() or input_string[j] == '.'):
        j += 1
      num_str = input_string[i:j]
      if '.' in num_str:
        if num_str.count('.') == 1:
          tokens.append((NUMERO_REAL,num_str))
        else:
          raise ValueError("Número invalido: " + num_str)
      else:
        tokens.append((NUMERO_INTEIRO,num_str))
      i = j

    # operadores aritiméticos /lógicos 
    if char == '=' and input_string[i+1] == '=':
      tokens.append((OPERADOR_IGUAL,char))
      i+=2

    elif char == '=':
      tokens.append((OPERADOR_ATRIBUICAO,char))
      i+=1

    elif char == '+':
      tokens.append((OPERADOR_SOMA,char))
      i+=1

    elif char == '-':
      tokens.append((OPERADOR_SUBTRACAO,char))
      i+=1

    elif char == '/':
      tokens.append((OPERADOR_DIVISAO,char))
      i+=1

    elif char == '%':
      tokens.append((OPERADOR_RESTO,char))
      i+=1

    elif char == '*' and input_string[i+1] == '*':
      tokens.append((OPERADOR_POTENCIACAO,char))
      i += 2

    elif char == '*':
      tokens.append((OPERADOR_MULTIPLICACAO,char))
      i+=1

    elif char == '>' and input_string[i+1] == '=':
      tokens.append((OPERADOR_MAIOR_IGUAL,char))
      i+=2

    elif char == '<' and input_string[i+1] == '=':
      tokens.append((OPERADOR_MENOR_IGUAL,char))
      i+=2

    elif char == '>':
      tokens.append((OPERADOR_MAIOR,char))
      i+=1

    elif char == '<':
      tokens.append((OPERADOR_MENOR,char))
      i+=1

    elif char == '!' and input_string[i+1] == '=':
      tokens.append((OPERADOR_DIFERENTE,char))
      i+=2
    
    elif char == '(':
       tokens.append((ABRE_PARENTESES,char))

    elif char == ')':
       tokens.append((FECHA_PARENTESES,char))

    elif char == '{':
       tokens.append((ABRE_CHAVES))

    elif char == '}':
       tokens.append((FECHA_CHAVES,char))

    elif char == '@':
        tokens.append((ARROBA,char))

    #detores de palavas/ identificadores
    if char.isalpha():
        k = i
        while k <len(input_string) and (input_string[k].isalpha() or input_string[k] == '.'):
            k += 1
        alpha_str = input_string[i:j].lower()
        if '_' in alpha_str:
            tokens.append((IDENTIFICADOR,alpha_str))

        elif '.' in alpha_str:
           
            if alpha_str.count('.') == 1 and alpha_str[0] == '.':
                
                if alpha_str == '.setle':
                    tokens.append((SETLE,alpha_str))

                elif alpha_str == '.kill':
                    tokens.append((KILL,alpha_str))

                elif alpha_str == '.flask':
                    tokens.append((FLASK,alpha_str))
            else:
                raise ValueError("Palavra reservada escrita errada: " + num_str)
              

        elif alpha_str == 'besary':
            tokens.append((BESARY,alpha_str))

        elif alpha_str == 'quen':
           tokens.append((QUEN,alpha_str))

        elif alpha_str == 'igni':
           tokens.append((IGNI,alpha_str))

        elif alpha_str == 'aard':
           tokens.append((AARD,alpha_str))

        elif alpha_str == 'yrden':
           tokens.append((YRDEN,alpha_str))

        elif alpha_str == 'axii':
           tokens.append((AXII,alpha_str))

        elif alpha_str == 'alkemy':
           tokens.append((ALKEMY,alpha_str))

        elif alpha_str == 'poti':
           tokens.append((POTI,alpha_str))

        elif alpha_str == 'howi':
           tokens.append((HOWI,alpha_str))

        elif alpha_str == 'pop':
           tokens.append((POP,alpha_str))

        elif alpha_str == 'journal':
           tokens.append((JOURNAL,alpha_str))
        
        elif alpha_str == 'ab':
            tokens.append((AB,alpha_str))

        elif alpha_str == 'on':
           tokens.append((ON,alpha_str))

        elif alpha_str == 'rb':
           tokens.append((RB,alpha_str))

        elif alpha_str == 'sign':
           tokens.append((SIGN,alpha_str))
        
        elif alpha_str == 'gins':
           tokens.append((GINS,alpha_str))

        elif alpha_str == 'nawed':
           tokens.append((NAWED,alpha_str))

        elif alpha_str == 'neker':
           tokens.append((NEKER,alpha_str))
        
        elif alpha_str == 'nekwar':
           tokens.append((NEKWAR,alpha_str))
           
        elif alpha_str == 'int':
           tokens.append((INT,alpha_str))

        elif alpha_str == 'float':
           tokens.append((FLOAT,alpha_str))

        elif alpha_str == 'string':
           tokens.append((STRING,alpha_str))

        elif alpha_str == 'bool':
           tokens.append((BOOL,alpha_str))

        elif alpha_str == 'true':
           tokens.append((TRUE,alpha_str))

        elif alpha_str == 'false':
           tokens.append((FALSE,alpha_str))

        else:
            tokens.append((IDENTIFICADOR,alpha_str))

        i = k
    while i< len(input_string) and input_string[i].isspace():
      i+=1
  
  return tokens

tokens = token()
for token_type, token_value in tokens:
    print(f"{token_type}: {token_value}")
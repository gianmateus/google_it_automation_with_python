# Pergunta 1
# # Você está trabalhando com um Arquivo CSV que contém informações de funcionários. 
# Cada registro tem um campo de nome, seguido de um campo de número de telefone e um campo de função. 
# O campo de número de telefone contém números de telefone dos EUA e 
# precisa ser modificado para o formato internacional, 
# com +1- na frente do número de telefone. O restante do número de telefone não deve ser alterado. 
# Preencha a expressão regular, usando grupos, para usar a função transform_record() para fazer isso.

import re
def transform_record(record):
  new_record = re.sub(___)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
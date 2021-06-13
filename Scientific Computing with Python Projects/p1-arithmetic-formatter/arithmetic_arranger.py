def arithmetic_arranger(problems,solve=False):

  


  letters="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
  if len(problems)>5:
    return "Error: Too many problems."
  for p in problems:
    if ("*" in p) or ("/" in p):
      return "Error: Operator must be '+' or '-'."
    for letter in p:
      if letter in letters:
        return "Error: Numbers must only contain digits."
    numbers=p.split()
    for number in numbers:
      if len(number)>4:
        return "Error: Numbers cannot be more than four digits."
  

  
  first_line=""
  second_line=""
  divider=""
  answerline=""

  for pccx in problems:
    numbers=pccx.split()
    longestnum = len(max(numbers, key=len))
    temp_fl=' '*(2+longestnum-len(numbers[0]))+numbers[0]
    temp_sl= numbers[1]+" "+' '*(longestnum-len(numbers[2]))+numbers[2]
    temp_divider='-'*(2+longestnum)
    if numbers[1]=="+":
      ans=int(numbers[0])+int(numbers[2])
    elif numbers[1]=="-":
      ans=int(numbers[0])-int(numbers[2])
    ans=str(ans)
    temp_ans=' '*(2+longestnum-len(ans))+ans


    first_line=first_line+temp_fl+"    "
    second_line=second_line+temp_sl+"    "
    divider=divider+temp_divider+"    "
    answerline=answerline+temp_ans+"    "

  first_line=first_line.rstrip()
  second_line=second_line.rstrip()
  divider=divider.rstrip()
  answerline=answerline.rstrip()

  if solve==True:
    arranged_problems=first_line+"\n"+second_line+"\n"+divider+"\n"+answerline
  else:
    arranged_problems=first_line+"\n"+second_line+"\n"+divider
  
  print("\n\n\n\n Qs: \n",problems,"\n",solve)
  print("\n Ans: \n")
  print(arranged_problems,"\n\n\n\n\n")

  return arranged_problems
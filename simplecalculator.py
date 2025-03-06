for choice in range(1,5):
  a= int(input("Enter first value: "))
  b= int(input("Enter second value: "))
  print("Press 1 for Addittion\nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
  option =int(input("Enter your option: "))
  match(option):
    case 1:
      add=a+b
      print("Addition : ", add)
    case 2:
      sub = a-b
      print("Subtraction : ",sub)
    case 3:
      product = a*b
      print("Multiplication : ", product)
    case 4:
      division = a/b
      print("Division : ",division)

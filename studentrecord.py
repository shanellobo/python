for i in range(1,3):
  name=input("Enter your name: ")
  regno=int(input("enter the register number"))
  marks1=float(input("enter the marks of subject 1"))
  marks2=float(input("enter the marks of subject 2"))
  marks3=float(input("enter the marks of subject 3"))
  marks=[marks1+marks2+marks3]
  avg=(marks1+marks2+marks3)/3
  passed=avg>=40
  student_record={"name":name,"register":regno,"marks":marks,"avg":avg,"passed":passed}
  print("\n========= Student Record =========")
  print("Name is: ",student_record["name"])
  print("Registration number: ",student_record["register"])
  print("Marks: ",student_record["marks"])
  print("Average: ",student_record["avg"])
  print("Passed: ",student_record["passed"])

#functions with outputs
def my_function():
  result = 3 * 2
  return result #return is the output keywork
                #output = result #likewise that can be saved to a                   variable 

def format_name(f_name, l_name):
  print(f_name.title())
  print(l_name.title())

format_name("wisti", "WISTIsEn")

#almost same as above, but formatted so both first and last mname appreat on same line  
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  print(f"{formated_f_name} {formated_l_name}")

format_name("wisti", "wISTisen")

#same end result as above 
def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("wISti", "wISTISen")
print(formated_string)


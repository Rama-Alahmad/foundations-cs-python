#assignment_04
## Exercise1 ##

def display_menu():
    print( "1. Sum Tuples\n"+"2. Export JSON\n"+"3. Import JSON\n"+"4. Exit")

        
def Sum_Tuples(tup1,tup2):
  lst1= []
  if len(tup1)==len(tup2): 
   for i in range(len(tup1)):
    lst1.append(tup1[i]+tup2[i])
   tup3 =tuple(lst1)
   return tup3
  else:
     print("different tupple length")

def Export_JSON(D,filename):
    json_s= "{\n"
    with open(filename, "w") as file:
        file.write(json_s)
        for key, value in D.items():
         json_s = f'"{key}":' 
         if isinstance(value,str): 
            json_s = f'"{value}"'
         elif isinstance(value,(int,float)):
            json_s = str(value) 
         elif isinstance(value,bool):
            json_s = str(value).lower() 
         elif isinstance(value,list):
            json_s = "[" + ",".join(f'"{item}') +']'
         elif value is None:
            json_s = 'null' 
         else:
            print("unavailable") 
         file.write(f'"{key}": {value}, \n')
         file.write("}\n")
   

def Import_JSON(JSON_File_Name):
    with open(JSON_File_Name, 'r') as f:
        js_Data = f.read().strip(' \n\t\r{}[]')
    js_Data = js_Data.replace('\n', '').replace(' ', '')
    objects = js_Data[1:-1].split('},{')
    dictionaries = []
    for obj in objects:
        obj = obj.strip(' {}')
        dictionary = {}
        item = obj.split(',')
        for item in items:
               keyValue= item.split(':', 1)
               key = keyValue[0].strip().strip('"')  
               value = keyValue[1].strip()
               dictionary[key] = value
        dictionaries.append(dictionary)

    return dictionaries

def main():
    display_menu()
    choice=int(input("Enter a choice:"))
    while(choice != 4):
      
      if choice == 1:
        tup1=tuple(map(int,input("Enter first set of int :").split()))
        tup2=tuple(map(int,input("Enter the second set of int :").split()))
        print("the result is:",Sum_Tuples(tup1,tup2))


      elif choice == 2:
        D = {}
        n = int(input("Enter the number of items(key+value) in the dictionary: "))
        for i in range(n):
                key = input(f"Enter key {i+1}: ")
                value = input(f"Enter value of key '{key}': ")
                D[key] = value
        filename = input("Enter file name: ")
        print("Export_JSON File Done succesfully ")


      elif choice == 3:
        JSON_File_Name = input("Enter the file name: ")
        dictionaries = Import_JSON(JSON_File_Name)
        print("Dictionaries Imported From JSON File: ")
        for i, d in enumerate(dictionaries):
            print(f"Dictionary {i+1}: {d}")


      elif choice == 4:
        break

      else:
        print("invalid choice,Try again") 

      display_menu()
      choice=int(input("Enter a choice:"))
    print("--------------")  
main()    

## Exercise2 ##

def a(N):
    return 1 / 6 * N + 8000 * N**3 + 24#(O(N^3))


def b(N):
    return 1 / 6 * N**3#(O(N^3))


def c(N):
    1 / 6 * factorial(N) + 200 * N**4 #(O(N!))
# def factorial(N):
#     result = 1
#     for i in range(1, N + 1):
#         result *= i
#     return result


def d(N):
    return N * log(N) + 1000 #(O(N \log N))


def e(N):
    return log(N) + N #(O(N))
# def log(N):
#     result = 0
#     while N > 1:
#         N /= 2
#         result += 1
#     return result

def f(N):
    return 1 / 2 * N * (N - 1) #(O(N^2))


def g(N):
    return N**2 + 200 * N ** log(N * 2) + 3 * N + 9000 #(O(N^2))


def h(N):
    return factorial(N) + 3 * N + 2 * N + N**3 + N**2 #(O(N!))


def main_2():
    N = 10

    print("a(N) =", a(N))
    print("b(N) =", b(N))
    print("c(N) =", c(N))
    print("d(N) =", d(N))
    print("e(N) =", e(N))
    print("f(N) =", f(N))
    print("g(N) =", g(N))
    print("h(N) =", h(N))

main_2()
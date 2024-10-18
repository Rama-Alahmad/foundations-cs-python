# assignment_03
def display_menu():
   print("1. Count Digits\n"+"2. Find Max\n"+"3. Count Tags\n"+"4. Exit")


def Count_Digits(n):
  if n == 0 :
    return 0
  else :
    return 1 + Count_Digits(n//10)


def Find_Max(lst,v):
   if not v:
     return 0
   elif v == 1:
    return lst[0]
   else:
     Max_value = Find_Max(lst,v-1)
     if lst[v-1] > Max_value:
       return lst[v-1]
     else :
      return Max_value   
   
def Count_Tags(html_code, tags):
    opening_tag = f"<{tags}"
    closing_tag = f"</{tags}>"
    count = 0
    start_index = html_code.find(opening_tag)
    
    while start_index != -1:
        end_index = html_code.find(closing_tag, start_index)
        if end_index == -1:
            break
        else:
         count += 1
         start_index = html_code.find(opening_tag, end_index)
    
    return count
html_code = '''
<!DOCTYPE html>
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>'''   

   
def main():
  display_menu()
  choice= int(input("Enter a choice:"))
  
  while (choice!=4):
   if choice == 1:
     num =int(input("Enter an integer:"))
     print("Number of Digits is:",Count_Digits(num))
   elif choice == 2:
      lst = input("Enter a list of integers :")
      v = len(lst)
      print("Maximum_Number is:",Find_Max(lst,v))   
   elif choice == 3:
      tags = input("Enter a tag:")
      print("Number of tags occurrences is:",Count_Tags(html_code, tags))
   elif choice == 4:
      break 
   else:
    print ("invalid choice")

   display_menu()
   choice= int(input("Enter a choice:"))

  print("-----------") 
main()  

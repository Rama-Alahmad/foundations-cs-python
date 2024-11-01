# # #assignment_05


# def display_menu():
#     print("1. Add Course\n"+"2. Enroll Student\n"+"3. Drop Course\n"+"4. List Student Courses\n"+"5. Save Course Catalog\n"+"6. Load Course Catalog\n"+"7. Exit\n"+"_ _ _ _ _ _ _ _ _ _ _ _ _ ") 

# class Node:
#     def __init__(self,data): 
#       self.data= data # data = course or student
#       self.next= None

# class linkedlist:
#     def __init__(self): 
#       self.head = None 

#     def append(self, data): 
#         new_node = Node(data) 
#         if not self.head: 
#           self.head = new_node 
#           return 
#         last_node = self.head 
#         while last_node.next:  
#           last_node = last_node.next 
#         last_node.next = new_node 

#     def remove(self, data): 
#       current_node = self.head 
#       prev_node = None 
#       while current_node and current_node.data != data: 
#          prev_node = current_node 
#          current_node = current_node.next 
#          if prev_node is None: 
#              self.head = current_node.next
#          elif current_node: 
#             prev_node.next = current_node.next 

#     def find(self, key, attr): 
#       current_node = self.head 
#       while current_node: 
#          if getattr(current_node.data, attr) == key: 
#             return current_node.data 
#          current_node = current_node.next 
#          return None 
      
#     def display(self): 
#       elements = [] 
#       current_node = self.head 
#       while current_node: 
#          elements.append(current_node.data) 
#          current_node = current_node.next 
#       return

# class Course:
#      def __init__(self, code, name, credits): 
#         self.code = code 
#         self.name = name 
#         self.credits = credits

# class Student: 
#      def __init__(self, student_id, name): 
#         self.student_id = student_id 
#         self.name = name 
#         self.courses = {} 

#      def enroll(self, course): 
#             if course in self.courses: 
#                 raise Exception("Already enrolled") 
#             self.courses.append(course) 

#      def drop(self, course): 
#         if course not in self.courses:  
#             raise Exception("Not enrolled in course") 
#         self.courses.remove(course) 
        
#      def list_courses(self): 
#         return self.courses.values()
     
# def save_catalog(catalog, filename): 
#     with open(filename, 'w') as file: 
#        json.dump([course.__dict__ for course in catalog.display()], file) 

# def load_catalog(filename): 
#     catalog = linkedlist()
#     with open(filename, 'r') as file:  
#          for data in json.load(file):
#           catalog.append(Course(**data))   
#     return catalog
# def main(): 
#     catalog = linkedlist() 
#     students = linkedlist() 

#     while True:
#          display_menu() 
#          choice = int(input("Choose an option: "))
#          if choice == 1: 
#             code = input("Course code: ") 
#             name = input("Course name: ") 
#             credits = int(input("Credit hours: ")) 
#             catalog.append(Course(code, name, credits))

#          elif choice == 2: 
#             student_id = input("Student ID: ") 
#             name = input("Student name: ")
#             course_code = input("Course code to enroll: ") 
#             student = students.find(student_id, 'student_id') 
#             if not student: 
#                student = Student(student_id, name) 
#                students.append(student) 
#             course = catalog.find(course_code, 'code')
#             if course: 
#                 student.enroll(course) 

#          elif choice == 3: 
#             student_id = input("Student ID: ") 
#             course_code = input("Course code to drop: ") 
#             student = next((s for s in students if s.student_id == student_id), None) 
#             if student: 
#                course = next((c for c in catalog if c.code == course_code), None) 
#             if course: 
#                 student.drop(course)

#          elif choice == 4: 
#                student_id = input("Student ID: ") 
#                student = students.find(student_id, 'student_id')
#                if student: 
#                   for course in student.list_courses(): 
#                      print(f"{course.code}: {course.name} ({course.credits} credits)")

#          elif choice == 5: 
#                filename = input("Filename to save catalog: ") 
#                save_catalog(catalog, filename) 
               
#          elif choice == 6: 
#                filename = input("Filename to load catalog: ") 
#                catalog = load_catalog(filename) 
               
#          elif choice == 7 :
#                 break
#          else:
#           print("invalid choice,Try again")  

# university_system = main()
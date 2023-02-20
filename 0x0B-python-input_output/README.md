# 0x0B. Python - Input/Output
## 0. Read file
### Instructions
Write a function that reads a text file (UTF8) and prints it to stdout:

1. Prototype: `def read_file(filename=""):`
2. You must use the with statement
3. You don’t need to manage file permission or file doesn't exist exceptions.
4. You are not allowed to import any module
<hr>

## 1. Write to a file
### Instructions
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

1. Prototype: ``def write_file(filename="", text=""):``
2. You must use the with statement
3. You don’t need to manage file permission exceptions.
4. Your function should create the file if doesn’t exist.
5. Your function should overwrite the content of the file if it already exists.
6. You are not allowed to import any module
<hr>

## 2. Append to a file
### Instructions
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

1. Prototype: `def append_write(filename="", text=""):`
2. If the file doesn’t exist, it should be created
3. You must use the with statement
4. You don’t need to manage file permission or file doesn't exist exceptions.
5. You are not allowed to import any module
<hr>

## 3. To JSON string
### Instructions
Write a function that returns the JSON representation of an object (string):

1. Prototype: `def to_json_string(my_obj):`
2. You don’t need to manage exceptions if the object can’t be serialized.
<hr>

## 4. From JSON string to Object
### Instructions
Write a function that returns an object (Python data structure) represented by a JSON string:

1. Prototype: `def from_json_string(my_str):`
2. You don’t need to manage exceptions if the JSON string doesn’t represent an object.
<hr>

## 5. Save Object to a file
### Instructions
Write a function that writes an Object to a text file, using a JSON representation:

1. Prototype: `def save_to_json_file(my_obj, filename):`
2. You must use the with statement
3. You don’t need to manage exceptions if the object can’t be serialized.
4. You don’t need to manage file permission exceptions.
<hr>

## 6. Create object from a JSON file
### Instructions
Write a function that creates an Object from a “JSON file”:

1. Prototype: `def load_from_json_file(filename):`
2. You must use the with statement
3. You don’t need to manage exceptions if the JSON string doesn’t represent an object.
4. You don’t need to manage file permissions / exceptions.
<hr>

## 7. Load, add, save
### Instructions
Write a script that adds all arguments to a Python list, and then save them to a file:

1. You must use your function save_to_json_file from 5-save_to_json_file.py
2. You must use your function load_from_json_file from 6-load_from_json_file.py
3. The list must be saved as a JSON representation in a file named add_item.json
4. If the file doesn’t exist, it should be created
5. You don’t need to manage file permissions / exceptions.
<hr>

## 8. Class to JSON
### Instructions
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

1. Prototype: `def class_to_json(obj):`
2. `obj` is an instance of a Class
3. All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
4. You are not allowed to import any module
<hr>

## 9. Student to JSON
### Instructions
Write a class Student that defines a student by:

1. Public instance attributes:
   * first_name
   * last_name
   * age
2. Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`
3. Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
4. You are not allowed to import any module
<hr>

## 10. Student to JSON with filter
### Instructions
Write a class Student that defines a student by: `(based on 9-student.py)`

1. Public instance attributes:
   * first_name
   * last_name
   * age
2. Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`
3. Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
4. If attrs is a list of strings, only attribute names contained in this list must be retrieved.
5. Otherwise, all attributes must be retrieved
6. You are not allowed to import any module
<hr>

## 11. Student to disk and reload
### Instructions
Write a class Student that defines a student by: (based on 10-student.py)

1. Public instance attributes:
   * first_name
   * last_name
   * age
2. Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`
3. Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
4. If attrs is a list of strings, only attributes name contain in this list must be retrieved.
5. Otherwise, all attributes must be retrieved
6. Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance:
7. You can assume json will always be a dictionary
8. A dictionary key will be the public attribute name
9. A dictionary value will be the value of the public attribute
10. You are not allowed to import any module
<hr>

## 12. Pascal's Triangle
### Instructions
Technical interview preparation:

1. You are not allowed to google anything
2. Whiteboard first
3. Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

4. Returns an empty list if n <= 0
5. You can assume n will be always an integer
6. You are not allowed to import any module
<hr>

## 13. Search and update
### Instructions
#### advanced
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

1. Prototype: `def append_after(filename="", search_string="", new_string=""):`
2. You must use the with statement
3. You don’t need to manage file permission or file doesn't exist exceptions.
4. You are not allowed to import any module
<hr>

## 14. Log parsing
### Instructions
#### advanced
Write a script that reads stdin line by line and computes metrics:

1. Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
2. Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
   * Total file size: File size: <total size>
   * where is the sum of all previous (see input format above)
   * Number of lines by status code:
   * possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
   * if a status code doesn’t appear, don’t print anything for this status code
   * format: <status code>: <number>
   * status codes should be printed in ascending order



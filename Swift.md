### Swift basic
  
#### 1. Simple Values
 - trong swift biên được khai báo bằng từ khoá var hoặc let, các biến ko bao h ngầm (implicitly) convert to another type
 - explicitly make an instance of the desired type Nếu muốn convert phải tạo một instance của kiểu mong muốn Exp: String(10) ỏ UInt("20")
 - Muốn điền biến vào trong string thì dùng cú pháp "Hello \(var)" write the back slash before parentheses
 - Muốn viết string nhiều dòng (multiple line) dùng syntax """ string here """ 
#### 2. Array
>  let emptyArray = [String]() _or_ emptyArray = []

```swift
- Tao mang co nhieu phan tu
let newArray = Array(repeating: 5, count: 10)
print(newArray)

- Cac build in function
let newArray = Array(repeating: 5, count: 10)
print(newArray)

var phones = ["iphone", "samsung", "HTC"]
phones.append("BlackBerry")
phones += ["Nokia"]
print(phones)

phones.remove(at: 1)
print(phones)

for (index, value) in phones.enumerated() {
    print(index, value)
}
```

#### 3. Kiểu tập hợp (tập cha, tập con, ..., các phương thức chứa, giao, giao ngoài ...) SET
> Là kiểu dữ liệu giống như mảng nhưng ko quan tâm đến thứ tự, no có các phương thức hoàn toàn giống array 
```swift
- Co them mot thuoc tinh khac
let set1: Set = [1,2,3,4,5,6]
let set2: Set = [4,6,8,9,10]
let itersection = set1.intersection(set2) // [4,6]

-union, subtracting, symetricDiffence ...
```
 
#### 3. Dictionary (là kiểu dữ liệu trong đó mỗi phần tử có key và value)
>  let emptyDictionary = [Key: Value]() _or_ emptyDictionary = [:]
```swift

let dictionary = ["name": "Anh Tus", "email": "anhtu@gmail.com"]
print(dictionary)
for (key, value) in dictionary {
    print(key, value)
}
for key in dictionary.keys {
    print(key)
}
for value in dictionary.values {
    print(value)
}
```
  
#### 4. Tuple 
> let (width, height) = (800, 600)
```Comparator operator
let (width, height) = (800, 600)
(width, height) < (400, 200)
```
  
#### 5.Arithmatic operater
> 

#### 6. For ... in {}
```swift
let range = 1...8
print(range)
let array = ["cat", "dog" ,"dinosaur", "lion"]
for x in array[...1] {
    print(x)
}
```
#### 7. Control flow (la cac vong lap for, while, if _ else, switch _ case)
- For iterate
```switch
for x in 0...<10 {
  print(x)
}
for x in stride(from: 1, to: 10, by: 0.1) {
  print(x)
}
- While interate
var start = 0
while (start < 100) {
  start += 1
  if (start % 2 = 0) {
    continue;
  }
}
- Repeat while          1
var start = 0
repeat {
    print(start)
} while start < 100
```
  
#### 8. Function:

#### 9. Closure:

#### 10. Enum

#### 11. Structure 
> Kieu luu tru gia tri tham tri (Validity)
- Structure
```swift
 struct markStruct {
   var mark1: Int
   var mark2: Int
   var mark3: Int

   init(mark1: Int, mark2: Int, mark3: Int) {
      self.mark1 = mark1
      self.mark2 = mark2
      self.mark3 = mark3
   }
}

var marks = markStruct(mark1: 98, mark2: 96, mark3:100)
print(marks.mark1)
print(marks.mark2)
print(marks.mark3)
```
#### 12. Class 
> Kieu luu tru gia tri tham chiếu (Reference)
- Structure
```swift
 class Student {
   var studentname: String
   var mark: Int 
   var mark2: Int 
   init(studentname: String, mark1: Int, mark2: Int) {
      self.studentname = studentname
      self.mark1 = mark1
   }
}
var student1 = Student("studentname", "mark1")
```
#### 13. 

  

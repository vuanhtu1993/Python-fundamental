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
- Inherit
```swift
 class Animal {
   // Attribute can be assigned
   var name: String = ""
   func eat() {
     print("Animal is eating")
   }
   // Read only attribute
   var description: String {
     return "this is an animal name \(self.name)"
   }
 }
 
 class Dog: Animal {
   func yarg() {
     print("the dog is yarging")
   }
   override func eat() {
     super.eat()
     print('the dog can also yarg')
   }
 {
 
 var myDog = Dog()
 myDog.yarg()
 myDog.eat()
```
#### 13. 

#### 14.

#### 15.

#### 16. Extension
> To add more method to the existing class or struct
``` swift

extension UIColor {
    static func rgba(_ r: CGFloat, _ g: CGFloat, _ b: CGFloat, _ a: CGFloat) -> UIColor {
        return UIColor(red: r/255.0, green: g/255.0, blue: b/255.0, alpha: a)
    }
    static func uiColorFromHex(_ hex: UInt, _ alpha: CGFloat) -> UIColor {
        let r = CGFloat((hex & 0xFF0000) >> 16) / 255.0
        let g = CGFloat((hex & 0x00FF00) >> 8) / 255.0
        let b = CGFloat(hex & 0x0000FF) / 255.0
        return self.init(red: r, green: g, blue: b, alpha: alpha)
    }
}

var darkRed = UIColor.uiColorFromHex(888888, 0.5)
print(darkRed)

```

#### 17. Protocol
> Dùng để định nghĩa các kiểu phương thức và thuộc tính cho enum, class, struct
```swift
// Protocol
protocol InitialProtocol{
    var name: String {get}
    init(name: String)
}

class People {
    
}
// Class Person inherited from People and conform InitialProtocol
class Person: People, InitialProtocol {
    var name: String
    
    required init(name: String) {
        self.name = name
    }
}

var person1 = Person(name: "Tus")
```
  
#### 17. Delegate

#### 18. Generic
> Presentation for the TYPE of variable, output function, ...
> Instead of fixed the type variable and output function we can define it when calling
```swift
// Generic
func swapVariable<T>(var1: inout T, var2: inout T) {
    let temp = var1
    var1 = var2
    var2 = temp
}

var a = 10
var b = 20
swapVariable(var1: &a, var2: &b)
print(a, b)

func findItem<T: Equatable> (of target: T, in arrayItem: [T]) -> Int? {
    for (index, item) in arrayItem.enumerated() {
        if(target == item) {
            return index
        }
    }
    return nil
}
let name = "AnhTus"
let arrayName = ["A", "B", "AnhTus"]
findItem(of: name, in: arrayName)
```

### Swift basic
  
#### 1. Simple Values
 - trong swift biên được khai báo bằng từ khoá var hoặc let, các biến ko bao h ngầm (implicitly) convert to another type
 - explicitly make an instance of the desired type Nếu muốn convert phải tạo một instance của kiểu mong muốn Exp: String(10) ỏ UInt("20")
 - Muốn điền biến vào trong string thì dùng cú pháp "Hello \(var)" write the back slash before parentheses
 - Muốn viết string nhiều dòng (multiple line) dùng syntax """ string here """ 
#### 2. Array
>  let emptyArray = [String]() _or_ emptyArray = []
 
#### 3. Dictionary
>  let emptyDictionary = [String: Float]() _or_ emptyDictionary = [:]
  
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

  
  
  

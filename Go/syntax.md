# <center> Go
---
# Packages

Every Go program is made up of packages.

Programs start running in package `main`.

## import
```go
import (
    "fmt"
    "math"
)
```
```go
import "fmt"
import "math"
```
the package name is the same as the last element of the import path

## Exported names
In Go, a name is exported if it begins with a capital letter
`math.pi` ×
`math.Pi` √

# Functions
```go
func add(x int, y int) int {
    return x + y
}
```
multiple results
```go
func swap(x, y string) (string, string) {
    return y, x
}

func main() {
    a, b := swap("hello", "world")
    fmt.Println(a, b)
}
```
Named return values
```go
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

func main() {
    a, b := split(17)
}
```

# Variables

## Declaration & Initialization
```go
var i int
var j = 1
var (
    ToBe   bool       = false
    MaxInt uint64     = 1<<64 - 1
    z      complex128 = cmplx.Sqrt(-5 + 12i)
)
k := 2  // function level only
```
Outside a function, every statement begins with a keyword (`var`, `func`, and so on) and so the `:=` construct is not available.

Variables declared without an explicit initial value are given their **zero value**
- `0` for numeric types,
- `false` for the boolean type, and
- `""` (the empty string) for strings.

## Basic Types
```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```
## Type Conversions
The expression `T(v)` converts the value `v` to the type `T`.

## Type inference
When declaring a variable without specifying an explicit type, the variable's type is inferred from the value on the right hand side.
```go
i := 42           // int
f := 3.142        // float64
g := 0.867 + 0.5i // complex128
```
# Constants

```go
const identifier [type] = value
```
An untyped constant takes the type needed by its context.

Numeric constants are high-precision values.

---
# Control Flow

## Iteration 
```go
for i := 0; i < 10; i++ {
    sum += i
}
```
The init and post statements are optional.
`for` is Go's `while`
```go
sum := 1
for sum < 1000 {
    sum += sum
}
```
forever
```go
for {
}
```

## Conditon
### If
```go
if x < 1 { fmt.Println(x) }
```

if with a short statement
```go
if v := math.Pow(x, n); v < lim {
    return v
}
```
Variables declared by the statement are only in scope until the end of the `if`
### If and Else
Variables declared inside an `if` short statement are also available inside any of the `else` blocks.
```go
if v := math.Pow(x, n); v < lim {
    return v
} else {
    fmt.Printf("%g >= %g\n", v, lim)
}
```
### Swith
Switch cases evaluate cases from top to bottom, stopping when a case succeeds.
```go
switch os := runtime.GOOS; os {
case "darwin":
    fmt.Println("macOS.")
case "linux":
    fmt.Println("Linux.")
default:
    fmt.Printf("%s.\n", os)
}
```
no `break`: Go only runs the selected case, not all the cases that follow.

switch with no condition 
```go
switch {
case t.Hour() < 12:
    fmt.Println("Good morning!")
case t.Hour() < 17:
    fmt.Println("Good afternoon.")
default:
    fmt.Println("Good evening.")
}
```

### Defer
The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

Deferred function calls are pushed onto a stack. When a function returns, its deferred calls are executed in last-in-first-out order.
```go
func main() {
    fmt.Println("counting")

    for i := 0; i < 10; i++ {
        defer fmt.Println(i)
    }

    fmt.Println("done")
}
```

## Pointers
```go
var p *int 
i := 42
p = &i
*p = 21
```

# Structs
```go
type Vertex struct {
    X int 
    Y int 
    // or: X, Y int
}

var (
    v1 = Vertex{1, 2} 
    v1.X = 0
    v2 = Vertex{X: 1}  // Y:0 is implicit
    v3 = Vertex{}      // X:0 and Y:0
    p  = &Vertex{1, 2} // has type *Vertex
    p.X = 3 // use dot notation 
)
```

# Arrays
```go
func main() {
    var a [2]string
    a[0] = "Hello"
    a[1] = "World"

    primes := [6]int{2, 3, 5, 7, 11, 13}
}
```

# Slices
```go
arr[low : high]
```

Slices are like references to arrays
Changing the elements of a slice modifies the corresponding elements of its underlying array, and vice versa.
```
Slice
+--------+-----+-----+
|  ptr   | len | cap |  ← Slice Header
+--------+-----+-----+
    |
    v
+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |  ← Underlying Array
+---+---+---+---+---+---+---+
```

- The **length** of a slice is the number of elements it contains.

- The **capacity** of a slice is the number of elements in the underlying array, counting from the first element in the slice.
  
## Slice Literals
This is an array literal:
```go
[3]bool{true, true, false}
```
And this creates the same array as above, then builds a slice that references it:
```go
[]bool{true, true, false}
```
## Nil Slices
```go
var s []int
```
The zero value of a slice is `nil`.
A nil slice has a length and capacity of 0 and has no underlying array.

## Make 
Slices can be created with the built-in `make` function; this is how you create dynamically-sized arrays.
```go
a := make([]int, 5)  // len(a)=5

b := make([]int, 0, 5) // len(b)=0, cap(b)=5
b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4
```
0 ≤ low ≤ high ≤ cap(s)
```go
b := make([]int, 0, 5)  // len(b)=0, cap(b)=5
c := b[:3]  // [0:3] correct
c := b[2:]  // [2:0] error
```

## Slices of slices
```go
board := [][]string{
    []string{"_", "_", "_"},
    []string{"_", "_", "_"},
    []string{"_", "_", "_"}, // <- comma here
}
```
```
+---------------+
| board0        | → ["_", "_", "_"]
+---------------+
| board1        | → ["_", "_", "_"]
+---------------+
| board2        | → ["_", "_", "_"]
+---------------+
```
## Appending to a slice
```go
func append(s []T, vs ...T) []T
```
```go
arr := [5]int{1, 2, 3, 4, 5} 
s := arr[:3]                // s = [1, 2, 3], len=3, cap=5
s = append(s, 6)            // modify the underlying array
fmt.Println(s)              // [1, 2, 3, 6]
fmt.Println(arr)            // [1, 2, 3, 6, 5]
```
```go
s := []int{1, 2, 3}        
s = append(s, 4)           // allocate a new, larger underlying array
fmt.Println(s)             // [1, 2, 3, 4]
fmt.Println(cap(s))        // maybe 6, denpends on the strategy
```

```go
combinedSlice := append(slice1, slice2...)
```
```go
slice1 := []int{1, 2, 3}
slice2 := []int{4, 5, 6}

combined := append(slice1, slice2...)
fmt.Println(combined) // [1 2 3 4 5 6]
```

## Range
The `range` form of the `for` loop iterates over a slice or map.
```go
var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

for i, v := range pow {...}

for i, _ := range pow
for i := range pow

for _, value := range pow
```

# Map
The zero value of a map is `nil`. A `nil` map has no keys, nor can keys be added.
```go
var m map[string]int
m["key"] = 1 // panic: assignment to nil map
```
The `make` function returns a map of the given type, initialized and ready for use.
```go
m := make(map[string]int)
m["Alice"] = 25
```
## Map Literals
```go
type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}
```
If the top-level type is just a type name, you can omit it from the elements of the literal.
```go
var m = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967},
	"Google":    {37.42202, -122.08408},
}
```
## Mutating Maps
```go
m[key] = elem   // insert
elem = m[key]   // retrieve
delete(m, key)  // delete
elem, ok = m[key]   // Test that a key is present
// - If key is in m, then elem is the value of key, ok is true
// - If key is not in the map, then elem is zero value, ok is false
```
```go
func WordCount(s string) map[string]int {
    words := strings.Fields(s) 
    cntmap := make(map[string]int)
    for _, w := range words {
        cntmap[w]++     // if w not in cntmap, return zero value! (different from python)
    }
    return cntmap
}
```


## Function Value
Function values may be used as function arguments and return values.
```go
func compute(fn func(float64, float64) float64) float64 {
    return fn(3, 4)
}

func main() {
    hypot := func(x, y float64) float64 {
        return math.Sqrt(x*x + y*y)
    }
    fmt.Println(hypot(5, 12))

    fmt.Println(compute(hypot))
    fmt.Println(compute(math.Pow))
}
```
## Function Closure
A closure is a function value that references variables from outside its body. The function may access and assign to the referenced variables; in this sense the function is "bound" to the variables.
```go
func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}

func main() {
    pos, neg := adder(), adder()
    for i := 0; i < 10; i++ {
        fmt.Println(
            pos(i),
            neg(-2*i),
        )
    }
}
```

---

# Methods
Go does not have classes. However, you can define methods on types.

A method is a function with a special receiver argument.

The receiver appears in its own argument list between the `func` keyword and the method name.
```go
type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 { //  a receiver of type Vertex named v.
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}
```
equivalent to 
```go
func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```
You can only declare a method with a receiver whose type is defined in the same package as the method.
You cannot declare a method with a receiver whose type is defined in another package (which includes the built-in types such as int).
```go
type MyFloat float64

func (f MyFloat) Abs() float64 {    // cannot use float64 directly
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}
```
With a **value receiver**, the Scale method operates on a copy of the original Vertex value.
Methods with **pointer receivers** can modify the value to which the receiver points.

```go

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}   
	v.Scale(10)     // automatically retrieve address &v and pass to Scale
	fmt.Println(v.Abs())
}
```
## Pointer indirection
Functions with a pointer argument must take a pointer:
```go
var v Vertex
ScaleFunc(v, 5)  // Compile error!
ScaleFunc(&v, 5) // OK
```
while methods with pointer receivers take either a value or a pointer as the receiver when they are called:
```go
var v Vertex
v.Scale(5)  // OK
p := &v
p.Scale(10) // OK
```
Functions that take a value argument must take a value of that specific type:
```go
var v Vertex
fmt.Println(AbsFunc(v))  // OK
fmt.Println(AbsFunc(&v)) // Compile error!
```
while methods with value receivers take either a value or a pointer as the receiver when they are called:
```go
var v Vertex
fmt.Println(v.Abs()) // OK
p := &v
fmt.Println(p.Abs()) // OK
```


# Interface
An interface type is defined as a set of method signatures.

## Implementation
Interfaces are implemented implicitly
A type implements an interface by implementing its methods. There is no explicit declaration of intent, no "implements" keyword.

A value of interface type can hold any value that implements those methods.
```go
package main

import (
    "fmt"
    "math"
)

type Abser interface {
    Abs() float64
}

func main() {
    var a Abser
    f := MyFloat(-math.Sqrt2)
    v := Vertex{3, 4}

    a = f  // a MyFloat implements Abser
    fmt.Println(a.Abs())    // 1.4142135623730951

    a = &v // a *Vertex implements Abser
    fmt.Println(a.Abs())    // 5

    // v is a Vertex (not *Vertex) and does NOT implement Abser.
    a = v   // error

	
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

type Vertex struct {
    X, Y float64
}

func (v *Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```
## Interface values
Under the hood, interface values can be thought of as a tuple of a value and a concrete type:
```
(value, type)
```
An interface value holds a value of a specific underlying concrete type.
Calling a method on an interface value executes the method of the same name on its underlying type.

## Interface values with nil underlying values
If the concrete value inside the interface itself is nil, the method will be called with a nil receiver.

Note that an interface value that holds a nil concrete value is itself non-nil.
```go
type I interface {
    M()
}

type T struct {
    S string
}

func (t *T) M() {
    if t == nil {
        fmt.Println("<nil>")
        return
    }
    fmt.Println(t.S)
}


func main() {
    var i I
    var t *T
    i = t
    describe(i)
    i.M()
}

func describe(i I) {
	fmt.Printf("(%v, %T)\n", i, i)
}
```

## Nil interface values

A nil interface value holds neither value nor concrete type.

Calling a method on a nil interface is a run-time error because there is no type inside the interface tuple to indicate which concrete method to call.
```go
func main() {
	var i I
	i.M()   // error
}
```

## The empty interface
The interface type that specifies zero methods is known as the empty interface:
```go
interface{}
```

Empty interfaces are used by code that handles values of unknown type. 
For example, `fmt.Print` takes any number of arguments of type `interface{}`.

## Type assertions
A type assertion provides access to an interface value's underlying concrete value.
```go
t := i.(T)
```
This statement asserts that the interface value i holds the concrete type T and assigns the underlying T value to the variable t.
If i does not hold a T, the statement will trigger a panic.

To test whether an interface holds a specific type:
```go
t, ok := i.(T)
```

## Type switches
A type switch is a construct that permits several type assertions in series.
```go
switch v := i.(type) {
case T:
    // here v has type T
case S:
    // here v has type S
default:
    // no match; here v has the same type as i
}
```

## Stringer
One of the most ubiquitous interfaces is `Stringer` defined by the `fmt` package.
```go
type Stringer interface {
    String() string
}
```
A `Stringer` is a type that can describe itself as a string. The `fmt` package (and many others) look for this interface to print values.

pseudocode of fmt.Println()
```go
func Println(a ...interface{}) {
    for _, v := range a {
        if s, ok := v.(fmt.Stringer); ok {
            // call String() if implemented
            fmt.Print(s.String())
        } else {
            // or use reflection to get the default format 
            fmt.Print(defaultFormat(v))
        }
    }
}
```
```go
type Person struct {
    Name string
    Age  int
}

func (p Person) String() string {
    return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}
```

## Errors
```go
type error interface {
    Error() string
}
```

```go
package main

import (
	"fmt"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number: %v", float64(e))
}

func Sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x)
	}

	z := 1.0
	for i := 0; i < 10; i++ {
		z -= (z*z - x) / (2 * z)
	}
	return z, nil
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(-2))
}
```
## Readers

## Images
Package image defines the Image interface:
```go
package image

type Image interface {
    ColorModel() color.Model
    Bounds() Rectangle
    At(x, y int) color.Color
}
```

# Generics
## Generic functions
Go functions can be written to work on multiple types using **type parameters**. 
The type parameters of a function appear between brackets, before the function's arguments.
```go
func Index[T comparable](s []T, x T) int {
    for i, v := range s {
        // v and x are type T, which has the comparable
        // constraint, so we can use == here.
        if v == x {
            return i
        }
    }
    return -1
}

func main() {
    si := []int{10, 20, 15, -10}
    fmt.Println(Index(si, 15))

    ss := []string{"foo", "bar", "baz"}
    fmt.Println(Index(ss, "hello"))
}
```

## Generic types


A type can be parameterized with a type parameter, which could be useful for implementing generic data structures.
```go
type List[T any] struct {
	next *List[T]
	val  T
}

func InsertAtHead[T any](head **List[T], value T) {
    newNode := &List[T]{val: value, next: *head}
    *head = newNode
}

func InsertAtTail[T any](head **List[T], value T) {
    newNode := &List[T]{val: value, next: nil}
    if *head == nil {
        *head = newNode
        return
    }
    current := *head
    for current.next != nil {
        current = current.next
    }
    current.next = newNode
}

func main() {
    var head *List[int]
    node := &List[int]{
        val:  42,      
        next: nil,
    }

    InsertAtHead(&head, 1)
}
```


import Foundation

//extension StringProtocol {
//    public subscript(i: Int) -> Element {
//        self[index(startIndex, offsetBy: i)]
//    }
//}

func solution(_ s:String) -> Bool {
    var stack: [Character] = []
    
    for i in s {
        if i == "(" {
            stack.append(i)
        } else {
            stack.popLast()
        }
    }
    
    if stack.isEmpty { return true }
    else { return false }
}


class DynamicArray:  
    def __init__(self):
        self.size = 0        
        self.capacity = 4    
        self.array = [None] * self.capacity 
    
    def print_state(self):
        
        print(f"Size: {self.size}, Capacity: {self.capacity}, Array: {' '.join(map(str, self.array[:self.size]))}")
    
    def append(self, value):
        if self.size == self.capacity:   
            
            old = self.array
            self.capacity *= 2 
            self.array = [None] * self.capacity  
            for i in range(self.size): 
                self.array[i] = old[i]
            print(f"RESIZED: {self.capacity//2} → {self.capacity}")  
        
        self.array[self.size] = value  
        self.size += 1  
    
    def pop(self):

        
        if self.size == 0:  
            print("Empty array")
            return None
        
        self.size -= 1 
        popped = self.array[self.size] 
        self.array[self.size] = None 
        print(f"Popped: {popped}") 
        return popped


print("Dynamic Array Demo")
da = DynamicArray() 


print("\n--- APPEND OPERATIONS ---")
da.append(10); da.print_state()
da.append(20); da.print_state()
da.append(30); da.print_state()
da.append(40); da.print_state()  

print("\n--- POP OPERATIONS ---")
da.pop(); da.print_state()
da.pop(); da.print_state()


# Dynamic Array
da = DynamicArray()
da.append(10)
da.append(20)
da.append(30)
print("Dynamic Array:", da.display()) 
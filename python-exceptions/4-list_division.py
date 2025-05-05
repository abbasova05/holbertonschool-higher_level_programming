#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            # Check if the elements at the current index are numbers (int or float)
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            
            # Try dividing the elements
            result.append(my_list_1[i] / my_list_2[i])
        
        except TypeError:
            print("wrong type")
            result.append(0)
        
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        
        except IndexError:
            print("out of range")
            result.append(0)
        
        finally:
            # Ensure the iteration moves forward
            pass

    return result

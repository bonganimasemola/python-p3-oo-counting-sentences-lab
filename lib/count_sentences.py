#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = None  
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
      
      
    def is_sentence(self):
        result = self._value.endswith(".")
        print(f"Value: {self._value}, Result: {result}")
        return result
    
    def is_question(self):
      return self._value.endswith("?")
    
    def is_exclamation(self):
      return self._value.endswith("!")
    
    def count_sentences(self):
      value = self.value
      for punc in ['!','?']:
        value = value.replace(punc, '.')
    
      sentences = [s for s in value.split('.') if s]
    
      return len(sentences)

    
      
     
  

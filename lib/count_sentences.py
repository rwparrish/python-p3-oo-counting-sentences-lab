#!/usr/bin/env python3
import re

class MyString:
  
  def __init__(self, value=""):
    self._value = value
    
    
  def get_value(self):
    return self._value
  
  def set_value(self, strValue):
    if type(strValue) != str:
      print("The value must be a string.")
    else:
      self._value = strValue
    
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
        pattern = r'[\w\s]+[.!?]'
        sentences = re.findall(pattern, self.value)
        return len(sentences)    
      
  value = property(get_value, set_value)

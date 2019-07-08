class Solution:
  # def checkBalancedParanthesis(self, exp):
  #     if exp:
  #
  #       self.mystack = []
  #       mydict = {')':'(', '}':'{', ']':'['}
  #       for i in exp:
  #         if i in mydict.values():
  #           self.push(i)
  #         elif i in mydict:
  #           popped = self.pop()
  #           if popped != mydict[i]:
  #             return 'Unbalanced'
  #       if len(self.mystack) == 0:
  #         return 'Balanced'
  #       else:
  #         return 'Unbalanced'

  def checkBalancedParanthesis(self, exp): #without using dict
      if exp:
        self.mystack = []
        for i in exp:
          if i == '(' or i == '{' or i == '[':
            self.push(i)
          elif i == ')' or i == '}' or i == ']':
            popped = self.pop()
            if popped == '(' and i == ')' or popped == '{' and i == '}' or popped == '[' and i == ']':
              continue
            else:
              return 'Unbalanced'
        if len(self.mystack) == 0:
          return 'Balanced'
        else:
          return 'Unbalanced'

  def push(self, elem):
    self.mystack.append(elem)
  def pop(self):
    if len(self.mystack) != 0:
        return self.mystack.pop()
  def top(self):
      if len(self.mystack) != 0:
          return self.mystack[-1]

exp = '}'
s = Solution()
print(s.checkBalancedParanthesis(exp))

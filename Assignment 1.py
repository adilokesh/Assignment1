#!/usr/bin/env python
# coding: utf-8

# ## Q1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
/
+
6
# sol1. 
# 
# 'hello',6,and -87.8 are values.
# *,-,/,and+ are the expressions.
# 

# ## Q2. What is the difference between string and variable?

# sol2. 
# ### Variable
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
#  ### Rules for variables:
#  1. Varible names should start with alphabets
# 2. variable names should not contain any special character like ^%&@#&
# 
# Example:

# In[4]:


myName = input()


# ###  Strings  
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# Example

# In[3]:


print('He said, "I want to eat an apple".')


# ## Q3. Describe three different data types.

#  Python has many built-in data types that can store different kinds of values. Here are three examples of data types in Python:
#  #### str:
#  This is the data type for strings, which are sequences of characters. Strings can be created using single quotes, double quotes, or triple quotes. For example, name = 'Alice' is a string variable. You can use various methods and operators to manipulate strings in Python.
# 

# ### int
# : This is the data type for integers, which are whole numbers without fractions or decimals. Integers can be positive or negative, and there is no limit to how long they can be. For example, age = 25 is an integer variable. You can use arithmetic operators and functions to perform calculations with integers in Python.
# 

# #### Float 
# This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.

# ## Q4. What is an expression made up of? What do all expressions do?

# 
# In Python, 2 + 2 is called an expression, which is the most basic kind of 
# programming instruction in the language. Expressions consist of values 
# (such as 2) and operators (such as +), and they can always evaluate (that is, 
# reduce) down to a single value. That means you can use expressions any
# where in Python code that you could also use a value.
#  In the previous example, 2 + 2 is evaluated down to a single value, 4. 
# A single value with no operators is also considered an expression.The order of operations (also called precedence) of Python math operators 
# is similar to that of mathematics. The ** operator is evaluated first; the *, 
# /, //, and % operators are evaluated next, from left to right; and the + and - 
# operators are evaluated last (also from left to right). You can use parenthe
# ses to override the usual precedence if you need to. Whitespace in between 
# the operators and values doesn’t matter for Python (except for the indenta
# tion at the beginning of the line), but a single space is convention.

# In[8]:




(5 - 1) * ((7 + 1) / (3 - 1))



# ## Q5. This assignment statements, like spam = 10. What is the difference between anexpression and a statement?
# 

#  sol5. 
#  An expression evaluates to a single value. A statement does not.
# 

# ## 6. After running the following code, what does the variable bacon contain?
# ## bacon = 22
# ## bacon + 1
6. The bacon variable is set to 22.

The bacon + 1 expression does not reassign the value in bacon (that would need an assignment statement: bacon = bacon + 1).
 
# ## 7. What should the values of the following two terms be?
# ## 'spam'+'spamspam'
# ## 'spam'*3

# In[14]:


'spam'+'spamspam'


# In[15]:


'spam'*3


# Both expressions evaluate to the string 'spamspamspam'.

# ## Q8. Why is eggs a valid variable name while 100 is invalid?

# sol8. Variable names cannot begin with a number.

# ## Q9. What three functions can be used to get the integer, floating-point number, or stringversion of a value?
# 

#  sol9. The int(), float(), and str() functions will evaluate to the integer, 
# f
#  loating-point number, and string versions of the value passed to them.

# ## Q10. Why does this expression cause an error? How can you fix it?
# ## 'I have eaten'+99+'burritos'

# sol10. The expression causes an error because 99 is an integer, and only 
# strings can be concatenated to other strings with the + operator. The 
# correct way is 

# In[25]:


'I have eaten'+99+'burritos'


# In[26]:


'I have eaten'+ ' 99 ' +'burritos'


#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1

# In[ ]:


# . Print an f-string that displays NLP stands for Natural Language Processing using the variables provided
a = "NLP stands for Natural Language Processing using the Variables provided."
a = print(f"{a}")


# # QUESTION 2

# In[2]:


# Create a file in the current working directory called contacts.txt by running the cell below.
get_ipython().run_cell_magic('writefile', 'contacts.txt', 'first_name\nlast_name\n')
    


# # QUESTION  3

# In[4]:


# Open the file and use .read() to save the contents of the file to a string called fields. Make sure the file is closed at the end
# Method 1
string = open('contacts.txt')
string.read()


# In[ ]:


# Method 2 - RECOMMENDED
with open ('contacts.txt','r') as a:
    fields = a.read()
fields


# # QUESTION 4

# In[7]:


# Use PyPDF2 to open the file Business_Proposal.pdf. Extract the text of page 2.
import PyPDF2
pdf_path = r'Business_Proposal.pdf'
f = open(pdf_path, 'rb')
f


# In[8]:


reader = PyPDF2.PdfReader(f)
reader


# In[9]:


page_two = reader.pages[0]
page_two


# In[10]:


# extracting page 2
page_two_text = page_two.extract_text()
page_two_text


#  #  QUESTION  5
# 

# In[17]:


# Open the file contacts.txt in append mode. Add the text of page 2 from above to contacts.txt.

with open('contacts.txt', 'a') as a:
    add_p2 = a.write(page_two_text)
    add_p2


# In[ ]:


# with open('contacts.txt', 'r') as a:
    b = a.read()
b


# # QUESTION 6

# In[19]:


# QUESTION-6. Using the page_two_text variable created above, extract any email addresses that were contained in the file Business_Proposal.pdf.
import re

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-8.-]+\.[A-Z|a=z]{2,}'
result = re.findall(pattern, page_two_text)
print(result)


# In[ ]:





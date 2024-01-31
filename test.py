import os
from dotenv import load_dotenv



load_dotenv()

field1 = os.getenv('FIELD1')
field2 = os.getenv('FIELD2')

# استفاده از مقادیر
print(field1)
print(field2)
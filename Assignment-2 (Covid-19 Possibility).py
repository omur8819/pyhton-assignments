age = False  # can be assigned only True/False
chronic = True  # can be assigned only True/False
immune = False  # can be assigned only True/False
risk = age and chronic or immune
print(risk)
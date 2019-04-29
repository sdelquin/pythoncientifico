input_str = '\n\n\t   Be the change that U wish to see in the world           \t      \t\n'
output_str = input_str.strip()
ref_index = output_str.find('U')
output_str[:ref_index].upper() + output_str[ref_index:].title()

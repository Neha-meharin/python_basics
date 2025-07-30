sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
min_value = min(sample_dict.values())
print("key with minimum value:", [k for k, v in sample_dict.items() if v == min_value][0])

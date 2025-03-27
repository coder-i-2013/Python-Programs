from collections import Counter

def value_frequency(test_dict, target_value):
  value_counts = Counter(test_dict.values())
  return value_counts[target_value]
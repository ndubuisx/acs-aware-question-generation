question_style_set = ["who", "where", "when", "why", "which", "what", "how"]
# questions that begin with these words can be answered with yes/no
feature_word_set = ["am", "is", "was", "were", "are", "does", "do", "did", 
               "have", "had", "has", "could", "can", "shall", "should", "will", "would", "may", "might"]

def style_classification(question, style_set, feature_word_set):
  for style in style_set:
    if style in question.lower():
      return style

  for word in feature_word_set:
    if word == question.split()[0].lower():
      return "yes-no"

  return "other"

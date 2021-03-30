def clue_extraction(passage, answer, question):
  max_clue_score = 0
  clue_chunk = ""
  candidate_chunks = [word.text for word in get_chunks(passage)]
  passage_tokens = [word for word in passage.split() if not word.lower() in all_stopwords]
  question_tokens = [word for word in question.split() if not word.lower() in all_stopwords]

  passage_stems = [stemmer.stem(token) for token in passage_tokens]
  questions_stems = [stemmer.stem(token) for token in question_tokens]

  for chunk in candidate_chunks:
    chunk_tokens = [word for word in chunk.split() if not word.lower() in all_stopwords]
    chunk_stems = [stemmer.stem(token) for token in chunk_tokens]

    num_chunk_question_token_overlap = len(set(chunk_tokens) & set(question_tokens))
    num_chunk_question_stem_overlap = len(set(chunk_stems) & set(chunk_stems))

    num_chunk_question_soft_copied_tokens = 0;

    for _chunk in chunk_tokens:
      for question in question_tokens:
        if (nlp(chunk).similarity(nlp(question)) > 0.5):
          num_chunk_question_soft_copied_tokens += 1
    
    chunk_in_question = True if chunk in question else False
    
    clue_score = num_chunk_question_token_overlap + num_chunk_question_stem_overlap + num_chunk_question_soft_copied_tokens + chunk_in_question

    if (clue_score > max_clue_score):
      clue_chunk = chunk
      max_clue_score = clue_score
  
  return clue_chunk


def get_chunks(text):
  doc = nlp(text)
  sentence = list(doc.sents)[0]
  candidate_chunks = []
  constituents = sentence._.constituents

  pos = ['NP', 'VP', 'PP']

  for chunk in constituents:
    if (len(chunk._.labels) != 0 and chunk._.labels[0] in pos):
      candidate_chunks.append(chunk)
  
  return list(candidate_chunks)

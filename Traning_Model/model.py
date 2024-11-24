from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Head.Ear import listen
from Head.Mouth import speak

# Load your Q&A dataset from a text file
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q, 'answer': a} for q, a in qna_pairs]
    return dataset


# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X



#Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset, threshold=0.2):
    """
    Retrieve the most relevant answer. First checks for exact matches
    before falling back to similarity scoring.
    """
    preprocessed_question = preprocess_text(question)

    # Step 1: Check for exact match in dataset
    for qa in dataset:
        if preprocess_text(qa['question']) == preprocessed_question:
            return qa['answer']

    # Step 2: Use similarity scoring if no exact match is found
    question_vec = vectorizer.transform([preprocessed_question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    best_match_score = similarities[0, best_match_index]

    # Step 3: Return match if score exceeds threshold, else default response
    if best_match_score >= threshold:
        return dataset[best_match_index]['answer']
    else:
        return ""

# Main function
def mind(text):
    # Replace 'your_dataset.txt' with the path to your Q&A dataset
    dataset_path = r'C:\FY MCA\Kanha\Data\brain_data\qna_data.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset, threshold=0.2)
    return answer

#
# while True:
#     x=input(listen())
#     mind(x)
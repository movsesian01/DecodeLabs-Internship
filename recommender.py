import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("raw_skills.csv")

tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(df['Skills'])

def recommend_tech_stack(user_skills, top_n=3):
    user_input_str = " ".join(user_skills)
    user_vector = tfidf.transform([user_input_str])

    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    df_results = df.copy()
    df_results['Match_Score'] = similarity_scores

    df_sorted = df_results.sort_values(by='Match_Score', ascending=False)

    top_recommendations = df_sorted.head(top_n)
    return top_recommendations[['Job_Role', 'Match_Score']]

if __name__ == "__main__":
    print("--- DecodeLabs Tech Stack Recommender ---")
    
    input_1 = input("Enter Skill 1: ").strip()
    input_2 = input("Enter Skill 2: ").strip()
    input_3 = input("Enter Skill 3: ").strip()

    user_skills = [input_1, input_2, input_3]
    recommendations = recommend_tech_stack(user_skills, top_n=3)

    print("\n--- TOP RECOMMENDED CAREER PATHS ---")
    for idx, row in recommendations.iterrows():
        percentage = round(row['Match_Score'] * 100, 2)
        print(f"Role: {row['Job_Role']} | Match Score: {percentage}%")
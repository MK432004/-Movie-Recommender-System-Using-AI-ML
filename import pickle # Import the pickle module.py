import pickle  # Import the pickle module
import os      # Import the os module for directory operations
import pandas as pd  # Import pandas for DataFrame operations

# Sample DataFrame (replace this with your actual DataFrame)
new_df = pd.DataFrame({
    'title': ['Movie 1', 'Movie 2', 'Movie 3'],
    'genre': ['Action', 'Comedy', 'Drama']
})

# Sample similarity matrix (replace this with your actual similarity matrix)
similarity = [[1, 0.5, 0.2], [0.5, 1, 0.3], [0.2, 0.3, 1]]

# Ensure the 'artifacts' directory exists
os.makedirs('artifacts', exist_ok=True)

# Save the DataFrame and similarity matrix using pickle
with open('artifacts/movie_list.pkl', 'wb') as movie_file:
    pickle.dump(new_df, movie_file)

with open('artifacts/similarity.pkl', 'wb') as similarity_file:
    pickle.dump(similarity, similarity_file)

print("Files saved successfully.")

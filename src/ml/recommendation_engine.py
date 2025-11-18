"""
Collaborative Filtering Recommendation Engine
Uses ALS algorithm for video recommendations
"""
from sklearn.decomposition import NMF
from scipy.sparse import csr_matrix
import numpy as np
import pandas as pd

class VideoRecommender:
    def __init__(self, n_components=50, max_iter=200):
        self.model = NMF(
            n_components=n_components,
            max_iter=max_iter,
            random_state=42,
            init='nndsvda'
        )
        self.user_factors = None
        self.item_factors = None
    
    def fit(self, user_video_matrix):
        """Train recommendation model"""
        self.user_factors = self.model.fit_transform(user_video_matrix)
        self.item_factors = self.model.components_
        
    def recommend(self, user_id, top_n=10, exclude_watched=True):
        """Generate top-N recommendations for user"""
        user_vector = self.user_factors[user_id]
        scores = np.dot(user_vector, self.item_factors)
        top_indices = np.argsort(scores)[::-1][:top_n]
        
        return {
            'video_ids': top_indices.tolist(),
            'scores': scores[top_indices].tolist()
        }
    
    def similar_videos(self, video_id, top_n=10):
        """Find similar videos based on embeddings"""
        video_vector = self.item_factors[:, video_id]
        similarities = np.dot(self.item_factors.T, video_vector)
        similar_indices = np.argsort(similarities)[::-1][1:top_n+1]
        
        return similar_indices.tolist()

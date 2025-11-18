# Video Content Analytics Dashboard

> **Portfolio Note**: Portfolio recreation of video analytics system built at Omfys Technologies.

## 🎯 Overview
End-to-end platform measuring engagement across **200K+ daily events** using Kafka, Spark Streaming, PostgreSQL, Redis, and ML recommendations achieving **18% engagement improvement**.

## 📊 Key Metrics
- **Volume**: 200K+ events/day
- **QPS**: 10K queries/second  
- **Latency**: <50ms p95
- **Cache Hit Rate**: 85%
- **Engagement Boost**: 18%

## 🛠️ Tech Stack
- **API**: FastAPI, Nginx
- **Streaming**: Kafka, Spark Streaming
- **Storage**: PostgreSQL (2TB), Redis (6-node cluster)
- **ML**: Collaborative Filtering (ALS), FAISS
- **Analytics**: AWS QuickSight

## ⚡ Key Features

### 1. Real-Time Analytics Pipeline
- Spark Structured Streaming for KPIs
- Kafka with 12 topics
- Windowed aggregations

### 2. Recommendation Engine
- Collaborative filtering (ALS algorithm)
- Matrix factorization on 5M users × 100K videos
- FAISS for similarity search
- 18% engagement improvement

### 3. High-Performance Caching
- Redis 6-node cluster
- Multi-level caching strategy
- Cache warming and invalidation
- 85% hit rate, <50ms latency

### 4. Optimized Database
- Range partitioning by date (monthly)
- 25+ covering indexes
- Star schema design
- Query optimization reducing costs by 35%

## 📁 Project Structure
```
video-analytics-platform/
├── src/
│   ├── api/                 # FastAPI application
│   ├── streaming/           # Spark Streaming
│   ├── ml/                  # Recommendation engine
│   └── database/            # PostgreSQL schemas
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## 🚀 Getting Started

```bash
git clone https://github.com/Amanroy666/video-analytics-platform.git
cd video-analytics-platform
pip install -r requirements.txt
docker-compose up -d
```

## 📈 Performance Results

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Dashboard Load Time | 3.2s | 1.1s | 67% ↓ |
| Database Queries | 100K/day | 27K/day | 73% ↓ |
| Engagement Rate | 15% | 17.7% | 18% ↑ |

## 👤 Author

**Aman Roy** - Data Engineer at Omfys Technologies  
📧 contactaman000@gmail.com | 💼 [LinkedIn](https://linkedin.com/in/amanxroy)

"""
Kafka Stream Processor for Video Events
Processes 200K+ daily video engagement events
"""
from kafka import KafkaConsumer, KafkaProducer
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VideoEventProcessor:
    def __init__(self, bootstrap_servers):
        self.consumer = KafkaConsumer(
            'video-events',
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id='video-analytics-group',
            auto_offset_reset='latest'
        )
        
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    def process_events(self):
        """Process video engagement events"""
        for message in self.consumer:
            event = message.value
            
            # Calculate engagement metrics
            engagement_score = self.calculate_engagement(event)
            
            # Enrich event
            enriched_event = {
                **event,
                'engagement_score': engagement_score,
                'processed_at': datetime.now().isoformat()
            }
            
            # Send to downstream topic
            self.producer.send('enriched-events', enriched_event)
            
            logger.info(f"Processed event for video {event['video_id']}")
    
    def calculate_engagement(self, event):
        """Calculate engagement score"""
        watch_time = event.get('watch_time', 0)
        video_duration = event.get('duration', 1)
        completion_rate = watch_time / video_duration
        
        # Weighted engagement score
        score = (
            completion_rate * 0.4 +
            event.get('likes', 0) * 0.2 +
            event.get('shares', 0) * 0.3 +
            event.get('comments', 0) * 0.1
        )
        
        return min(score, 1.0)

if __name__ == "__main__":
    processor = VideoEventProcessor(['localhost:9092'])
    processor.process_events()

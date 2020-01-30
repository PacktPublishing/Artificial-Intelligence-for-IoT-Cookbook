from luminol.anomaly_detector import AnomalyDetector
import time

# ts = 'data.csv'  # or
ts = { 
    '1490323038': 3,
    '1490323048': 4,
    '1490323058': 6,
    '1490323068': 78,
    '1490323078': 67,
    '1490323088': 5,
}

my_detector = AnomalyDetector(ts)
score = my_detector.get_all_scores()
anom_score = []

for (timestamp, value) in score.iteritems():
    t_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    anom_score.append([t_str, value])

for score in anom_score:
    print(score)
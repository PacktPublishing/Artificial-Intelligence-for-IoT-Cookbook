from luminol.anomaly_detector import AnomalyDetector
import time

my_detector = AnomalyDetector('Turbidity.csv')
score = my_detector.get_all_scores()


for (timestamp, value) in score.iteritems():
    t_str = time.strftime('%y-%m-%d %H:%M:%S', time.localtime(timestamp))
    if value > 0:
        print(f'{t_str}, {value}')
        

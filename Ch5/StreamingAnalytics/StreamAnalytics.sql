WITH AnomalyDetectionStep AS
(
    SELECT
        EVENTENQUEUEDUTCTIME AS time,
        CAST(gyro AS float) AS gyro,
        AnomalyDetection_SpikeAndDip(CAST(gyro AS float), 95, 120, 'spikesanddips')
            OVER(LIMIT DURATION(second, 120)) AS SpikeAndDipScores
    FROM tempin
)
SELECT
    *
INTO output
FROM AnomalyDetectionStep;